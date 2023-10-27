from transformers import (
    AutoTokenizer,
    AutoModelForCausalLM,
    BitsAndBytesConfig,
    pipeline,
)
from peft import LoraConfig, get_peft_model, PeftConfig, PeftModel
from peft import prepare_model_for_kbit_training

from torch import cuda
import torch
import os
import flask
import transformers
from datasets import load_dataset, Dataset
import pandas as pd



class model_finetuning:
    def __init__(self, model, tokenizer, data, data_path):
        self.model = model
        self.tokenizer = tokenizer
        self.data = data
        self.data_path = data_path

    def load_data(self):
        self.data = Dataset.from_pandas(self.data_path)
    def load_pretrained(self):
        ROOT = os.path.abspath(os.sep)
        self.model = AutoModelForCausalLM.from_pretrained(
            os.path.join(ROOT, 'model', 'pretrained_model')
            )        
    def gradient_checkpointing(self):
         
        self.model.gradient_checkpointing_enabling()
        self.model = prepare_model_for_kbit_training(self.model)

    def print_trainable_parameters(self):
        """
        Prints the number of trainable parameters in the model.
        """

        trainable_params = 0
        all_param = 0
        for _, param in self.model.named_parameters():
            all_param += param.numel()
            if param.requires_grad:
                trainable_params += param.numel()
        print(
            f"trainable params: {trainable_params} || all params: {all_param} || trainable%: {100 * trainable_params / all_param}"
        )

    def create_lora_config(self):
        config = LoraConfig(
            r=16,
            lora_alpha=32,
            target_modules=["query_key_value"],
            lora_dropout=0.05,
            bias="none",
            task_type="CAUSAL_LM",
        )
        self.model = get_peft_model(self.model, config)
        self.print_trainable_parameters(self.model)

    def train(self):
        training_args = transformers.TrainingArguments(
            gradient_accumulation_steps=4,
            num_train_epochs=3,
            learning_rate=2e-4,
            fp16=True,
            save_total_limit=4,
            logging_steps=25,
            output_dir=ROOT,  # give the location where you want to store checkpoints
            save_strategy="epoch",
            optim="paged_adamw_8bit",
            lr_scheduler_type="cosine",
            warmup_ratio=0.05,
        )
        trainer = transformers.Trainer(
            model=self.model,
            train_dataset=self.data,
            args=training_args,
            data_collator=transformers.DataCollatorForLanguageModeling(
                self.tokenizer, mlm=False
            ),
        )
        self.model.config.use_cache = (
            False  # silence the warnings. Please re-enable for inference!
        )
        trainer.train()
        ROOT = os.getcwd()
        self.model.save_pretrained(os.path.join(ROOT, 'model', '1') )

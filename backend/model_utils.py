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


def load_model():
    ROOT = os.path.abspath(os.sep)
    quantization_config = BitsAndBytesConfig(
        load_in_4bit=True,
        bnb_4bit_compute_dtype=torch.float16,
        bnb_4bit_quant_type="nf4",
        bnb_4bit_use_double_quant=True,
    )
    model_4bit = AutoModelForCausalLM.from_pretrained(
        "tiiuae/falcon-7b-instruct",
        device_map="auto",
        quantization_config=quantization_config,
    )

    tokenizer = AutoTokenizer.from_pretrained("tiiuae/falcon-7b-instruct")

    model_4bit.save_pretrained(os.path.join(ROOT, 'model', 'pretrain_model', 'model'))
    tokenizer.save_pretrained(os.path.join(ROOT, 'model', 'pretrain_model', 'model'))

class model_inference:
    def __init__(self, model_path):
        self.model = None
        self.model_inf = None
        self.encoding = None
        self.tokenizer = None
        self.device = None
        self.model_path = model_path
    def load_model(self):
        self.device = 'cuda' if cuda.is_available() else 'cpu'
        torch.cuda.empty_cache()

        config = PeftConfig.from_pretrained(self.model_path)
        self.model = AutoModelForCausalLM.from_pretrained(
            config.base_model_name_or_path,
            #     load_in_8bit=True,
                # device_map=self.device,
            trust_remote_code=True,
        )
        self.tokenizer = AutoTokenizer.from_pretrained(
            config.base_model_name_or_path,
            trust_remote_code=True,
        )
        self.model_inf = PeftModel.from_pretrained(self.model, self.model_path)
        print("load_model complete")
    
    def encode_prompt(self, prompt):
        prompt = prompt.strip()
        self.encoding = self.tokenizer(prompt, return_tensors="pt").to(self.model.device)

    def inference(self):
        # set the generation configuration params 
        gen_config = self.model_inf.generation_config
        gen_config.max_new_tokens = 200
        gen_config.temperature = 0.2
        gen_config.top_p = 0.7
        gen_config.num_return_sequences = 1
        gen_config.pad_token_id = self.tokenizer.eos_token_id
        gen_config.eos_token_id = self.tokenizer.eos_token_id

        # do the inference 
        with torch.inference_mode():
            outputs = self.model.generate(input_ids = self.encoding.input_ids, attention_mask = self.encoding.attention_mask, generation_config = gen_config )
        print(self.tokenizer.decode(outputs[0], skip_special_tokens = True ))




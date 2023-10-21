from transformers import (
    AutoTokenizer,
    AutoModelForCausalLM,
    BitsAndBytesConfig,
    pipeline,
)
# from peft import LoraConfig, get_peft_model, PeftConfig
# from peft import prepare_model_for_kbit_training

# from finetune_data_preprocessing import get_data
from torch import cuda
import torch
import os
import flask

ROOT = os.getcwd()


def load_model():
    quantization_config = BitsAndBytesConfig(
        load_in_4bit=True,
        bnb_4bit_compute_dtype=torch.float16,
        bnb_4bit_quant_type="nf4",
        bnb_4bit_use_double_quant=True,
    )

    pass


def prompt_model(article_list):
    
    for article in article_list:
        article






from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig, pipeline
from peft import LoraConfig, get_peft_model, PeftConfig
from peft import prepare_model_for_kbit_training
# from finetune_data_preprocessing import get_data
from torch import cuda
import torch
import os
ROOT = os.getcwd()


def load_model():
    pass



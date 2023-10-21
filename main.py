from transformers import AutoTokenizer, AutoModelForCausalLM
import os
from peft import LoraConfig, get_peft_model, PeftConfig
from peft import prepare_model_for_kbit_training
# model_name = "tiiuae/falcon-7b-instruct" 
import requests


if __name__ == "__main__":

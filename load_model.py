from transformers import AutoTokenizer, AutoModelForCausalLM
import os
from peft import LoraConfig, get_peft_model, PeftConfig
from peft import prepare_model_for_kbit_training
# model_name = "tiiuae/falcon-7b-instruct" 


def download_model(root):
    model = AutoModelForCausalLM.from_pretrained(
        "tiiuae/falcon-7b-instruct",
    #     load_in_8bit=True,  #if you want to load the 8-bit model
    #     device_map='auto', 
        trust_remote_code=True,
    )
    model.save_pretrained(root)


def tokenizer():
    tokenizer = AutoTokenizer.from_pretrained(
    "tiiuae/falcon-7b-instruct",
    )

if __name__ == "__main__":
    root = os.getcwd()
    download_model(root)


    # tokenizer.pad_token = tokenizer.eos_token
    # data = data.map(gen_and_tok_prompt)

    # config = PeftConfig.from_pretrained("location where new model is stored")
    # model = AutoModelForCausalLM.from_pretrained(
    #     root,
    #     # config.base_model_name_or_path,
    # #     load_in_8bit=True,
    # #     device_map='auto',
    #     trust_remote_code=True,

    # )

    # tokenizer = AutoTokenizer.from_pretrained(
    #     model.base_model_name_or_path)

    # model_inf = PeftModel.from_pretrained(model,"location where new model is stored" )


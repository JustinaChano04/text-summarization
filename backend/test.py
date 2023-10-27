from model_utils import load_model, model_inference
import os



if __name__ == "__main__":
    ROOT = os.getcwd() 

    load_model()




    # modelObj = model_inference(os.path.join(ROOT, "model_tuning"))
    # modelObj.load_model()
    # modelObj.encode_prompt("Hello World")
    # modelObj.inference()








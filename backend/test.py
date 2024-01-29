# from model_utils import load_model, model_inference
# import os


def decode(message_file):
    pyramid_lines = {}
    
    # Read the pyramid lines from the file
    with open(message_file, 'r') as file:

        # Parse each line and insert each number, string to a dictionary 
        for line in file:
            pyramid_lines[int(line.strip().split()[0])] = line.strip().split()[1]

    out_str = ""
    i, idx = 1, 1
    while i in pyramid_lines:
        
        if idx in pyramid_lines:
            out_str += pyramid_lines[idx] + " "
        i += 1
        idx += i

    return out_str

if __name__ == "__main__":
    path = "/path/coding_qual_input.txt"
    result = decode(path)
    print(result)










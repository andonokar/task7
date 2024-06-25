import json
import pickle
import sys
from sys import argv

import pandas as pd

if __name__ == '__main__':
    if len(argv) != 2:
        print("Usage: python3 main.py {json_data} | {file_name.json}")
        sys.exit(1)
    if argv[1].endswith('.json'):
        try:
            with open(argv[1], 'r') as file:
                data = json.load(file)
        except FileNotFoundError:
            print("File not found")
            sys.exit(1)
        except json.decoder.JSONDecodeError:
            print("Invalid JSON from file")
            sys.exit(1)
    else:
        try:
            data = json.loads(argv[1])
        except json.decoder.JSONDecodeError:
            print("Invalid JSON provided")
            sys.exit(1)

    data_to_be_predicted = pd.DataFrame(data)
    with open("model.pkl", 'rb') as model_file:
        model = pickle.load(model_file)
    prediction = model.predict(data_to_be_predicted)
    json_data = json.dumps(prediction.tolist())
    print(json_data)

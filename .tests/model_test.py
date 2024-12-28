import joblib
import pandas as pd
from sklearn.metrics import accuracy_score
import yaml

def test_model():


    # # Load the YAML file
    # with open('config.yaml', 'r') as file:
    #     config = yaml.safe_load(file)
    
    # # Access the data
    # path = config['path']
    # features = config['features']
    # assert len(features) == 2


    
    penguins_test = pd.read_csv(".tests/penguins_test.csv")
    penguins_test = penguins_test.dropna() # remove none
    X = penguins_test.drop(columns = ["species"])
    y = penguins_test["species"] # categorial
    features = ['bill_length_mm', 'bill_depth_mm']
    X = X[features]
    model = joblib.load("penguins_model.joblib")
    prediction = model.predict(X)
    score = accuracy_score(y, prediction)
    assert score > 0.9

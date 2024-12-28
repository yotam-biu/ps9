import joblib
from main import main
import pandas as pd

def test_model():
    data_path = ".tests/penguins_test.csv"
    data_test = pd.read_csv(data_path)
    model_path = "penguins_model.joblib"
    model = joblib.load(model_path)
    assert main() == 274

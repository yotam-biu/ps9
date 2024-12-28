import joblib
from main import main
import pandas as pd

def test_model():
    path = "penguins_model.joblib"
    model = joblib.load(path)
    assert main() == 274

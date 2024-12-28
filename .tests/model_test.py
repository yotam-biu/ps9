import joblib
from main import main
import pandas as pd

def test_model():
    #model = joblib.load("penguins_model.joblib"
    assert main() == 222

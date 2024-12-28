import pandas as pd
from sklearn.externals import joblib


def main():
  file_path = "penguins.csv"
  data = pd.read_csv(file_path)
  path = "penguins_model.joblib"
  model = joblib.load(path)
  return len(data) - 1

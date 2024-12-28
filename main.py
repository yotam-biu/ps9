import pandas as pd

def main():
  file_path = "penguins.csv"
  data = pd.read_csv(file_path)
  return len(data)

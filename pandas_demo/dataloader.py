# pandas

# data loader

import pandas as pd

DATA_PATH = "../data/"
DATA_FILE = "pokemon_data.csv"
dataframe = pd.read_csv(DATA_PATH+DATA_FILE)

print(dataframe.head(5))

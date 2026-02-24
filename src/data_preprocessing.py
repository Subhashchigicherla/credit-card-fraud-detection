import pandas as pd

def preprocess():
    df = pd.read_csv("data/creditcard.csv")
    
    # Features: all columns except Class
    X = df.drop("Class", axis=1)
    
    # Target: Class column
    y = df["Class"]
    
    return X, y
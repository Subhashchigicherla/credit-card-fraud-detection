import pandas as pd
import numpy as np

def generate_data(rows=1000):
    data = {
        "amount": np.random.uniform(10, 5000, rows),
        "old_balance": np.random.uniform(0, 10000, rows),
        "new_balance": np.random.uniform(0, 10000, rows),
        "is_fraud": np.random.randint(0, 2, rows)
    }

    df = pd.DataFrame(data)
    df.to_csv("transactions.csv", index=False)
    return df
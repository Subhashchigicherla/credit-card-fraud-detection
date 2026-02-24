# Credit Card Fraud Detection System

A Streamlit-based web application for detecting credit card fraud using machine learning.

## Features

- User authentication (login/signup)
- Fraud detection prediction
- Data analytics and visualization
- Dashboard with metrics and charts

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/credit-card-fraud-detection.git
   cd credit-card-fraud-detection
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   streamlit run src/app.py
   ```

## Deployment

### To GitHub

1. Create a new repository on GitHub.
2. Push the code:
   ```bash
   git remote add origin https://github.com/yourusername/credit-card-fraud-detection.git
   git push -u origin master
   ```

### To Streamlit Cloud

1. Push the code to GitHub (as above).
2. Go to [share.streamlit.io](https://share.streamlit.io).
3. Connect your GitHub account.
4. Select the repository and branch.
5. Set the main file path to `src/app.py`.
6. Click Deploy.

## Requirements

- Python 3.7+
- Streamlit
- Pandas
- Scikit-learn
- Plotly
- SQLite (for user database)

## Data

The application uses the Credit Card Fraud Detection dataset from Kaggle. Place `creditcard.csv` in the `data/` folder.

## Model

Train the model using:
```bash
  You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
  Network URL: http://192.168.0.237:8501
````

The trained model will be saved as `models/fraud_model.pkl`.

## License

MIT License

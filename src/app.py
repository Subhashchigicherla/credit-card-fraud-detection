import streamlit as st
import pandas as pd
import os
from auth import validate_login, register_user
from utils import load_model, predict

# ---------------- Config ----------------
st.set_page_config(page_title="Credit Card Fraud Detection System", layout="wide")

DATA_PATH = "data/creditcard.csv"
MODEL_PATH = "models/fraud_model.pkl"

# ---------------- Initialize session ----------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.username = ""
if "current_page" not in st.session_state:
    st.session_state.current_page = "Login"

# ---------------- Helpers ----------------
def load_dataset():
    if not os.path.exists(DATA_PATH):
        st.error(f"Dataset not found at {DATA_PATH}. Download it from Kaggle and place in the data folder.")
        st.stop()
    return pd.read_csv(DATA_PATH)

def load_trained_model():
    if not os.path.exists(MODEL_PATH):
        st.error(f"Trained model not found at {MODEL_PATH}. Run 'python src/model_training.py' first.")
        st.stop()
    return load_model()

# ---------------- Login / Signup Page ----------------
def login_page():
    st.title("Credit Card Fraud Detection System")
    st.markdown("---")

    menu = ["Login", "Sign Up"]
    choice = st.selectbox("Menu", menu, index=0)

    if choice == "Login":
        username = st.text_input("Username", key="login_user")
        password = st.text_input("Password", type="password", key="login_pass")
        if st.button("Login", key="login_btn"):
            if validate_login(username, password):
                st.session_state.logged_in = True
                st.session_state.username = username
                st.session_state.current_page = "Overview"
            else:
                st.error("Invalid credentials ❌")

    elif choice == "Sign Up":
        new_user = st.text_input("Username", key="signup_user")
        new_email = st.text_input("Email", key="signup_email")
        new_pass = st.text_input("Password", type="password", key="signup_pass")
        if st.button("Register", key="signup_btn"):
            success = register_user(new_user, new_pass, new_email)
            if success:
                st.success("Registration successful ✅ Check your Gmail to confirm.")
            else:
                st.error("Registration failed ❌ (username/email may already exist)")

# ---------------- Dashboard Page ----------------
def dashboard():
    # ---------- Logout ----------
    st.sidebar.title(f"Welcome, {st.session_state.username}")
    if st.sidebar.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.username = ""
        st.session_state.current_page = "Login"
        return  # Stop dashboard rendering, go back to login page

    # ---------- Sidebar Navigation ----------
    page = st.sidebar.radio("Navigation", ["Overview", "Fraud Alerts", "Analytics"], index=["Overview","Fraud Alerts","Analytics"].index(st.session_state.current_page))
    st.session_state.current_page = page

    df = load_dataset()
    model = load_trained_model()

    # ---------- Overview ----------
    if page == "Overview":
        total_tx = len(df)
        total_fraud = df['Class'].sum()
        fraud_pct = df['Class'].mean() * 100
        avg_amount = df['Amount'].mean()

        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Total Transactions", f"{total_tx}")
        col2.metric("Total Frauds", f"{total_fraud}", delta=f"{fraud_pct:.2f}%")
        col3.metric("Fraud Percentage", f"{fraud_pct:.4f}%")
        col4.metric("Avg Transaction", f"${avg_amount:.2f}")

        st.subheader("Transaction Amount Distribution")
        import plotly.express as px
        fig = px.histogram(df, x="Amount", nbins=50, title="Transaction Amount Distribution")
        st.plotly_chart(fig, use_container_width=True)

    # ---------- Fraud Alerts ----------
    elif page == "Fraud Alerts":
        st.subheader("Predict Fraud for a Transaction")
        sample_idx = st.number_input("Row index", min_value=0, max_value=len(df)-1, value=0)
        input_row = df.drop("Class", axis=1).iloc[[sample_idx]]
        if st.button("Predict Fraud"):
            pred, proba = predict(model, input_row)
            if pred[0] == 1:
                st.error(f"Fraud Detected! Probability: {proba[0]:.2f}")
            else:
                st.success(f"Transaction Safe. Probability of Fraud: {proba[0]:.2f}")

    # ---------- Analytics ----------
    elif page == "Analytics":
        st.subheader("Fraud Analytics")
        import plotly.express as px
        fig = px.box(df, x="Class", y="Amount", color="Class", title="Fraud vs Transaction Amount")
        st.plotly_chart(fig, use_container_width=True)

        corr = df.corr()
        fig = px.imshow(corr, text_auto=True, color_continuous_scale='RdBu_r', title="Correlation Heatmap")
        st.plotly_chart(fig, use_container_width=True)

        feature = st.selectbox("Select feature for grouping", df.columns.drop(['Class']))
        grouped = df.groupby([feature, 'Class']).size().reset_index(name='count')
        fig = px.bar(grouped, x=feature, y='count', color='Class', barmode='group', title=f"Fraud Count by {feature}")
        st.plotly_chart(fig, use_container_width=True)

# ---------------- MAIN ----------------
if st.session_state.logged_in:
    dashboard()
else:
    login_page()
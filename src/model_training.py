from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib
from data_preprocessing import preprocess

def train_model():
    X, y = preprocess()
    
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    
    model = RandomForestClassifier(n_estimators=100, random_state=42, class_weight='balanced')
    model.fit(X_train, y_train)
    
    joblib.dump(model, "models/fraud_model.pkl")
    print("Model trained and saved to models/fraud_model.pkl")
    
    print("Training accuracy:", model.score(X_train, y_train))
    print("Test accuracy:", model.score(X_test, y_test))

if __name__ == "__main__":
    train_model()
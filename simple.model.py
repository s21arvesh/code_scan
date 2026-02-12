from sklearn.linear_model import LogisticRegression
import joblib

model = LogisticRegression()
joblib.dump(model, "model.joblib")

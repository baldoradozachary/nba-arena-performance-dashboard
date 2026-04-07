import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score

# Load data
df = pd.read_csv("nba_arena_data_2026.csv")

# Feature engineering
df["attendance_rate"] = df["attendance"] / df["arena_capacity"]
df["win_flag"] = (df["team_score"] > df["opponent_score"]).astype(int)

# One-hot encode categorical columns
df_model = pd.get_dummies(df, columns=["team", "opponent"], drop_first=True)

# Predict attendance
X = df_model.drop(columns=["attendance", "date"])
y = df_model["attendance"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = RandomForestRegressor(n_estimators=200, random_state=42)
model.fit(X_train, y_train)

preds = model.predict(X_test)

print("Attendance Prediction Model Results")
print(f"MAE: {mean_absolute_error(y_test, preds):.2f}")
print(f"R^2: {r2_score(y_test, preds):.4f}")

feature_importance = pd.DataFrame({
    "feature": X.columns,
    "importance": model.feature_importances_
}).sort_values("importance", ascending=False)

print("\nTop Feature Importances:")
print(feature_importance.head(10).to_string(index=False))

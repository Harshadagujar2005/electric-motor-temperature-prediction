import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import pickle

# ---- Load Dataset ----
df = pd.read_csv("motor_temperature.csv")

# Select features & target
X = df[["ambient_temp", "coolant_temp", "voltage_d", "voltage_q", 
        "motor_speed", "current_d", "current_q"]]
y = df["pm_temperature"]   # target column

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestRegressor()
model.fit(X_train, y_train)

# Save trained model
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ Model trained and saved as model.pkl")

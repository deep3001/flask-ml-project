import numpy as np
import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Sample Data (House size vs. Price)
data = {
    "Size (sq ft)": [500, 700, 900, 1200, 1500, 1800, 2100, 2500, 3000, 3500, 4000, 4500],
    "Price ($1000s)": [150, 180, 220, 260, 300, 340, 380, 420, 470, 520, 570, 620]
}

df = pd.DataFrame(data)

# Split Data
X = df[["Size (sq ft)"]]
y = df["Price ($1000s)"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Model
model = LinearRegression()
model.fit(X_train, y_train)

# Save Model
pickle.dump(model, open("model.pkl", "wb"))

print("Model training complete. Saved as 'model.pkl'.")

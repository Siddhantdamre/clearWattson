from sklearn.ensemble import RandomForestClassifier
import numpy as np

# Example training data (replace with real sensor data)
X_train = np.array([[6.8, 1.2], [7.2, 0.9], [6.5, 1.5]])  # pH and turbidity
y_train = np.array([0, 0, 1])  # 0: Safe, 1: Contaminated

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Predict contamination for new data
new_data = np.array([[7.1, 1.0]])  # New sensor readings
prediction = model.predict(new_data)
print(f"Prediction: {'Contaminated' if prediction[0] else 'Safe'}")

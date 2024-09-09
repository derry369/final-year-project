import pandas as pd
import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import joblib

# Load your data
# Assume the CSV file has columns: 'PacketSize', 'InterDepartureRate', 'Bandwidth'
data = pd.read_csv('traffic_log.csv')

# Define your features and target variable
X = data[['Packet Size (bytes)', 'Inter-Departure Rate (packets/second)']]
y = data['Bandwidth Required (Mbps)']

# Create polynomial features (degree 2, can be adjusted)
poly = PolynomialFeatures(degree=2, include_bias=False)
X_poly = poly.fit_transform(X)

# Train the polynomial regression model
model = LinearRegression()
model.fit(X_poly, y)

# Predict the target variable using the trained model
y_pred = model.predict(X_poly)

# Calculate performance metrics
mse = mean_squared_error(y, y_pred)
r2 = r2_score(y, y_pred)

# Save the trained model
joblib.dump((model, poly), 'polynomial_regression_model.pkl')

# Print performance evaluation metrics
print("Mean Squared Error (MSE):", mse)
print("R² Score:", r2)
print("Model trained and saved successfully.")


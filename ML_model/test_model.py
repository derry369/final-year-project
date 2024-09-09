import numpy as np
import joblib

# Load the trained model and polynomial feature transformer
model, poly = joblib.load('polynomial_regression_model.pkl')

def predict_bandwidth(packet_size, inter_departure_rate):
    # Prepare the input data
    input_features = np.array([[packet_size, inter_departure_rate]])
    
    # Generate polynomial features
    input_poly = poly.transform(input_features)
    
    # Predict the bandwidth
    predicted_bandwidth = model.predict(input_poly)[0]
    
    # Ensure non-negative bandwidth
    return max(0, round(predicted_bandwidth, 2))

# Example usage
if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: python predict_bandwidth.py <packet_size> <inter_departure_rate>")
    else:
        packet_size = int(sys.argv[1])
        inter_departure_rate = int(sys.argv[2])
        
        predicted_bandwidth = predict_bandwidth(packet_size, inter_departure_rate)
        print("Predicted Bandwidth (Mbps):", predicted_bandwidth)

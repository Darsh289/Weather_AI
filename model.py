import numpy as np
from sklearn.linear_model import LinearRegression

# Training Data (Example)
X = np.array([
    [30, 70, 1010],
    [32, 65, 1008],
    [25, 80, 1005],
    [28, 75, 1007]
])

y = np.array([31, 33, 26, 29])  # Next day temperature

model = LinearRegression()
model.fit(X, y)

def predict_weather(temp, humidity, pressure):
    prediction = model.predict([[temp, humidity, pressure]])
    return round(prediction[0],2)
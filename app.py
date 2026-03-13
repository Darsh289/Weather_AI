from flask import Flask, render_template, request
from weather_api import get_weather
from model import predict_weather

# Create Flask app
app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def home():

    prediction = None
    city = None
    temp = None
    humidity = None
    pressure = None
    condition = None

    if request.method == "POST":

        city = request.form["city"]

        data = get_weather(city)

        if data:
            temp = data["temp"]
            humidity = data["humidity"]
            pressure = data["pressure"]
            condition = data["condition"]

            prediction = predict_weather(temp, humidity, pressure)

    return render_template(
        "index.html",
        city=city,
        temp=temp,
        humidity=humidity,
        pressure=pressure,
        prediction=prediction,
        condition=condition
    )

if __name__ == "__main__":
    app.run(debug=True)
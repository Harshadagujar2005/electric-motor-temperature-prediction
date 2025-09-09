from flask import Flask, render_template_string, request
import pickle
import numpy as np

# Load trained model
model = pickle.load(open("model.pkl", "rb"))

app = Flask(__name__)

# Simple HTML template
html_template = """
<!DOCTYPE html>
<html>
<head>
    <title>Electric Motor Temperature Prediction</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; }
        .container { max-width: 500px; margin: auto; padding: 20px; border: 1px solid #ddd; border-radius: 10px; }
        h2 { text-align: center; }
        label { display: block; margin-top: 10px; }
        input { width: 100%; padding: 8px; margin-top: 5px; }
        button { margin-top: 15px; width: 100%; padding: 10px; background: #007BFF; color: white; border: none; border-radius: 5px; }
        .result { margin-top: 20px; font-size: 18px; color: red; text-align: center; }
    </style>
</head>
<body>
    <div class="container">
        <h2>Electric Motor Temperature Prediction</h2>
        <form method="POST">
            <label>Ambient Temp:</label><input type="number" name="ambient_temp" required>
            <label>Coolant Temp:</label><input type="number" name="coolant_temp" required>
            <label>Voltage d:</label><input type="number" step="any" name="voltage_d" required>
            <label>Voltage q:</label><input type="number" step="any" name="voltage_q" required>
            <label>Motor Speed:</label><input type="number" name="motor_speed" required>
            <label>Current d:</label><input type="number" step="any" name="current_d" required>
            <label>Current q:</label><input type="number" step="any" name="current_q" required>
            <button type="submit">Submit</button>
        </form>
        {% if result is not none %}
            <div class="result">Predicted Temperature: {{ result }} °C</div>
        {% endif %}
    </div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        # Get form values
        values = [float(request.form.get(col)) for col in 
                  ["ambient_temp", "coolant_temp", "voltage_d", "voltage_q", "motor_speed", "current_d", "current_q"]]
        prediction = model.predict([np.array(values)])[0]
        result = round(prediction, 2)
    return render_template_string(html_template, result=result)

if __name__ == "__main__":
    app.run(debug=True)

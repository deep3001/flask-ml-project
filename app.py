from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np

app = Flask(__name__ , template_folder="template")

# Load the trained model
model = pickle.load(open("model.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")  # ✅ Ensure the template is correct

@app.route("/predict", methods=["POST"])  # ✅ Must be POST
def predict():
    try:
        # Get input from form
        size = float(request.form["size"])
        prediction = model.predict([[size]])  # Predict using model
        
        # ✅ Return prediction properly
        return render_template("index.html", prediction_text=f"Predicted Price: ${prediction[0]:,.2f}")
    
    except Exception as e:
        return jsonify({"error": str(e)})  # Show error message if needed

if __name__ == "__main__":
    app.run(debug=True)

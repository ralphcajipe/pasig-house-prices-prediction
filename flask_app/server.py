from flask import Flask, request, render_template
import ydf

app = Flask(__name__)

# Load the model
model = ydf.from_tensorflow_decision_forests("../models/pasig-model")

@app.route('/', methods=['GET', 'POST'])
def predict():
    data = {
        "Bedrooms": "",
        "Bath": "",
        "Floor_area_sqm": "",
        "Latitude": "",
        "Longitude": "",
    }
    prediction = None
    formatted_prediction = None

    if request.method == 'POST':
        data = request.form.to_dict()
        examples = {
            "Bedrooms" : [int(data['Bedrooms'])],
            "Bath" : [int(data['Bath'])],
            "Floor_area_sqm" : [int(data['Floor_area_sqm'])],
            "Latitude" : [float(data['Latitude'])],
            "Longitude" : [float(data['Longitude'])],
        }
        prediction = model.predict(examples)
        formatted_prediction = "{:,}".format(prediction[0])

    return render_template('index.html', prediction=formatted_prediction, data=data)

if __name__ == '__main__':
    app.run(port=5000, debug=True)
    
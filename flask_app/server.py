from flask import Flask, request, render_template, jsonify
import ydf

app = Flask(__name__)

# Load the model
model = ydf.from_tensorflow_decision_forests("./models/pasig-model")

@app.route('/', methods=['GET', 'POST'])
def predict():
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
        return jsonify({'prediction': formatted_prediction, 'data': data})

    return render_template('index.html')

if __name__ == '__main__':
    app.run(port=5000, debug=True)
    
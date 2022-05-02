import os
import cloudpickle
from flask import Flask

app = Flask(__name__)


@app.route('/predict', methods=['POST'])
def predict():
    pickler = cloudpickle.load('phish-model-1649995335.cloudpickle')
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        response_object['message'] = post_data



if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))

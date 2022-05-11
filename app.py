from flask import Flask, request
import numpy as np
import pandas as pd
import pickle
import os
from error import Property
from pydantic import ValidationError

app = Flask(__name__)

modelfile = "finalized_model.sav"
model = pickle.load(open(modelfile, "rb"))     

@app.route("/")
def alive():
    return "alive"

@app.route("/predict", methods=["GET"])
def predict_get():
    format = '''{
        "data": {
            "area": int,
            "property-type": Optional["APARTMENT" | "HOUSE" | "OTHERS"],
            "rooms-number": Optional[int],
            "zip-code": Optional[int],
            "land-area": Optional[int],
            "garden": Optional[bool],
            "garden-area": Optional[int],
            "equipped-kitchen": Optional[bool],
            "full-address": Optional[str],
            "swimming-pool": Optional[bool],
            "furnished": Optional[bool],
            "open-fire": Optional[bool],
            "terrace": Optional[bool],
            "terrace-area": Optional[int],
            "facades-number": Optional[int],
            "building-state": Optional["NEW" | "GOOD" | "TO RENOVATE" | "JUST RENOVATED" | "TO REBUILD"]
            }
        }'''        
    return format

@app.route("/predict", methods=["POST"])
def predict_post():
    json_data = request.get_json()
    try:
        valid_property = Property(**json_data['data'])
    except ValidationError as e:
        return e.json()
    property = valid_property.dict()
    data_array = np.array([property["area"]]).reshape(-1, 1)
    return {"prediction" : model.predict(data_array)[0][0]}

if __name__ == "__main__":
    port = os.environ.get("PORT", 5000)
    app.run(host="0.0.0.0", port=port)

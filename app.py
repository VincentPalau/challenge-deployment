from flask import Flask, request, jsonify
import numpy as np
import pandas as pd
import pickle

app = Flask(__name__)

modelfile = "finalized_model.sav"
model = pickle.load(open(modelfile, "rb"))

@app.route("/predict", methods=["POST"])
def predict():
    json_data = request.get_json()["data"]
    data_array = np.array([json_data["area"]]).reshape(-1, 1)
    return str(model.predict(data_array))

# @app.route("/", methods=["GET"])
# def alive():
#     if server alive
#     return "alive"

# @app.route("/predict", methods=["GET", "POST"])
# if methods == "POST":
#     def predict():
#         json_data = request.get_json()["data"]
#         data_array = np.array([json_data["area"]]).reshape(-1, 1)
#         return str(model.predict(data_array))
# elif methods == "GET":
#     def explain():
#         format = {
#             "data": {
#                 "area": int,
#                 "property-type": "APARTMENT" | "HOUSE" | "OTHERS", # optional
#                 "rooms-number": int, # optional
#                 "zip-code": int, # optional
#                 "land-area": int, # optional
#                 "garden": bool, # optional
#                 "garden-area": int, # optional
#                 "equipped-kitchen": bool, # optional
#                 "full-address": str, # optional
#                 "swimming-pool": bool, # optional
#                 "furnished": bool, # optional
#                 "open-fire": bool, # optional
#                 "terrace": bool, # optional
#                 "terrace-area": int, # optional
#                 "facades-number": int, # optional
#                 "building-state": "NEW" | "GOOD" | "TO RENOVATE" | "JUST RENOVATED" | "TO REBUILD" # optional
#                 }
#             }
#         return "Fill in the data in the following format : " + format

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)

from flask import request
import numpy as np

def preprocess():
    """Take data from a new house as input and return those data preprocessed as output"""
    json_data = request.get_json()["data"]
    data_array = np.array([json_data["area"]]).reshape(-1, 1)
    return data_array

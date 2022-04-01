import pickle
from preprocessing import cleaning_data

data_array = cleaning_data.preprocess()
modelfile = "finalized_model.sav"
model = pickle.load(open(modelfile, "rb"))
model.predict(data_array)

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle

df = pd.read_csv(r"C:\Users\vpala\Artificial Intelligence\BeCode\challenge-deployment\properties_clean.csv")

y = np.array(df["Price"])
x = np.array(df["Living area"])

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.30, random_state=1)

X_train = X_train.reshape(-1, 1)
y_train = y_train.reshape(-1, 1)
regressor = LinearRegression().fit(X_train, y_train)
regressor.score(X_train, y_train)

X_test = X_test.reshape(-1, 1)
regressor.predict(X_test)
regressor.score(X_test, y_test)

# save model to disk
filename = "finalized_model.sav"
pickle.dump(regressor, open(filename, "wb"))

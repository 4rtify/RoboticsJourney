# Save Model Using Pickle
from pandas import read_csv
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from pickle import dump
from pickle import load
filename = 'pima-indians-diabetes.data.csv'
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
dataframe = read_csv(filename, names=names)
array = dataframe.values
X = array[:,0:8]
Y = array[:,8]
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.33, random_state=7)
# Fit the model on 33%
model = LogisticRegression(solver='liblinear')
model.fit(X_train, Y_train)
# save the model to disk
filename = 'finalized_model.sav'
dump(model, open(filename, 'wb'))

# some time later...

# load the model from disk
loaded_model = load(open(filename, 'rb'))
result = loaded_model.score(X_test, Y_test)
print(result)


import joblib
joblib.dump(model, 'model_filename.pkl')

# Transfer or email file:

# Load the File:
loaded_model = joblib.load('model_filename.pkl') 

# Predict with New Unseen Data:
new_data = [...]  # Replace with actual new data
predictions = loaded_model.predict(new_data)
print(predictions)




@inproceedings{Street1993NuclearFE,
  title={Nuclear feature extraction for breast tumor diagnosis},
  author={William Nick Street and William H. Wolberg and Olvi L. Mangasarian},
  booktitle={Electronic imaging},
  year={1993},
  url={https://api.semanticscholar.org/CorpusID:14922543}
}
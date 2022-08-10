import pandas as pd


# save filepath to variable for easier access
melbourne_file_path = 'melb_data.csv'
# read the data and store data in DataFrame titled melbourne_data
melbourne_data = pd.read_csv(melbourne_file_path)
# print(melbourne_data.columns) # <== columns just returns an list of the headings of each column in the dataset
melbourne_data.columns

# save a copy of the DataFrame with any data that is not available (.dropna(axis=)) and store it in the variable melbourne_data
melbourne_data = melbourne_data.dropna(axis=0)
# print(melbourne_data)

# By convention the prediction target is called y
y = melbourne_data.Price

# We create a feature variable labled melbourne_feature to store only the columns (or features) that we want to include in our dataset
melbourne_feature = ["Rooms", "Bathroom", "Landsize", "Lattitude", "Longtitude"]

# By convention the Data is called X 
X = melbourne_data[melbourne_feature]
# Remember that the describe() method will print a summary of the data and in this case that data will be the Columns stored in melbourne_feature which are then specifically referenced in the melbourne_data data set which is now stored in X
print(X.describe()) # <== We need to frequently check our data with the describe() method
# head() is a method which shows the five top rows
print(X.head())  

# The steps to building and using a model are:

#     Define: What type of model will it be? A decision tree? Some other type of model? Some other parameters of the model type are specified too.
#     Fit: Capture patterns from provided data. This is the heart of modeling.
#     Predict: Just what it sounds like
#     Evaluate: Determine how accurate the model's predictions are.

from sklearn.tree import DecisionTreeRegressor

# Define model. Specify a number for random_state to ensure same results each run
melbourne_model = DecisionTreeRegressor(random_state=1)

# Fit model
melbourne_model.fit(X, y)

print("Making predictions for the following 5 houses:")
print(X.head())
print("The predictions are")
print(melbourne_model.predict(X.head()))


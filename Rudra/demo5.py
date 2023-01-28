import pandas as pd
from sklearn.model_selection import train_test_split
from keras.models import Sequential                         #pip install keras      #pip install tensorflow
from keras.layers import Dense

# Load the data
FileName = "USA_Housing.csv"
FilePath = pd.read_csv(FileName)
Data = FilePath.dropna(axis=0)

# Split the data into features and target
Y = Data.Price
Data_Features = ["Avg. Area Income","Avg. Area House Age","Avg. Area Number of Rooms","Avg. Area Number of Bedrooms","Area Population"]
X = Data[Data_Features]

# Split the data into train and test sets
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

# Create the model
model = Sequential()
model.add(Dense(10, input_dim=5, activation='relu'))
model.add(Dense(10, activation='relu'))
model.add(Dense(1))

# Compile the model
model.compile(loss='mean_squared_error', optimizer='adam')

# Fit the model to the training data
model.fit(X_train, Y_train, epochs=50, batch_size=32)

# Evaluate the model on the test data
test_loss = model.evaluate(X_test, Y_test)
print(test_loss)

# Get new inputs from user
new_income = float(input("Enter the average income: "))
new_age = float(input("Enter the average house age: "))
new_rooms = float(input("Enter the average number of rooms: "))
new_bedrooms = float(input("Enter the average number of bedrooms: "))
new_population = float(input("Enter the area population: "))
new_data = [[new_income, new_age, new_rooms, new_bedrooms, new_population]]

# Use the model to predict the price of the new inputs
price = model.predict(new_data)
print("The predicted price of the house is: ", price[0])
import pandas as pd
from sklearn.model_selection import train_test_split
from keras.models import Sequential                         #pip install keras      #pip install tensorflow
from keras.layers import Dense

# Load the data
FileName = "mars-weather.csv"
FilePath = pd.read_csv(FileName)
Data = FilePath.dropna(axis=0)

# Split the data into features and target
Y = Data.pressure
Data_Features = ["id","sol","min_temp","max_temp"]
X = Data[Data_Features]

# Split the data into train and test sets
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)


# Create the model
model = Sequential()
model.add(Dense(10, input_dim=4, activation='relu'))
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
new_id = int(input("Enter the id: "))
new_sol = int(input("Enter the sol: "))
new_min_temp = int(input("Enter the min_temp: "))
new_max_temp = int(input("Enter the max_temp: "))
new_data = [[new_id, new_sol, new_min_temp, new_max_temp]]

# Use the model to predict the price of the new inputs
pressure = model.predict(new_data)
print("The predicted pressure on the Mars is: ", pressure[0])
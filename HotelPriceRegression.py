import pandas as pd 
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

#Load Dataset
hotel_dataset = pd.read_csv('Hotels.csv')

#Define explanatory variables and a dependant variable
X = hotel_dataset[['Hotel_star_rating', 'Distance', 'Customer_rating', 'Squares']]

y = hotel_dataset['Price(BAM)']

#Divide the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split (X, y, test_size=.40, random_state=101)

#Train the model
linear = LinearRegression()

linear.fit(X_train, y_train)

#Get variation coefficients
coeff = pd.DataFrame(linear.coef_, X.columns, columns=['Coefficient'])

#Test using the test set
predictions = linear.predict(X_test)

print('MAE:', metrics.mean_absolute_error(y_test, predictions)) 
print('MSE:', metrics.mean_squared_error(y_test, predictions)) 
print('RMSE:', np.sqrt(metrics.mean_squared_error(y_test, predictions))) 

#Predicting the price of a new hotel
cols = ["Hotel_star_rating", "Distance", "Customer_rating", "Squares"]

hotel_star_rating = float(input("Rating of the hotel (From 1 to 5): "))
distance = float(input("Distance from the hotel to midtown (in mts): "))
customer_rating = float(input("Public rating by users (From 1 to 10): "))
squares = float(input("How big is the room? (in square meters) "))

# Create data frame with predictions
df_pred = pd.DataFrame([(hotel_star_rating, distance, customer_rating, squares)], columns = cols)
print("\nThe price of the hotel will be of %i " %round(linear.predict(df_pred)[0]))
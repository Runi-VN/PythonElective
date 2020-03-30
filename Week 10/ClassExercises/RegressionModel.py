import sklearn.linear_model
import pandas as pd
import numpy as np

# save data in a file: car_sales.csv
# plot car sales as a function to GDP (is there a linear relationship?)
# fit data to a sklearn linear regression model
# predict sales if GDP hits 9 trillion lakhs

data = pd.read_csv("car_sales.csv")
print(data)

xs = data['GDP(trillion)']
ys = data['4wheeler_car_sale']
xs_reshape = np.array(xs).reshape(-1, 1)
print(xs)
print(xs.shape)
print(xs_reshape.shape)
print(xs_reshape)


model = sklearn.linear_model.LinearRegression()
model.fit(xs_reshape, ys)
print(model.coef_)
print(model.intercept_)

predicted = model.predict(xs_reshape)
print(predicted)
spending_9tril = model.predict([[9]])
print('9 trillion GDP means this much car sales: {}'.format(spending_9tril[0]))

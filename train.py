import os
import pandas as pd
import pandas.errors as pd_errors

def read_data(file):
    with open(file, 'r') as f:
        next(f)
        mileage = []
        price = []
        for line in f:
            val = line.split(',')
            mileage.append(float(val[0]))
            price.append(float(val[1]))
    return mileage, price


def save_param(theta0, theta1, file):
    with open(file, 'w') as f:
        f.write(str(theta0) + ',' + str(theta1))
        

def normalize_data(column):
    min_val = min(column)
    max_val = max(column)
    range_val = max_val - min_val
    normalized_column = [(val - min_val) / range_val for val in column]
    return normalized_column
    

def denormalize_data(column, max_val, min_val):
    range_val = max_val - min_val
    denormalized_column = [val * range_val + min_val for val in column]
    return denormalized_column


def linear_regression(mileageNorm, priceNorm, learning_rate, epochs):

    theta0 = 0.0
    theta1 = 0.0

    for _ in range(epochs):
        tmp0 = 0.0
        tmp1 = 0.0
        for i in range(len(mileageNorm)):
            predicted = theta0 + (theta1 * mileageNorm[i])
            tmp0 += (predicted - priceNorm[i])
            tmp1 += (predicted - priceNorm[i]) * mileageNorm[i]
        theta0 -= ((learning_rate * tmp0) / len(mileageNorm))
        theta1 -= ((learning_rate * tmp1) / len(mileageNorm))

    return theta0, theta1


def main():
    
    if not os.path.isfile('data.csv'):
        print("The data file is missing")
        return
    
    try:
        data = pd.read_csv('data.csv', delimiter=",", skiprows=1 ,dtype="float")
    except pd_errors.EmptyDataError:
        print("The data is empty")
        return
    
    km = data.iloc[:, 0]
    price = data.iloc[:, 1]

    normalized_km = normalize_data(km)
    normalized_price = normalize_data(price)

    learning_rate = 0.1
    epochs = 1000
    theta0, theta1 = linear_regression(normalized_km, normalized_price, learning_rate, epochs)
    save_param(theta0, theta1, 'parameters.txt')


if __name__ == "__main__":
    main()
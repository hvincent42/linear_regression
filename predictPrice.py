import os
import pandas as pd
import pandas.errors as pd_errors


def read_para(file):
    with open(file, 'r') as f:
        thetas = f.read().split(',')

    try:
        theta0 = float(thetas[0])
        theta1 = float(thetas[1])
    except ValueError:
        return 0, 0
    return theta0, theta1

def estimatePrice(mileage, theta0, theta1):
    return theta0 + (theta1 * mileage)

def main():

    if not os.path.isfile('parameters.txt'):
        print("The parameters file is missing")
        return
    
    theta0, theta1 = read_para('parameters.txt')

    if theta0 == 0 and theta1 == 0:
        print("Model not trained or value error")
        return
    
    try:
        data = pd.read_csv('data.csv', delimiter=",", skiprows=1 ,dtype="float")
    except pd_errors.EmptyDataError:
        print("The data is empty")
        return

    mileage = data.iloc[:, 0]
    price = data.iloc[:, 1]

    while True:
        try:
            mileageInput = int(input("Enter the mileage of car: "))
            break
        except ValueError:
            print("Please enter a valid number for mileage.")


    normMileage = (mileageInput - min(mileage)) / (max(mileage) - min(mileage))

    result = theta0 + (theta1 * normMileage)
    
    result = result * (max(price) - min(price)) + min(price)

    print(f"The estimated price of a car with a mileage of {int(mileageInput)} is", int(result))


if __name__ == "__main__":
    main()
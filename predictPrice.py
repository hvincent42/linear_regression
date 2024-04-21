import pandas as pd

def read_parameters(file):
    with open(file, 'r') as f:
        thetas = f.read().split(',')
    return float(thetas[0]), float(thetas[1])


def estimatePrice(mileage, theta0, theta1):
    return theta0 + (theta1 * mileage)


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


def main():

    theta0, theta1 = read_parameters('parameters.txt')
    mileageInput = float(input("Enter the mileage of car: "))

    data = pd.read_csv('data.csv', delimiter=",", skiprows=1 ,dtype="float")
    mileage = data.iloc[:, 0]
    price = data.iloc[:, 1]

    new_mileage = (mileageInput - min(mileage)) / (max(mileage) - min(mileage))

    result = theta1 * new_mileage + theta0
    
    result = result * (max(price) - min(price)) + min(price)

    print(f"The estimated price of the car is with a mileage of {mileageInput}: ", result)


if __name__ == "__main__":
    main()
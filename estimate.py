
from train import training

def estimate():
    try:
        w0 = 0
        w1 = 0
        mileage = float(input("Input mileage: "))
        learningRate = 0.01
        iteration = 10000

        w0, w1 = training(w0, w1, learningRate, iteration)

        estimation = w0 + w1 * mileage
        #print(f"w0, w1 : {w0}, {w1}")
        print(f"estimation: {estimation}")

    except AssertionError as e:
        print(e)
    except ValueError:
        print("Error: Invalid mileage input")


if __name__ == "__main__":
    estimate()

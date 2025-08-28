# Import necessary libraries.
from stock_prediction.data_load import prepare_data
from stock_prediction.train_evaluate import train_and_evaluate
from stock_prediction.plot import plot_results
from stock_prediction.predict import predict

# Define min function to run the model.
def main():
    X, y = prepare_data()
    model, x_test, y_test, y_pred = train_and_evaluate(X, y)
    plot_results(x_test, y_test, y_pred)
    prediction = predict()

if __name__ == "__main__":
    main()
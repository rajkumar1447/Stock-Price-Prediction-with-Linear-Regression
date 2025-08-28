# Import necessary Libraries.
import matplotlib.pyplot as plt

# Function to plot the results.
def plot_results(x_test, y_test, y_pred):
    """Plot actual vs predicted stock prices."""
    plt.figure(figsize=(10, 6))
    plt.plot(x_test, y_test, label='Actual Stock Prices', marker='o')
    plt.plot(x_test, y_pred, label='Predicted Stock Prices', marker='x')
    plt.title("Actual vs Predicted Stock Prices")
    plt.xlabel("Date (ordinal)")
    plt.ylabel("Stock Price ($)")
    plt.legend()
    plt.show()
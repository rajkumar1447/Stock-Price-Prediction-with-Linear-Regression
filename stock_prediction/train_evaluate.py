# Import necessary libraries.
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

# Function to Train and evaluate the model.
def train_and_evaluate(X, y):
    """Split data, train Linear Regression model, and evaluate it."""
    x_train, x_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = LinearRegression()
    model.fit(x_train, y_train)

    y_pred = model.predict(x_test)

    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    print(f"\nMean Squared Error: {mse:.2f}")
    print(f"R2 Score: {r2:.2f}")

    return model, x_test, y_test, y_pred
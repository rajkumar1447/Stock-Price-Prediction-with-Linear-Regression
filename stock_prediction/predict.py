# Import Necessary Libraries.
import pandas as pd
from .train_evaluate import train_and_evaluate
from .data_load import prepare_data

# Function to predict with the new data.
def predict():
    # prepare data
    x, y = prepare_data()
    
    # train model
    model, x_test, y_test, y_pred = train_and_evaluate(x, y)

    # future date prediction
    future_date = pd.Timestamp('2025-12-12').toordinal()
    future_date = pd.DataFrame({'Date': [future_date]})
    
    predicted_price = model.predict(future_date)
    return predicted_price[0]
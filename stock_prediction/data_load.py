# Import necessary Packages.
import pandas as pd

# Function to load the data.
def prepare_data():
    data = {
    'Date': pd.date_range(start='2025-01-01', periods=10, freq='D'),
    'Close': [150,158,152,180,160,164,185,140,158,165]
    }
    
    df = pd.DataFrame(data)

    # Convert datetime to ordinal numbers for regression
    df['Date'] = df['Date'].map(pd.Timestamp.toordinal)

    x = df[['Date']]
    y = df['Close']

    return x, y
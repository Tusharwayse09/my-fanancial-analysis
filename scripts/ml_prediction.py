import numpy as np
from sklearn.linear_model import LinearRegression


def predict_future_growth(values, years_ahead=3):
    """
    values: list of historical values
    returns: list of future predictions
    """

    if len(values) < 2:
        return []

    X = np.array(range(len(values))).reshape(-1, 1)
    y = np.array(values)

    model = LinearRegression()
    model.fit(X, y)

    future_X = np.array(
        range(len(values), len(values) + years_ahead)
    ).reshape(-1, 1)

    predictions = model.predict(future_X)

    return [round(float(p), 2) for p in predictions]

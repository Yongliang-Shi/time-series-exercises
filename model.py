import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.metrics import mean_squared_error
from math import sqrt

import warnings
warnings.filterwarnings("ignore")

# %%
def evaluate(target_var):
    """
    Compute the Mean Squared Error and the Root Mean Squared Error to evaluate.
    Parameter: target variable
    """
    rmse = round(sqrt(mean_squared_error(validate[target_var], yhat_df[target_var])), 0) # How about validate, yhat_df
    return rmse

# %%
def plot_and_eval(target_var):
    """
    Use the evaluate function and also plot train and test values with the predicted values in order to compare performance. 
    Need to have train, validate and yhat_df datasets before use the function
    Can be used in a for loop
    """
    plt.figure(figsize = (12,4))
    plt.plot(train[target_var], label = 'Train', linewidth = 1)
    plt.plot(validate[target_var], label = 'Validate', linewidth = 1)
    plt.plot(yhat_df[target_var])
    plt.title(target_var)
    rmse = evaluate(target_var)
    print(target_var, '-- RMSE: {:.0f}'.format(rmse))
    plt.show()

# %%
def append_eval_df(model_type, target_var):
    """
    To append evaluation metrics for each model type, target variable and metric type
    Parameters: model_type and target_var
    Need to have the eval_df before use the function
    """
    rmse = evaluate(target_var)
    d = {'model_type': [model_type], 'target_var': [target_var], 'rmse': [rmse]}
    d = pd.DataFrame(d)
    return eval_df.append(d, ignore_index = True)
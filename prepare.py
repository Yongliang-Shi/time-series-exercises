import warnings
warnings.filterwarnings("ignore")

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from datetime import timedelta, datetime
from time import strftime

# %%
def prep_store(store):
    """
    Prepare store data for exploration
    """
    store.sale_date = pd.to_datetime(store.sale_date, format='%a, %d %b %Y %H:%M:%S %Z') # Convert to datetime
    store.sale_date = pd.to_datetime(store.sale_date.dt.date)  # Remove the time from the date
    store = store.set_index('sale_date').sort_index()
    store['month'] = store.index.month
    store['day_of_week'] = store.index.day_name()
    store['sales_total'] = store.sale_amount * store.item_price
    return store

def prep_ops(ops):
    ops.Date = pd.to_datetime(ops.Date) # Convert to datetime 
    ops = ops.set_index('Date').sort_index() # Set Date as index
    ops['month'] = ops.index.month
    ops['year'] = ops.index.year
    ops.fillna(0, inplace=True)
    return ops
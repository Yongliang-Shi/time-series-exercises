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
    store.sale_date = pd.to_datetime(store.sale_date, format='%a, %d %b %Y %H:%M:%S %Z')
    store = store.set_index('sale_date').sort_index()
    store['month'] = store.index.month
    store['day_of_week'] = store.index.day_name()
    store['sales_total'] = store.sale_amount * store.item_price
    return store
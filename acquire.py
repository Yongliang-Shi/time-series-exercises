import warnings
warnings.filterwarnings("ignore")

import numpy as np
import pandas as pd
import requests
import os

# %%
def get_items():
    filename = 'df_items.csv'
    if os.path.isfile(filename):
        return pd.read_csv(filename, index_col=0)
    else: 
        base_url = 'https://python.zach.lol'
        response = requests.get(base_url + '/api/v1/items')
        items = response.json()
        df_items = pd.DataFrame(items['payload']['items'])
        pages = 2
        for page in range(0, pages):
            response = requests.get(base_url + items['payload']['next_page'])
            items = response.json()
            df_items = pd.concat([df_items, pd.DataFrame(items['payload']['items'])])
        return df_items

# %%
def get_stores():
    filename = 'df_stores.csv'
    if os.path.isfile(filename):
        return pd.read_csv(filename, index_col=0)
    else: 
        response = requests.get('https://python.zach.lol/api/v1/stores')
        stores = response.json()
        df_stores = pd.DataFrame(stores['payload']['stores'])
        return df_stores

# %%
def get_sales():
    filename = 'df_sales.csv'
    if os.path.isfile(filename):
        return pd.read_csv(filename, index_col=0)
    else: 
        # Create a base_url
        base_url = 'https://python.zach.lol'

        # Load the first page of the data
        response = requests.get(base_url + '/api/v1/sales')
        sales = response.json()

        # Conver the data to df
        df_sales = pd.DataFrame(sales['payload']['sales'])

        # For loop the rest of the pages

        pages = 182
        for page in range(0, pages):
            response = requests.get(base_url + sales['payload']['next_page'])
            sales = response.json()
            df_sales = pd.concat([df_sales, pd.DataFrame(sales['payload']['sales'])])
        return df_sales

# %%
def get_store_sales():
    filename = 'store_sales.csv'
    if os.path.isfile(filename):
        return pd.read_csv(filename, index_col=0)
    else: 
        df_sales = get_sales()
        df_stores = get_stores()
        df_items = get_items()
        df = df_sales.set_index('store').join(df_stores.set_index('store_id'))
        df = df.set_index('item').join(df_items.set_index('item_id'))
        df.set_index('sale_id', inplace=True)
        return df

# %%
def get_opsd_germany():
    filename = 'opsd_germany.csv'
    if os.path.isfile(filename):
        return pd.read_csv(filename, index_col=0)
    else: 
        df_opsd = pd.read_csv('https://raw.githubusercontent.com/jenfly/opsd/master/opsd_germany_daily.csv', index_col=0)
        return df_opsd
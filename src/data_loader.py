import pandas as pd

def load_viewing_data(path):
    return pd.read_csv(path)

def load_clickstream_data(path):
    return pd.read_csv(path)

def load_devices_data(path):
    return pd.read_csv(path)

def load_profiles_data(path):
    return pd.read_csv(path)

def load_search_history_data(path):
    return pd.read_csv(path)

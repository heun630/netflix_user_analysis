import pandas as pd
def preprocess_viewing_data(df):
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['hour'] = df['Start Time'].dt.hour
    df['weekday'] = df['Start Time'].dt.day_name()
    return df

def preprocess_devices_data(df):
    device_type_mapping = {
        'Device Type 0': 'TV',
        'Device Type 1': 'Smartphone',
        'Device Type 2': 'Tablet',
        'Device Type 3': 'Game Console',
        'Device Type 4': 'Netflix Stick',
        'Device Type 5': 'Media Player',
        'Device Type 6': 'PC',
        'Device Type 7': 'Smart TV',
        'Device Type 8': 'Set-top Box',
        'Device Type 9': 'Other Device',
        'Device Type 10': 'Projector'
    }
    df['Device Type Name'] = df['Device Type'].map(device_type_mapping)
    return df

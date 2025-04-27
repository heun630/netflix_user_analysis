def analyze_hourly_views(df):
    return df['hour'].value_counts().sort_index()

def analyze_weekday_views(df):
    weekday_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    return df['weekday'].value_counts().reindex(weekday_order)

def analyze_device_views(df_devices):
    return df_devices['Device Type Name'].value_counts()

def analyze_top_titles(df, top_n=10):
    return df['Title'].value_counts().head(top_n)

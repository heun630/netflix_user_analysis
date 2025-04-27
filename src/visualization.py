import matplotlib.pyplot as plt
import seaborn as sns

def plot_hourly_views(hourly_views):
    plt.figure(figsize=(10,6))
    sns.lineplot(x=hourly_views.index, y=hourly_views.values, marker='o')
    plt.title('Netflix Viewing Activity by Hour')
    plt.xlabel('Hour of the Day')
    plt.ylabel('Number of Views')
    plt.grid(True)
    plt.show()

def plot_weekday_views(weekday_views):
    plt.figure(figsize=(10,6))
    sns.barplot(x=weekday_views.index, y=weekday_views.values)
    plt.title('Netflix Viewing Activity by Day of the Week')
    plt.xlabel('Day of the Week')
    plt.ylabel('Number of Views')
    plt.xticks(rotation=45)
    plt.show()

def plot_device_views(device_views):
    plt.figure(figsize=(8,8))
    plt.pie(device_views, labels=device_views.index, autopct='%1.1f%%', startangle=140)
    plt.title('Viewing Distribution by Device Type')
    plt.show()

def plot_top_titles(top_titles):
    plt.figure(figsize=(10,6))
    sns.barplot(x=top_titles.values, y=top_titles.index)
    plt.title('Top 10 Most Watched Titles')
    plt.xlabel('Number of Views')
    plt.ylabel('Title')
    plt.show()

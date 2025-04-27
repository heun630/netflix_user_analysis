import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd

# 데이터 불러오기
viewing_df = pd.read_csv('outputs/processed_viewing_activity.csv')
devices_df = pd.read_csv('outputs/processed_devices.csv')

# 시간대별 시청량 준비
hourly_views = viewing_df['hour'].value_counts().sort_index()
fig_hourly = px.line(x=hourly_views.index, y=hourly_views.values, markers=True,
                     labels={'x': 'Hour of Day', 'y': 'Number of Views'},
                     title='Viewing Activity by Hour')

# 요일별 시청량 준비
weekday_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
weekday_views = viewing_df['weekday'].value_counts().reindex(weekday_order)
fig_weekday = px.bar(x=weekday_views.index, y=weekday_views.values,
                     labels={'x': 'Day of the Week', 'y': 'Number of Views'},
                     title='Viewing Activity by Day of the Week')

# 디바이스별 시청 비율 준비
device_views = devices_df['Device Type Name'].value_counts()
fig_device = px.pie(names=device_views.index, values=device_views.values,
                    title='Viewing Distribution by Device Type')

# 인기 타이틀 Top 10 준비
top_titles = viewing_df['Title'].value_counts().head(10)
fig_top_titles = px.bar(x=top_titles.values, y=top_titles.index, orientation='h',
                        labels={'x': 'Number of Views', 'y': 'Title'},
                        title='Top 10 Most Watched Titles')

# Dash 앱 생성
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1('Netflix User Behavior Dashboard', style={'textAlign': 'center'}),

    html.Div([
        dcc.Graph(figure=fig_hourly),
        dcc.Graph(figure=fig_weekday)
    ], style={'display': 'flex', 'flexDirection': 'row', 'justifyContent': 'space-around'}),

    html.Div([
        dcc.Graph(figure=fig_device),
        dcc.Graph(figure=fig_top_titles)
    ], style={'display': 'flex', 'flexDirection': 'row', 'justifyContent': 'space-around'})
])

if __name__ == '__main__':
    app.run(debug=True)


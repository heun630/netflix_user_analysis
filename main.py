from src.data_loader import load_viewing_data, load_clickstream_data, load_devices_data, load_profiles_data, load_search_history_data
from src.preprocess import preprocess_viewing_data, preprocess_devices_data
from src.analysis import analyze_hourly_views, analyze_weekday_views, analyze_device_views, analyze_top_titles
from src.visualization import plot_hourly_views, plot_weekday_views, plot_device_views, plot_top_titles
import os

# 데이터 경로 설정
data_dir = 'data/'
outputs_dir = 'outputs/'

# outputs 폴더가 없으면 생성
if not os.path.exists(outputs_dir):
    os.makedirs(outputs_dir)

# 1. 데이터 불러오기
print("\n[INFO] Loading datasets...")
viewing_df = load_viewing_data(os.path.join(data_dir, 'All_ViewingActivity.csv'))
clickstream_df = load_clickstream_data(os.path.join(data_dir, 'All_Clickstream.csv'))
devices_df = load_devices_data(os.path.join(data_dir, 'All_Devices.csv'))
profiles_df = load_profiles_data(os.path.join(data_dir, 'All_Profiles.csv'))
search_df = load_search_history_data(os.path.join(data_dir, 'All_SearchHistory.csv'))

# 2. 데이터 전처리
print("[INFO] Preprocessing viewing and devices data...")
viewing_df = preprocess_viewing_data(viewing_df)
devices_df = preprocess_devices_data(devices_df)

# 3. 전처리 데이터 저장
print("[INFO] Saving preprocessed datasets...")
viewing_df.to_csv(os.path.join(outputs_dir, 'processed_viewing_activity.csv'), index=False)
devices_df.to_csv(os.path.join(outputs_dir, 'processed_devices.csv'), index=False)
clickstream_df.to_csv(os.path.join(outputs_dir, 'processed_clickstream.csv'), index=False)
profiles_df.to_csv(os.path.join(outputs_dir, 'processed_profiles.csv'), index=False)
search_df.to_csv(os.path.join(outputs_dir, 'processed_search_history.csv'), index=False)

# 4. 분석 및 시각화
print("[INFO] Analyzing and visualizing user behavior...")

hourly_views = analyze_hourly_views(viewing_df)
plot_hourly_views(hourly_views)

weekday_views = analyze_weekday_views(viewing_df)
plot_weekday_views(weekday_views)

device_views = analyze_device_views(devices_df)
plot_device_views(device_views)

top_titles = analyze_top_titles(viewing_df, top_n=10)
plot_top_titles(top_titles)

print("\n[INFO] All processes completed successfully!")
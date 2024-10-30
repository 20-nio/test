import requests
import math
import re

# 定数
API_KEY = "SoDEHo3oE0yN8uTTySW8JkABdqCb5gE4cK0uZ1XU"

# サンプル定数
COMMAND = "10"      # 太陽
CENTER = "500@10"  # 観測地点：地球の中心
START_TIME = '"2024-10-28 12:00"'
STOP_TIME = '"2024-10-28 12:01"'
STEP_SIZE = "1m"

# APIリクエスト関数
def get_horizon_data(command, center, start_time, stop_time, step_size):
    url = "https://ssd.jpl.nasa.gov/api/horizons.api"
    params = {
        "format": "text",
        "COMMAND": command,
        "CENTER": center,
        "START_TIME": start_time,
        "STOP_TIME": stop_time,
        "STEP_SIZE": step_size,
        "REF_PLANE": "ECLIPTIC",
        "QUANTITIES": "3"
    }

    # リクエストを送信
    response = requests.get(url, params=params)

    # レスポンスが成功した場合
    if response.status_code == 200:
        return response.text
    else:
        print("APIリクエストに失敗しました:", response.status_code)
        return None
    
horizon_data = get_horizon_data(COMMAND, CENTER, START_TIME, STOP_TIME, STEP_SIZE)
print("取得したデータ:\n", horizon_data)

if horizon_data:
    match = re.search(r'Pole \(RA,DEC\), deg\. *= \(([\d\.\-]+), ([\d\.\-]+)\)', horizon_data)  #この時点ではtext型

if match:
    ra = float(match.group(1))  # 赤経をfloatに変換
    dec = float(match.group(2))  # 赤緯をfloatに変換
    print(f"赤経 (RA): {ra}度")
    print(f"赤緯 (DEC): {dec}度")
else:
    print("赤経と赤緯の値が見つかりませんでした。")





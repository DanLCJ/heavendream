import requests
import json
from .myKey import KEY

mykey = '&key=' + KEY  # KEY VALUE EDITTING IN MYKEY.PY!

__plugin_version__ = '2.0'

url_api_geo = 'https://geoapi.qweather.com/v2/city/lookup?'
url_api_weather = 'https://devapi.qweather.com/v7/weather/'
# url_api_rain = 'https://devapi.qweather.com/v7/minutely/5m'
url_api_air = 'https://devapi.qweather.com/v7/air/now'


def get_info_v2(city_kw, dist_kw):
    url_geo = url_api_geo + 'location=' + dist_kw + mykey
    info = requests.get(url_geo).json()

    # legel address judgement
    if info['location'][0]:
        for i in range(0, len(info['location'])):
            # 遍历所有的地区
            city = info['location'][i]
            # 条件为城市名对应；若输入为单一城市，则城市名与地区名相同，一旦相同便跳出循环
            if city_kw == city['adm2']:
                city_info = 1
                city_id = city['id']
                district_name = city['name']
                city_name = city['adm2']
                province_name = city['adm1']
                break
                # country_name = city['country']
                # lat = city['lat']
                # lon = city['lon']
                # blocked latitude and longitude due to rain information blocked
            # 若某个憨憨写了省份，可以更改说明语句
            elif city_kw == city['adm1']:
                city_info = 3
                break
            # 若遍历后仍未找到信息，说明用户输入为单一名称且名称为区级名
            else:
                city_info = 2
    else:
        city_info = 0

    if city_info == 0:
        msg = '并没有找到呢，再检查一下输入的城市/城区名对不对吧~'
        return msg

    if city_info == 2:
        msg = '请不要单独输入区级名！格式为“天气 城市 地区”！'
        return msg

    if city_info == 3:
        msg = 'Lylia知道是哪个省！格式为“天气 城市 地区”！'
        return msg

    url_now = url_api_weather + 'now?location=' + city_id + mykey
    url_24h = url_api_weather + '24h?location=' + city_id + mykey
    url_3d = url_api_weather + '3d?location=' + city_id + mykey
    url_air = url_api_air + '?location=' + city_id + mykey

    weather_now = requests.get(url_now).json()
    weather_24h = requests.get(url_24h).json()
    weather_3d = requests.get(url_3d).json()
    air_now = requests.get(url_air).json()

    # current weather data
    current_weather = weather_now['now']['text']
    current_temp = weather_now['now']['temp']
    current_fl_temp = weather_now['now']['feelsLike']
    current_air = air_now['now']['aqi']

    # today weather data
    today_weather = weather_3d['daily'][0]['textDay']
    today_min_temp = weather_3d['daily'][0]['tempMin']
    today_max_temp = weather_3d['daily'][0]['tempMax']

    # future 1h weather data
    future1h_weather = weather_24h['hourly'][1]['text']
    future1h_temp = weather_24h['hourly'][1]['temp']

    # tomorrow weather data
    tomorrow_weather = weather_3d['daily'][1]['textDay']
    tomorrow_min_temp = weather_3d['daily'][1]['tempMin']
    tomorrow_max_temp = weather_3d['daily'][1]['tempMax']

    if district_name == city_name:
        msg = province_name + ' ' + city_name + '市\n' + \
            '当前天气：' + current_weather + ' ' + current_temp + '℃  体感温度：' + current_fl_temp + '℃\n' + \
            '空气质量指数：' + current_air + '\n' + \
            '今日天气：' + today_weather + ' ' + today_min_temp + ' - ' + today_max_temp + '℃\n' + \
            '1小时后天气：' + future1h_weather + ' ' + future1h_temp + '℃\n' + \
            '明日天气：' + tomorrow_weather + ' ' + tomorrow_min_temp + ' - ' + tomorrow_max_temp + '℃'
    else:
        msg = province_name + ' ' + city_name + '市' + ' ' + district_name + '区\n' + \
            '当前天气：' + current_weather + ' ' + current_temp + '℃  体感温度：' + current_fl_temp + '℃\n' + \
            '空气质量指数：' + current_air + '\n' + \
            '今日天气：' + today_weather + ' ' + today_min_temp + ' - ' + today_max_temp + '℃\n' + \
            '1小时后天气：' + future1h_weather + ' ' + future1h_temp + '℃\n' + \
            '明日天气：' + tomorrow_weather + ' ' + tomorrow_min_temp + ' - ' + tomorrow_max_temp + '℃'

    return msg


'''
# Code test
print('请输入城市:')
city_input = input()
print('请输入地区:')
dist_input = input()
msg = get_info_v2(city_input, dist_input)
print(msg)
'''

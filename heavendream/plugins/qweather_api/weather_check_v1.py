import requests
import json
from .myKey import KEY

from nonebot import on_command
from nonebot.matcher import Matcher
from nonebot.params import ArgPlainText, CommandArg
from nonebot.adapters.onebot.v11 import Message

# @origin basic author: InTereSTingHE
# @robot modified author: DanLCJ

__plugin_name__ = 'qweather_api'
__plugin_usage__ = '用法：命令为“天气”时，自动定位命令后方的城市，返回城市的天气信息；若没有则进行二次询问'

# blocked rain information sending temporarily

mykey = '&key=' + KEY  # KEY VALUE EDITTING IN MYKEY.PY!

url_api_geo = 'https://geoapi.qweather.com/v2/city/lookup?'
url_api_weather = 'https://devapi.qweather.com/v7/weather/'
# url_api_rain = 'https://devapi.qweather.com/v7/minutely/5m'
url_api_air = 'https://devapi.qweather.com/v7/air/now'


def get_info(city_kw):
    url_geo = url_api_geo + 'location=' + city_kw + mykey
    info = requests.get(url_geo).json()

    # legel address judgement
    if info != {'code': '404'}:
        city_info = 1
        city = info['location'][0]
        city_id = city['id']
        district_name = city['name']
        city_name = city['adm2']
        province_name = city['adm1']
        # country_name = city['country']
        # lat = city['lat']
        # lon = city['lon']
        # blocked latitude and longitude due to rain information blocked
    else:
        city_info = 0
        city_id = '101210113'
        district_name = '西湖'
        city_name = '杭州'
        province_name = '浙江省'

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

    return city_info, district_name, city_name, province_name, \
        current_weather, current_temp, current_fl_temp, current_air, \
        today_weather, today_min_temp, today_max_temp, \
        future1h_weather, future1h_temp, \
        tomorrow_weather, tomorrow_min_temp, tomorrow_max_temp


def msg_generator(city_kw):
    city_info, district_name, city_name, province_name, \
        current_weather, current_temp, current_fl_temp, current_air, \
        today_weather, today_min_temp, today_max_temp, \
        future1h_weather, future1h_temp, \
        tomorrow_weather, tomorrow_min_temp, tomorrow_max_temp = get_info(city_kw)

    if city_info == 0:
        msg = '并没有找到呢，再检查一下输入的城市名对不对吧~'
        return msg

    if district_name == city_name:
        msg = province_name + ' ' + city_name + '市\n' + \
            '当前天气：' + current_weather + ' ' + current_temp + '℃  体感温度：' + current_fl_temp + '℃\n' + \
            '空气质量指数：' + current_air + '\n' + \
            '今日天气：' + today_weather + ' ' + today_min_temp + ' - ' + today_max_temp + '℃\n' + \
            '1小时后天气：' + future1h_weather + ' ' + future1h_temp + '℃\n' + \
            '明日天气：' + tomorrow_weather + ' ' + tomorrow_min_temp + ' - ' + tomorrow_max_temp + '℃'
    else:
        msg = province_name + ' ' + city_name + '市\n' + ' ' + district_name + '区\n' + \
            '当前天气：' + current_weather + ' ' + current_temp + '℃  体感温度：' + current_fl_temp + '℃\n' + \
            '空气质量指数：' + current_air + '\n' + \
            '今日天气：' + today_weather + ' ' + today_min_temp + ' - ' + today_max_temp + '℃\n' + \
            '1小时后天气：' + future1h_weather + ' ' + future1h_temp + '℃\n' + \
            '明日天气：' + tomorrow_weather + ' ' + tomorrow_min_temp + ' - ' + tomorrow_max_temp + '℃'

    return msg


# robot function part
wther_permission = lambda sender: (sender.is_groupchat) or sender.is_superuser
wther = on_command('天气', aliases={'tianqi', 'weather'}, priority=8)


@wther.handle()
async def _handle(matcher: Matcher, city: Message = CommandArg(), permission=wther_permission):
    if KEY == '':
        await wther.reject_arg('city', prompt='没有设置KEY值！请机器人超级用户检查！')
    if city.extract_plain_text() and city.extract_plain_text()[0] != '_':
        matcher.set_arg('city', city)


@wther.got('city', prompt='你想查询哪个城市的天气呢？')
async def _(city: str = ArgPlainText('city')):
    if city[0] != '_':
        await wther.send('Lylia观星中，请稍等片刻...', at_sender=True)
        msg = msg_generator(city)
        await wther.send(msg, at_sender=True)
    else:
        await wther.reject_arg('city', prompt='不能使用“_”作为查询前缀！请重新输入！')


'''
# Code test
print('请输入城市:')
city_input = input()
msg = msg_generator(city_input)
print(msg)
'''
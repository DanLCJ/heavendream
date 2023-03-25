import time
from nonebot import require, get_bots
from nonebot.adapters.onebot.v11 import Message
from .weather_info import *

__plugin_name__ = 'morning_greeting'
__plugin_usage__ = '用法：简单的定时器应用，定时发送天气信息'


gmm_weather_msg = get_info_v3('温州', '温州', '温州')
zee_weather_msg = get_info_v3('天津', '天津', '东丽')
ermiao_weather_msg = get_info_v3('南宁', '南宁', '西乡塘')
oo_weather_msg = get_info_v3('重庆', '重庆', '江北')
bro_weather_msg = get_info_v3('东莞', '东莞', '东莞')
guozi_weather_msg = get_info_v3('德阳', '德阳', '广汉')
#guozi_weather_msg = get_info_v3('四川', '成都', '双流')
youzi_weather_msg = get_info_v3('北京', '北京', '海淀')
#youzi_weather_msg = get_info_v3('河北', '石家庄', '新华')
xxiang_weather_msg = get_info_v3('杭州', '杭州', '西湖')
gmm_at = Message('[CQ:at,qq=1316957934]')
zee_at = Message('[CQ:at,qq=173934284]')
ermiao_at = Message('[CQ:at,qq=2713436219]')
oo_at = Message('[CQ:at,qq=2412871611]')
bro_at = Message('[CQ:at,qq=1976473767]')
youzi_at = Message('[CQ:at,qq=2559168031]')

timing_weekday = require("nonebot_plugin_apscheduler").scheduler
timing_weekend = require("nonebot_plugin_apscheduler").scheduler


@timing_weekday.scheduled_job("cron", hour='06', minute='45', id="weekday_morning_greeting")
async def weekday_morning_greeting():
    bot, = get_bots().values()
    if time.localtime().tm_wday != 5 and time.localtime().tm_wday != 6:
        await bot.send_msg(message_type="group", group_id=480193020, message=zee_at + 'Zee早上好~\n' + zee_weather_msg)
        await bot.send_msg(message_type="group", group_id=480193020, message=ermiao_at + '二喵早上好~\n' + ermiao_weather_msg)
        await bot.send_msg(message_type="group", group_id=480193020, message=oo_at + '圈圈早上好~\n' + oo_weather_msg)
        await bot.send_msg(message_type="group", group_id=480193020, message=bro_at + '大哥早上好~\n' + bro_weather_msg)
        await bot.send_msg(message_type="group", group_id=480193020, message=youzi_at + '柚子早上好~\n' + youzi_weather_msg)
        await bot.send_msg(message_type="private", user_id=983407665, message='香香早上好~\n' + xxiang_weather_msg)
        await bot.send_msg(message_type="private", user_id=702055401, message='果子早上好~\n' + guozi_weather_msg)
    # if time.localtime().tm_wday != 2:
        await bot.send_msg(message_type="group", group_id=480193020, message=gmm_at + '顾顾早上好~\n' + gmm_weather_msg)


@timing_weekday.scheduled_job("cron", hour='08', minute='00', id="weekend_morning_greeting")
async def weekend_morning_greeting():
    bot, = get_bots().values()
    if time.localtime().tm_wday == 5 or time.localtime().tm_wday == 6:
        await bot.send_msg(message_type="group", group_id=480193020, message=zee_at + 'Zee早上好~\n' + zee_weather_msg)
        await bot.send_msg(message_type="group", group_id=480193020, message=ermiao_at + '二喵早上好~\n' + ermiao_weather_msg)
        await bot.send_msg(message_type="group", group_id=480193020, message=oo_at + '圈圈早上好~\n' + oo_weather_msg)
        await bot.send_msg(message_type="group", group_id=480193020, message=bro_at + '大哥早上好~\n' + bro_weather_msg)
        await bot.send_msg(message_type="group", group_id=480193020, message=youzi_at + '柚子早上好~\n' + youzi_weather_msg)
        await bot.send_msg(message_type="private", user_id=983407665, message='香香早上好~\n' + xxiang_weather_msg)
        await bot.send_msg(message_type="private", user_id=702055401, message='果子早上好~\n' + guozi_weather_msg)
    # if time.localtime().tm_wday == 2:
        await bot.send_msg(message_type="group", group_id=480193020, message=gmm_at + '顾顾早上好~\n' + gmm_weather_msg)

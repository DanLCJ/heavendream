import os.path
import time
from nonebot import require, get_bots
from nonebot.adapters.onebot.v11 import Message

__plugin_name__ = 'scheduler_3pm'
__plugin_usage__ = '用法：简单的定时器应用，定时发送图片'

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
tea_img_path = os.path.join(BASE_DIR, "drinktea.gif")
water_img_path = os.path.join(BASE_DIR, "drinkwater.gif")

timing_3pm = require("nonebot_plugin_apscheduler").scheduler
timing_10am = require("nonebot_plugin_apscheduler").scheduler
timing_8pm = require("nonebot_plugin_apscheduler").scheduler


@timing_3pm.scheduled_job("cron", hour='15', minute='00', id="drink_tea")
async def drink_tea():
    tea_image = Message('[CQ:image,file=https://inews.gtimg.com/newsapp_match/0/13589566094/0]')
    bot, = get_bots().values()
    await bot.send_msg(message_type="group", group_id=931872640, message=tea_image)
    await bot.send_msg(message_type="group", group_id=869679752, message=tea_image)
    await bot.send_msg(message_type="group", group_id=480193020, message=tea_image)


@timing_10am.scheduled_job("cron", hour='10', minute='00', id="drink_water")
async def drink_tea():
    water_image = Message('[CQ:image,file=https://tva3.sinaimg.cn/large/a6a681ebgy1goh0fixke6g209t09m7uq.gif]')
    bot, = get_bots().values()
    await bot.send_msg(message_type="group", group_id=931872640, message=water_image)
    await bot.send_msg(message_type="group", group_id=869679752, message=water_image)
    await bot.send_msg(message_type="group", group_id=480193020, message=water_image)


@timing_8pm.scheduled_job("cron", hour='20', minute='00', id="rank_notice")
async def drink_tea():
    rank_msg = Message('疯排开始了！是时候展现真正的技术了！')
    bot, = get_bots().values()
    if time.localtime().tm_wday == 5 or time.localtime().tm_wday == 6:
        await bot.send_msg(message_type="group", group_id=869679752, message=rank_msg)
        await bot.send_msg(message_type="group", group_id=480193020, message=rank_msg)

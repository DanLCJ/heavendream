import random
import re
import json
from nonebot import on_regex, rule, on_message, on_notice
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event
from nonebot.permission import Permission
from nonebot.adapters import cqhttp as cq
from .dic import *
from .config import Config

__plugin_name__ = 'autoreply'
__plugin_usage__ = '自动回复对话中对应的词库'
__plugin_priority__ = 30


async def morning_checker(event: Event) -> bool:
    if event.get_plaintext() == "早":
        return True
    elif event.get_plaintext() == "早安":
        return True
    elif event.get_plaintext() == "早安~":
        return True
    elif event.get_plaintext() == "早呀":
        return True
    elif event.get_plaintext() == "早早":
        return True
    elif event.get_plaintext() == "早早早":
        return True
    elif event.get_plaintext() == "早~":
        return True
    elif event.get_plaintext() == "早上好":
        return True


async def night_checker(event: Event) -> bool:
    if event.get_plaintext() == "晚安":
        return True
    elif event.get_plaintext() == "晚安安":
        return True
    elif event.get_plaintext() == "晚安~":
        return True


haha = on_regex(r"哈哈*")
lylia_call = on_regex(r"(lylia|莉莉娅|Lylia)")
qmark = on_regex(r"(？)+")
hug = on_regex(r"(抱|贴)+", rule=rule.to_me())
morning = on_message(rule=morning_checker, priority=30, block=False)
night = on_message(rule=night_checker, priority=30, block=False)
chat_notice = on_notice(priority=30)


@haha.handle()
async def haha_handle(bot: Bot, event: Event, state: T_State):
    try:
        uid = event.get_user_id()
    except:
        pass
    # 如果读取正常没有出错
    else:
        if uid not in Config.block_uid:
            msg = "哈哈哈哈"
            ch = ['哈', '哈哈']
            ending = ['~', '', '嗝', '（']
            for i in range(random.randint(0, 5)):
                msg += random.choice(ch)
            msg += random.choices(ending, [1, 6, 1, 2])[0]
            await bot.send(event, msg)


@lylia_call.handle()
async def lylia_call_handle(bot: Bot, event: Event, state: T_State):
    await bot.send(event, random.choice(["笨蛋Lylia不在嘎", "叫笨蛋Lylia干嘛", "调戏哒咩呦",
                                         "_(:_」∠)_又叫我", "笨蛋莉莉娅不在嘎", "叫笨蛋莉莉娅干嘛"])
                   + random.choices(["", "（", "~"], [2, 2, 1])[0])


@qmark.handle()
async def qmark_handle(bot: Bot, event: Event, state: T_State):
    try:
        uid = event.get_user_id()
    except:
        pass
    # 如果读取正常没有出错
    else:
        if uid not in Config.block_uid:
            msg_qmark = res_qmark()
            await qmark.send(message=msg_qmark)


@morning.handle()
async def morning_handle(bot: Bot, event: Event, state: T_State):
    try:
        uid = event.get_user_id()
    except:
        pass
    # 如果读取正常没有出错
    else:
        if uid not in Config.block_uid:
            msg_morning = res_morning()
            await morning.send(message=msg_morning)


@night.handle()
async def night_handle(bot: Bot, event: Event, state: T_State):
    try:
        uid = event.get_user_id()
    except:
        pass
    # 如果读取正常没有出错
    else:
        if uid not in Config.block_uid:
            msg_night = res_night()
            await night.send(message=msg_night)


@hug.handle()
async def hug_handle(bot: Bot, event: Event, state: T_State):
    await bot.send(event, random.choice(["抱抱", "抱~", "抱住", "贴贴"])
                   + random.choice(["", "嘿嘿"])
                   + random.choices(["", "~", "x"], [2, 2, 1])[0], at_sender=True)


@chat_notice.handle()
async def chat_poke_handle(bot: Bot, event: Event, state: T_State):
    try:
        ids = event.get_session_id()
    except:
        pass
    # 如果读取正常没有出错，因为有些notice格式不支持session
    else:
        # 如果这是一条群聊信息
        if ids.startswith("group"):
            _, group_id, user_id = event.get_session_id().split("_")
            # 只对列表中的群使用
            # if group_id in Config.used_in_group:
            description = event.get_event_description()
            values = json.loads(description.replace("'", '"'))
            # 如果被戳的是机器人
            if values['notice_type'] == 'notify' and values['sub_type'] == 'poke' and str(
                    values['target_id']) == Config.bot_id:
                await bot.send(event, random.choice(["笨蛋Lylia不在嘎", "戳笨蛋Lylia干嘛", "调戏哒咩呦",
                                         "_(:_」∠)_别戳啦，痒~", "笨蛋莉莉娅不在嘎", "戳笨蛋莉莉娅干嘛"]))

from nonebot import on_message
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event
from nonebot.internal.rule import Rule as Rule
from .dic import *

__plugin_name__ = 'autoreply'
__plugin_usage__ = '自动回复对话中对应的词库'
__plugin_priority__ = 30


async def haha_checker(event: Event) -> bool:
    if event.get_plaintext() == "哈哈":
        return True
    elif event.get_plaintext() == "哈哈哈":
        return True
    elif event.get_plaintext() == "哈哈哈哈":
        return True
    elif event.get_plaintext() == "哈哈哈哈哈":
        return True
    elif event.get_plaintext() == "哈哈哈哈哈哈":
        return True
    elif event.get_plaintext() == "哈哈哈哈哈哈哈":
        return True
    elif event.get_plaintext() == "哈哈哈哈哈哈哈哈":
        return True
    elif event.get_plaintext() == "哈哈哈哈哈哈哈哈哈":
        return True
    elif event.get_plaintext() == "哈哈哈哈哈哈哈哈哈哈":
        return True


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


async def qmark_checker(event: Event) -> bool:
    if event.get_plaintext() == "？":
        return True
    elif event.get_plaintext() == "？？":
        return True
    elif event.get_plaintext() == "？？？":
        return True
    elif event.get_plaintext() == "？？？？":
        return True
    elif event.get_plaintext() == "？？？？？":
        return True
    elif event.get_plaintext() == "？？？？？？":
        return True
    elif event.get_plaintext() == "?":
        return True
    elif event.get_plaintext() == "??":
        return True
    elif event.get_plaintext() == "???":
        return True


hahas = on_message(rule=haha_checker, priority=30, block=False)
mornings = on_message(rule=morning_checker, priority=30, block=False)
nights = on_message(rule=night_checker, priority=30, block=False)
qmarks = on_message(rule=qmark_checker, priority=30, block=False)


@hahas.handle()
async def autoreply_haha(bot: Bot, event: Event, state: T_State):
    private_id = event.get_session_id()
    if private_id == "583625087" or private_id == "983407665":
        msg_haha = res_haha()
        await hahas.send(message=msg_haha)
    else:
        _, group_id, user_id = event.get_session_id().split("_")
        if group_id == "480193020" and user_id != "1955733408":
            msg_haha = res_haha()
            await hahas.send(message=msg_haha)


@mornings.handle()
async def autoreply_morning(bot: Bot, event: Event, state: T_State):
    private_id = event.get_session_id()
    if private_id == "583625087" or private_id == "983407665":
        msg_morning = res_morning()
        await mornings.send(message=msg_morning)
    else:
        _, group_id, user_id = event.get_session_id().split("_")
        if group_id == "480193020" and user_id != "1955733408":
            msg_morning = res_morning()
            await mornings.send(message=msg_morning)


@nights.handle()
async def autoreply_night(bot: Bot, event: Event, state: T_State):
    private_id = event.get_session_id()
    if private_id == "583625087" or private_id == "983407665":
        msg_night = res_night()
        await nights.send(message=msg_night)
    else:
        _, group_id, user_id = event.get_session_id().split("_")
        if group_id == "480193020" and user_id != "1955733408":
            msg_night = res_night()
            await nights.send(message=msg_night)


@qmarks.handle()
async def autoreply_qmark(bot: Bot, event: Event, state: T_State):
    private_id = event.get_session_id()
    if private_id == "583625087" or private_id == "983407665":
        msg_qmark = res_qmark()
        await qmarks.send(message=msg_qmark)
    else:
        _, group_id, user_id = event.get_session_id().split("_")
        if group_id == "480193020" and user_id != "1955733408":
            msg_qmark = res_qmark()
            await qmarks.send(message=msg_qmark)

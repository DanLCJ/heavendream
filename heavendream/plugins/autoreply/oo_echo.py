import time
from nonebot import on_message
from nonebot.adapters import Bot, Event
from nonebot.adapters.onebot.v11 import Message
from nonebot.typing import T_State

__plugin_name__ = 'scheduler_echo'
__plugin_usage__ = '自动检测oo的发言，并根据时间戳计算时间差并自动发送指定消息'
__plugin_priority__ = 30

init_last_response = time.time()


async def user_checker(event: Event) -> bool:
    if event.get_user_id() == "2412871611":
        return True

matcher = on_message(rule=user_checker, priority=30, block=False)


@matcher.handle()
async def _(bot: Bot, event: Event, state: T_State):
    global init_last_response
    ids = event.get_session_id()
    if ids.startswith("group"):
        _, group_id, user_id = event.get_session_id().split("_")
        if user_id == "2412871611":
            delta_time = int(time.time()) - int(init_last_response)
            init_last_response = time.time()
            if delta_time > 2700:
                emoji = '[CQ:face,id=144]'
                Emoji = Message(emoji)
                message = 'oo帅哥来咯' + Emoji + Emoji + Emoji + 'oo帅哥来咯' + Emoji + Emoji + Emoji + 'oo帅哥来咯' + Emoji + Emoji + Emoji + 'oo帅哥来咯' + Emoji + Emoji + Emoji \
                    + 'oo帅哥来咯' + Emoji + Emoji + Emoji + 'oo帅哥来咯' + Emoji + Emoji + Emoji + 'oo帅哥来咯' + Emoji + Emoji + Emoji + 'oo帅哥来咯' + Emoji + Emoji + Emoji
                await matcher.send(message=message)

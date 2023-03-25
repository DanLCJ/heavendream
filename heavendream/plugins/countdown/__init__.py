import time
from nonebot import on_message
from nonebot.adapters import Event


__plugin_name__ = 'countdown'
__plugin_usage__ = '用法： 自动倒计时三秒'
__plugin_priority__ = 30


async def message_checker(event: Event) -> bool:
    if event.get_plaintext() == "倒计时":
        return True
    elif event.get_plaintext() == "数":
        return True

countdown_permission = lambda sender: (sender.is_groupchat) or sender.is_superuser
countdown = on_message(rule=message_checker, priority=30, block=False)


@countdown.handle()
async def _(event: Event, permission=countdown_permission):
    ids = event.get_session_id()
    # 如果这是一条群聊信息：格式为“group_groupid_userid”
    if ids.startswith("group"):
        # 如果需要增加权限，提前增加群号码与限定qq号
        # _, group_id, user_id = event.get_session_id().split("_")
        time_left = 4
        while time_left > 1:
            time.sleep(1)
            time_left = time_left - 1
            num = str(time_left)
            await countdown.send(num)

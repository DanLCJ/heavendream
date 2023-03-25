import random
from nonebot import on_message
from nonebot.adapters import Event


__plugin_name__ = 'rollthedice'
__plugin_usage__ = '用法： 投骰子'
__plugin_priority__ = 30


async def message_checker(event: Event) -> bool:
    if event.get_plaintext() == "投骰子":
        return True
    elif event.get_plaintext() == "骰子":
        return True

rollthedice_permission = lambda sender: (sender.is_groupchat) or sender.is_superuser
rollthedice = on_message(rule=message_checker, priority=30, block=False)


@rollthedice.handle()
async def _(event: Event, permission=rollthedice_permission):
    ids = event.get_session_id()
    # 如果这是一条群聊信息：格式为“group_groupid_userid”
    if ids.startswith("group"):
        # 如果需要增加权限，提前增加群号码与限定qq号
        # _, groupid, userid = event.get_session_id().split("_")
        mark = random.randint(1, 20)
        msg = str('你的点数是：' + str(mark))
        await rollthedice.send(msg, at_sender=True)
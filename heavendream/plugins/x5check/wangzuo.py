from nonebot import on_message
from nonebot.adapters import Event
from nonebot.adapters.onebot.v11 import Message

__plugin_name__ = 'wangzuo'
__plugin_usage__ = '用法： 群员发送王座时，自动发送王座爆点截图'
__plugin_priority__ = 11

async def message_checker(event: Event) -> bool:
    if event.get_plaintext() == "王座":
        return True

matcher = on_message(rule=message_checker, priority=11)

# restriction only for group chat
wangzuo_permission = lambda sender: sender.is_groupchat


@matcher.handle()
async def _(permission=wangzuo_permission):
    await matcher.send('2023年3月3日王座（若需要更新请联系曦秋）')
    await matcher.finish(Message('[CQ:image,file=https://c2cpicdw.qpic.cn/offpic_new/583625087/583625087-1201871592-64B84674E96F403EB5509D5290D147EA/0?term=3&amp,subType=0]'))

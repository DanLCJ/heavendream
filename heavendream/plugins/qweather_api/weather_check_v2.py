import json
from .myKey import KEY
from .weather_info_v2 import *

from nonebot import on_command
from nonebot.matcher import Matcher
from nonebot.params import Arg, ArgPlainText, CommandArg
from nonebot.adapters.onebot.v11 import Message

# @origin basic author: InTereSTingHE
# @robot modified author: DanLCJ
# v2: 精准到区级

__plugin_name__ = 'qweather_api'
__plugin_usage__ = '用法：命令为“天气”时，自动定位命令后方的城市，返回城市的天气信息；若没有则进行二次询问；现在可支持区级定位'
__plugin_example__ = '天气 杭州 西湖'
__plugin_priority__ = 8


# robot function part
wther_permission = lambda sender: (sender.is_groupchat) or sender.is_superuser
wther = on_command('天气 ', aliases={'tianqi', 'weather'}, priority=8)


@wther.handle()
async def _handle(matcher: Matcher, args: Message = CommandArg(), permission=wther_permission):
    if KEY == '':
        await wther.finish('city', prompt='没有设置KEY值！请机器人超级用户检查！')    
    if args.extract_plain_text() and args.extract_plain_text()[0] != '_':
        matcher.set_arg('city', args)


@wther.got('city', prompt='你想查询哪个城市的天气呢？')
async def _(city: Message = Arg(), city_name: str = ArgPlainText('city')):
    name = city_name.strip().split(' ')
    if not name[0]:
        name = await wther.aget(key='city', prompt='请问是什么城市呢？', at_sender=True)
    if name[0] != '_':
        if len(name) == 2:
            await wther.send('Lylia观星中，请稍等片刻...', at_sender=True)
            msg = get_info_v2(name[0], name[1])
            await wther.send(msg, at_sender=True)
        else:
            await wther.send('Lylia观星中，请稍等片刻...', at_sender=True)
            msg = get_info_v2(name[0], name[0])
            await wther.send(msg, at_sender=True)
    else:
        await wther.finish('city', prompt='不能使用“_”作为查询前缀！请重新输入！')

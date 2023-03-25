from nonebot import on_message
from nonebot.adapters import Event

__plugin_name__ = 'update_instruction'
__plugin_usage__ = '用法： 群员说"更新日志"时，自动回复更新日志'
__plugin_priority__ = 15

msg = "更新日志：" + "\n" + \
    "2022.6.8  v0.1.0 基本实现Lylia通讯协议；" + "\n" + \
    "2022.6.11 v0.2.0 添加了基于wttr的天气查询模块；" + "\n" + \
    "2022.6.17 v0.3.0 添加了触发关键词的自动回复；" + "\n" + \
    "2022.6.20 v0.4.0 添加了定时器模块；" + "\n" + \
    "2022.6.22 v0.5.0 更新天气查询源为和风天气API，并优化所发送天气信息；" + "\n" + \
    "2022.7.11 v0.6.0 添加了查询爆点模块，支持星动与弹珠模式；" + "\n" + \
    "2022.7.14 v0.6.1 更新爆点数据，支持弦月模式；" + "\n" + \
    "2022.7.15 v0.6.2 优化了权限访问，重做查询命令判定机制；" + "\n" + \
    "2022.7.16 v0.6.3 更新爆点数据，支持泡泡模式；" + "\n" + \
    "2022.7.21 v0.7.0 增加Lylia简单交互，更容易查询命令；" + "\n" + \
    "2022.7.23 v0.8.0 更新天气模块，天气定位可精确到区级；" + "\n" + \
    "2022.7.26 v0.9.0 添加了入群退群提醒模块；" + "\n" + \
    "2022.7.29 v0.9.1 爆点查询模块添加了王座查询；" + "\n" + \
    "2022.8.1 v1.0.0 Lylia正式上线，增设爆点模块访问组;" + "\n" + \
    "2022.9.30 v1.1.0 更新天气模块，增强兼容性。" + "\n" + \
    "********************" + "\n" + \
    "如果有遇到任何问题或者建议，欢迎联系管理员或者曦秋！"


async def message_checker(event: Event) -> bool:
    if event.get_plaintext() == "更新日志":
        return True
    elif event.get_plaintext() == "gengxinrizhi":
        return True

matcher = on_message(rule=message_checker, priority=15)

help_permission = lambda sender: sender.is_superuser


@matcher.handle()
async def _handle(permission=help_permission):
    await matcher.send(msg)

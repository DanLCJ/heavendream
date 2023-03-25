from nonebot import on_keyword

__plugin_name__ = 'wishecho'
__plugin_usage__ = '用法： 群员说关键词"好运"时，自动回复"El Psy Congroo"'

matcher = on_keyword(['好运'])

wish_permission = lambda sender: (sender.is_groupchat) or sender.is_superuser

@matcher.handle()
async def wishecho_(permission=wish_permission):
    await matcher.send('El Psy Kongroo')
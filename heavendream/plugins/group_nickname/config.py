import json
import os
from nonebot import on_command
from nonebot.adapters import Event
from nonebot.adapters.onebot.v11 import GroupMessageEvent
from nonebot.log import logger
from nonebot.params import ArgPlainText


def readgroup():
    try:
        with open("./datename/groupinfo.json", "r+", encoding="utf-8") as f:
            return json.load(f)
    except(FileNotFoundError):
        return []


def readcard():
    try:
        with open("./datename/cardinfo.json", "r+", encoding="utf-8") as f:
            return json.load(f)
    except(FileNotFoundError):
        return {}


global user
global id_nickname
global bot_id
user = readgroup()
id_nickname = readcard()
bot_id = 1955733408


async def user_checker(event: Event) -> bool:
    if event.get_user_id() == "583625087":
        return True
    elif event.get_user_id() == "583644186":
        return True

start = on_command("开启群名片时间", rule=user_checker, priority=35)
end = on_command("关闭群名片时间", rule=user_checker, priority=35)
data_upload = on_command("datename更新缓存", rule=user_checker, priority=39)


@start.handle()
async def start_Service():
    await start.send("请输入你的昵称")


@start.got("nickname")
async def strat_2(event: GroupMessageEvent, a: str = ArgPlainText("nickname")):
    o = []
    o.append(str(event.group_id))
    o.append(str(bot_id))
    user.append(str(o))
    logger.success("datenowname:开启成功")
    id_nickname[str(bot_id)] = a
    await start.finish("ok")


@end.handle()
async def end_service(event: GroupMessageEvent):
    try:
        o = []
        o.append(str(event.group_id))
        o.append(str(bot_id))
        user.remove(str(o))
        id_nickname.pop(str(bot_id))
    except(ValueError):
        logger.error("datenowname:关闭失败 指定用户不存在")
        pass
    else:
        logger.success("datenowname:关闭现在时间昵称成功！")
        await end.finish("关闭现在时间昵称成功！")


@data_upload.handle()
async def upload_data():
    if os.path.exists("datename") is False:
        os.mkdir("datename")
    with open("./datename/groupinfo.json", "w+", encoding="utf-8") as g:
        g.write(str(user))
        g.close()
    with open("./datename/cardinfo.json", "w+", encoding="utf-8") as g:
        g.write(str(id_nickname).replace("'", '"'))
        g.close()
    await data_upload.finish("更新缓存完成")

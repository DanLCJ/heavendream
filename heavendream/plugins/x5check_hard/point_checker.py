import sqlite3
import os.path
from nonebot import on_command
from nonebot.matcher import Matcher
from nonebot.adapters import Event
from nonebot.params import ArgPlainText, CommandArg
from nonebot.adapters.onebot.v11 import Message
# from nonebot.adapters.onebot.v11.permission import GROUP_ADMIN
from .config import Config


__plugin_name__ = 'x5check_point_checker'
__plugin_usage__ = '用法： 简易炫舞查询高难度歌曲爆点'
__plugin_priority__ = 5

default_ability = '极限'
abnormal_single = '***爆气***'

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "top.db")

def xingdong_check(kw):
    conn = sqlite3.connect(db_path)
    c = conn.cursor()

    judgement = "SELECT * FROM xingdongtop WHERE SONG LIKE '%" + kw + "%'"

    try:

        c.execute(judgement)
        info = c.fetchone()

        song_name = info[0]
        point = info[1]
        point_disc = info[2]
        bpm = info[3]
        half_combo = info[4]
        judge_4key = info[5]
        abi = info[6]

        if abi == 2:
            abi_msg = abnormal_single
        else:
            abi_msg = default_ability

        if judge_4key == 2:
            key_msg = '【5k】'
        else:
            key_msg = ''

        msg = song_name + key_msg + '  bpm:' + bpm + '\n' + \
            '爆点：' + point + '\n' + \
            '爆点描述：' + '\n' + point_disc + '\n' + \
            '半cb：' + half_combo + '\n' + \
            '技能：' + abi_msg
        conn.commit()
        conn.close()

        return msg

    except Exception:
        msg = '未找到所对应的歌曲'
        conn.commit()
        conn.close()
        return msg

# robot function part
x5checktop_permission = lambda sender: (sender.is_groupchat) or sender.is_superuser
x5checktop_xingdong = on_command('xingdongtop ', priority=Config.priority)

@x5checktop_xingdong.handle()
async def _handlexingdong(matcher: Matcher, kw: Message = CommandArg(), permission=x5checktop_permission):
    if kw.extract_plain_text() and kw.extract_plain_text()[0] != '_':
        matcher.set_arg('kw', kw)


@x5checktop_xingdong.got('kw', prompt='你想查询星动模式的哪一首？')
async def _xingdong(event: Event, kw: str = ArgPlainText('kw')):    
    if kw[0] != '_':
        ids = event.get_session_id()
        # 如果这是一条群聊信息：格式为“group_groupid_userid”
        if ids.startswith("group"):
            _, group_id, user_id = event.get_session_id().split("_")
            if group_id in Config.used_in_group and user_id != Config.bot_id:
                msg = xingdong_check(kw)
                await x5checktop_xingdong.send(msg, at_sender=True)
            else:
                await x5checktop_xingdong.finish('喵喵？')
        # 如果这是一条私聊消息：
        elif ids in Config.authorized_ids:
            msg = xingdong_check(kw)
            await x5checktop_xingdong.send(msg, at_sender=True)
        else:
            await x5checktop_xingdong.finish('Lylia不支持查询爆表！')
    else:
        await x5checktop_xingdong.finish('不能使用“_”作为查询前缀！请谨言慎行！')

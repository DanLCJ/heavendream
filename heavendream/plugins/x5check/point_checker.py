#!/usr/bin/python

import sqlite3
import os.path
from nonebot import on_command
from nonebot.matcher import Matcher
from nonebot.adapters import Event
from nonebot.params import ArgPlainText, CommandArg
from nonebot.adapters.onebot.v11 import Message
# from nonebot.adapters.onebot.v11.permission import GROUP_ADMIN
from nonebot.exception import IgnoredException
from .config import Config

__plugin_name__ = 'x5check_point_checker'
__plugin_usage__ = '用法： 简易炫舞查询爆点插件，“aa”表示星动模式，“dd”表示弹珠模式，“ss”表示弦月模式，“ff”表示泡泡模式'
__plugin_priority__ = 5

default_ability = '默认：单排带极限'
abnormal_single = '***单排带爆气***'
abnormal_double = '@@@双排带极限@@@'

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "test.db")


def xingdong_check(kw):
    conn = sqlite3.connect(db_path)
    c = conn.cursor()

    judgement = "SELECT * FROM xingdong WHERE ID LIKE '%" + kw + "%'"

    try:

        c.execute(judgement)
        info = c.fetchone()

        song_name = info[1]
        former_point = info[2]
        former_disc = info[3]
        latter_point = info[4]
        latter_disc = info[5]
        double_score = info[6]
        single_point = info[7]
        single_disc = info[8]
        single_score = info[9]
        single_abi = info[10]

        if single_abi == 2:
            abi_msg = abnormal_single
        elif single_abi == 3:
            abi_msg = abnormal_double
        else:
            abi_msg = default_ability

        msg = '歌名：' + song_name + '\n' + \
            '双排前爆：' + former_point + '\n' + \
            '前爆描述：' + former_disc + '\n' +\
            '双排后爆：' + latter_point + '\n' +\
            '后爆描述：' + latter_disc + '\n' +\
            '双排指数：' + double_score + '\n' +\
            '**********************' + '\n' + \
            '单排爆点：' + single_point + '\n' + \
            '爆点描述：' + single_disc + '\n' + \
            '单排指数：' + single_score + '\n' +\
            '技能：' + abi_msg
        conn.commit()
        conn.close()

        return msg

    except Exception:
        msg = '未找到所对应的歌曲'
        conn.commit()
        conn.close()
        return msg


def danzhu_check(kw):
    conn = sqlite3.connect(db_path)
    c = conn.cursor()

    judgement = "SELECT * FROM danzhu WHERE ID LIKE '%" + kw + "%'"

    try:

        c.execute(judgement)
        info = c.fetchone()
        song_name = info[1]
        former_point = info[2]
        former_disc = info[3]
        latter_point = info[4]
        latter_disc = info[5]
        double_score = info[6]
        single_point = info[7]
        single_disc = info[8]
        single_score = info[9]
        single_abi = info[10]

        if single_abi == 2:
            abi_msg = abnormal_single
        elif single_abi == 3:
            abi_msg = abnormal_double
        else:
            abi_msg = default_ability

        msg = '歌名：' + song_name + '\n' + \
            '双排前爆：' + former_point + '\n' + \
            '前爆描述：' + former_disc + '\n' +\
            '双排后爆：' + latter_point + '\n' +\
            '后爆描述：' + latter_disc + '\n' +\
            '双排指数：' + double_score + '\n' +\
            '**********************' + '\n' + \
            '单排爆点：' + single_point + '\n' + \
            '爆点描述：' + single_disc + '\n' + \
            '单排指数：' + single_score + '\n' +\
            '技能：' + abi_msg
        conn.commit()
        conn.close()

        return msg

    except Exception:
        msg = '未找到所对应的歌曲'
        conn.commit()
        conn.close()
        return msg


def xianyue_check(kw):
    conn = sqlite3.connect(db_path)
    c = conn.cursor()

    judgement = "SELECT * FROM xianyue WHERE ID LIKE '%" + kw + "%'"

    try:

        c.execute(judgement)
        info = c.fetchone()
        song_name = info[1]
        former_point = info[2]
        former_disc = info[3]
        latter_point = info[4]
        latter_disc = info[5]
        # double_score = info[6]
        single_point = info[7]
        single_disc = info[8]
        # single_score = info[9]
        single_abi = info[10]

        if single_abi == 2:
            abi_msg = abnormal_single
        elif single_abi == 3:
            abi_msg = abnormal_double
        else:
            abi_msg = default_ability

        msg = '歌名：' + song_name + '\n' + \
            '双排前爆：' + former_point + '\n' + \
            '前爆描述：' + former_disc + '\n' +\
            '双排后爆：' + latter_point + '\n' +\
            '后爆描述：' + latter_disc + '\n' +\
            '**********************' + '\n' + \
            '单排爆点：' + single_point + '\n' + \
            '爆点描述：' + single_disc + '\n' + \
            '技能：' + abi_msg
        conn.commit()
        conn.close()

        return msg

    except Exception:
        msg = '未找到所对应的歌曲'
        conn.commit()
        conn.close()
        return msg


def paopao_check(kw):
    conn = sqlite3.connect(db_path)
    c = conn.cursor()

    judgement = "SELECT * FROM paopao WHERE ID LIKE '%" + kw + "%'"

    try:

        c.execute(judgement)
        info = c.fetchone()
        song_name = info[1]
        former_point = info[2]
        former_disc = info[3]
        latter_point = info[4]
        latter_disc = info[5]
        # double_score = info[6]
        single_point = info[7]
        single_disc = info[8]
        # single_score = info[9]
        single_abi = info[10]

        if single_abi == 2:
            abi_msg = abnormal_single
        elif single_abi == 3:
            abi_msg = abnormal_double
        else:
            abi_msg = default_ability

        msg = '歌名：' + song_name + '\n' + \
            '双排前爆：' + former_point + '\n' + \
            '前爆描述：' + former_disc + '\n' +\
            '双排后爆：' + latter_point + '\n' +\
            '后爆描述：' + latter_disc + '\n' +\
            '**********************' + '\n' + \
            '单排爆点：' + single_point + '\n' + \
            '爆点描述：' + single_disc + '\n' + \
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
x5check_permission = lambda sender: (sender.is_groupchat) or sender.is_superuser
x5check_xingdong = on_command('aa ', priority=Config.priority)
x5check_danzhu = on_command('dd ', priority=Config.priority)
x5check_xianyue = on_command('ss ', priority=Config.priority)
x5check_paopao = on_command('ff ', priority=Config.priority)


@x5check_xingdong.handle()
async def _handlexingdong(matcher: Matcher, kw: Message = CommandArg(), permission=x5check_permission):
    if kw.extract_plain_text() and kw.extract_plain_text()[0] != '_':
        matcher.set_arg('kw', kw)


@x5check_xingdong.got('kw', prompt='你想查询星动模式的哪一首？')
async def _xingdong(event: Event, kw: str = ArgPlainText('kw')):    
    if kw[0] != '_':
        ids = event.get_session_id()
        # 如果这是一条群聊信息：格式为“group_groupid_userid”
        if ids.startswith("group"):
            _, group_id, user_id = event.get_session_id().split("_")
            if group_id == Config.used_in_group_ks:
                msg = 'Lylia正在闭关修炼中……'
                await x5check_xingdong.send(msg, at_sender=True)
            elif group_id in Config.used_in_group_no_permissions and user_id != Config.bot_id:
                msg = xingdong_check(kw)
                await x5check_xingdong.send(msg, at_sender=True)
            else:
                await x5check_xingdong.finish('喵喵？')
        # 如果这是一条私聊消息：
        elif ids in Config.authorized_ids:
            msg = xingdong_check(kw)
            await x5check_xingdong.send(msg, at_sender=True)
        else:
            await x5check_xingdong.finish('Lylia不支持查询爆表！')
    else:
        await x5check_xingdong.finish('不能使用“_”作为查询前缀！请谨言慎行！')


@x5check_danzhu.handle()
async def _handledanzhu(matcher: Matcher, kw: Message = CommandArg(), permission=x5check_permission):
    if kw.extract_plain_text() and kw.extract_plain_text()[0] != '_':
        matcher.set_arg('kw', kw)


@x5check_danzhu.got('kw', prompt='你想查询弹珠模式的哪一首？')
async def _danzhu(event: Event, kw: str = ArgPlainText('kw')):    
    if kw[0] != '_':
        ids = event.get_session_id()
        # 如果这是一条群聊信息：格式为“group_groupid_userid”
        if ids.startswith("group"):
            _, group_id, user_id = event.get_session_id().split("_")
            if group_id == Config.used_in_group_ks:
                msg = 'Lylia正在闭关修炼中……'
                await x5check_danzhu.send(msg, at_sender=True)
            elif group_id in Config.used_in_group_no_permissions and user_id != Config.bot_id:
                msg = danzhu_check(kw)
                await x5check_danzhu.send(msg, at_sender=True)
            else:
                await x5check_danzhu.finish('嗷呜？')
        # 如果这是一条私聊消息：
        elif ids in Config.authorized_ids:
            msg = danzhu_check(kw)
            await x5check_danzhu.send(msg, at_sender=True)
        else:
            await x5check_danzhu.finish('Lylia不支持查询爆表！')
    else:
        await x5check_danzhu.finish('不能使用“_”作为查询前缀！请谨言慎行！')


@x5check_xianyue.handle()
async def _handlexianyue(matcher: Matcher, kw: Message = CommandArg(), permission=x5check_permission):
    if kw.extract_plain_text() and kw.extract_plain_text()[0] != '_':
        matcher.set_arg('kw', kw)


@x5check_xianyue.got('kw', prompt='你想查询弦月模式的哪一首？')
async def _xianyue(event: Event, kw: str = ArgPlainText('kw')):    
    if kw[0] != '_':
        ids = event.get_session_id()
        # 如果这是一条群聊信息：格式为“group_groupid_userid”
        if ids.startswith("group"):
            _, group_id, user_id = event.get_session_id().split("_")
            if group_id == Config.used_in_group_ks:
                msg = 'Lylia正在闭关修炼中……'
                await x5check_xianyue.send(msg, at_sender=True)
            elif group_id in Config.used_in_group_no_permissions and user_id != Config.bot_id:
                msg = xianyue_check(kw)
                await x5check_xianyue.send(msg, at_sender=True)
            else:
                await x5check_xianyue.finish('嘎嘎？')
        # 如果这是一条私聊消息：
        elif ids in Config.authorized_ids:
            msg = xianyue_check(kw)
            await x5check_xianyue.send(msg, at_sender=True)
        else:
            await x5check_xianyue.finish('Lylia不支持查询爆表！')
    else:
        await x5check_xianyue.finish('不能使用“_”作为查询前缀！请谨言慎行！')


@x5check_paopao.handle()
async def _handlepaopao(matcher: Matcher, kw: Message = CommandArg(), permission=x5check_permission):
    if kw.extract_plain_text() and kw.extract_plain_text()[0] != '_':
        matcher.set_arg('kw', kw)


@x5check_paopao.got('kw', prompt='你想查询泡泡模式的哪一首？')
async def _paopao(event: Event, kw: str = ArgPlainText('kw')):    
    if kw[0] != '_':
        ids = event.get_session_id()
        # 如果这是一条群聊信息：格式为“group_groupid_userid”
        if ids.startswith("group"):
            _, group_id, user_id = event.get_session_id().split("_")
            if group_id == Config.used_in_group_ks:
                msg = 'Lylia正在闭关修炼中……'
                await x5check_paopao.send(msg, at_sender=True)
            elif group_id in Config.used_in_group_no_permissions and user_id != Config.bot_id:
                msg = paopao_check(kw)
                await x5check_paopao.send(msg, at_sender=True)
            else:
                await x5check_paopao.finish('咩？')
        # 如果这是一条私聊消息：
        elif ids in Config.authorized_ids:
            msg = paopao_check(kw)
            await x5check_paopao.send(msg, at_sender=True)
        else:
            await x5check_paopao.finish('Lylia不支持查询爆表！')
    else:
        await x5check_paopao.finish('不能使用“_”作为查询前缀！请谨言慎行！')
'''
# Code test
print('请输入歌曲:')
city_input = input()
msg = xingdong_check(city_input)
print(msg)
'''

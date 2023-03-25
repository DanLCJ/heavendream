from nonebot import on_notice, on_command
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event
from nonebot.adapters.onebot.v11 import MessageSegment
from nonebot.permission import SUPERUSER
import json
import os
from .config import Config
from .model import *

__plugin_name__ = 'join_and_leave'
__plugin_usage__ = '用法： 提示有人加群或者退群，并记录此人在该群的历史退群次数。'
__plugin_priority__ = 10

# 创建数据库
create_db()

img_path = 'file:///' + os.path.split(os.path.realpath(__file__))[0] + '/img/'


# 通报加群与退群
join_and_leave = on_notice(priority=Config.priority)


@join_and_leave.handle()
async def handle_first_receive(bot: Bot, event: Event, state: T_State):
    try:
        ids = event.get_session_id()
    except:
        pass
    # 如果读取正常没有出错，因为有些notice格式不支持session
    else:
        # 如果这是一条群聊信息
        if ids.startswith("group"):
            _, group_id, user_id = event.get_session_id().split("_")
            # 只对列表中的群使用
            if group_id in Config.used_in_group:
                description = event.get_event_description()
                values = json.loads(description.replace("'", '"'))
                # 有新人加群
                if values['notice_type'] == 'group_increase':
                    # 获取此人是否曾经退群
                    leave_record = get_exist_data(user_id, group_id)
                    print(leave_record)
                    if len(leave_record) == 0:
                        await join_and_leave.send(
                            'Lylia监测到有只小可爱' + MessageSegment.at(values['user_id']) + '闪现进来了~')
                        # await join_and_leave.finish(
                            # MessageSegment.at(values['user_id']) + '爆点查询可以来找我，详细功能可以输入“Lylia帮助”试试看~')
                    # 如果此人之前曾经退群过，发出警告
                    else:
                        await join_and_leave.send(
                            'Lylia监测到有只小可爱' + MessageSegment.at(values['user_id']) + '闪现进来了~')
                        await join_and_leave.finish(
                            f"警告：记录表明这只小可爱曾经退群过{leave_record[0][0]}次！")
                # 有人退群
                elif values['notice_type'] == 'group_decrease':
                    add_data(user_id, group_id)
                    # 自己退群
                    if values['sub_type'] == 'leave':
                        infos = str(await bot.get_stranger_info(user_id=values['user_id']))
                        nickname = json.loads(infos.replace("'", '"'))['nickname'] + '(' + str(values['user_id']) + ')'
                        await join_and_leave.finish(
                            nickname + '在这一刻选择了离开我们。\n')
                    # 被踢出群
                    elif values['sub_type'] == 'kick':
                        infos = str(await bot.get_stranger_info(user_id=values['user_id']))
                        nickname = json.loads(infos.replace("'", '"'))['nickname'] + '(' + str(values['user_id']) + ')'
                        operator_infos = str(await bot.get_stranger_info(user_id=values['operator_id']))
                        operator_nickname = json.loads(operator_infos.replace("'", '"'))['nickname'] + '(' + str(
                            values['operator_id']) + ')'
                        await join_and_leave.finish('超级可爱的' + operator_nickname + '面无表情地把' + \
                                                    nickname + '一脚踢出了这个世界！')

# 管理员专属指令
# 查询命令
copyer_helper = on_command("退群帮助", priority=Config.priority)
@copyer_helper.handle()
async def handle_first_receive(bot: Bot, event: Event, state: T_State):
    await copyer_helper.finish('''退群指令仅限bot管理员使用：
退群次数查询 [QQ号]——查询指定用户在当前群的退群次数
退群次数排行——查询当前群的退群次数最多的人''')

get_leave_data = on_command("退群次数查询", priority=Config.priority)
@get_leave_data.handle()
async def handle_first_receive(bot: Bot, event: Event, state: T_State):
    ids = event.get_session_id()
    # 如果这是一条群聊信息
    if ids.startswith("group"):
        _, group_id, ask_user_id = event.get_session_id().split("_")
        if group_id in Config.used_in_group and ask_user_id in Config.superviser:
            search_id = str(event.get_message()).strip()
            leave_record = get_exist_data(search_id, group_id)
            infos = str(await bot.get_stranger_info(user_id=search_id))
            nickname = json.loads(infos.replace("'", '"'))['nickname'] + '(' + str(search_id) + ')'
            if len(leave_record) == 0:
                await join_and_leave.finish(nickname+"没有退出过该群。")
            else:
                await join_and_leave.finish(f"{nickname}退出过该群{leave_record[0][0]}次。")


get_most_leave_user = on_command("退群次数排行", priority=Config.priority)
@get_most_leave_user.handle()
async def handle_first_receive(bot: Bot, event: Event, state: T_State):
    ids = event.get_session_id()
    # 如果这是一条群聊信息
    if ids.startswith("group"):
        _, group_id, ask_user_id = event.get_session_id().split("_")
        if group_id in Config.used_in_group and ask_user_id in Config.superviser:
            leave_record = search_most_leave(group_id)
            if len(leave_record) == 0:
                await get_most_leave_user.finish("该群暂无退群数据")
            else:
                result = '前五位退群最多的人是：\n'
                for user_id, leave in leave_record:
                    infos = str(await bot.get_stranger_info(user_id=user_id))
                    nickname = json.loads(infos.replace("'", '"'))['nickname'] + '(' + str(user_id) + ')'
                    result += nickname + f'\n退群:{leave}次\n\n'
                await get_most_leave_user.finish(result[:-1])

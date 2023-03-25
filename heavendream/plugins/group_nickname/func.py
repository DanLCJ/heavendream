import random
from datetime import datetime


def genshin_countdown():
    time_format = '%Y %m %d %H:%M:%S'
    target = datetime.strptime("2023 4 12 11:00:00", time_format)

    now = datetime.now()
    timedelta = target-now
    days = timedelta.days
    secs = timedelta.seconds
    hours = secs//3600
    secs = secs % 3600
    mins = secs // 60
    secs = secs % 60
    suffix = str(" | 距离3.6版本更新还有" + str(days) + "天" + str(hours) + "时" + str(mins) + "分" + str(secs) + "秒")
    return suffix


def genshin_char_countdown():
    time_format = '%Y %m %d %H:%M:%S'
    target = datetime.strptime("2023 4 11 14:59:00", time_format)

    now = datetime.now()
    timedelta = target-now
    days = timedelta.days
    secs = timedelta.seconds
    hours = secs//3600
    secs = secs % 3600
    mins = secs // 60
    secs = secs % 60
    suffix = str(" | 当前版本限定卡池还剩" + str(days) + "天" + str(hours) + "时" + str(mins) + "分" + str(secs) + "秒")
    return suffix


def peking_timing():
    suffix = " | 现在是北京时间" + str(datetime.now().strftime("%H:%M:%S"))
    return suffix


def name_suffix():
    mark = random.randint(0, 2)
    if mark == 0:
        suffix = genshin_countdown()
        return suffix
    elif mark == 1:
        suffix = genshin_char_countdown()
        return suffix
    else:
        suffix = peking_timing()
        return suffix

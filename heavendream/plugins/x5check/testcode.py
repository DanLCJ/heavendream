#!/usr/bin/python

import sqlite3
import os.path


default_ability = '单排带极限'
abnormal_single = '***单排带爆气***'
abnormal_double = '***双排带极限***'

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
            '双排爆气指数：' + double_score + '\n' + \
            '**********************' + '\n' + \
            '单排爆点：' + single_point + '\n' + \
            '爆点描述' + single_disc + '\n' + \
            '单排爆气指数：' + single_score + '\n' + \
            '技能：' + abi_msg
        conn.commit()
        conn.close()

        return msg

    except Exception:
        msg = '未找到所对应的歌曲'
        conn.commit()
        conn.close()
        return msg


# Code test
print('请输入歌曲:')
city_input = input()
msg = xingdong_check(city_input)
print(msg)

import sqlite3
import os

# 数据库文件的路径
db_path = os.path.split(os.path.realpath(__file__))[0] + '/data/join_and_leave.db'


# 如果不存在的话，创建数据库，并且创建数据表
def create_db():
    conn = sqlite3.connect(db_path)
    try:
        create_tb_cmd = '''
            CREATE TABLE IF NOT EXISTS leave_record
            (user_id INT8,
            group_id INT8,
            leave INT);
            '''
        conn.execute(create_tb_cmd)
    except:
        pass
    conn.commit()
    conn.close()


# 查询指定人退群次数，返回退群次数
def get_exist_data(user_id, group_id):
    conn = sqlite3.connect(db_path)
    insert_cmd = f'SELECT leave from leave_record where user_id == {user_id} and group_id = {group_id}'
    cursor = list(conn.execute(insert_cmd))
    conn.close()
    # 如果不存在，则返回空列表
    # 否则返回退群次数
    return cursor


# 添加退群用户
def add_data(user_id, group_id):
    leave = get_exist_data(user_id, group_id)
    # 如果用户数据还不存在
    if not leave:
        cmd = f'INSERT INTO leave_record (user_id,group_id,leave) VALUES ({user_id}, {group_id}, {1});'
    # 否则计数+1
    else:
        cmd = f'UPDATE leave_record SET leave = {leave[0][0]+1} WHERE user_id == {user_id} and group_id = {group_id};'

    conn = sqlite3.connect(db_path)
    conn.execute(cmd)
    conn.commit()
    conn.close()


# 返回该群退群次数最高的人，返回用户qq号与退群次数
def search_most_leave(group_id):
    conn = sqlite3.connect(db_path)
    insert_cmd = f'SELECT user_id,leave from leave_record WHERE group_id = {group_id} order by -leave limit 5'
    cursor = list(conn.execute(insert_cmd))
    conn.close()
    return cursor

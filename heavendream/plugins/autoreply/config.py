class Config:
    # 记录在哪些群组中使用
    used_in_group = ["131551175"]
    # 插件执行优先级
    priority = 10
    # 接话冷却时间（秒），在这段时间内不会连续两次接话
    chat_cd = 15
    # 戳一戳冷却时间（秒）
    notice_cd = 900
    # 机器人QQ号
    bot_id = "1055733408"
    # 管理员QQ号，管理员无视冷却cd和触发概率
    super_uid = ["583625087"]
    # 屏蔽对话QQ号，无视该用户对话
    block_uid = ["1712129165"]
    # 聊天回复概率，用百分比表示，0-100%
    p_chat_response = 60
    # 戳一戳回复概率，用百分比表示，0-100%
    p_poke_response = 20
    # 默认禁言时间，每多戳一次会在默认禁言时间上翻倍
    default_ban_time = 60

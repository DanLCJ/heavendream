from random import choice
from nonebot.adapters.onebot.v11 import Message


def res_haha():
    responses_haha = ['？？？', '¿', '哈哈哈哈哈哈哈']
    return choice(responses_haha)


def res_morning():
    responses_morning = ['早上好鸭~', '早早早~', '早~']
    return choice(responses_morning)


def res_night():
    responses_night = ['晚安安~', '安安~', '明早见~']
    return choice(responses_night)


def res_qmark():
    qmark_1 = Message('[CQ:image,file=http://5b0988e595225.cdn.sohucs.com/images/20181203/bcd7a53ed07c422d8a8d411356849842.gif]')
    qmark_2 = Message('[CQ:image,file=https://mmbiz.qpic.cn/mmbiz_gif/9jcTic3iaLYuL5QWibgiazBC5IH1ZEjV3R8vUyjibbMfuVAL7ibZ2wcss32Opo2qPUAE28QRFibTOgrGlz5zseYibH4Ofg/640?wx_fmt=gif]')
    qmark_3 = Message('[CQ:image,file=https://mmbiz.qpic.cn/mmbiz_gif/9jcTic3iaLYuL5QWibgiazBC5IH1ZEjV3R8v0hibuSbHicUMK6wOsc9iboK6D0qsWib9PKd3qc5PHI1Mo7Q4Co0OluqBQQ/640?wx_fmt=gif]')
    qmark_4 = Message('[CQ:image,file=https://mmbiz.qpic.cn/mmbiz_gif/9jcTic3iaLYuL5QWibgiazBC5IH1ZEjV3R8vmh1cvPTNpWmKJT4Ux8gtzMRrcmBkwibvhZUIiacKStptyHhHiaKicibfJGg/640?wx_fmt=gif]')
    qmark_5 = Message('[CQ:image,file=http://img.soogif.com/315ojponXEfWDRNzqDuHKXqnXLVw8qx8.JPEG]')
    qmark_6 = Message('[CQ:image,file=http://img.soogif.com/SE3LpXjxWqFlg23c5mhGHJfpAB3C11cl.gif]')
    qmark_7 = Message('[CQ:image,file=http://img.soogif.com/h8GncDjSaYFzGkUgMYJdqCI2QDnFj56X.JPEG]')
    responses_qmark = [qmark_1, qmark_2, qmark_3, qmark_4, qmark_5, qmark_6, qmark_7]
    return choice(responses_qmark)

from nonebot import on_command
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event
from nonebot.internal.rule import Rule as Rule


async def user_checker(event: Event) -> bool:
    if event.get_user_id() == "583625087":
        return True
rule = Rule(user_checker, to_me)

printer_kongsu = on_command("forwardkongsu", rule=rule, priority=20)
printer_qiri = on_command("forwardqiri", rule=rule, priority=20)


@printer_kongsu.handle()
async def forward_kongsu(bot: Bot, event: Event, state: T_State):
    msg = str(event.get_message()).strip()
    _, echo_msg = msg.split(" ")
    await bot.send_msg(message_type="group", group_id=869679752, message=echo_msg)


@printer_qiri.handle()
async def forward_qiri(bot: Bot, event: Event, state: T_State):
    msg = str(event.get_message()).strip()
    _, echo_msg = msg.split(" ")
    await bot.send_msg(message_type="group", group_id=480193020, message=echo_msg)

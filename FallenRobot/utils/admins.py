from typing import Callable

from pyrogram.types import Message
from pyrogram.enums import ChatMemberStatus

from FallenRobot import pbot, DRAGONS


def can_change_info(func: Callable) -> Callable:
    async def non_admin(_, message: Message):
        if message.from_user.id in DRAGONS:
            return await func(_, message)

        check = await app.get_chat_member(message.chat.id, message.from_user.id)
        if check.status not in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
            return await message.reply_text("» ʏᴏᴜ'ʀᴇ ɴᴏᴛ ᴀɴ ᴀᴅᴍɪɴ ʙᴀʙʏ, ᴘʟᴇᴀsᴇ sᴛᴀʏ ɪɴ ʏᴏᴜʀ ʟɪᴍɪᴛs.")

        admin = (await app.get_chat_member(message.chat.id, message.from_user.id)).privileges
        if admin.can_change_info:
            return await func(_, message)
        else:
            return await message.reply_text("`You don't have permissions to change group info.")

    return non_admin
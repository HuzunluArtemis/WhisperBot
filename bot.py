# Copyright (C) 2022 GNU GENERAL PUBLIC LICENCE
#
# Licensed under the GNU GENERAL PUBLIC LICENCE, Version 3 (the "License");
# you may not use this file except in compliance with the License.
#
# Copyright (C) 2022 @SeorangDion for WhisperBot repo
# FROM WhisperBot <https://github.com/SeorangDion/WhisperBot>
# t.me/DionProjects & t.me/DionSupport
# Don't remove this credits!


from telethon import events, TelegramClient, Button
import logging
from telethon.tl.functions.users import GetFullUserRequest as us
import os


logging.basicConfig(level=logging.INFO)

BOT_NAME = os.environ.get("BOT_NAME", None)
BOT_USERNAME = os.environ.get("BOT_USERNAME", None)
TOKEN = os.environ.get("TOKEN", None)

bot = TelegramClient(
        "Dion",
        api_id=6,
        api_hash="23c93aa64d16911f521bd0b16291af57"
        ).start(
                bot_token=TOKEN
                )
db = {}

@bot.on(events.NewMessage(pattern="^[!?/]start$"))
async def stsrt(event):
    await event.reply(
            f"**Heya, I am a {BOT_NAME}!**\n\nType /help to see how to use me!\nType /repo to deploy your own bot like {BOT_NAME}.")


@bot.on(events.NewMessage(pattern="^[!?/]help$"))
async def stsrt(event):
    await event.reply(
            f"**• How to use {BOT_NAME}:**\n\nClick the button below or\n\nType __{BOT_USERNAME} wspr <username> | <text>__\nExample: `{BOT_USERNAME} wspr @Xflzu | Hello!`",
            buttons=[
                [Button.switch_inline("Go Inline", query="wspr")]
                ]
            )


@bot.on(events.NewMessage(pattern="^[!?/]repo$"))
async def stsrt(event):
    await event.reply(
            f"Click the button below to deploy bot like {BOT_NAME}",
            buttons=[
                [Button.url("Click Here", "https://telegram.dog/XTZ_HerokuBot?start=U2VvcmFuZ0Rpb24vV2hpc3BlckJvdCBkaW9u")]
                ]
            )


@bot.on(events.InlineQuery())
async def die(event):
    if len(event.text) != 0:
        return
    me = (await bot.get_me()).username
    
@bot.on(events.InlineQuery(pattern="wspr"))
async def inline(event):
    me = (await bot.get_me()).username
    try:
        inp = event.text.split(None, 1)[1]
        user, msg = inp.split("|")
    except IndexError:
        await event.answer(
                [], 
                switch_pm=f"@{me} [UserID]|[Message]",
                switch_pm_param="start"
                )
    except ValueError:
        await event.answer(
                [],
                switch_pm=f"Give a message too!",
                switch_pm_param="start"
                )
    try:
        ui = await bot(us(user))
    except BaseException:
        await event.answer(
                [],
                switch_pm="Invalid User ID/Username",
                switch_pm_param="start"
                )
        return
    db.update({"user_id": ui.user.id, "msg": msg, "self": event.sender.id})
    text = f"""
A Whisper Has Been Sent To [{ui.user.first_name}](tg://user?id={ui.user.id})!
Click The Below Button To See The Message!\n
**Note:** __Only {ui.user.first_name} can open this!__
    """
    dn = event.builder.article(
            title="Send your secret message!",
            description=f"Powered by {BOT_NAME}",
            text=text,
            buttons=[
                [Button.inline(" Show Message! ", data="wspr")]
                ]
            )
    await event.answer(
            [dn],
            switch_pm="Yahoo! A secret message.",
            switch_pm_param="start"
            )


@bot.on(events.CallbackQuery(data="wspr"))
async def ws(event):
    user = int(db["user_id", "1867048626"])
    lol = [int(db["self"])]
    lol.append(user)
    if event.sender.id not in lol:
        await event.answer("🔐 This message is not for you ningga!", alert=True)
        return
    msg = db["msg"]
    if msg == []:
        await event.anwswer(
                "Oops!\nIt's looks like message got deleted from my server!", alert=True)
        return
    await event.answer(msg, alert=True)

print("Started Bot, by @SeorangDion.")
bot.run_until_disconnected()

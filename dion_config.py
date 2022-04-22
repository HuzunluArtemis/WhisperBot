# Copyright (C) 2022 @SeorangDion for WhisperBot repo
# FROM WhisperBot <https://github.com/SeorangDion/WhisperBot>
# t.me/DionProjects & t.me/DionSupport
# Don't remove this credits!

import os

# Config Vars
DIONAPI_HASH = "23c93aa64d16911f521bd0b16291af57"
DIONAPI_KEY = 14624642
DIONBOT_NAME = os.environ.get("BOT_NAME", None) # Your bot name, example: Dion Bot
BOT_USERNAME = os.environ.get("BOT_USERNAME", None) # Your bot username with (@), example: @WhisperXRobot
DION_TOKEN = os.environ.get("TOKEN", None) # Your token bot, get one from t.me/botfather

# Config Text
START_TEXT = f"**Heya, I am a {DIONBOT_NAME}!**\n\nType /help to see how to use me!\nType /repo to deploy your own bot like {DIONBOT_NAME}."

HELP_TEXT = f"**• How to use {DIONBOT_NAME}:**\n\nClick the button below or\n\nType __{BOT_USERNAME} wspr <username> | <text>__\nExample: `{BOT_USERNAME} wspr @Xflzu | Hello!`"

REPO_TEXT = f"Click the button below to deploy bot like {DIONBOT_NAME}"

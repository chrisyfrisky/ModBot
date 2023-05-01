# SPDX-License-Identifier: MIT

"""
The main module for ModBot that runs the bot.
"""

import json
import sys

import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='?', intents=discord.Intents.default())

with open('config/config.json', 'r') as file:
    config = json.load(file)
    test_guild = discord.Object(config['test_guild'])

@bot.event
async def on_ready():
    print('Readying...')

    await bot.load_extension('cogs.test')
    await bot.load_extension('cogs.info')
    await bot.load_extension('cogs.moderation')

    bot.tree.copy_global_to(guild=test_guild)
    synced_commands = await bot.tree.sync(guild=test_guild)
    print(f'Successfully synced {len(synced_commands)} command(s).')

    print('Ready!')

if __name__ == '__main__':
    with open('config/bot_token.conf', 'r') as file:
        token = file.readline().strip()

    bot.run(token)

# SPDX-License-Identifier: MIT

"""
A test cog, to serve as a reference for other cogs.
"""

import discord
from discord import app_commands
from discord.ext import commands

class TestCog(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @app_commands.command(name='test')
    async def test(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message('test')

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(TestCog(bot))

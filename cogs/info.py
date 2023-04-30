# SPDX-License-Identifier: MIT

"""
An info cog, to give information on various things.
"""

import discord
from discord import app_commands
from discord.ext import commands

class InfoCog(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @app_commands.command(name='info-user')
    async def info_user(self, interaction: discord.Interaction, member:
                        discord.Member) -> None:
        """Looks up information on a member

        Parameters
        ----------
        member: discord.Member
            the member to look up
        """
        embed = discord.Embed(title=member, color=discord.Color.blurple())
        embed.add_field(name='ID', value=member.id)
        embed.add_field(name='Joined Discord on',
                        value=member.joined_at.strftime('%d %b %Y'))
        embed.add_field(name='Joined server on',
                        value=member.created_at.strftime('%d %b %Y'))
        await interaction.response.send_message(f'Information for {member}:',
                                                embed=embed)

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(InfoCog(bot))

# SPDX-License-Identifier: MIT

"""
A moderation cog, to provide tools for moderators.
"""

import discord
from discord import app_commands
from discord.ext import commands

class ModerationCog(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @app_commands.command()
    @app_commands.guild_only()
    @app_commands.checks.has_permissions(ban_members=True)
    @app_commands.checks.bot_has_permissions(ban_members=True)
    async def xban(self, interaction: discord.Interaction, user: str, reason:
                   str | None = None) -> None:
        """Ban a user by ID, even if they aren't on the server

        Parameters
        ----------
        id: str
            the user ID to ban (handled as a string due to Discord limitation)
        reason: str, optional
            the reason for the ban
        """
        try:
            user_id = int(user)
        except ValueError:
            await interaction.response.send_message('Invalid integer provided.')
            return

        if user_id <= 0:
            await interaction.response.send_message('ID must be positive.')
            return

        if reason is None:
            reason = ''
        reason = f'[Ban by {interaction.user}] ' + reason

        try:
            await interaction.guild.ban(discord.Object(user_id), reason=reason)
        except discord.NotFound:
            await interaction.response.send_message(f'User ID {user} does not '
                                                    'exist.')
        except discord.Forbidden:
            await interaction.response.send_message("I don't have permissions "
                                                    'to ban people.')
        except discord.HTTPException:
            await interaction.response.send_message('Unable to ban.')
        else:
            await interaction.response.send_message('Successfully banned user '
                                                    f'ID {user}.')

    @xban.error
    async def on_xban_error(self, interaction: discord.Interaction, error:
                            app_commands.AppCommandError):
        await interaction.response.send_message(error)

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(ModerationCog(bot))

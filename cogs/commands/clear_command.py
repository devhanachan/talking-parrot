from discord.ext import commands
from discord import app_commands
import discord
import os
from dotenv import load_dotenv

load_dotenv()

class clear_command (commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot

    @app_commands.command(name="clear_cog",description="this is owner command")
    @app_commands.checks.has_permissions(administrator=True)
    async def clear_cog(self, i:discord.Interaction):
        await i.response.defer(thinking=True)

        # seperate part from thinking 
        guild=discord.Object(id=int(os.getenv("GUILDID")))
        if guild:
            self.bot.tree.clear_commands(guild=guild)
            # sync cogs again
            await self.bot.tree.sync(guild=guild)
            await i.followup.send("Cogs all pursed")
        else:
            print("error in clear_cog")

async def setup(bot:commands.Bot):
    await bot.add_cog(clear_command(bot))
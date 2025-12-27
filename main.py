import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv()

class parrotbot ( commands.Bot ): 
    def __init__ ( self ):
        super().__init__(
            command_prefix=commands.when_mentioned,
            intents=discord.Intents.all()
        )

    async def setup_hook(self):
        extensions=[
            "cogs.events.on_ready",
            "cogs.commands.ping",
            "cogs.commands.clear_command",
            "cogs.commands.voice_",
            "cogs.events.on_message"
        ]
        failed = []
        for i in extensions:
            try:
                await self.load_extension(i)
                print(f"[OK] loaded: {i}")
            except Exception as error:
                failed.append((i, error))
                print(f"[FAIL] load: {i} -> {type(error).__name__}: {error}")
        if failed:
            raise RuntimeError(f"Some extensions failed: {[n for n, _ in failed]}")
        # guildId_str = os.getenv("GUILDID")
        
        # guild = discord.Object(id=int(guildId_str))
        await self.tree.sync()

          ### OLD STUPID CODE
        #         await self.tree.sync(guild=guild)
        #     #events
        #     await self.load_extension(on_ready)
        #     #commadns
        #     await self.load_extension("cogs.commands.ping")
        #     await self.load_extension("cogs.commands.clear_command")
        #     # I have to do this because I need it to sync fast so i choose my server
        #     # the user are not allowed to see any cogs outside my server
        #     # let me know if anyone read my code and see anybug 
            
        #     guildID=int(os.getenv("GUILDID"))
        #     guild=discord.Object(id=guildID)
        #     if guild:
        #         # this will register all global commadns to this guild
        #         # before syncing them globally (to make it fast in debug)
        #         self.tree.copy_global_to(guild=guild)
        #         await self.tree.sync(guild=guild)
        # except Exception as e:
        #     print(f"FAILED to load {on_ready}")

runme=parrotbot()
runme.run(
    reconnect=True,
    token=os.getenv("DC_TK"),
    
)
import discord
from discord.ext import commands
from discord import utils
from config import TOKEN, PREFIX
import datetime
from database.database import DbClient, Database
from dataminer import utcnow

COGS = [
    "dataminer.guild",
    "dataminer.member",
    "dataminer.message",
    "dataminer.reactions",
    "dataminer.status",
    "dataminer.voice",

    "cogs.analyze",
    "cogs.stats",
    "cogs.role_info",
    "cogs.user_info",
    "cogs.blacklist",
    "cogs.plot",
    "cogs.help"
]

class Bot(commands.AutoShardedBot):
    def __init__(self, **kwargs):
        intents = discord.Intents(
            guilds=True,
            members=True,
            bans=True,
            emojis=True,
            voice_states=True,
            messages=True,
            reactions=True,
            presences=True,
            invites=True
        )
        super(Bot, self).__init__(
            command_prefix=PREFIX,
            description="A discord bot that analyze your discord server",
            intents=intents,
        )
        self.launch = __import__("datetime").datetime.utcnow()
        self.version = "0.6.1"
        self.creator = "Bambus#8446"
        self.github_url = "https://github.com/JannesT3011/AnalyticsCube"
        
        self.db = DbClient().collection

        self.remove_command("help")

    async def load_cogs(self):
        for ext in COGS:
            try:
                await self.load_extension(ext)
            except Exception as e:
                print(f"Cant load {ext}")
                raise e
    
    async def on_ready(self):
        await self.load_cogs()
        await self.change_presence(activity=discord.Game(name=f"{PREFIX}help"))
        print(f"{self.user.id}\n"f"{utils.oauth_url(self.user.id)}\n"f"{self.user.name}\n""Ready!")

    async def on_message(self, message):
        """IGNORE PRIVATE MESSAGE"""
        if not message.guild:
            return
        await self.process_commands(message)
    
    async def on_guild_join(self, guild):
        try:
            await Database().init_db(str(guild.id))
            await self.bot.db.update_many({"_id": str(guild.id)}, {"$push": {"users": {"timestamp": utcnow, "count": guild.member_count}}})
        except:
            return

    async def on_guild_remove(self, guild):
        try:
            await Database().delete_db(str(guild.id))
        except:
            return

    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.BotMissingPermissions):
            return await ctx.send(embed=ErrorEmbed(str(error)))

        elif isinstance(error, commands.BotMissingPermissions):
            return await ctx.send(embed=ErrorEmbed(str(error)))
        
        elif isinstance(error, commands.BotMissingRole):
            return await ctx.send(embed=ErrorEmbed(str(error)))
        
        elif isinstance(error, commands.CheckFailure):
            return await ctx.send(embed=ErrorEmbed(str(error)))
        
        elif isinstance(error, commands.CommandNotFound):
            return await ctx.send(embed=ErrorEmbed("This isn't a command! Please use the `help` command"))
        
        elif isinstance(error, commands.BadArgument):
            owner = self.get_user(self.owner_id)
            return await owner.send(embed=OwnerErrorEmbed(str(error), ctx.guild.name))

class ErrorEmbed(discord.Embed):
    def __init__(self, description):
        super().__init__(
            title="Error",
            description=description,
            color=discord.Color.red(),
            timestamp=datetime.datetime.utcnow(),
        )
        self.set_footer(text=f'{bot.user.name} made with <3 by Bambus#8446', icon_url=bot.user.avatar_url)

class OwnerErrorEmbed(discord.Embed):
    def __init__(self, description, server):
        super().__init__(
            title=f"Error on server {server}",
            description=f"```{description}```",
            color=discord.Color.red(),
            timestamp=datetime.datetime.utcnow(),
        )
        self.set_footer(text=f'{bot.user.name} made with <3 by Bambus#8446', icon_url=bot.user.avatar_url)

bot = Bot()

bot.run(TOKEN)
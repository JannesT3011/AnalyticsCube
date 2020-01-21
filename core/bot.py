from discord.ext import commands
from discord import utils
from core.database import DbClient
from CONFIG import TOKEN, DEFAULT_PREFIX, OWNER_ID
from .cogs import COGS
import discord
import datetime

def get_prefix(bot, message):
    if not message.guild:
        return commands.when_mentioned_or(DEFAULT_PREFIX)(bot, message)

    pr_list = bot.db.find({"_id": str(message.guild.id)})
    for pr in pr_list:
        prefix = pr["prefix"]

    return commands.when_mentioned_or(prefix, DEFAULT_PREFIX)(bot, message)

async def run():
    bot = Bot()
    try:
        await bot.start(TOKEN)
    except Exception as err:
        await bot.logout()
        print(f"An error occurred: {err}")


class Bot(commands.AutoShardedBot):
    def __init__(self, **kwargs):
        super(Bot, self).__init__(
            command_prefix=get_prefix,
            description="A discord bot that analyze your discord server"
        )
        self.launch = __import__("datetime").datetime.utcnow()
        self.version = "0.0.1"
        self.creator = "Bambus#8446"
        self.github_url = "https://github.com/Bmbus/DiscordAnalytica"
        self.owner_id = OWNER_ID
        self.db = DbClient().collection

        for ext in COGS:
            try:
                self.load_extension(ext)
            except Exception as e:
                print(f"Cant load {ext}")
                raise e
    
    async def on_ready(self):
        print(f"{self.user.id}\n"f"{utils.oauth_url(self.user.id)}\n"f"{self.user.name}\n""Ready!")

    async def on_message(self, message):
        if not message.guild:
            return
        await self.process_commands(message)
    
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.BotMissingPermissions):
            return await ctx.send(ErrorEmbed(str(error)))

        elif isinstance(error, commands.BotMissingPermissions):
            return await ctx.send(ErrorEmbed(str(error)))
        
        elif isinstance(error, commands.BotMissingRole):
            return await ctx.send(ErrorEmbed(str(error)))
        
        elif isinstance(error, commands.CheckFailure):
            return await ctx.send(ErrorEmbed(str(error)))
        
        elif isinstance(error, commands.CommandNotFound):
            return await ctx.send(ErrorEmbed("This isn't a command! Please use the `help` command"))
        
        elif isinstance(error, commands.BadArgument):
            owner = self.get_user(self.owner_id)
            return await owner.send(embed=OwnerErrorEmbed(str(error), ctx.guild.name))

bot = Bot()

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
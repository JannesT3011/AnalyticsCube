from discord.ext import commands
from . import OWNER_ID


def is_bot_owner():
    async def pred(ctx):
        return ctx.author.id == OWNER_ID
    return commands.check(pred)
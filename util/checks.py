from discord.ext import commands

def is_on_blacklist():
    async def predicate(ctx):
        data = await ctx.bot.db.find_one({"_id": str(ctx.guild.id)})
        blacklist = data["blacklist"]
        return str(ctx.guild.id) in blacklist
    return commands.check(predicate)

async def in_blacklist(db, guild, channel):
    data = await db.find_one({"_id": str(guild.id)})
    blacklist = data["blacklist"]

    return str(channel.id) in blacklist
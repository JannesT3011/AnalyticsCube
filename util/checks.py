from discord.ext import commands

def is_on_blacklist():
    async def predicate(ctx):
        data = await ctx.bot.db.find_one({"_id": str(ctx.guild.id)})
        blacklist = data["blacklist"]
        return str(ctx.guild.id) in blacklist
    return commands.check(predicate)
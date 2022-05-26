import discord
from discord.ext import commands

class Blacklist(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.has_permissions(administrator=True)
    @commands.group(name='blacklist', invoke_without_command=True)
    async def blacklist(self, ctx):
        data = await self.bot.db.find_one({"_id": str(ctx.guild.id)})
        channels = data["blacklist"]
        blacklist_channels = [self.bot.get_channel(int(channel)).name for channel in channels]
        return await ctx.send(embed=discord.Embed(title="These channel are on the blacklist:", description=", \n".join(blacklist_channels)))
    
    @commands.has_permissions(administrator=True)
    @blacklist.command(name="add")
    async def blacklist_add(self, ctx, channel:discord.TextChannel):
        data = await self.bot.db.find_one({"_id": str(ctx.guild.id)})
        blacklist = data["blacklist"]
        if str(channel.id) in blacklist:
            return await ctx.send("Channel already in blacklist", delete_after=4)
        await self.bot.db.update_many({"_id": str(ctx.guild.id)}, {"$push": {"blacklist": str(channel.id)}})
        return await ctx.send("Channel successfully added to blacklist!", delete_after=4)
    
    @commands.has_permissions(administrator=True)
    @blacklist.command(name="remove")
    async def blacklist_remove(self, ctx, channel:discord.TextChannel):
        data = await self.bot.db.find_one({"_id": str(ctx.guild.id)})
        blacklist = data["blacklist"]
        if str(channel.id) not in blacklist:
            return await ctx.send("Channel not in blacklist!", delete_after=4)
        await self.bot.db.update_many({"_id": str(ctx.guild.id)}, {"$pull": {"blacklist": str(channel.id)}})
        return await ctx.send("Channel successfully removed from blacklist!", delete_after=4)

async def setup(bot):
    await bot.add_cog(Blacklist(bot))
from discord.ext import commands
from . import utcnow

"""
COLLECT DATA IF A USER JOIN/LEAVES A SERVER
"""

class Member(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        push_data = {"timestamp": utcnow}
        await self.bot.db.update_many({"_id": str(member.guild.id)}, {"$push": {"userjoins": push_data}})
        await self.bot.db.update_many({"_id": str(member.guild.id)}, {"$push": {"users": {"timestamp": utcnow, "count": member.guild.member_count}}})
        return

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        push_data = {"timestamp": utcnow}
        await self.bot.db.update_many({"_id": str(member.guild.id)}, {"$push": {"userleave": push_data}})
        await self.bot.db.update_many({"_id": str(member.guild.id)}, {"$push": {"users": {"timestamp": utcnow, "count": member.guild.member_count}}})
        return
    
    @commands.Cog.listener()
    async def on_member_ban(self, guild, user):
        push_data = {"timestamp": utcnow}
        await self.bot.db.update_many({"_id": str(guild.id)}, {"$push": {"user_ban": push_data}})
        return
    
    @commands.Cog.listener()
    async def on_member_unban(self, guild, user):
        push_data = {"timestamp": utcnow}
        await self.bot.db.update_many({"_id": str(guild.id)}, {"$push": {"user_unban": push_data}})
        return


def setup(bot):
    bot.add_cog(Member(bot))
import discord
from discord.ext import commands

class Userinfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.has_permissions(administrator=True)
    @commands.cooldown(1, 5.0, commands.BucketType.user)
    @commands.command(name='userinfo')
    async def name_command(self, ctx, *, user:discord.Member):

        roles = []
        for role in user.roles:
            roles.append(str(role))
        embed = discord.Embed(title=f"Infos about {user.name}", color=user.color)
        embed.set_thumbnail(url=user.avatar_url)
        embed.add_field(name="Roles:", value=", \n".join(roles) ,inline=False)
        embed.add_field(name="ID:", value=user.id, inline=False)
        embed.add_field(name="Status:", value=user.status, inline=False)
        embed.add_field(name="Activity", value=user.activity, inline=False)
        embed.add_field(name="Nick:", value=user.nick, inline=False)
        embed.add_field(name="Bot:", value="Yes" if user.bot else "No", inline=False)
        if not user.premium_since is None:
            embed.add_field(name="Premium since", value=user.premium_since, inline=False)
        embed.add_field(name="Joined:", value=str(user.joined_at).split(".")[0], inline=False)

        return await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Userinfo(bot))
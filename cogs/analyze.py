from discord import Embed
from discord.ext import commands
from dataminer.bot_data import bot_requests
from disputils import BotEmbedPaginator
from analytics.analytics import Analytics

class Analyze(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.has_permissions(administrator=True)
    @commands.group(name='analyze', invoke_without_command=True)
    async def analyze_command(self, ctx):
        return await ctx.send("please select option")
    
    @commands.has_permissions(administrator=True)
    @commands.cooldown(1, 10.0, commands.BucketType.user)
    @analyze_command.command(name="message")
    async def analyze_message_command(self, ctx):
        embeds = await Analytics(str(ctx.guild.id), self.bot.db).analyze_message()
        
        paginator = BotEmbedPaginator(ctx, embeds)
        await bot_requests(ctx.message, str(ctx.command), self.bot.db)
        await ctx.trigger_typing()

        return await paginator.run()
    
    @commands.has_permissions(administrator=True)
    @commands.cooldown(1, 10.0, commands.BucketType.user)
    @analyze_command.command(name="message_edit")
    async def analyze_message_edit_command(self, ctx):
        embeds = await Analytics(str(ctx.guild.id), self.bot.db).analyze_message_edit()

        paginator = BotEmbedPaginator(ctx, embeds)
        await bot_requests(ctx.message, str(ctx.command), self.bot.db)
        await ctx.trigger_typing()

        return await paginator.run()
    
    @commands.has_permissions(administrator=True)
    @commands.cooldown(1, 10.0, commands.BucketType.user)
    @analyze_command.command(name="message_delete")
    async def analyze_message_delete_command(self, ctx):
        embeds = await Analytics(str(ctx.guild.id), self.bot.db).analyze_message_delete()
        
        paginator = BotEmbedPaginator(ctx, embeds)
        await bot_requests(ctx.message, str(ctx.command), self.bot.db)
        await ctx.trigger_typing()

        return await paginator.run()
    
    @commands.has_permissions(administrator=True)
    @commands.cooldown(1, 10.0, commands.BucketType.user)
    @analyze_command.command(name="reactions")
    async def analyze_reactions_command(self, ctx):
        embeds = await Analytics(str(ctx.guild.id), self.bot.db).analyze_reaction()

        paginator = BotEmbedPaginator(ctx, embeds)
        await bot_requests(ctx.message, str(ctx.command), self.bot.db)
        await ctx.trigger_typing()

        return await paginator.run()
    
    @commands.has_permissions(administrator=True)
    @commands.cooldown(1, 10.0, commands.BucketType.user)
    @analyze_command.command(name="botrequests")
    async def analyze_botrequests_commands(self, ctx):
        embeds = await Analytics(str(ctx.guild.id), self.bot.db).analyze_botrequests()

        paginator = BotEmbedPaginator(ctx, embeds)
        await bot_requests(ctx.message, str(ctx.command), self.bot.db)
        await ctx.trigger_typing()

        return await paginator.run()

    @commands.has_permissions(administrator=True)
    @commands.cooldown(1, 10.0, commands.BucketType.user)
    @analyze_command.command(name="userjoin")
    async def analyze_userjoin_command(self, ctx):
        embeds = await Analytics(str(ctx.guild.id), self.bot.db).analyze_userjoin()
        
        paginator = BotEmbedPaginator(ctx, embeds)
        await bot_requests(ctx.message, str(ctx.command), self.bot.db)
        await ctx.trigger_typing()

        return await paginator.run()
    
    @commands.cooldown(1, 10.0, commands.BucketType.user)
    @commands.cooldown(1, 10.0, commands.BucketType.user)
    @analyze_command.command(name="userleaves", aliases=["userleave"])
    async def analyze_command_userleaves(self, ctx):
        embeds = await Analytics(str(ctx.guild.id), self.bot.db).analyze_userleave()
        
        paginator = BotEmbedPaginator(ctx, embeds)
        await bot_requests(ctx.message, str(ctx.command), self.bot.db)
        await ctx.trigger_typing()
        return await paginator.run()

    @commands.has_permissions(administrator=True)
    @commands.cooldown(1, 10.0, commands.BucketType.user)
    @analyze_command.command(name="mentions", aliases=["mention"])
    async def analyze_command_mentions(self, ctx):
        embeds = await Analytics(str(ctx.guild.id), self.bot.db).analyze_mentions()
        
        paginator = BotEmbedPaginator(ctx, embeds)
        await bot_requests(ctx.message, str(ctx.command), self.bot.db)
        await ctx.trigger_typing()
        
        return await paginator.run()

    @commands.has_permissions(administrator=True)
    @commands.cooldown(1, 10.0, commands.BucketType.user)
    @analyze_command.command(name="botmsg", aliases=["bot_msg", "bot-msg"])
    async def analyze_command_botmsg(self, ctx):
        embeds = await Analytics(str(ctx.guild.id), self.bot.db).analyze_botembeds()
        
        paginator = BotEmbedPaginator(ctx, embeds)
        await bot_requests(ctx.message, str(ctx.command), self.bot.db)
        await ctx.trigger_typing()
        
        return await paginator.run()

    @commands.has_permissions(administrator=True)
    @commands.cooldown(1, 10.0, commands.BucketType.user)
    @analyze_command.command(name="status", aliases=["game"])
    async def analyze_command_status(self, ctx):
        embeds = await Analytics(str(ctx.guild.id), self.bot.db).analyze_status()
        
        paginator = BotEmbedPaginator(ctx, embeds)
        await bot_requests(ctx.message, str(ctx.command), self.bot.db)
        await ctx.trigger_typing()
        
        return await paginator.run()

    @commands.has_permissions(administrator=True)
    @commands.cooldown(1, 10.0, commands.BucketType.user)
    @analyze_command.command(name="users")
    async def analyze_command_botmsg(self, ctx):
        embeds = await Analytics(str(ctx.guild.id), self.bot.db).analyze_users()
        
        paginator = BotEmbedPaginator(ctx, embeds)
        await bot_requests(ctx.message, str(ctx.command), self.bot.db)
        await ctx.trigger_typing()
        
        return await paginator.run()
    
    @commands.has_permissions(administrator=True)
    @commands.cooldown(1, 10.0, commands.BucketType.user)
    @analyze_command.command(name="user_ban")
    async def analyze_command_botmsg(self, ctx):
        embeds = await Analytics(str(ctx.guild.id), self.bot.db).analyze_user_ban()
        
        paginator = BotEmbedPaginator(ctx, embeds)
        await bot_requests(ctx.message, str(ctx.command), self.bot.db)
        await ctx.trigger_typing()
        
        return await paginator.run()
    
    @commands.has_permissions(administrator=True)
    @commands.cooldown(1, 10.0, commands.BucketType.user)
    @analyze_command.command(name="user_unban")
    async def analyze_command_botmsg(self, ctx):
        embeds = await Analytics(str(ctx.guild.id), self.bot.db).analyze_user_unban()
        
        paginator = BotEmbedPaginator(ctx, embeds)
        await bot_requests(ctx.message, str(ctx.command), self.bot.db)
        await ctx.trigger_typing()
        
        return await paginator.run()
    
    @commands.has_permissions(administrator=True)
    @commands.cooldown(1, 10.0, commands.BucketType.user)
    @analyze_command.command(name="voice")
    async def analyze_command_botmsg(self, ctx):
        embeds = await Analytics(str(ctx.guild.id), self.bot.db).analyze_voice()
        
        paginator = BotEmbedPaginator(ctx, embeds)
        await bot_requests(ctx.message, str(ctx.command), self.bot.db)
        await ctx.trigger_typing()
        
        return await paginator.run()
    
    @commands.has_permissions(administrator=True)
    @commands.cooldown(1, 10.0, commands.BucketType.user)
    @analyze_command.command(name="user_nickchange")
    async def analyze_command_botmsg(self, ctx):
        embeds = await Analytics(str(ctx.guild.id), self.bot.db).analyze_nickchange()
        
        paginator = BotEmbedPaginator(ctx, embeds)
        await bot_requests(ctx.message, str(ctx.command), self.bot.db)
        await ctx.trigger_typing()
        
        return await paginator.run()
    
    @commands.has_permissions(administrator=True)
    @commands.cooldown(1, 10.0, commands.BucketType.user)
    @analyze_command.command(name="invites")
    async def analyze_command_botmsg(self, ctx):
        embeds = await Analytics(str(ctx.guild.id), self.bot.db).analyze_invites()
        
        paginator = BotEmbedPaginator(ctx, embeds)
        await bot_requests(ctx.message, str(ctx.command), self.bot.db)
        await ctx.trigger_typing()
        
        return await paginator.run()

    @commands.has_permissions(administrator=True)
    @commands.cooldown(1, 10.0, commands.BucketType.user)
    @analyze_command.command(name="guild_updates")
    async def analyze_command_botmsg(self, ctx):
        embeds = await Analytics(str(ctx.guild.id), self.bot.db).analyze_guild_updates()
        
        paginator = BotEmbedPaginator(ctx, embeds)
        await bot_requests(ctx.message, str(ctx.command), self.bot.db)
        await ctx.trigger_typing()
        
        return await paginator.run()

def setup(bot):
    bot.add_cog(Analyze(bot))
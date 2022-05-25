from discord import Embed
from discord.ext import commands
from util.data import load_data
from analytics.graphics import *
from disputils import BotEmbedPaginator
from dataminer.bot_data import bot_requests

class Plot(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.has_permissions(administrator=True)
    @commands.group(name='plot', invoke_without_command=True)
    async def plot(self, ctx):
        return await ctx.send('test')
    

    @commands.has_permissions(administrator=True)
    @commands.cooldown(1, 30.0, commands.BucketType.user)
    @plot.command(name="message")
    async def plot_message(self, ctx):
        """PLOT MESSAGE DATA"""
        data = await load_data(self.bot.db, str(ctx.guild.id))
        if len(data["message"]) == 0:
            return await ctx.send("No data collected yet!", delete_after=4)        
        hour_plot = plot_timestamp_hours(data["message"], str(ctx.guild.id), "message")
        weekday_plot = plot_timestamp_weekdays(data["message"], str(ctx.guild.id), "message")
        channel_plot = plot_channels(data["message"], str(ctx.guild.id), "message", self.bot)

        embeds = [
            Embed(title="Message Plots:", description="Click to see the different plots"),
            Embed(title="Messages send in which hours:").set_image(url=hour_plot),
            Embed(title="Messages send on which weekdays:").set_image(url=weekday_plot),
            Embed(title="Messages send in which channels").set_image(url=channel_plot)
        ]
        paginator = BotEmbedPaginator(ctx, embeds)
        await bot_requests(ctx.message, str(ctx.command), self.bot.db)
        await ctx.trigger_typing()

        return await paginator.run()

    @commands.has_permissions(administrator=True)
    @commands.cooldown(1, 30.0, commands.BucketType.user)
    @plot.command(name="message_edit")
    async def plot_message_edit(self, ctx):
        """PLOT MESSAGE EDIT DATA"""
        data = await load_data(self.bot.db, str(ctx.guild.id))
        if len(data["message_edit"]) == 0:
            return await ctx.send("No data collected yet!", delete_after=4)        
        hour_plot = plot_timestamp_hours(data["message_edit"], str(ctx.guild.id), "message edits")
        weekday_plot = plot_timestamp_weekdays(data["message_edit"], str(ctx.guild.id), "message edits")
        channel_plot = plot_channels(data["message_edit"], str(ctx.guild.id), "message edits", self.bot)

        embeds = [
            Embed(title="Message Plots:", description="Click to see the different plots"),
            Embed(title="Messages edited in which hours:").set_image(url=hour_plot),
            Embed(title="Messages edited on which weekdays:").set_image(url=weekday_plot),
            Embed(title="Messages edited in which channels").set_image(url=channel_plot)
        ]
        paginator = BotEmbedPaginator(ctx, embeds)
        await bot_requests(ctx.message, str(ctx.command), self.bot.db)
        await ctx.trigger_typing()

        return await paginator.run()
    
    @commands.has_permissions(administrator=True)
    @commands.cooldown(1, 30.0, commands.BucketType.user)
    @plot.command(name="message_delete")
    async def plot_message_delete(self, ctx):
        """PLOT MESSAGE DELETE DATA"""
        data = await load_data(self.bot.db, str(ctx.guild.id))
        if len(data["message_delete"]) == 0:
            return await ctx.send("No data collected yet!", delete_after=4)        
        hour_plot = plot_timestamp_hours(data["message_delete"], str(ctx.guild.id), "message")
        weekday_plot = plot_timestamp_weekdays(data["message_delete"], str(ctx.guild.id), "message")
        channel_plot = plot_channels(data["message_delete"], str(ctx.guild.id), "message", self.bot)

        embeds = [
            Embed(title="Message Plots:", description="Click to see the different plots"),
            Embed(title="Messages deleted in which hours:").set_image(url=hour_plot),
            Embed(title="Messages deleted on which weekdays:").set_image(url=weekday_plot),
            Embed(title="Messages deleted in which channels").set_image(url=channel_plot)
        ]
        paginator = BotEmbedPaginator(ctx, embeds)
        await bot_requests(ctx.message, str(ctx.command), self.bot.db)
        await ctx.trigger_typing()

        return await paginator.run()
    
    @commands.has_permissions(administrator=True)
    @commands.cooldown(1, 30.0, commands.BucketType.user)
    @plot.command(name="reaction")
    async def plot_reaction(self, ctx):
        """PLOT REACTION DATA"""
        data = await load_data(self.bot.db, str(ctx.guild.id))
        if len(data["reaction"]) == 0:
            return await ctx.send("No data collected yet!", delete_after=4)        
        hour_plot = plot_timestamp_hours(data["reaction"], str(ctx.guild.id), "reaction")
        weekday_plot = plot_timestamp_weekdays(data["reaction"], str(ctx.guild.id), "reaction")
        channel_plot = plot_channels(data["reaction"], str(ctx.guild.id), "reaction", self.bot)

        embeds = [
            Embed(title="reaction Plots:", description="Click to see the different plots"),
            Embed(title="reactions send in which hours:").set_image(url=hour_plot),
            Embed(title="reactions send on which weekdays:").set_image(url=weekday_plot),
            Embed(title="reactions send in which channels").set_image(url=channel_plot)
        ]
        paginator = BotEmbedPaginator(ctx, embeds)
        await bot_requests(ctx.message, str(ctx.command), self.bot.db)
        await ctx.trigger_typing()

        return await paginator.run()
    
    @commands.has_permissions(administrator=True)
    @commands.cooldown(1, 30.0, commands.BucketType.user)
    @plot.command(name="botrequests")
    async def plot_botrequests(self, ctx):
        """PLOT BOT REQUESTS DATA"""
        data = await load_data(self.bot.db, str(ctx.guild.id))
        if len(data["bot_requests"]) == 0:
            return await ctx.send("No data collected yet!", delete_after=4)        
        hour_plot = plot_timestamp_hours(data["bot_requests"], str(ctx.guild.id), "bot_requests")
        weekday_plot = plot_timestamp_weekdays(data["bot_requests"], str(ctx.guild.id), "bot_requests")
        channel_plot = plot_channels(data["bot_requests"], str(ctx.guild.id), "bot_requests", self.bot)

        embeds = [
            Embed(title="Bot requests Plots:", description="Click to see the different plots"),
            Embed(title="Bot requests send in which hours:").set_image(url=hour_plot),
            Embed(title="Bot requests send on which weekdays:").set_image(url=weekday_plot),
            Embed(title="Bot requests send in which channels").set_image(url=channel_plot)
        ]
        paginator = BotEmbedPaginator(ctx, embeds)
        await bot_requests(ctx.message, str(ctx.command), self.bot.db)
        await ctx.trigger_typing()

        return await paginator.run()
    
    @commands.has_permissions(administrator=True)
    @commands.cooldown(1, 30.0, commands.BucketType.user)
    @plot.command(name="userjoin")
    async def plot_userjoin(self, ctx):
        """PLOT USERJOIN DATA"""
        data = await load_data(self.bot.db, str(ctx.guild.id))
        if len(data["userjoins"]) == 0:
            return await ctx.send("No data collected yet!", delete_after=4)        
        hour_plot = plot_timestamp_hours(data["userjoins"], str(ctx.guild.id), "userjoins")
        weekday_plot = plot_timestamp_weekdays(data["userjoins"], str(ctx.guild.id), "userjoins")

        embeds = [
            Embed(title="userjoins Plots:", description="Click to see the different plots"),
            Embed(title="userjoins counted in which hours:").set_image(url=hour_plot),
            Embed(title="userjoins counted on which weekdays:").set_image(url=weekday_plot),
        ]
        paginator = BotEmbedPaginator(ctx, embeds)
        await bot_requests(ctx.message, str(ctx.command), self.bot.db)
        await ctx.trigger_typing()

        return await paginator.run()
    
    @commands.has_permissions(administrator=True)
    @commands.cooldown(1, 30.0, commands.BucketType.user)
    @plot.command(name="userleaves")
    async def plot_userleave(self, ctx):
        """PLOT USERLEAVES DATA"""
        data = await load_data(self.bot.db, str(ctx.guild.id))
        if len(data["userleave"]) == 0:
            return await ctx.send("No data collected yet!", delete_after=4)        
        hour_plot = plot_timestamp_hours(data["userleave"], str(ctx.guild.id), "userleave")
        weekday_plot = plot_timestamp_weekdays(data["userleave"], str(ctx.guild.id), "userleave")

        embeds = [
            Embed(title="userleave Plots:", description="Click to see the different plots"),
            Embed(title="userleaves counted in which hours:").set_image(url=hour_plot),
            Embed(title="userleaves counted on which weekdays:").set_image(url=weekday_plot),
        ]
        paginator = BotEmbedPaginator(ctx, embeds)
        await bot_requests(ctx.message, str(ctx.command), self.bot.db)
        await ctx.trigger_typing()

        return await paginator.run()
    
    @commands.has_permissions(administrator=True)
    @commands.cooldown(1, 30.0, commands.BucketType.user)
    @plot.command(name="mentions", aliases=["mention"])
    async def plot_mentions(self, ctx):
        """PLOT MENTIONS DATA"""
        data = await load_data(self.bot.db, str(ctx.guild.id))
        if len(data["mentions"]) == 0:
            return await ctx.send("No data collected yet!", delete_after=4)        
        hour_plot = plot_timestamp_hours(data["mentions"], str(ctx.guild.id), "mentions")
        weekday_plot = plot_timestamp_weekdays(data["mentions"], str(ctx.guild.id), "mentions")
        channel_plot = plot_channels(data["mentions"], str(ctx.guild.id), "mentions", self.bot)

        embeds = [
            Embed(title="mentions Plots:", description="Click to see the different plots"),
            Embed(title="mentions send in which hours:").set_image(url=hour_plot),
            Embed(title="mentions send on which weekdays:").set_image(url=weekday_plot),
            Embed(title="mentions send in which channels").set_image(url=channel_plot)
        ]
        paginator = BotEmbedPaginator(ctx, embeds)
        await bot_requests(ctx.message, str(ctx.command), self.bot.db)
        await ctx.trigger_typing()

        return await paginator.run()
    
    @commands.has_permissions(administrator=True)
    @commands.cooldown(1, 30.0, commands.BucketType.user)
    @plot.command(name="botmsg", aliases=["bot_msg", "bot-msg"])
    async def plot_botmsg(self, ctx):
        """PLOT BOTMSG DATA"""
        data = await load_data(self.bot.db, str(ctx.guild.id))
        if len(data["bot_msg"]) == 0:
            return await ctx.send("No data collected yet!", delete_after=4)
        hour_plot = plot_timestamp_hours(data["bot_msg"], str(ctx.guild.id), "bot_msg")
        weekday_plot = plot_timestamp_weekdays(data["bot_msg"], str(ctx.guild.id), "bot_msg")
        channel_plot = plot_channels(data["bot_msg"], str(ctx.guild.id), "bot_msg", self.bot)

        embeds = [
            Embed(title="Bot message Plots:", description="Click to see the different plots"),
            Embed(title="Bot messages send in which hours:").set_image(url=hour_plot),
            Embed(title="Bot messages send on which weekdays:").set_image(url=weekday_plot),
            Embed(title="Bot messages send in which channels").set_image(url=channel_plot)
        ]
        paginator = BotEmbedPaginator(ctx, embeds)
        await bot_requests(ctx.message, str(ctx.command), self.bot.db)
        await ctx.trigger_typing()

        return await paginator.run()
    
    @commands.has_permissions(administrator=True)
    @commands.cooldown(1, 30.0, commands.BucketType.user)
    @plot.command(name="status", aliases=["game"])
    async def plot_status(self, ctx):
        """PLOT STATUS DATA"""
        data = await load_data(self.bot.db, str(ctx.guild.id))
        if len(data["status"]) == 0:
            return await ctx.send("No data collected yet!", delete_after=4)
        hour_plot = plot_timestamp_hours(data["status"], str(ctx.guild.id), "status")
        weekday_plot = plot_timestamp_weekdays(data["status"], str(ctx.guild.id), "status")

        embeds = [
            Embed(title="status Plots:", description="Click to see the different plots"),
            Embed(title="Status changed in which hours:").set_image(url=hour_plot),
            Embed(title="Status changed on which weekdays:").set_image(url=weekday_plot),
        ]
        paginator = BotEmbedPaginator(ctx, embeds)
        await bot_requests(ctx.message, str(ctx.command), self.bot.db)
        await ctx.trigger_typing()

        return await paginator.run()
    
    @commands.has_permissions(administrator=True)
    @commands.cooldown(1, 30.0, commands.BucketType.user)
    @plot.command(name="users")
    async def plot_users(self, ctx):
        """PLOT USERS DATA"""
        data = await load_data(self.bot.db, str(ctx.guild.id))
        if len(data["users"]) == 0:
            return await ctx.send("No data collected yet!", delete_after=4)
        
        link = plot_users(data["users"], str(ctx.guild.id))

        return await ctx.send(embed=Embed(title="User count plot", description="See the trend of user count").set_image(url=link))
    
    @commands.has_permissions(administrator=True)
    @commands.cooldown(1, 30.0, commands.BucketType.user)
    @plot.command(name="user_ban")
    async def plot_user_ban(self, ctx):
        """PLOT USER BAN DATA"""
        data = await load_data(self.bot.db, str(ctx.guild.id))
        if len(data["user_ban"]) == 0:
            return await ctx.send("No data collected yet!", delete_after=4)
        hour_plot = plot_timestamp_hours(data["user_ban"], str(ctx.guild.id), "user_ban")
        weekday_plot = plot_timestamp_weekdays(data["user_ban"], str(ctx.guild.id), "user_ban")

        embeds = [
            Embed(title="user_ban Plots:", description="Click to see the different plots"),
            Embed(title="user_bans send in which hours:").set_image(url=hour_plot),
            Embed(title="user_bans send on which weekdays:").set_image(url=weekday_plot),
        ]
        paginator = BotEmbedPaginator(ctx, embeds)
        await bot_requests(ctx.message, str(ctx.command), self.bot.db)
        await ctx.trigger_typing()

        return await paginator.run()
    
    @commands.has_permissions(administrator=True)
    @commands.cooldown(1, 30.0, commands.BucketType.user)
    @plot.command(name="user_unban")
    async def plot_user_unban(self, ctx):
        """PLOT USER UNBAN DATA"""
        data = await load_data(self.bot.db, str(ctx.guild.id))
        if len(data["user_unban"]) == 0:
            return await ctx.send("No data collected yet!", delete_after=4)
        hour_plot = plot_timestamp_hours(data["user_unban"], str(ctx.guild.id), "user_unban")
        weekday_plot = plot_timestamp_weekdays(data["user_unban"], str(ctx.guild.id), "user_unban")

        embeds = [
            Embed(title="user_unban Plots:", description="Click to see the different plots"),
            Embed(title="user_unbans send in which hours:").set_image(url=hour_plot),
            Embed(title="user_unbans send on which weekdays:").set_image(url=weekday_plot),
        ]
        paginator = BotEmbedPaginator(ctx, embeds)
        await bot_requests(ctx.message, str(ctx.command), self.bot.db)
        await ctx.trigger_typing()

        return await paginator.run()
    
    @commands.has_permissions(administrator=True)
    @commands.cooldown(1, 30.0, commands.BucketType.user)
    @plot.command(name="voice")
    async def plot_voice(self, ctx):
        """PLOT VOICE DATA"""
        data = await load_data(self.bot.db, str(ctx.guild.id))
        if len(data["voice"]) == 0:
            return await ctx.send("No data collected yet!", delete_after=4)
        hour_plot = plot_timestamp_hours(data["voice"], str(ctx.guild.id), "voice")
        weekday_plot = plot_timestamp_weekdays(data["voice"], str(ctx.guild.id), "voice")
        channel_plot = plot_channels(data["voice"], str(ctx.guild.id), "voice", self.bot)

        embeds = [
            Embed(title="voice Plots:", description="Click to see the different plots"),
            Embed(title="voices connected in which hours:").set_image(url=hour_plot),
            Embed(title="voices connected on which weekdays:").set_image(url=weekday_plot),
            Embed(title="voices connected in which channels").set_image(url=channel_plot)
        ]
        paginator = BotEmbedPaginator(ctx, embeds)
        await bot_requests(ctx.message, str(ctx.command), self.bot.db)
        await ctx.trigger_typing()

        return await paginator.run()
    
    @commands.has_permissions(administrator=True)
    @commands.cooldown(1, 30.0, commands.BucketType.user)
    @plot.command(name="user_nickchange")
    async def plot_user_nickchange(self, ctx):
        """PLOT USER NICKCHANGE DATA"""
        data = await load_data(self.bot.db, str(ctx.guild.id))
        if len(data["user_nickchange"]) == 0:
            return await ctx.send("No data collected yet!", delete_after=4)
        hour_plot = plot_timestamp_hours(data["user_nickchange"], str(ctx.guild.id), "user_nickchange")
        weekday_plot = plot_timestamp_weekdays(data["user_nickchange"], str(ctx.guild.id), "user_nickchange")

        embeds = [
            Embed(title="user nickchange Plots:", description="Click to see the different plots"),
            Embed(title="user nickchanges send in which hours:").set_image(url=hour_plot),
            Embed(title="user nickchanges send on which weekdays:").set_image(url=weekday_plot),
        ]
        paginator = BotEmbedPaginator(ctx, embeds)
        await bot_requests(ctx.message, str(ctx.command), self.bot.db)
        await ctx.trigger_typing()

        return await paginator.run()
    
    @commands.has_permissions(administrator=True)
    @commands.cooldown(1, 30.0, commands.BucketType.user)
    @plot.command(name="invites")
    async def plot_invites(self, ctx):
        """PLOT INVITES DATA"""
        data = await load_data(self.bot.db, str(ctx.guild.id))
        if len(data["invite_create"]) == 0:
            return await ctx.send("No data collected yet!", delete_after=4)
        hour_plot = plot_timestamp_hours(data["invite_create"], str(ctx.guild.id), "invite_create")
        weekday_plot = plot_timestamp_weekdays(data["invite_create"], str(ctx.guild.id), "invite_create")

        embeds = [
            Embed(title="invite_create Plots:", description="Click to see the different plots"),
            Embed(title="invite_creates send in which hours:").set_image(url=hour_plot),
            Embed(title="invite_creates send on which weekdays:").set_image(url=weekday_plot),
        ]
        paginator = BotEmbedPaginator(ctx, embeds)
        await bot_requests(ctx.message, str(ctx.command), self.bot.db)
        await ctx.trigger_typing()

        return await paginator.run()
    
    @commands.has_permissions(administrator=True)
    @commands.cooldown(1, 30.0, commands.BucketType.user)
    @plot.command(name="guild_updates")
    async def plot_guild_updates(self, ctx):
        """PLOT GUILD UPDATES DATA"""
        data = await load_data(self.bot.db, str(ctx.guild.id))
        if len(data["guild_update"]) == 0:
            return await ctx.send("No data collected yet!", delete_after=4)
        hour_plot = plot_timestamp_hours(data["guild_update"], str(ctx.guild.id), "guild_update")
        weekday_plot = plot_timestamp_weekdays(data["guild_update"], str(ctx.guild.id), "guild_update")

        embeds = [
            Embed(title="guild_update Plots:", description="Click to see the different plots"),
            Embed(title="guild_updates send in which hours:").set_image(url=hour_plot),
            Embed(title="guild_updates send on which weekdays:").set_image(url=weekday_plot),
        ]
        paginator = BotEmbedPaginator(ctx, embeds)
        await bot_requests(ctx.message, str(ctx.command), self.bot.db)
        await ctx.trigger_typing()

        return await paginator.run()

def setup(bot):
    bot.add_cog(Plot(bot))
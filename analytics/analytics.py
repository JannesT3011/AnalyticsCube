from json import load

from matplotlib.pyplot import title
from database.database import DbClient
from discord import Embed
import pandas as pd
from util.data import load_data


class Analytics:
    def __init__(self, server_id: str, db):
        self.server_id = server_id
        self.db = db

    @staticmethod
    def no_data_embed(topic: str) -> Embed:
        """CREATE AN EMBED IF NO DATA WAS COLLECTED"""
        embed = Embed(title="SORRY", description=f"Sorry, but there were no `{topic}` data collected on this server!")
        return embed

    async def analyze_message(self):
        """ANALYZE THE MESSAGE DATA"""
        data = await load_data(self.db, self.server_id)
        data = data["message"]
        if len(data) == 0:
            return self.no_data_embed("message")

        # ANALYZE THE DATA:
        df = pd.DataFrame(data)
        channelid_counts = pd.value_counts(df["channelid"])
        role_counts = pd.value_counts(df["roles"])
        df["timestamp"] = pd.to_datetime(df["timestamp"])
        df["hours"] = df["timestamp"].dt.hour
        df["weekday"] = df["timestamp"].dt.day_name()
        hours_count = pd.value_counts(df["hours"])
        weekday_count = pd.value_counts(df["weekday"])

        embed_title = "Message ~ Analytics"
        embeds = [
            Embed(title=embed_title, description="Here you can see the analyzed message data"),
            Embed(title=embed_title, description="Message counted in channels:\n"f"```{channelid_counts}```"),
            Embed(title=embed_title, description="Message send from roles:\n"f"```{role_counts}```"),
            Embed(title=embed_title, description="Message counted in which hours:\n"f"```{hours_count}```"),
            Embed(title=embed_title, description="Message counted on which weekday:\n"f"```{weekday_count}```")
        ]
        return embeds
    
    async def analyze_message_delete(self):
        """ANALYZE MESSAGE DELETE"""
        data = await load_data(self.db, self.server_id)
        data = data["message_delete"]
        if len(data) == 0:
            return self.no_data_embed("message delete")
        
        # ANALYZE THE DATA
        df = pd.DataFrame(data)
        role_counts = pd.value_counts(df["roles"])
        channelid_counts = pd.value_counts(df["channelid"])
        df["timestamp"] = pd.to_datetime(df["timestamp"])
        df["hours"] = df["timestamp"].dt.hour
        df["weekday"] = df["timestamp"].dt.day_name()
        hours_count = pd.value_counts(df["hours"])
        weekday_count = pd.value_counts(df["weekday"])

        embed_title = "Message delete ~ Analytics"
        embeds = [
            Embed(title=embed_title, description="Here you can see the analyzed message edit data"),
            Embed(title=embed_title, description="Message delete counted in channels:\n"f"```{channelid_counts}```"),
            Embed(title=embed_title, description="Message delete from roles:\n"f"```{role_counts}```"),
            Embed(title=embed_title, description="Message delete counted in which hours:\n"f"```{hours_count}```"),
            Embed(title=embed_title, description="Message delete counted on which weekday:\n"f"```{weekday_count}```")
        ]
        return embeds
    
    async def analyze_message_edit(self):
        """ANALYZE MESSAGE EDIT"""
        data = await load_data(self.db, self.server_id)
        data = data["message_edit"]
        if len(data) == 0:
            return self.no_data_embed("message edit")
        
        # ANALYZE THE DATA
        df = pd.DataFrame(data)
        role_counts = pd.value_counts(df["roles"])
        channelid_counts = pd.value_counts(df["channelid"])
        df["timestamp"] = pd.to_datetime(df["timestamp"])
        df["hours"] = df["timestamp"].dt.hour
        df["weekday"] = df["timestamp"].dt.day_name()
        hours_count = pd.value_counts(df["hours"])
        weekday_count = pd.value_counts(df["weekday"])

        embed_title = "Message edit ~ Analytics"
        embeds = [
            Embed(title=embed_title, description="Here you can see the analyzed message edit data"),
            Embed(title=embed_title, description="Message edits counted in channels:\n"f"```{channelid_counts}```"),
            Embed(title=embed_title, description="Message edits from roles:\n"f"```{role_counts}```"),
            Embed(title=embed_title, description="Message edits counted in which hours:\n"f"```{hours_count}```"),
            Embed(title=embed_title, description="Message edits counted on which weekday:\n"f"```{weekday_count}```")
        ]
        return embeds


    async def analyze_reaction(self):
        """ANALYZE THE REACTION DATA"""
        data = await load_data(self.db, self.server_id)
        data = data["reaction"]
        if len(data) == 0:
            return self.no_data_embed("reaction")

        # ANALYZE THE DATA:
        df = pd.DataFrame(data)
        name_count = pd.value_counts(df["reactionname"])
        role_counts = pd.value_counts(df["roles"])
        channelid_counts = pd.value_counts(df["channelid"])
        df["timestamp"] = pd.to_datetime(df["timestamp"])
        df["hours"] = df["timestamp"].dt.hour
        df["weekday"] = df["timestamp"].dt.day_name()
        hours_count = pd.value_counts(df["hours"])
        weekday_count = pd.value_counts(df["weekday"])

        embed_title = "Reaction ~ Analytics"
        embeds = [
            Embed(title=embed_title, description="Here you can see the analyzed reaction data"),
            Embed(title=embed_title, description="Reaction counted by name:\n"f"```{name_count}```"),
            Embed(title=embed_title, description="Reaction counted in channels:\n"f"```{channelid_counts}```"),
            Embed(title=embed_title, description="Reaction send from roles:\n"f"```{role_counts}```"),
            Embed(title=embed_title, description="Reaction counted in which hours:\n"f"```{hours_count}```"),
            Embed(title=embed_title, description="Reaction counted on which weekday:\n"f"```{weekday_count}```")
        ]
        return embeds

    async def analyze_botrequests(self):
        """ANALYZE THE BOT-REQUESTS DATA"""
        data = await load_data(self.db, self.server_id)
        data = data["bot_requests"]
        if len(data) == 0:
            return self.no_data_embed("bot-requests")

        # ANALYZE THE DATA:
        df = pd.DataFrame(data)
        name_count = pd.value_counts(df["cmdname"])
        role_counts = pd.value_counts(df["roles"])
        channelid_counts = pd.value_counts(df["channelid"])
        embed_title = "Bot-Requests ~ Analytics"
        df["timestamp"] = pd.to_datetime(df["timestamp"])
        df["hours"] = df["timestamp"].dt.hour
        df["weekday"] = df["timestamp"].dt.day_name()
        hours_count = pd.value_counts(df["hours"])
        weekday_count = pd.value_counts(df["weekday"])

        embeds = [
            Embed(title=embed_title, description="Here you can see the analyzed bot-requests data"),
            Embed(title=embed_title, description="Executed CMD-names counted:\n"f"```{name_count}```"),
            Embed(title=embed_title, description="Bot-Requests messages counted in channels:\n"f"```{channelid_counts}```"),
            Embed(title=embed_title, description="Bot-Requests messages send from roles:\n"f"```{role_counts}```"),
            Embed(title=embed_title, description="Bot-Requests counted in which hours:\n"f"```{hours_count}```"),
            Embed(title=embed_title, description="Bot-Requests counted on which weekday:\n"f"```{weekday_count}```")
        ]
        return embeds

    async def analyze_botmsg(self):
        """ANALYZE THE BOT MSG DATA"""
        data = await load_data(self.db, self.server_id)
        data = data["bot_msg"]
        if len(data) == 0:
            return self.no_data_embed("bot-message")

        # ANALYZE THE DATA:
        df = pd.DataFrame(data)
        channelid_counts = pd.value_counts(df["channelid"])
        role_counts = pd.value_counts(df["roles"])
        df["timestamp"] = pd.to_datetime(df["timestamp"])
        df["hours"] = df["timestamp"].dt.hour
        df["weekday"] = df["timestamp"].dt.day_name()
        hours_count = pd.value_counts(df["hours"])
        weekday_count = pd.value_counts(df["weekday"])

        embed_title = "Bot-Message ~ Analytics"
        embeds = [
            Embed(title=embed_title, description="Here you can see the analyzed bot-message data"),
            Embed(title=embed_title, description=f"Total bot messages: {len(data)}"),
            Embed(title=embed_title, description="BotMessages counted in channels:\n"f"```{channelid_counts}```"),
            Embed(title=embed_title, description="BotMessages send from roles:\n"f"```{role_counts}```"),
            Embed(title=embed_title, description="BotMessages send in which hours:\n"f"```{hours_count}```"),
            Embed(title=embed_title, description="BotMessages send on which day:\n"f"```{weekday_count}```")
        ]
        return embeds

    async def analyze_users(self): # TODO show last 10 users at timestamp
        data = await load_data(self.db, self.server_id)
        data = data["users"]
        if len(data) == 0:
            return self.no_data_embed("users")
        
        # ANALYZE THE DATA:
        df = pd.DataFrame(data)
        result = df.head(10)
        #df["timestamp"] = pd.to_datetime(df["timestamp"])
        #df["hours"] = df["timestamp"].dt.hour
        #df["weekday"] = df["timestamp"].dt.day_name()
        #hours_count = pd.value_counts(df["hours"])
        #weekday_count = pd.value_counts(df["weekday"])

        embed_title = "Users ~ Analytics"
        embeds = [
            Embed(title=embed_title, description="Here you can see the analyzed users data"),
            Embed(title=embed_title, description=f"```{result}```")
            #Embed(title=embed_title, description="Users counted in which hours:\n"f"```{hours_count}```"),
            #Embed(title=embed_title, description="Users counted in which hours:\n"f"```{hours_count}```"),
            #Embed(title=embed_title, description="Users counted on which weekdays:\n"f"```{weekday_count}```")
        ]
        return embeds
        

    async def analyze_userjoin(self):
        data = await load_data(self.db, self.server_id)
        data = data["userjoins"]
        if len(data) == 0:
            return self.no_data_embed("userjoins")

        # ANALYZE THE DATA:
        df = pd.DataFrame(data)
        df["timestamp"] = pd.to_datetime(df["timestamp"])
        df["hours"] = df["timestamp"].dt.hour
        df["weekday"] = df["timestamp"].dt.day_name()
        hours_count = pd.value_counts(df["hours"])
        weekday_count = pd.value_counts(df["weekday"])

        embed_title = "Userjoin ~ Analytics"
        embeds = [
            Embed(title=embed_title, description="Here you can see the analyzed message data"),
            Embed(title=embed_title, description="Userjoins counted in which hours:\n"f"```{hours_count}```"),
            Embed(title=embed_title, description="Userjoins counted on which weekdays:\n"f"```{weekday_count}```")
        ]
        return embeds

    async def analyze_userleave(self):
        data = await load_data(self.db, self.server_id)
        data = data["userleave"]
        if len(data) == 0:
            return self.no_data_embed("userleave")

        # ANALYZE THE DATA:
        df = pd.DataFrame(data)
        df["timestamp"] = pd.to_datetime(df["timestamp"])
        df["hours"] = df["timestamp"].dt.hour
        df["weekday"] = df["timestamp"].dt.day_name()
        hours_count = pd.value_counts(df["hours"])
        weekday_count = pd.value_counts(df["weekday"])

        embed_title = "Userleave ~ Analytics"

        embeds = [
            Embed(title=embed_title, description="Here you can see the analyzed message data"),
            Embed(title=embed_title, description="Userleaves counted in which hour:\n"f"```{hours_count}```"),
            Embed(title=embed_title, description="Userleaves counted on which weekday:\n"f"```{weekday_count}```")
        ]
        return embeds

    async def analyze_mentions(self):
        data = await load_data(self.db, self.server_id)
        data = data["mentions"]
        if len(data) == 0:
            return self.no_data_embed("mentions")

        # ANALYZE THE DATA:
        df = pd.DataFrame(data)
        ment_roles_counts = pd.value_counts(df["ment_role"])
        role_counts = pd.value_counts(df["roles"])
        channelid_counts = pd.value_counts(df["channelid"])
        df["timestamp"] = pd.to_datetime(df["timestamp"])
        df["hours"] = df["timestamp"].dt.hour
        df["weekday"] = df["timestamp"].dt.day_name()
        hours_count = pd.value_counts(df["hours"])
        weekday_count = pd.value_counts(df["weekday"])

        embed_title = "Mentions ~ Analytics"

        embeds = [
            Embed(title=embed_title, description="Here you can see the analyzed mentions data"),
            Embed(title=embed_title, description="Mentions counted in channels:\n"f"```{channelid_counts}```"),
            Embed(title=embed_title, description="Mentions send from roles:\n"f"```{role_counts}```"),
            Embed(title=embed_title, description="Roles mentioned:\n"f"```{ment_roles_counts}```"),
            Embed(title=embed_title, description="Mentions counted in which hour:\n"f"```{hours_count}```"),
            Embed(title=embed_title, description="Mentions counted on which weekday:\n"f"```{weekday_count}```")
        ]
        return embeds

    async def analyze_status(self): # TODO falsche felder
        data = await load_data(self.db, self.server_id)
        data = data["status"]
        if len(data) == 0:
            return self.no_data_embed("status")

        # ANALYZE THE DATA:
        df = pd.DataFrame(data)
        df["timestamp"] = pd.to_datetime(df["timestamp"])
        df["hours"] = df["timestamp"].dt.hour
        df["weekday"] = df["timestamp"].dt.day_name()
        hours_count = pd.value_counts(df["hours"])
        weekday_count = pd.value_counts(df["weekday"])
        game_counts = pd.value_counts(df["game"])
        role_counts = pd.value_counts(df["roles"])

        embed_title = "Status/Game ~ Analytics"

        embeds = [
            Embed(title=embed_title, description="Here you can see the analyzed message data"),
            Embed(title=embed_title, description="Which games play the most:\n"f"```{game_counts}```"),
            Embed(title=embed_title, description="Game played from which roles:\n"f"```{role_counts}```"),
            Embed(title=embed_title, description="Game counted in which hour:\n"f"```{hours_count}```"),
            Embed(title=embed_title, description="Game counted on which weekday:\n"f"```{weekday_count}```")
        ]
        return embeds
    
    async def analyze_user_ban(self):
        data = await load_data(self.db, self.server_id)
        data = data["user_ban"]
        if len(data) == 0:
            return self.no_data_embed("user ban")
        
        # ANALYZE THE DATA:
        df = pd.DataFrame(data)
        df["timestamp"] = pd.to_datetime(df["timestamp"])
        df["hours"] = df["timestamp"].dt.hour
        df["weekday"] = df["timestamp"].dt.day_name()
        hours_count = pd.value_counts(df["hours"])
        weekday_count = pd.value_counts(df["weekday"])

        embed_title = "User bans ~ Analytics"

        embeds = [
            Embed(title=embed_title, description="Here you can see the analyzed user ban data"),
            Embed(title=embed_title, description="User bans counted in which hour:\n"f"```{hours_count}```"),
            Embed(title=embed_title, description="User bans counted on which weekday:\n"f"```{weekday_count}```")
        ]
        return embeds
    
    async def analyze_user_unban(self):
        data = await load_data(self.db, self.server_id)
        data = data["user_unban"]
        if len(data) == 0:
            return self.no_data_embed("user unban")
        
        # ANALYZE THE DATA:
        df = pd.DataFrame(data)
        df["timestamp"] = pd.to_datetime(df["timestamp"])
        df["hours"] = df["timestamp"].dt.hour
        df["weekday"] = df["timestamp"].dt.day_name()
        hours_count = pd.value_counts(df["hours"])
        weekday_count = pd.value_counts(df["weekday"])

        embed_title = "User unbans ~ Analytics"

        embeds = [
            Embed(title=embed_title, description="Here you can see the analyzed user unban data"),
            Embed(title=embed_title, description="User bans counted in which hour:\n"f"```{hours_count}```"),
            Embed(title=embed_title, description="User bans counted on which weekday:\n"f"```{weekday_count}```")
        ]
        return embeds
    
    async def analyze_voice(self): # TOOD leave/join at timestamp
        data = await load_data(self.db, self.server_id)
        data  = data["voice"]
        if len(data) == 0:
            return self.no_data_embed("voice")
        
        # ANALYZE THE DATA:
        df = pd.DataFrame(data)
        df["timestamp"] = pd.to_datetime(df["timestamp"])
        df["hours"] = df["timestamp"].dt.hour
        df["weekday"] = df["timestamp"].dt.day_name()
        hours_count = pd.value_counts(df["hours"])
        weekday_count = pd.value_counts(df["weekday"])
        channel_count = pd.value_counts(df["channel"])
        join_count = pd.value_counts(df["join"])
        leave_count = pd.value_counts(~df["join"])
        role_counts = pd.value_counts(df["roles"])

        embed_title = "Voice channels ~ Analytics"

        embeds = [
            Embed(title=embed_title, description="Here you can see the analyzed user unban data"),
            Embed(title=embed_title, description="User connected the most to channel:\n"f"```{channel_count}```"),
            Embed(title=embed_title, description="Voice joins/leaves counted in which hour:\n"f"```{hours_count}```"),
            Embed(title=embed_title, description="Voice joins/leaves counted on which weekday:\n"f"```{weekday_count}```"),
            Embed(title=embed_title, description="Join counts overall\n"f"{join_count}"),
            Embed(title=embed_title, description="Leave counts overall\n"f"{leave_count}"),
            Embed(title=embed_title, description="Channel joins/leaves from which roles\n"f"{role_counts}")
        ]
        return embeds
    
    async def analyze_nickchange(self):
        data = await load_data(self.db, self.server_id)
        data["user_nickchange"]
        if len(data) == 0:
            return self.no_data_embed("Nickname change")
        
        # ANALYZE THE DATA:
        df = pd.DataFrame(data)
        df["timestamp"] = pd.to_datetime(df["timestamp"])
        df["hours"] = df["timestamp"].dt.hour
        df["weekday"] = df["timestamp"].dt.day_name()
        hours_count = pd.value_counts(df["hours"])
        weekday_count = pd.value_counts(df["weekday"])
        role_counts = pd.value_counts(df["roles"])

        embed_title = "Nickname change ~ Analytics"

        embeds = [
            Embed(title=embed_title, description="Here you can see the analyzed user unban data"),
            Embed(title=embed_title, description="User nickname change counted in which hour:\n"f"```{hours_count}```"),
            Embed(title=embed_title, description="User nickname change counted on which weekday:\n"f"```{weekday_count}```"),
            Embed(title=embed_title, description="User nickname change from which roles\n"f"{role_counts}")
        ]
        return embeds
    
    async def analyze_invites(self):
        data = await load_data(self.db, self.server_id)
        data["invite_create"]
        if len(data) == 0:
            return self.no_data_embed("Invite create")
        
        # ANALYZE THE DATA:
        df = pd.DataFrame(data)
        df["timestamp"] = pd.to_datetime(df["timestamp"])
        df["hours"] = df["timestamp"].dt.hour
        df["weekday"] = df["timestamp"].dt.day_name()
        hours_count = pd.value_counts(df["hours"])
        weekday_count = pd.value_counts(df["weekday"])

        embed_title = "Invites ~ Analytics"

        embeds = [
            Embed(title=embed_title, description="Here you can see the analyzed user unban data"),
            Embed(title=embed_title, description="Invite creation counted in which hour:\n"f"```{hours_count}```"),
            Embed(title=embed_title, description="Invite creation counted on which weekday:\n"f"```{weekday_count}```")
        ]
        return embeds
    
    async def analyze_guild_updates(self):
        data = await load_data(self.db, self.server_id)
        data["guild_update"]
        if len(data) == 0:
            return self.no_data_embed("Guild update")
        
        # ANALYZE THE DATA:
        df = pd.DataFrame(data)
        df["timestamp"] = pd.to_datetime(df["timestamp"])
        df["hours"] = df["timestamp"].dt.hour
        df["weekday"] = df["timestamp"].dt.day_name()
        hours_count = pd.value_counts(df["hours"])
        weekday_count = pd.value_counts(df["weekday"])

        embed_title = "Guild updates ~ Analytics"

        embeds = [
            Embed(title=embed_title, description="Here you can see the analyzed user unban data"),
            Embed(title=embed_title, description="Guild updates counted in which hour:\n"f"```{hours_count}```"),
            Embed(title=embed_title, description="Guild updates counted on which weekday:\n"f"```{weekday_count}```")
        ]
        return embeds
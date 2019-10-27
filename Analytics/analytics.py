from core import DbClient
from discord import Embed
import pandas
from util.create_csv import CSV


class Analytics:
    def __init__(self, server_id: str):
        self.db = DbClient().collection
        self.server_id = server_id
        self.data = self.db.find_one({"_id": server_id})

    @staticmethod
    def no_data_embed(topic: str) -> Embed:
        """CREATE AN EMBED IF NO DATA WAS COLLECTED"""
        embed = Embed(title="SORRY", description=f"Sorry, but there were no `{topic}` data collected on this server!")
        return embed

    def analyze_message(self):
        """ANALYZE THE MESSAGE DATA"""
        data = self.data["message"]

        if len(data) == 0:
            return self.no_data_embed("message")

        # CONVERT MONGODB JSON DATA TO CSV:
        CSV(self.server_id, data).create_csv("message")

        # ANALYZE THE DATA:
        df = pandas.read_csv(f"./src/csv/{self.server_id}_message.csv")
        channelid_counts = pandas.value_counts(df["channelid"])
        role_counts = pandas.value_counts(df["roles"])
        df["timestamp"] = pandas.to_datetime(df["timestamp"])
        df["hours"] = df["timestamp"].dt.hour
        df["weekday"] = df["timestamp"].dt.day_name()
        hours_count = pandas.value_counts(df["hours"])
        weekday_count = pandas.value_counts(df["weekday"])

        embed_title = "Message ~ Analytics"
        embeds = [
            Embed(title=embed_title, description="Here you can see the analyzed message data"),
            Embed(title=embed_title, description="Message counted in channels:\n"f"```{channelid_counts}```"),
            Embed(title=embed_title, description="Message send from roles:\n"f"```{role_counts}```"),
            Embed(title=embed_title, description="Message counted in which hours:\n"f"```{hours_count}```"),
            Embed(title=embed_title, description="Message counted on which weekday:\n"f"```{weekday_count}```")
        ]
        return embeds

    def analyze_reaction(self):
        """ANALYZE THE REACTION DATA"""
        data = self.data["reaction"]

        if len(data) == 0:
            return self.no_data_embed("reaction")

        # CONVERT MONGODB JSON DATA TO CSV:
        CSV(self.server_id, data).create_csv("reaction")

        # ANALYZE THE DATA:
        df = pandas.read_csv(f"./src/csv/{self.server_id}_reaction.csv")
        name_count = pandas.value_counts(df["reactionname"])
        role_counts = pandas.value_counts(df["roles"])
        channelid_counts = pandas.value_counts(df["channelid"])
        df["timestamp"] = pandas.to_datetime(df["timestamp"])
        df["hours"] = df["timestamp"].dt.hour
        df["weekday"] = df["timestamp"].dt.day_name()
        hours_count = pandas.value_counts(df["hours"])
        weekday_count = pandas.value_counts(df["weekday"])

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

    def analyze_botrequests(self):
        """ANALYZE THE BOT-REQUESTS DATA"""
        data = self.data["bot_requests"]

        if len(data) == 0:
            return self.no_data_embed("bot-requests")

        # CONVERT MONGODB JSON DATA TO CSV:
        CSV(self.server_id, data).create_csv("bot_requests")
        # ANALYZE THE DATA:
        df = pandas.read_csv(f"./src/csv/{self.server_id}_bot_requests.csv")
        name_count = pandas.value_counts(df["cmdname"])
        role_counts = pandas.value_counts(df["roles"])
        channelid_counts = pandas.value_counts(df["channelid"])
        embed_title = "Bot-Requests ~ Analytics"
        df["timestamp"] = pandas.to_datetime(df["timestamp"])
        df["hours"] = df["timestamp"].dt.hour
        df["weekday"] = df["timestamp"].dt.day_name()
        hours_count = pandas.value_counts(df["hours"])
        weekday_count = pandas.value_counts(df["weekday"])

        embeds = [
            Embed(title=embed_title, description="Here you can see the analyzed bot-requests data"),
            Embed(title=embed_title, description="Executed CMD-names counted:\n"f"```{name_count}```"),
            Embed(title=embed_title, description="Bot-Requests messages counted in channels:\n"f"```{channelid_counts}```"),
            Embed(title=embed_title, description="Bot-Requests messages send from roles:\n"f"```{role_counts}```"),
            Embed(title=embed_title, description="Bot-Requests counted in which hours:\n"f"```{hours_count}```"),
            Embed(title=embed_title, description="Bot-Requests counted on which weekday:\n"f"```{weekday_count}```")
        ]
        return embeds

    def analyze_botmsg(self):
        """ANALYZE THE BOT MSG DATA"""
        data = self.data["bot_msg"]

        if len(data) == 0:
            return self.no_data_embed("bot-message")

        # CONVERT MONGODB JSON DATA TO CSV:
        CSV(self.server_id, data).create_csv("bot_msg")

        # ANALYZE THE DATA:
        df = pandas.read_csv(f"./src/csv/{self.server_id}_bot_msg.csv")
        channelid_counts = pandas.value_counts(df["channelid"])
        role_counts = pandas.value_counts(df["roles"])
        df["timestamp"] = pandas.to_datetime(df["timestamp"])
        df["hours"] = df["timestamp"].dt.hour
        df["weekday"] = df["timestamp"].dt.day_name()
        hours_count = pandas.value_counts(df["hours"])
        weekday_count = pandas.value_counts(df["weekday"])

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

    def analyze_userjoin(self):
        data = self.data["userjoins"]

        if len(data) == 0:
            return self.no_data_embed("userjoins")

        # CONVERT MONGODB JSON DATA TO CSV:
        CSV(self.server_id, data).create_csv("userjoin")

        # ANALYZE THE DATA:
        df = pandas.read_csv(f"./src/csv/{self.server_id}_userjoin.csv")
        df["timestamp"] = pandas.to_datetime(df["timestamp"])
        df["hours"] = df["timestamp"].dt.hour
        df["weekday"] = df["timestamp"].dt.day_name()
        hours_count = pandas.value_counts(df["hours"])
        weekday_count = pandas.value_counts(df["weekday"])

        embed_title = "Userjoin ~ Analytics"
        embeds = [
            Embed(title=embed_title, description="Here you can see the analyzed message data"),
            Embed(title=embed_title, description="Userjoins counted in channels:\n"f"```{hours_count}```"),
            Embed(title=embed_title, description="Userjoins send from roles:\n"f"```{weekday_count}```")
        ]
        return embeds

    def analyze_userleave(self):
        data = self.data["userleave"]

        if len(data) == 0:
            return self.no_data_embed("userleave")

        # CONVERT MONGODB JSON DATA TO CSV:
        CSV(self.server_id, data).create_csv("userleave")

        # ANALYZE THE DATA:
        df = pandas.read_csv(f"./src/csv/{self.server_id}_userleave.csv")
        df["timestamp"] = pandas.to_datetime(df["timestamp"])
        df["hours"] = df["timestamp"].dt.hour
        df["weekday"] = df["timestamp"].dt.day_name()
        hours_count = pandas.value_counts(df["hours"])
        weekday_count = pandas.value_counts(df["weekday"])

        embed_title = "Userleave ~ Analytics"

        embeds = [
            Embed(title=embed_title, description="Here you can see the analyzed message data"),
            Embed(title=embed_title, description="Userleaves counted in which hour:\n"f"```{hours_count}```"),
            Embed(title=embed_title, description="Userleaves counted on which weekday:\n"f"```{weekday_count}```")
        ]
        return embeds

    def analyze_mentions(self):
        data = self.data["mentions"]
        print(data)
        if len(data) == 0:
            return self.no_data_embed("mentions")

        # CONVERT MONGODB JSON DATA TO CSV:
        CSV(self.server_id, data).create_csv("mentions")

        # ANALYZE THE DATA:
        df = pandas.read_csv(f"./src/csv/{self.server_id}_mentions.csv")
        ment_roles_counts = pandas.value_counts(df["ment_role"])
        role_counts = pandas.value_counts(df["roles"])
        channelid_counts = pandas.value_counts(df["channelid"])
        df["timestamp"] = pandas.to_datetime(df["timestamp"])
        df["hours"] = df["timestamp"].dt.hour
        df["weekday"] = df["timestamp"].dt.day_name()
        hours_count = pandas.value_counts(df["hours"])
        weekday_count = pandas.value_counts(df["weekday"])

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

    def analyze_status(self):
        data = self.data["status"]

        if len(data) == 0:
            return self.no_data_embed("status")

        # CONVERT MONGODB JSON DATA TO CSV:
        CSV(self.server_id, data).create_csv("status")

        # ANALYZE THE DATA:
        df = pandas.read_csv(f"./src/csv/{self.server_id}_status.csv")
        df["timestamp"] = pandas.to_datetime(df["timestamp"])
        df["hours"] = df["timestamp"].dt.hour
        df["weekday"] = df["timestamp"].dt.day_name()
        hours_count = pandas.value_counts(df["hours"])
        weekday_count = pandas.value_counts(df["weekday"])
        game_counts = pandas.value_counts(df["game"])
        role_counts = pandas.value_counts(df["roles"])

        embed_title = "Status/Game ~ Analytics"

        embeds = [
            Embed(title=embed_title, description="Here you can see the analyzed message data"),
            Embed(title=embed_title, description="Which games play the most:\n"f"```{game_counts}```"),
            Embed(title=embed_title, description="Game played from which roles:\n"f"```{role_counts}```"),
            Embed(title=embed_title, description="Game counted in which hour:\n"f"```{hours_count}```"),
            Embed(title=embed_title, description="Game counted on which weekday:\n"f"```{weekday_count}```")
        ]
        return embeds
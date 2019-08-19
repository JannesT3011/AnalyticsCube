from core import DbClient
from discord import Embed
import pandas
from util.create_csv import create_csv
from dataminer import today, month, year


class MessageAnalytics:
    def __init__(self, server_id: str):
        self.db = DbClient().collection
        self.server_id = server_id
        self.data = self.db.find_one({"_id": server_id})

    @staticmethod
    def no_data_embed(topic: str) -> Embed:
        """CREATE AN EMBED IF NO DATA WAS COLLECTED"""
        embed = Embed(title="SORRY", description=f"Sorry, but there were no `{topic}` collected on this server!")
        return embed

    def analyze(self):
        """ANALYZE THE MESSAGE DATA"""
        data = self.data["message"]

        if len(data) == 0:
            return self.no_data_embed("message")
        elif len(data) == 1:
            return data[0]

        # CONVERT MONGODB JSON DATA TO CSV
        csv_col = ["msgid", "timestamp", "roles", "channelid"]
        csv_file = f"./src/csv/{self.server_id}_message.csv"
        create_csv(csv_file, csv_col, data)

        # ANALYZE THE DATA:
        df = pandas.read_csv(f"./src/csv/{self.server_id}_message.csv")
        channelid_counts = pandas.value_counts(df["channelid"])
        role_counts = pandas.value_counts(df["roles"])

        embed_title = "Message ~ Analytics"
        embeds = [
            Embed(title=embed_title, description="Here you can see the analyzed message data"),
            Embed(title=embed_title, description="Message counted in channels:\n"f"```{channelid_counts}```"),
            Embed(title=embed_title, description="Message send from roles:\n"f"```{role_counts}```")
        ]
        return embeds
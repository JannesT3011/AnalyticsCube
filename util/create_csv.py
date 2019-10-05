import csv


class CSV:
    def __init__(self, guild_id:str, data:dict):
        self.guild_id = guild_id
        self.data = data
        self.fieldnames = {
            "message": ["msgid", "timestamp", "roles", "channelid"],
            "reaction": ["reactionname", "timestamp", "roles", "channelid"],
            "bot_requests": ["cmdname", "timestamp", "channelid", "roles"],
            "bot_msg": ["msgid", "timestamp", "roles", "channelid"],
            "userjoin": ["timestamp"],
            "userleave": ["timestamp"],
            "mentions": ["ment_role", "timestamp", "roles", "channelid"]
        }

    def create_csv(self, name):
        dir = f"./src/csv/{self.guild_id}_{name}.csv"
        with open(dir, "w") as file:
            writer = csv.DictWriter(file, self.fieldnames[name])
            writer.writeheader()
            for json_data in self.data:
                writer.writerow(json_data)
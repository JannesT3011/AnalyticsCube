import csv


def create_csv(name:str, fieldnames:list, data):
    with open(name, "w") as file:
        writer = csv.DictWriter(file, fieldnames)
        writer.writeheader()
        for json_data in data:
            writer.writerow(json_data)
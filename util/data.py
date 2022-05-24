async def load_data(db, id:str):
    data = await db.find_one({"_id": id})
    return data
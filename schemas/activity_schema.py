def activityEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "name": item["name"],
        "description": item["description"],
        "type": item["type"],
        "travel": item["travel"]
    }

def entityList(entity) -> dict:
    return [activityEntity(item) for item in entity]

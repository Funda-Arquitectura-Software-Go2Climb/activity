from fastapi import APIRouter, HTTPException
from config.db import conn
from bson import ObjectId
from models.activity import Activity
from schemas.activity_schema import activityEntity, entityList

activity_router = APIRouter()

@activity_router.get('/activities')
def find_all_activities():
    return entityList(conn.mydatabase.activities.find())

@activity_router.post('/activities')
def create_activity(activity: Activity):
    new_activity = activity.dict()
    if "id" in new_activity: del new_activity["id"]  # Eliminar id si está presente para evitar conflictos
    inserted_id = conn.mydatabase.activities.insert_one(new_activity).inserted_id
    return {"id": str(inserted_id)}

@activity_router.get('/activities/{id}')
def find_activity(id: str):
    activity = conn.mydatabase.activities.find_one({"_id": ObjectId(id)})
    if activity:
        return activityEntity(activity)
    else:
        raise HTTPException(status_code=404, detail="Activity not found")

@activity_router.put('/activities/{id}')
def update_activity(id: str, activity_data: Activity):
    activity = conn.mydatabase.activities.find_one({"_id": ObjectId(id)})
    if activity:
        update_data = activity_data.dict(exclude_unset=True)
        if "id" in update_data: del update_data["id"]
        conn.mydatabase.activities.update_one({"_id": ObjectId(id)}, {"$set": update_data})
        return {"status": "Activity updated successfully"}
    else:
        raise HTTPException(status_code=404, detail="Activity not found")

@activity_router.delete('/activities/{id}')
def delete_activity(id: str):
    activity = conn.mydatabase.activities.find_one({"_id": ObjectId(id)})
    if activity:
        conn.mydatabase.activities.delete_one({"_id": ObjectId(id)})
        return {"status": "Activity deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail="Activity not found")

@activity_router.get('/activities/travel/{travel_id}')
def find_activities_by_travel(travel_id: int):
    activities = conn.mydatabase.activities.find({"travel": travel_id})
    return entityList(activities)
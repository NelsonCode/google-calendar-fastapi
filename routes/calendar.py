from fastapi import APIRouter, Request

from functions.calendar import create_event, delete_event, get_event, update_event


routes_calendar = APIRouter()


@routes_calendar.post("/create")
async def create(request: Request):
    template = await request.json()
    return create_event(template)


@routes_calendar.get("/event/{eventId}")
def get(eventId: str):
    return get_event(eventId)


@routes_calendar.delete("/delete/{eventId}")
def delete(eventId: str):
    return delete_event(eventId)


@routes_calendar.put("/update/{eventId}")
async def put(request: Request, eventId: str):
    template = await request.json()
    return update_event(eventId,template)
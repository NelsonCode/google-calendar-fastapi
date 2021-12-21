from fastapi import FastAPI
from routes.calendar import routes_calendar

app = FastAPI()

app.include_router(routes_calendar, prefix="/calendar")
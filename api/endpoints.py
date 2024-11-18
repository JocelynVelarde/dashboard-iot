from fastapi import FastAPI
from queries import all_houses, all_persons, insert_sensor, insert_log_sensor, all_sensors, all_rooms
from pydantic import BaseModel
from fastapi.exceptions import HTTPException

app = FastAPI()

class Sensor(BaseModel):
    type_: str
    unit: str
    room_id: int

class LogSensor(BaseModel):
    date_: str
    measure: int
    sensor_id: int


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/get-all-houses")
async def get_all_houses():
    return all_houses()

@app.get("/get-all-persons")
async def get_all_persons():
    return all_persons()

@app.get("/get-all-rooms")
async def get_all_rooms():
    return all_rooms()
    
@app.post("/add-sensor")
async def add_sensor(sensor: Sensor):
    result = insert_sensor(sensor.type_, sensor.unit, sensor.room_id)
    if result["message"] == "Sensor inserted successfully.":
        return result
    else:
        raise HTTPException(status_code=500, detail=result["message"])
    
@app.get("/get-all-sensors")
async def get_all_sensors():
    return all_sensors()

@app.post("/add-log-sensor")
async def add_log_sensor(log_sensor: LogSensor):
    result = insert_log_sensor(log_sensor.date_, log_sensor.measure, log_sensor.sensor_id)
    if result["message"] == "Log sensor inserted successfully.":
        return result
    else:
        raise HTTPException(status_code=500, detail=result["message"])




    



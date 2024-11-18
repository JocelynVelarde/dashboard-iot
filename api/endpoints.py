from fastapi import FastAPI
from queries import all_houses, all_persons, insert_sensor, insert_log_sensor, all_sensors, all_rooms, insert_person, insert_house, insert_room, sound_sensor_logs
from pydantic import BaseModel
from fastapi.exceptions import HTTPException

app = FastAPI()

class Sensor(BaseModel):
    type_: str
    unit: str
    room_id: int

class Room(BaseModel):
    num_windows: int
    num_doors: int

class Person(BaseModel):
    room_id: int
    name: str

class LogSensor(BaseModel):
    date_: str
    measure: int
    sensor_id: int

class House(BaseModel):
    direction_ip: str
    direction: str


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

@app.get("/sound-sensor-logs")
async def get_sound_logs():
    return sound_sensor_logs()
    
@app.post("/add-sensor")
async def add_sensor(sensor: Sensor):
    result = insert_sensor(sensor.type_, sensor.unit, sensor.room_id)
    if result["message"] == "Sensor inserted successfully.":
        return result
    else:
        raise HTTPException(status_code=500, detail=result["message"])
    
@app.post("/add-room")
async def add_room(room: Room):
    result = insert_room(room.num_windows, room.num_doors)
    if result["message"] == "Room inserted successfully.":
        return result
    else:
        raise HTTPException(status_code=500, detail=result["message"])
    
@app.post("/add-person")
async def add_person(person: Person):
    result = insert_person(person.room_id, person.name)
    if result["message"] == "Person inserted successfully.":
        return result
    else:
        raise HTTPException(status_code=500, detail=result["message"])
    
@app.post("/add-house")
async def add_house(house: House):
    result = insert_house(house.direction_ip, house.direction)
    if result["message"] == "House inserted successfully.":
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




    



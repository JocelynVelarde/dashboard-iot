from fastapi import FastAPI
from queries import all_houses, all_persons, insert_sensor, insert_log_sensor, all_sensors, all_rooms, insert_person, insert_house, insert_room, get_sound_logs, get_ir_logs, get_magnetic_logs, get_push_logs, get_ultrasonic_logs, count_persons, count_sensors, count_houses, count_rooms, recent_house, recent_person, recent_room, recent_sensor, insert_actuator, insert_log_actuator
from pydantic import BaseModel
from fastapi.exceptions import HTTPException

app = FastAPI()

class Sensor(BaseModel):
    type_: str
    unit: str
    room_id: int

class Actuator(BaseModel):
    condition: int
    sensor_id_a: int

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

class LogActuator(BaseModel):
    date_a: str
    active: int
    actuator_id: int

class House(BaseModel):
    direction_ip: str
    direction: str


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/get-all-houses")
async def get_all_houses():
    return all_houses()

@app.get("/recent-house")
async def get_recent_house():
    return recent_house()

@app.get("/recent-person")
async def get_recent_person():
    return recent_person()

@app.get("/recent-room")
async def get_recent_room():
    return recent_room()

@app.get("/recent-sensor")
async def get_recent_sensor():
    return recent_sensor()

@app.get("/get-all-persons")
async def get_all_persons():
    return all_persons()

@app.get("/count-persons")
async def count_person():
    return count_persons()

@app.get("/count-rooms")
async def count_room():
    return count_rooms()

@app.get("/count-houses")
async def count_house():
    return count_houses()

@app.get("/count-sensors")
async def count_sensor():
    return count_sensors()

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
    
@app.post("/add-actuator")
async def add_actuator(actuator: Actuator):
    result = insert_actuator(actuator.condition, actuator.sensor_id_a)
    if result["message"] == "Actuator inserted successfully.":
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

@app.get("/get-sound-logs")
async def get_sound_log():
    return get_sound_logs()

@app.get("/get-ultrasonic-logs")
async def get_ultrasonic_log():
    return get_ultrasonic_logs()

@app.get("/get-magnetic-logs")
async def get_magnetic_log():
    return get_magnetic_logs()

@app.get("/get-ir-logs")
async def get_ir_log():
    return get_ir_logs()

@app.get("/get-push-logs")
async def get_push_log():
    return get_push_logs()

@app.post("/add-log-sensor")
async def add_log_sensor(log_sensor: LogSensor):
    result = insert_log_sensor(log_sensor.date_, log_sensor.measure, log_sensor.sensor_id)
    if result["message"] == "Log sensor inserted successfully.":
        return result
    else:
        raise HTTPException(status_code=500, detail=result["message"])
    
@app.post("/add-log-actuator")
async def add_log_actuator(log_actuator: LogActuator):
    result = insert_log_actuator(log_actuator.date_a, log_actuator.active, log_actuator.actuator_id)
    if result["message"] == "Log actuator inserted successfully.":
        return result
    else:
        raise HTTPException(status_code=500, detail=result["message"])




    



from fastapi import FastAPI
from queries import all_houses, all_persons

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/get-all-houses")
async def get_all_houses():
    return all_houses()

@app.get("/get-all-persons")
async def get_all_persons():
    return all_persons()
    
# Ultrasonic sensor
@app.get("/object-distance")
async def get_ultrasonic():
    return {"Historical times of objects detected at x distance": 10}

@app.post("/object-distance")
async def post_ultrasonic():
    return {"Object detected at x distance, alert in LCD": 10}

# Infrared sensor
@app.get("/person-side")
async def get_infrared():
    return {"Historical times of persons detected aside": 20}

@app.post("/person-side")
async def post_infrared():
    return {"Person detected on the side, perform a vibration": 20}

# Sound sensor
@app.get("/decibel-sound")
async def get_sound():
    return {"Historical decibels": 30}

@app.post("/decibel-sound")
async def post_sound():
    return {"Sound detected at certain decibels, alert in LEDs": 30}

# Magnetic sensor
@app.get("/magnetic-door")
async def get_magnetic_door():
    return {"Historical times of door opened": 40}

@app.post("/magnetic-door")
async def post_magnetic_door():
    return {"Door opened, buzzer up": 40}

# Push button
@app.get("/panic-button")
async def get_panic_button():
    return {"Historical times of panic button pressed": 50}

@app.post("/panic-button")
async def post_panic_button():
    return {"Panic button pressed, close with motor": 50}
    



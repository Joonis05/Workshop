from fastapi import FastAPI

app = FastAPI

app.post("/add_engine")
def add_engine(engine):
    pass

app.post("/add_vehicle")
def add_vehicle(vehicle):
    pass

app.get("/engines")
def see_engines(engines_list):
    pass

app.get("/vehicles")
def see_vehicles(vehicles_list):
    pass
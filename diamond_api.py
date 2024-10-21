from fastapi import FastAPI
import json
app = FastAPI()


@app.get("/")
def home():
    with open('DiamondFeeder.json', 'r') as file:
        jsoneddata = json.load(file)
        return jsoneddata

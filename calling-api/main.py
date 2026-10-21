# main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import httpx
import os
import asyncio 

app = FastAPI() 

open_mateo_url = "https://api.open-meteo.com/v1/forecast" 

class ValidateCurrent(BaseModel):
    time: str
    temperature_2m: float
    
class OpenMateoResponse(BaseModel):
    latitude: float
    longitude: float
    current: ValidateCurrent


@app.get("/weather")
async def get_weather():

    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(
                open_mateo_url, 
                params={
                    "latitude": 14.6, 
                    "longitude": 121.0,
                    "current": "temperature_2m",
                    }
                )
            respone = response.json()
        except:
            raise HTTPException(status_code=400, detail="Error getting weather data")

    raw_json = response.json()
    weather_data = OpenMateoResponse(**raw_json)

    var1 = weather_data.current.time
    var2 = weather_data.latitude
    var3 = weather_data.longitude
    var4 = weather_data.current.temperature_2m
    return {"time": var1, "latitude": var2, "longitude": var3, "temperature_2m": var4}





from fastapi import FastAPI, Path  , HTTPException , Query
import json

app = FastAPI()

def load_data():
    with open('patients.json','r') as f:
        data = json.load(f)
    
    return data

@app.get("/")
def hello():
    return "Patient data reading API"

@app.get("/about")
def about():
    return "Fully functional API  which reads patient data efficiently using FastAPI"

@app.get("/view")
def view():
    data = load_data()

    return data

@app.get('/patient/{patient_id}')
def view_patient(patient_id:str):
    data = load_data()

    for record in data:
        if record in data:
            return record[patient_id]
        raise HTTPException(status_code = 404,detail="patient id not found ")

@app.get('/sort')
def sort_patients(sort_by : str = Query(..., description='Sort on the basis of height , width or bmi '), order: str=Query('asc', description='sort in asc or dsc order')):

    valid_fields =['height','weight','bmi']

    if sort_by not in valid_fields:
        raise HTTPException(status_code=400, detail=f'Invalid field select from {valid_fields}')
    
    if order not in ['asc','desc']:
        raise HTTPException(status_code=400 , detail='Invalid order , select between asc and desc')
    
    data = load_data()

    sort_order = True if order == "desc" else False

    sorted_data = sorted(data.values(), key=lambda x: x.get(sort_by ,0),reverse=sort_order)

    return sorted_data
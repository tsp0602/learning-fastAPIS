from pydantic import BaseModel , Field , EmailStr

class Patient(BaseModel):
    name : str
    age : int 

def insert_patient_data(patient : Patient):
    print(patient.name)
    print(patient.age)
    print("data inserted successfully....")


patient_info={"name":"Tejas","age":'21'}

patient1 = Patient(**patient_info)

insert_patient_data(patient1)
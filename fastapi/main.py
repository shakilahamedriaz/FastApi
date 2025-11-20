from fastapi import FastAPI, Path, HTTPException, Query  # fastapi for building the API, Path for path parameters
import json  # json for handling JSON data
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(
    title="Patient Management API",
    description="A fully functional API to manage patient data.",
    version="Alpha 1.0"
)


# used to allow urls 
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://127.0.0.1:3000",
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "*",
    ],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


# load patient data from JSON file.
def load_data():
    with open("patients.json", "r") as f:
        data = json.load(f)
    return data


# route endpoint for home
@app.get("/")
def hello():
    return {"message": "Patient Management API"}


# route endpoint for about
@app.get('/about')
def about():
    return {"message": "A fully functional API to manage patient data."}


# route endpoint for view all patients
@app.get('/patient')
def view():
    data = load_data()
    return data


# route endpoint for view a specific patient by ID
#here path function is used to add metadata and validation to the patient_id parameter
@app.get('/patient/{patient_id}')
def view_patient(patient_id: str = Path(..., description="The ID of the patient in the DB", example="P001")):
    #load all the patient data
    data = load_data()
    if patient_id in data:
      return data[patient_id]
    return  HTTPException(status_code = 404, detail = "patient not found")




# HTTP status codes
# 200 OK - The request has succeeded.
# 201 Created - The request has been fulfilled and has resulted in one or more new resources
# 204 No Content - The server successfully processed the request, but is not returning any content.

# 301 Moved Permanently - The requested resource has been assigned a new permanent URI.
# 302 Found - The requested resource resides temporarily under a different URI.


# 400 Bad Request - The server could not understand the request due to invalid syntax.
# 401 Unauthorized - The client must authenticate itself to get the requested response.
# 403 Forbidden - The client does not have access rights to the content.
# 404 Not Found - The server can not find the requested resource.

# 500 Internal Server Error - The server has encountered a situation it doesn't know how to handle.
# 502 Bad Gateway - The server, while acting as a gateway or proxy, received an invalid response from the upstream server.
# 503 Service Unavailable - The server is not ready to handle the request.



# Query Parameters :
# Used to filter results or specify additional options for the request.
# Example: /patients?age=30&gender=male&sort_by=age

@app.get('/sort')
def sort_patients(sort_by: str = Query(..., description='Sort on the basis of height, weight or bmi'), order: str = Query('asc', description='sort in asc or desc order')):
    valid_fields = ['height', 'weight', 'bmi']

    if sort_by not in valid_fields:
        raise HTTPException(status_code=400, detail=f"Invalid sort_by field. Must be one of {valid_fields}")
    
    if order not in ['asc', 'desc']:
        raise HTTPException(status_code=400, detail="Invalid order. Must be 'asc' or 'desc'")
    
    data = load_data()

    sort_order = True if order == 'asc' else False
    sorted_data = sorted(data.values(), key=lambda x: x.get(sort_by, 0), reverse=sort_order)
    return sorted_data


# Query Parameters help to filter and sort data based on specific criteria, enhancing the API's usability and flexibility.
# Example: /patients?age=30&gender=male&sort_by=age
# In this example, we filter patients who are 30 years old and


# path Parameters are used to identify specific resources within the API.# Example: /patients/{patient_id}
# In this example, patient_id is a path parameter that uniquely identifies a patient in the database.   



@app.post('/health')
def health_check():
    return {"status": "API is healthy"}
from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated


# EmailStr: to validate email addresses.
# AnyUrl: to validate URL fields.
# Field: to provide additional validation and metadata for model fields.

# Define a pydantic model
class patient(BaseModel):

    #name: str = Field(max_length=50)  # name must be between 2 and 50 characters
    name: Annotated[str, Field(max_length=50, title="Name of the patient", description="Name must be between 2 and 50 characters", examples=["John Doe", "Jane Smith"])]  # name must be between 2 and 50 characters
    email: EmailStr
    Linkdlin_url: AnyUrl
    age: int
    weight: float = Annotated(float, Field(gt=0, lt=500, strict=True, description="Weight must be between 0 and 500 kg")])
    married: bool = Annotated[bool, Field(default=None, description="Marital status of the patient")]
    allergies: Optional[List[str]] = Field(max_length=100) # Optional field
    contact_details: Dict[str, str]





# Type validation: means: to validate the data types of the fields in the model.
# Data validation: means: to validate the values of the fields in the model.


def created_patient_data(patient1: patient):
    print("\nPatient Name:", patient1.name)
    print("Patient Email:", patient1.email)
    print("Patient Linkdlin URL:", patient1.Linkdlin_url)
    print("Patient Age:", patient1.age)
    print("Patient Weight:", patient1.weight)
    print("Married:", patient1.married)
    print("Allergies:", patient1.allergies)
    print("Contact Details:", patient1.contact_details)

    print("Patient data created successfully.\n")



# Create an instance of the model and validate data
patient_info = {
        'name' : 'John Doe',
        'email' : 'john.doeexample@gmail.com',
        'Linkdlin_url' : 'https://www.linkedin.com/in/shakilahamedriaz',
        'age' : 30,
        'weight' : 70.5,
        'married' : False,
        'allergies' : ['pollen', 'nuts'],
        'contact_details' : {'phone': '123-456-7890', 'email': 'john.doe@example.com'}
}


# this is how we create a patient object using the Pydantic model
patient1 = patient(**patient_info) 


# call for patient function
print("\nPatient Information:")
created_patient_data(patient1)  # we are passing the patient1 object to create function.
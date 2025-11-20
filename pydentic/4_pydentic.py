from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator
from typing import List, Dict, Optional, Annotated


# EmailStr: to validate email addresses.
# AnyUrl: to validate URL fields.
# Field: to provide additional validation and metadata for model fields.

# Define a pydantic model
class patient(BaseModel):

    name: str 
    email: EmailStr
    Linkdlin_url: AnyUrl
    age: int
    weight: float 
    allergies: List[str]
    contact_details: Dict[str, str]



    @field_validator("email")
    @classmethod
    def email_validator(cls, value):
        valid_domains = ["diu.edu.bd", "yahoo.com"]
        domain_name = value.split('@')[-1]

        if domain_name not in valid_domains:
            raise ValueError(f"Email domain '{domain_name}' is not allowed. Allowed domains are: {', '.join(valid_domains)}")

        return value # return the validated value


    @field_validator("name")
    @classmethod
    def transform_name(cls, value):
        return value.upper() # transform the name to uppercase


   
# Type validation: means: to validate the data types of the fields in the model.
# Data validation: means: to validate the values of the fields in the model.


def created_patient_data(patient1: patient):

    print("\nPatient Name:", patient1.name)
    print("Patient Email:", patient1.email)
    print("Patient Linkdlin URL:", patient1.Linkdlin_url)
    print("Patient Age:", patient1.age)
    print("Patient Weight:", patient1.weight)
    print("Allergies:", patient1.allergies)
    print("Contact Details:", patient1.contact_details)


    print("Patient data created successfully.\n")



# Create an instance of the model and validate data
patient_info = {
        'name' : 'John Doe',
        'email' : 'john.doeexample@diu.edu.bd',
        'Linkdlin_url' : 'https://www.linkedin.com/in/shakilahamedriaz',
        'age' : 30,
        'weight' : 70.5,
        'married' : False,
        'allergies' : ['pollen', 'nuts'],
        'contact_details' : {'phone': '123-456-7890', 'email': 'john.doe@example.com'}
} # validation process happens here


# this is how we create a patient object using the Pydantic model
patient1 = patient(**patient_info) 


# call for patient function
print("\nPatient Information:")
created_patient_data(patient1)  # we are passing the patient1 object to create function.
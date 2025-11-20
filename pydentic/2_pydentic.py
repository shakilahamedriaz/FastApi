from pydantic import BaseModel

# Define a Pydantic model
class Patient(BaseModel):
    name: str
    age: int



# Create an instance of the model and validate data, instance menas an object created from a class.
def insert_patient_data(patient1: Patient):
    print(patient1.name)
    print(patient1.age)
    print("Inserted Successfully.")


# Update patient data with validation
def update_patient_data(patient1: Patient):
    if patient1.age < 0:
        raise ValueError("Age cannot be negative.")
    
    print(patient1.name)
    print(patient1.age)
    print("Updated Successfully.")



def delete_patient_data(patient1: Patient):
    print(f"Patient {patient1.name} and {patient1.age} deleted successfully.")



class doctor(BaseModel):
    name: str
    specialization: str
    contact_number: str


def insert_doctor_data(doctor1: doctor):
    print(doctor1.name)
    print(doctor1.specialization)
    print(doctor1.contact_number)
    print("Doctor data inserted successfully.")



# this is how we create a patient object using the Pydantic model
Patient_info = {'name': 'Alice', 'age': -29}
doctor_info =  {'name': 'Dr. Smith', 'specialization': 'Cardiology', 'contact_number': '123-456-7890'}


# Unpack the dictionary to create a Patient instance or object
patient1 = Patient(**Patient_info)  
doctor1 = doctor(**doctor_info)


# call for patient functions
print("Patient Information:")
insert_patient_data(patient1)  # we are passing the patient1 object to insert function.
update_patient_data(patient1)  # we can reuse the same patient1 object for updating data as well.
delete_patient_data(patient1)  # we can reuse the same patient1 object for deleting data as well.


# call for doctor function
print("\nDoctor Information:")
insert_doctor_data(doctor1)  # we are passing the doctor1 object to insert function.
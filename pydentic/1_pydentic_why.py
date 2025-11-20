def insert_patient_data(name: str, age: int):

    if type(name) == str and type(age) == int:
        print(name)
        print(age)
        print("Patient data inserted successfully.")
    else:
        raise TypeError("Invalid data types for name or age.")
    

insert_patient_data("John Doe", 30)

# pydantic menas "data validation and settings management using python type annotations"
# In avobe code we are using type annotations to specify that name should be a string and age should be an integer.
# Pydantic will validate the data types at runtime and raise an error if the types do not match.
# Pydantic is widely used in FastAPI to validate request and response data, ensuring that the data conforms to the expected types and formats.
# This helps in building robust and reliable APIs.
# Pydantic also provides features like data parsing, serialization, and model definition, making it easier to work with complex data structures in Python applications.




def update_patient_data(name: str, age: int):

    if type(name) == str and type(age) == int:
        if age < 0:
            raise ValueError("Age cannot be negative.")
        
        print(name)
        print(age)
        print("Updated Successfully.")
    else:
        raise TypeError("Incorrect Data Types.")
    

update_patient_data("Jane Doe", 25)

# Type validation means checking that the data provided matches the expected data types.
# Example: If a function expects a string and an integer, type validation ensures that the provided values are indeed a string and an integer.


# Data validation: Data validation is the process of ensuring that the data provided meets certain criteria or rules beyond just type checking.
# Example: If a function expects a string (name) and an integer (age), data.



## **** In summary,
# these twofunctions above demonstrate type validation and data validation using basic Python constructs.
# In real-world applications, especially in web development with frameworks like FastAPI, libraries like Pydantic are used to handle these validations more efficiently and effectively.






# Pydantic Workflow:

# 1️⃣ Define a Pydantic model

# Represents the ideal schema of the data.

# Includes expected fields, their types, and validation constraints (e.g., gt=0 for positive numbers).


# 2️⃣ Instantiate the model with raw input data

# Input is usually a dictionary or JSON-like structure.

# Pydantic validates the data and coerces it into correct Python types automatically.

# If data doesn’t meet the model’s requirements, Pydantic raises a ValidationError.


# 3️⃣ Pass the validated model object

# Use it in functions or throughout the codebase.

# Ensures your program works with clean, type-safe, and logically valid data.


# Notes:

# name → str

# age → int (gt=0)

# Output is a Pydantic object (validated)
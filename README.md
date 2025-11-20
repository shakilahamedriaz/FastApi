# FastAPI & Pydantic Learning Repository 🚀

A comprehensive guide to learning **FastAPI** and **Pydantic** from A to Z, with a focus on building robust APIs for **Machine Learning** applications.

## 📚 Table of Contents

- [Overview](#overview)
- [Learning Objectives](#learning-objectives)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Repository Structure](#repository-structure)
- [Learning Path](#learning-path)
  - [1. Pydantic Fundamentals](#1-pydantic-fundamentals)
  - [2. FastAPI Basics](#2-fastapi-basics)
  - [3. Machine Learning Integration](#3-machine-learning-integration)
- [Key Concepts](#key-concepts)
- [Running the Examples](#running-the-examples)
- [API Documentation](#api-documentation)
- [Best Practices](#best-practices)
- [Resources](#resources)
- [Contributing](#contributing)

---

## 🎯 Overview

This repository is designed as a complete learning resource for building production-ready APIs using **FastAPI** and **Pydantic**. It covers everything from basic data validation to deploying machine learning models as RESTful APIs.

FastAPI is a modern, fast (high-performance) web framework for building APIs with Python 3.7+ based on standard Python type hints. Combined with Pydantic's powerful data validation, it's perfect for building ML APIs.

---

## 🎓 Learning Objectives

By working through this repository, you will learn:

- ✅ **Pydantic**: Data validation, settings management, and type annotations
- ✅ **FastAPI**: Building REST APIs, routing, request/response handling
- ✅ **Data Validation**: Type checking, custom validators, and field constraints
- ✅ **HTTP Methods**: GET, POST, PUT, DELETE operations
- ✅ **Query & Path Parameters**: Building flexible API endpoints
- ✅ **Machine Learning**: Deploying ML models via APIs
- ✅ **API Best Practices**: Error handling, CORS, documentation, and testing
- ✅ **Production Readiness**: Performance optimization and deployment

---

## 📋 Prerequisites

Before starting, you should have:

- **Python 3.7+** installed on your system
- Basic understanding of Python programming
- Familiarity with REST API concepts (helpful but not required)
- Basic knowledge of machine learning (for ML sections)

---

## 💻 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/shakilahamedriaz/FastApi.git
cd FastApi
```

### 2. Create a Virtual Environment

```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Required Packages

```bash
pip install fastapi uvicorn pydantic pydantic[email]
```

### 4. For Machine Learning Examples (Optional)

```bash
pip install scikit-learn pandas numpy tensorflow torch
```

---

## 📁 Repository Structure

```
FastApi/
│
├── pydentic/                    # Pydantic learning modules
│   ├── 1_pydentic_why.py       # Why use Pydantic? Type & data validation basics
│   ├── 2_pydentic.py           # Basic Pydantic models and instances
│   ├── 3_pydentic.py           # Advanced validation with Field, EmailStr, URLs
│   └── 4_pydentic.py           # Custom validators and field transformations
│
├── fastapi/                     # FastAPI learning modules
│   └── main.py                 # Patient Management API example
│
├── .gitignore                  # Git ignore file
└── README.md                   # This file
```

---

## 🛤️ Learning Path

### 1. Pydantic Fundamentals

Start with the **pydentic/** folder to understand data validation:

#### **1_pydentic_why.py** - Why Pydantic?
- Understanding type validation vs. data validation
- Manual validation challenges
- Introduction to Pydantic workflow
- Benefits for API development

**Key Concepts:**
```python
# Without Pydantic - Manual validation
def insert_patient(name: str, age: int):
    if type(name) != str or type(age) != int:
        raise TypeError("Invalid types")
    if age < 0:
        raise ValueError("Age cannot be negative")

# With Pydantic - Automatic validation
from pydantic import BaseModel

class Patient(BaseModel):
    name: str
    age: int
```

#### **2_pydentic.py** - Basic Pydantic Models
- Creating Pydantic models
- Model instantiation and validation
- Using models in functions
- Data type coercion

**Key Concepts:**
```python
class Patient(BaseModel):
    name: str
    age: int

patient = Patient(name="Alice", age=29)
```

#### **3_pydentic.py** - Advanced Field Validation
- Using `Field()` for constraints
- Email validation with `EmailStr`
- URL validation with `AnyUrl`
- Optional fields and default values
- Complex types: Lists, Dicts

**Key Concepts:**
```python
from pydantic import BaseModel, EmailStr, Field
from typing import List, Optional

class Patient(BaseModel):
    name: str = Field(max_length=50)
    email: EmailStr
    age: int = Field(gt=0, lt=150)
    allergies: Optional[List[str]] = None
```

#### **4_pydentic.py** - Custom Validators
- Using `@field_validator` decorator
- Custom validation logic
- Data transformation
- Complex business rules

**Key Concepts:**
```python
from pydantic import field_validator

class Patient(BaseModel):
    email: EmailStr
    
    @field_validator("email")
    @classmethod
    def validate_domain(cls, value):
        allowed_domains = ["diu.edu.bd", "yahoo.com"]
        domain = value.split('@')[-1]
        if domain not in allowed_domains:
            raise ValueError(f"Domain {domain} not allowed")
        return value
```

---

### 2. FastAPI Basics

Explore the **fastapi/** folder for API development:

#### **main.py** - Patient Management API

This comprehensive example demonstrates:

**Core Features:**
- ✅ Creating a FastAPI application
- ✅ API metadata (title, description, version)
- ✅ CORS middleware configuration
- ✅ Route endpoints and decorators
- ✅ Path parameters with validation
- ✅ Query parameters for filtering/sorting
- ✅ HTTP methods (GET, POST)
- ✅ Error handling with HTTPException
- ✅ JSON data handling

**API Endpoints:**

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Home endpoint |
| GET | `/about` | API information |
| GET | `/patient` | List all patients |
| GET | `/patient/{patient_id}` | Get specific patient |
| GET | `/sort?sort_by=<field>&order=<asc\|desc>` | Sort patients |
| POST | `/health` | Health check |

**HTTP Status Codes Covered:**
- 200 OK - Success
- 201 Created - Resource created
- 400 Bad Request - Invalid input
- 404 Not Found - Resource not found
- 500 Internal Server Error - Server error

---

### 3. Machine Learning Integration

FastAPI is excellent for serving ML models. Here's how to integrate them:

#### Example: Serving a Scikit-Learn Model

```python
from fastapi import FastAPI
from pydantic import BaseModel, Field
import pickle
import numpy as np

app = FastAPI(title="ML Model API")

# Load your trained model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

# Define input data schema
class PredictionInput(BaseModel):
    feature1: float = Field(..., description="First feature")
    feature2: float = Field(..., description="Second feature")
    feature3: float = Field(..., description="Third feature")
    
    class Config:
        json_schema_extra = {
            "example": {
                "feature1": 5.1,
                "feature2": 3.5,
                "feature3": 1.4
            }
        }

# Define output schema
class PredictionOutput(BaseModel):
    prediction: int
    probability: float

@app.post("/predict", response_model=PredictionOutput)
def predict(input_data: PredictionInput):
    # Convert to numpy array
    features = np.array([[
        input_data.feature1,
        input_data.feature2,
        input_data.feature3
    ]])
    
    # Make prediction
    prediction = model.predict(features)[0]
    probability = model.predict_proba(features)[0].max()
    
    return PredictionOutput(
        prediction=int(prediction),
        probability=float(probability)
    )
```

#### Example: Image Classification API

```python
from fastapi import FastAPI, File, UploadFile
from pydantic import BaseModel
import tensorflow as tf
from PIL import Image
import io

app = FastAPI(title="Image Classification API")

# Load model
model = tf.keras.models.load_model("image_classifier.h5")

class ClassificationResult(BaseModel):
    class_name: str
    confidence: float

@app.post("/classify", response_model=ClassificationResult)
async def classify_image(file: UploadFile = File(...)):
    # Read and preprocess image
    image_bytes = await file.read()
    image = Image.open(io.BytesIO(image_bytes))
    image = image.resize((224, 224))
    image_array = tf.keras.preprocessing.image.img_to_array(image)
    image_array = tf.expand_dims(image_array, 0)
    
    # Predict
    predictions = model.predict(image_array)
    class_idx = predictions.argmax()
    confidence = predictions[0][class_idx]
    
    return ClassificationResult(
        class_name=f"Class_{class_idx}",
        confidence=float(confidence)
    )
```

---

## 🔑 Key Concepts

### Pydantic

1. **BaseModel**: Foundation for all Pydantic models
2. **Field**: Advanced field configuration and validation
3. **Validators**: Custom validation logic with `@field_validator`
4. **Type Hints**: Python type annotations for automatic validation
5. **Data Parsing**: Automatic type conversion and validation
6. **Serialization**: Converting models to JSON/dict

### FastAPI

1. **Routing**: Defining endpoints with decorators (`@app.get`, `@app.post`)
2. **Path Parameters**: Dynamic URL segments (`/patient/{patient_id}`)
3. **Query Parameters**: URL query strings (`?sort_by=age&order=desc`)
4. **Request Body**: Pydantic models for request validation
5. **Response Models**: Pydantic models for response validation
6. **Middleware**: CORS, authentication, logging
7. **Dependency Injection**: Reusable dependencies
8. **Auto Documentation**: Swagger UI and ReDoc

---

## 🏃 Running the Examples

### Running Pydantic Examples

```bash
# Navigate to pydentic folder
cd pydentic

# Run any example
python 1_pydentic_why.py
python 2_pydentic.py
python 3_pydentic.py
python 4_pydentic.py
```

### Running FastAPI Server

```bash
# Navigate to fastapi folder
cd fastapi

# Run with uvicorn
uvicorn main:app --reload

# Or specify host and port
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

The server will start at: `http://127.0.0.1:8000`

---

## 📖 API Documentation

FastAPI automatically generates interactive API documentation:

- **Swagger UI**: http://127.0.0.1:8000/docs
- **ReDoc**: http://127.0.0.1:8000/redoc
- **OpenAPI JSON**: http://127.0.0.1:8000/openapi.json

These provide:
- Interactive API testing
- Request/response schemas
- Parameter descriptions
- Example values

---

## 🎨 Best Practices

### 1. **Data Validation**
```python
# Always use Pydantic models for request/response
class UserCreate(BaseModel):
    username: str = Field(min_length=3, max_length=50)
    email: EmailStr
    age: int = Field(gt=0, lt=150)
```

### 2. **Error Handling**
```python
from fastapi import HTTPException

@app.get("/user/{user_id}")
def get_user(user_id: int):
    user = get_user_from_db(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
```

### 3. **Response Models**
```python
class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    
    class Config:
        from_attributes = True

@app.get("/user/{user_id}", response_model=UserResponse)
def get_user(user_id: int):
    return get_user_from_db(user_id)
```

### 4. **Dependency Injection**
```python
from fastapi import Depends

def get_db():
    db = Database()
    try:
        yield db
    finally:
        db.close()

@app.get("/users")
def read_users(db: Database = Depends(get_db)):
    return db.get_users()
```

### 5. **Environment Variables**
```python
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "My API"
    admin_email: str
    database_url: str
    
    class Config:
        env_file = ".env"

settings = Settings()
```

---

## 📚 Resources

### Official Documentation
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Pydantic Documentation](https://docs.pydantic.dev/)
- [Uvicorn Documentation](https://www.uvicorn.org/)

### Tutorials & Courses
- [FastAPI Tutorial - Official](https://fastapi.tiangolo.com/tutorial/)
- [Full Stack FastAPI and PostgreSQL - Base Project Generator](https://github.com/tiangolo/full-stack-fastapi-postgresql)

### Machine Learning with FastAPI
- [Deploying ML Models with FastAPI](https://fastapi.tiangolo.com/advanced/custom-response/)
- [TensorFlow Serving with FastAPI](https://www.tensorflow.org/tfx/guide/serving)

### Books
- "Building Data Science Applications with FastAPI" by François Voron
- "FastAPI: Modern Python Web Development" by Bill Lubanovic

### Community
- [FastAPI GitHub](https://github.com/tiangolo/fastapi)
- [FastAPI Discord](https://discord.com/invite/VQjSZaeJmf)
- [Stack Overflow - FastAPI Tag](https://stackoverflow.com/questions/tagged/fastapi)

---

## 🤝 Contributing

Contributions are welcome! If you'd like to add more examples or improve existing ones:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📝 License

This project is for educational purposes. Feel free to use and modify as needed.

---

## 🎯 Next Steps

1. **Complete all Pydantic examples** in the `pydentic/` folder
2. **Run the FastAPI application** and explore the endpoints
3. **Experiment with the interactive docs** at `/docs`
4. **Build your own ML API** using the examples as templates
5. **Explore advanced topics**: WebSockets, Background Tasks, Testing
6. **Deploy your API**: Docker, AWS, Heroku, or Render

---

## 💡 Quick Start Checklist

- [ ] Install Python 3.7+
- [ ] Clone this repository
- [ ] Create virtual environment
- [ ] Install dependencies (`pip install fastapi uvicorn pydantic`)
- [ ] Run Pydantic examples (`python pydentic/1_pydentic_why.py`)
- [ ] Start FastAPI server (`uvicorn fastapi.main:app --reload`)
- [ ] Visit http://127.0.0.1:8000/docs
- [ ] Try the API endpoints
- [ ] Build your first ML API
- [ ] Deploy to production

---

**Happy Learning! 🚀**

For questions or feedback, feel free to open an issue or reach out!

---

**Repository maintained by:** [Shakil Ahamed Riaz](https://github.com/shakilahamedriaz)

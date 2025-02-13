import uvicorn
from fastapi import FastAPI, Request, Path, Query, HTTPException
from pydantic import BaseModel, Field

app = FastAPI()

class PersonRequest(BaseModel):
    id: int
    name: str

class PersonResponse(PersonRequest):
    href: str

@app.post("/person", response_model=PersonResponse)
def process_person(request: Request, person: PersonRequest):
    entity_response = PersonResponse(**person.model_dump(), href=str(request.url))
    return entity_response

class Student(BaseModel):
    id: int = Field(0, description="Id of Student", ge=0, lt=10)
    name: str = Field("john", description="Name of Student", min_length=3, max_length=20)

class StudentResponse(Student):
    index: int = Field(None, description="Index of Student", ge=0)
    href: str
    class Config:
        json_schema_extra = {
            "description": "This an example for the student response body",
            "example": {
                "id": 1,
                "name": "john",
                "href": "http://127.0.0.1:8000/student"
            }
        }

students: dict[int, Student]  = {}

@app.get("/student/{student_index}", response_model=StudentResponse)
def get_student(request: Request,
                student_index: int = Path(description="Index of Student", ge=0, lt=10)):
    if student_index not in students:
        raise HTTPException(status_code=404, detail="Student does not exist")
    student = students[student_index]
    return StudentResponse(**student.model_dump(), href=str(request.url))

@app.post("/student/{student_id}", response_model=StudentResponse)
def create_student(request: Request,
                   student_id: int = Path(description="Id of Student", ge=0, lt=10),
                   student_name: str = Query("john", description="Name of Student", min_length=3, max_length=20)):
    index = len(students)
    students[index] = Student(id=student_id, name=student_name)
    return StudentResponse(id=student_id, name=student_name, index=index ,href=str(request.url))

@app.post("/student", response_model=StudentResponse)
def create_student(request: Request, student: Student):
    index = len(students)
    students[index] = student
    return StudentResponse(**student.model_dump(), index=index ,href=str(request.url))

if __name__ == "__main__":
    uvicorn.run("document:app", reload=True)

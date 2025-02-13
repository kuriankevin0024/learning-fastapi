import uvicorn
from fastapi import FastAPI, Request
from typing import Optional
from pydantic import BaseModel
from urllib.parse import urlencode

class Person(BaseModel):
    name: str
    age: int
    male: bool
    religion: str
    job: str

class UpdatePerson(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    male: Optional[bool] = None
    religion: Optional[str] = None
    job: Optional[str] = None

initial_person = Person(name="john", age=25, male=True, religion="christan", job="engineer")
people: dict[int, Person] = {1: initial_person}

app = FastAPI()

@app.get("/")
def root():
    return {"data": "Root Path"}

@app.get("/people")
def get_people():
    return people

@app.get("/person/{person_id}")
def get_person(person_id: int):
    if person_id not in people:
        return {"data": "Person Does Not Exist"}
    return people[person_id]

@app.post("/person/{person_id}/v1")
def create_person(person_id: int, name: str, age: int, male: bool = True,
               religion: str = None, job: Optional[str] = None):
    if person_id in people:
        return {"data": "Person Exists"}
    if religion is None:
        religion = "None"
    if job is None:
        job = "None"
    people[person_id] = Person(name=name, age=age, male=male, religion=religion, job=job)
    return people[person_id]

@app.post("/person/{person_id}/v2")
def create_person(person_id: int, person: Person):
    if person_id in people:
        return {"data": "Person Exists"}
    people[person_id] = person
    return people[person_id]

@app.put("/person/{person_id}")
def update_person(person_id: int, person: Person):
    if person_id not in people:
        return {"data": "Person Does Not Exist"}
    people[person_id] = person
    return people[person_id]

@app.patch("/person/{person_id}")
def update_person(person_id: int, part_person: UpdatePerson):
    if person_id not in people:
        return {"data": "Person Does Not Exist"}
    if part_person.name is not None:
        people[person_id].name = part_person.name
    if part_person.age is not None:
        people[person_id].age = part_person.age
    if part_person.male is not None:
        people[person_id].male = part_person.male
    if part_person.religion is not None:
        people[person_id].religion = part_person.religion
    if part_person.job is not None:
        people[person_id].job = part_person.job
    return people[person_id]

@app.delete("/person/{person_id}")
def delete_person(person_id: int):
    if person_id not in people:
        return {"data": "Person Does Not Exist"}
    del people[person_id]
    return {"data": f"Person Deleted. ID:{person_id}"}

@app.post("/person/{person_id}/v3", name="create_person_href")
def create_person_href(request: Request, person_id: int, name: str, age: int, male: bool = True,
               religion: str = None, job: Optional[str] = None):
    if person_id in people:
        return {"data": "Person Exists"}
    if religion is None:
        religion = "None"
    if job is None:
        job = "None"
    people[person_id] = Person(name=name, age=age, male=male, religion=religion, job=job)

    # approach 1: simple
    generated_href = str(request.url)
    print(f"simple href: {generated_href}")

    # approach 2: custom
    base_url = request.url_for("create_person_href", person_id=person_id)
    query_params = request.query_params
    if query_params:
        query_string = urlencode(query_params, doseq=True)
        generated_href = f"{base_url}?{query_string}"
    else:
        generated_href = base_url
    print(f"custom href: {generated_href}")

    response = {
        "href": generated_href,
        "person": people[person_id]
    }
    return response

if __name__ == "__main__":
    uvicorn.run("controller:app", reload=True)

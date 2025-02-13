import uvicorn
from fastapi import FastAPI, Request
from typing import Optional
from pydantic import BaseModel
from urllib.parse import urlencode

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Root Path"}

class Person(BaseModel):
    name: str
    age: int
    male: bool
    religion: str
    job: str

class PatchPerson(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    male: Optional[bool] = None
    religion: Optional[str] = None
    job: Optional[str] = None

people: dict[int, Person] = {}
people[len(people)] = Person(name="john", age=25, male=True, religion="christan", job="engineer")

@app.get("/person/{person_index}")
def get_person(person_index: int):
    if person_index not in people:
        return {"message": "Person does not exist"}
    return people[person_index]

@app.post("/person")
def post_person(person: Person):
    index =len(people)
    people[index] = person
    return people[index]

@app.put("/person/{person_index}")
def put_person(person_index: int, person: Person):
    if person_index not in people:
        return {"message": "Person does not exist"}
    people[person_index] = person
    return people[person_index]

@app.patch("/person/{person_index}")
def patch_person(person_index: int, person: PatchPerson):
    if person_index not in people:
        return {"message": "Person does not exist"}
    existing_person = people[person_index]
    if person.name is not None:
        existing_person.name = person.name
    if person.age is not None:
        existing_person.age = person.age
    if person.male is not None:
        existing_person.male = person.male
    if person.religion is not None:
        existing_person.religion = person.religion
    if person.job is not None:
        existing_person.job = person.job
    return people[person_index]

@app.delete("/person/{person_index}")
def delete_person(person_index: int):
    if person_index not in people:
        return {"message": "Person does not exist"}
    del people[person_index]
    return {"message": f"Person with index {person_index} deleted"}

@app.get("/people")
def get_people():
    return people

@app.post("/person/{person_index}", name="create_person")
def create_person(request: Request, person_index: int, name: str, age: int, male: bool = True,
               religion: str = None, job: Optional[str] = None):
    if person_index in people:
        return {"message": "Person exist"}
    people[person_index] = Person(name=name, age=age, male=male, religion=str(religion), job=str(job))

    # approach 1: simple
    generated_href = str(request.url)
    print(f"simple href: {generated_href}")

    # approach 2: custom
    base_url = request.url_for("create_person", person_index=person_index)
    query_params = request.query_params
    if query_params:
        query_string = urlencode(query_params, doseq=True)
        generated_href = f"{base_url}?{query_string}"
    else:
        generated_href = base_url
    print(f"custom href: {generated_href}")

    return {
        "person": people[person_index],
        "href": generated_href
    }

if __name__ == "__main__":
    uvicorn.run("fast_api:app", reload=True)

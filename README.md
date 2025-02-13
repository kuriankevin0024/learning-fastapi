# learning-fastapi

## Local Setup
* Create python venv: `py -3.13 -m venv venv`
* Activate python venv: `venv\Scripts\activate`
* Update pip: `pip install --upgrade pip`
* Install Dependencies: `pip install -r requirements.txt`

## FastAPI Setup
* Install FastAPI: `pip install fastapi`
* Install Uvicorn: `pip install uvicorn`

## Application Startup
* Run: `uvicorn webapp.app.controller:app --reload`
* Base Url: `http://127.0.0.1:8000/`
* Doc Url: `http://127.0.0.1:8000/docs`

## Troubleshooting
### To reduce the reload time
* `pip install watchfiles`

## Environment and Dependencies
* Python Version: `Python 3.13.1`
* Pip Version: `pip 25.0.1 from C:\Users\mimphiz\Documents\GitHub\learning-fastapi\venv\Lib\site-packages\pip (python 3.13)`
* Dependencies

| Package           | Version |
|-------------------|---------|
| annotated-types   | 0.7.0   |
| anyio             | 4.8.0   |
| click             | 8.1.8   |
| colorama          | 0.4.6   |
| fastapi           | 0.115.8 |
| h11               | 0.14.0  |
| idna              | 3.10    |
| pip               | 25.0.1  |
| pydantic          | 2.10.6  |
| pydantic_core     | 2.27.2  |
| sniffio           | 1.3.1   |
| starlette         | 0.45.3  |
| typing_extensions | 4.12.2  |
| uvicorn           | 0.34.0  |

## FastAPI
* Path: `webapp/app/fast_api.py`
* Root Get API: `@app.get("/")`
* Get API with Path Param: `@app.get("/person/{person_index}")`
* Post API with Request Body: `@app.post("/person")`
* Put API with Path Param and Request Body: `@app.put("/person/{person_index}")`
* Patch API with Path Param and Request Body(Optional Fields): `@app.patch("/person/{person_index}")`
* Delete API with Path Param: `@app.delete("/person/{person_index}")`
* Get All API: `@app.get("/people")`
* Post API with Path and Query(Default and Optional) Params: `@app.post("/person/{person_index}", name="create_person")`
* Adding href(Simple and Custom) to response body: `@app.post("/person/{person_index}", name="create_person")`

## APIRouter
* Path: `webapp/app/api_router.py`
* Adding paths from different files

## Swagger API
* Path: `webapp/app/swagger_api.py`
* Default success response example value: `@app.post("/person", response_model=PersonResponse)`
* Custom success response example value and description: `@app.get("/student/{student_index}", response_model=StudentResponse)`
* Description and validation for path param: `@app.get("/student/{student_index}", response_model=StudentResponse)`
* Description, validation and default value for query param: `@app.post("/student/{student_id}", response_model=StudentResponse)`
* Description, validation and default value for fields in request and response object: `@app.post("/student", response_model=StudentResponse)`
* Return exception in case of failure: `@app.get("/student/{student_index}", response_model=StudentResponse)`
* Creating response object from request object: `@app.post("/student", response_model=StudentResponse)`

> Best option for optional query params -> from typing import Optional

# Todo
* APIRouter Learning
* Pydentic Learning

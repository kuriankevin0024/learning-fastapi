# learning-fastapi

## Local Setup
* Create python venv: `py -3.13 -m venv venv`
* Activate python venv: `venv\Scripts\activate`
* Update pip: `pip install --upgrade pip`

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

Get API
Get All API

Get API with Path Param
Get API Path Param With Description
Get API with Query Param

Post API Query Param with Default Value
Post API Query Param with Optional Value(Best option -> from typing import Optional)

Patch API with Path and Query Params

Post API with Request Body
Put API with Request Body
Patch API Request Body with Optional Fields
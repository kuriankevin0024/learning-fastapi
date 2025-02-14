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

## FastAPI Implementations
### Vanilla Implementation
* Path: `webapp/app/fast_api/fast_api_v1.py`
### DataClass Implementation
* Path: `webapp/app/fast_api/fast_api_v2.py`
* @dataclass: used to create request and response objects
### Pydantic Implementation
* Path: `webapp/app/fast_api/fast_api_v3.py`
* Pydantic BaseModel: used to create request and response objects
* Pydantic Field: used to provide documentation and basic validation
### Documentation Implementation
* Path: `webapp/app/fast_api/fast_api_v4.py`
* FastAPI HTTPException: used to return response code and response message
* FastAPI Path, Query and Body: used to provide documentation and basic validation
  * Path cannot have optional or default value
  * Body description is not working as expected
* response_model: used to update basic example for success response
* Config.json_schema_extra: used to update documentation and custom example for success response
* request: used to collect url, path and query information to create href

## APIRouter
* Path: `webapp/app/api_router.py`
* Adding paths from different files

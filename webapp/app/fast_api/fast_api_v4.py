import uvicorn
from fastapi import FastAPI, Request, Path, Query, Body, HTTPException
from pydantic import BaseModel
from urllib.parse import urlencode

app = FastAPI()

@app.get("/")
def root():
    return {"message": "fast_api_v4"}

class Data(BaseModel):
    m_bool: bool
    m_int: int
    m_str: str

class ResponseData(BaseModel):
    data: Data
    index: int
    href: str
    class Config:
        json_schema_extra = {
            "description": "Example of the data response body",
            "example": {
                "data": {
                    "m_bool": True,
                    "m_int": 0,
                    "m_str": "m str 0"
                },
                "index": 0,
                "href": "http://127.0.0.1:8000/data/0"
            }
        }

class ResponseDataMap(BaseModel):
    data_map: dict[int, Data]
    href: str

class ResponsePagedDataMap(BaseModel):
    data_map: dict[int, Data]
    href: str
    next_href: str

data_map: dict[int, Data] = {}

@app.get("/data", response_model=ResponseDataMap)
def get_data_all(request: Request):
    href = str(request.url)
    return ResponseDataMap(data_map=data_map, href=href)

@app.get("/data/{index}", response_model=ResponseData)
def get_data(request: Request,
             index: int = Path(..., description="index of data", ge=0)): # mandatory
    if index not in data_map:
        raise HTTPException(status_code=404, detail="data does not exist")
    href = str(request.url)
    return ResponseData(data=data_map[index], index=index, href=href)

@app.post("/data", response_model=ResponseData)
def post_data(request: Request,
              data: Data = Body(..., description="body of data")): # mandatory
    index =len(data_map)
    data_map[index] = data
    href = str(request.url)
    return ResponseData(data=data_map[index], index=index, href=href)

@app.get("/data/{version}/page", name= "get_data_page",response_model=ResponsePagedDataMap)
def get_data_page(request: Request,
                  version: str = Path(..., description="api version", min_length=2, max_length=3), # mandatory
                  index: int = Query(default=0, description="starting index", ge=0), # default
                  page_size: int = Query(None, description="page size", gt=0, le=10)): # optional
    if page_size is None:
        page_size = 10

    next_index = index + page_size

    data_list = list(data_map.items())
    paged_data_map = dict(data_list[index: next_index])

    next_href = ""
    if next_index < len(data_map):
        base_url = request.url_for("get_data_page", version=version)
        next_query_params = dict(request.query_params)
        next_query_params["index"] = next_index
        next_query_params_string = urlencode(next_query_params, doseq=True)
        next_href = f"{base_url}?{next_query_params_string}"

    href = str(request.url)
    return ResponsePagedDataMap(data_map=paged_data_map, href=href, next_href=next_href)

@app.post("/data/load", response_model=ResponseDataMap)
def post_data_load(request: Request,
                   count: int = Query(..., description="count of data", gt=0)): # mandatory
    for i in range(count):
        data_map[i] = Data(m_bool=True, m_int=i, m_str=f"m str {i}")
    href = str(request.url)
    return ResponseDataMap(data_map=data_map, href=href)

if __name__ == "__main__":
    uvicorn.run("fast_api_v4:app", reload=True)

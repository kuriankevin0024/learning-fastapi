import uvicorn
from fastapi import FastAPI
from dataclasses import dataclass
from typing import Optional

app = FastAPI()

@app.get("/")
def root():
    return {"message": "fast_api_v2"}

@dataclass
class Data:
    m_bool: bool
    m_int: int
    m_str: str

@dataclass
class OptionalData:
    o_bool: Optional[bool] = None
    o_int: Optional[int] = None
    o_str: Optional[str] = None

data_dict: dict[int, Data] = {}

@app.get("/data")
def get_data_all():
    return data_dict

@app.get("/data/{index}")
def get_data(index: int):
    if index not in data_dict:
        return {"message": "data does not exist"}
    return data_dict[index]

@app.post("/data")
def post_data(data: Data):
    index =len(data_dict)
    data_dict[index] = data
    return {"message": f"index:{index}"}

@app.put("/data/{index}")
def put_data(index: int, data: Data):
    if index not in data_dict:
        return {"message": "data does not exist"}
    data_dict[index] = data
    return data_dict[index]

@app.patch("/data/{index}")
def patch_data(index: int, optional_data: OptionalData):
    if index not in data_dict:
        return {"message": "data does not exist"}
    data = data_dict[index]
    if optional_data.o_bool is not None:
        data.m_bool = optional_data.o_bool
    if optional_data.o_int is not None:
        data.m_int = optional_data.o_int
    if optional_data.o_str is not None:
        data.m_str = optional_data.o_str
    return data_dict[index]

@app.delete("/data/{index}")
def delete_data(index: int):
    if index not in data_dict:
        return {"message": "data does not exist"}
    del data_dict[index]
    return {"message": "data deleted"}

if __name__ == "__main__":
    uvicorn.run("fast_api_v2:app", reload=True)

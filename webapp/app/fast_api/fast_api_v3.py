import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Optional

app = FastAPI()

@app.get("/")
def root():
    return {"message": "fast_api_v3"}

class Data(BaseModel):
    m_bool: bool = Field(True, description="m bool") # default
    # m_int: int = Field(description="m int", ge=0, lt=10) # mandatory -> less readable
    m_int: int = Field(..., description="m int", ge=0, lt=10) # mandatory
    m_str: str = Field(None, description="m str", min_length=2, max_length=10) # optional

class OptionalData(BaseModel):
    o_bool: Optional[bool] = Field(None, description="o bool") # optional
    o_int: Optional[int] = Field(None, description="o int", ge=0, lt=10) # optional
    o_str: Optional[str] = Field(None, description="o str", min_length=2, max_length=10) # optional

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
    if optional_data.m_bool is not None:
        data.m_bool = optional_data.m_bool
    if optional_data.m_int is not None:
        data.m_int = optional_data.m_int
    if optional_data.m_str is not None:
        data.m_str = optional_data.m_str
    return data_dict[index]

@app.delete("/data/{index}")
def delete_data(index: int):
    if index not in data_dict:
        return {"message": "data does not exist"}
    del data_dict[index]
    return {"message": "data deleted"}

if __name__ == "__main__":
    uvicorn.run("fast_api_v3:app", reload=True)

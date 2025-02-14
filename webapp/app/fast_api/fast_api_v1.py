import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "fast_api_v1"}

class Data:
    def __init__(self, m_bool: bool, m_int: int, m_str: str):
        self.m_bool = m_bool
        self.m_int = m_int
        self.m_str = m_str

    def to_dict(self):
        return {
            "m_bool": self.m_bool,
            "m_int": self.m_int,
            "m_str": self.m_str,
        }

data_dict: dict[int, Data] = {}

@app.get("/data")
def get_data_all():
    response_data = {}
    for key, value in data_dict.items():
        response_data[key] = value.to_dict()
    return response_data

@app.get("/data/{index}")
def get_data(index: int):
    if index not in data_dict:
        return {"message": "data does not exist"}
    return data_dict[index].to_dict()

@app.post("/data")
def post_data(request_data: dict):
    try:
        m_bool = request_data["m_bool"]
        m_int = request_data["m_int"]
        m_str = request_data["m_str"]
        data = Data(m_bool=m_bool, m_int=m_int, m_str=m_str)
    except KeyError as e:
        return {"error": f"missing key: {str(e)}"}
    index =len(data_dict)
    data_dict[index] = data
    return {"message": f"index:{index}"}

@app.put("/data/{index}")
def put_data(index: int, request_data: dict):
    if index not in data_dict:
        return {"message": "data does not exist"}
    try:
        m_bool = request_data["m_bool"]
        m_int = request_data["m_int"]
        m_str = request_data["m_str"]
        data = Data(m_bool=m_bool, m_int=m_int, m_str=m_str)
    except KeyError as e:
        return {"error": f"missing key: {str(e)}"}
    data_dict[index] = data
    return data_dict[index].to_dict()

@app.patch("/data/{index}")
def patch_data(index: int, request_data: dict):
    if index not in data_dict:
        return {"message": "data does not exist"}
    data = data_dict[index]
    if "m_bool" in request_data:
        data.m_bool = request_data["m_bool"]
    if "m_int" in request_data:
        data.m_int = request_data["m_int"]
    if "m_str" in request_data:
        data.m_str = request_data["m_str"]
    return data.to_dict()

@app.delete("/data/{index}")
def delete_data(index: int):
    if index not in data_dict:
        return {"message": "data does not exist"}
    del data_dict[index]
    return {"message": "data deleted"}

if __name__ == "__main__":
    uvicorn.run("fast_api_v1:app", reload=True)

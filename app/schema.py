from pydantic import BaseModel

class PostCreate(BaseModel):
    title:str
    content:str

class PostResponse(BaseModel): # specifies the value to be returned in our documentation
     title:str
     content:str
from distutils.dep_util import newer

from fastapi import FastAPI
from fastapi import HTTPException
from app.schema import Postcreate
app = FastAPI()

text_post ={}
@app.post("/posts")
def get_all_post(limit:int):
    if limit:
        return list(text_posts.values(0)][:limit]
    return text_posts

@app.get("/id")
def get_post(id:int):
    if id not in text_post
        raise HTTPException(status_code=404, detail="post not found")
    return text_post.get(id)

@app.post("/posts")
def create_post(post:Postcreate):
    new_post={"title":post.title,"content":post.content}
    text_post[max(text_post.keys())+1]=new_post
    return new_post




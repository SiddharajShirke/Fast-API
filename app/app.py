from fastapi import FastAPI,HTTPException,File,UploadFile,Form ,Depends
from app.schema import PostCreate , PostResponse
from app.db import create_db_and_tables, get_async_session, Post
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from contextlib import asynccontextmanager
from sqlalchemy import select
from app.image import imagekit
from imagekitio.models.UploadFileRequestOptions import UploadFileRequestOptions
import shutil
import uuid
import os
import tempfile

@asynccontextmanager
async def lifespan(app: FastAPI) :
    await create_db_and_tables()
    yield

app = FastAPI(lifespan=lifespan)

@app.post("/upload")   # helps to upload the posts
async def upload_file  (
           file: UploadFile = File(...),
           caption: str = Form(""),
           session: AsyncSession = Depends(get_async_session),
):

    temp_file_path=None

    try:                     # save the temporary copy of a file
        with tempfile.NamedTemporaryFile(delete=False , suffix=os.path.splitext(file.filename)[1]) as temp_file:
             temp_file_path=temp_file.name
             shutil.copyfileobj(file.file,temp_file)

        upload_result=imagekit.upload_file(
            file=open(temp_file_path,"rb"),
            file_name=file.filename,
            options=UploadFileRequestOptions(
                use_unique_file_name=True,
                tags=["backend_upload"]
            )
        )

        if upload_result.response_metadata.http_status_code==200:
            post=Post(
                user_id = user.id,
                caption=caption,
                url=upload_result.url,
                file_type="video" if file.content_type.startswith("video/") else "image",
                file_name=upload_result.name
            )

            session.add(post)
            await session.commit()    # saves the content in database
            await session.refresh(post)
            return post

    except Exception as e :
                  raise HTTPException(status_code=404, detail=str(e))
    finally:
             if  temp_file_path and os.path.exists(temp_file_path):
                 os.unlike(temp_file_path),
                 file.file.close(0)

@app.get("/feed")   # helps to get posts
async def  get_feed(
        session: AsyncSession = Depends(get_async_session)
):
     result= await session.execute(select(Post).order_by(Post.created_at.desc()))  # helps us to query data by adding filters
     post= [row[0]for row in result.scalars().all()]

     post_data=[]
     for post in posts:
         posts_data.append(
             {
                  "id": str(post.id),
                  "caption": post.caption,
                  "url": post.url,
                  "file_type": post.file_type,
                  "file_name": post.file_name,
                  "created_at": post.created_at,
             }
         )

     return {"posts": posts_data}

@app.delete("/post/{post_id]")
async def delete_post(post_id:str , session: AsyncSession = Depends(get_async_session)):
    try:
        post_uuid=uuid.UUID(post_id)

        result=await session.execute(select(Post).where(Post.id == post_uuid))
        post=result.scalars().first()

        if not post :
            raise HTTPException(status_code=404, detail="Post not found")

        await session.delete(post)
        await session.commit()

        return {"sucess" : True , "message" :"Post deleted successfully "}

    except Exception as e :
        raise HTTPException(status_code=404, detail=str(e))




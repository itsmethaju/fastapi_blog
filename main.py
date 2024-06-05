from fastapi import FastAPI, File, UploadFile, HTTPException
from pydantic import BaseModel
from typing import List
from models import blog,Work,Team,Contact
import psycopg2
from fastapi.middleware.cors import CORSMiddleware
from helper.email import send_confirmation_email
# Connect to PostgreSQL
connection = psycopg2.connect(
    host='localhost',
    user='blog',
    password='bloog1',
    dbname='bloog'
)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/blog/")
async def upload_video(description: str, title: str, video_url: str):
    with connection.cursor() as cursor:
        try:
            insert_query = '''
            INSERT INTO blog (video_url, description, title)
            VALUES (%s, %s, %s)
            RETURNING id
            '''
            cursor.execute(insert_query, (video_url, description, title))

            connection.commit()
            video_id = cursor.fetchone()[0]
        except Exception as e:
            connection.rollback()
            raise HTTPException(status_code=500, detail=str(e))
    

    return {"id": video_id, "video_url": video_url, "description": description, "title": title}

@app.get("/get_blog/", response_model=List[blog])
async def get_videos():
    try:
        with connection.cursor() as cursor:
            sql = "SELECT id, video_url, description, title FROM blog"
            cursor.execute(sql)
            result = cursor.fetchall()
            videos = [blog(id=row[0], video_url=row[1], description=row[2], title=row[3]) for row in result]
            return videos
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.delete("/blog/{video_id}")
async def delete_video(video_id: int):
    with connection.cursor() as cursor:
        try:
            delete_query = '''
            DELETE FROM blog
            WHERE id = %s
            '''
            cursor.execute(delete_query, (video_id,))
            connection.commit()
            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="blog not found")
            else:
                return {"message": "Video deleted successfully"}
        except Exception as e:
            connection.rollback()
            raise HTTPException(status_code=500, detail=str(e))

@app.post("/works/")
async def upload_work(description: str, title: str, img_url: str):
    with connection.cursor() as cursor:
        try:

            insert_query = '''
            INSERT INTO work (img_url, description, title)
            VALUES (%s, %s, %s)
            RETURNING id
            '''
            cursor.execute(insert_query, (img_url, description, title))
            connection.commit()
            work_id = cursor.fetchone()[0]
        except Exception as e:
            connection.rollback()
            raise HTTPException(status_code=500, detail=str(e))
    
    return {"id": work_id, "img_url": img_url, "description": description, "title": title}


@app.get("/works/", response_model=List[Work])
async def get_works():
    try:
        with connection.cursor() as cursor:
            sql = "SELECT id, img_url, description, title FROM work"
            cursor.execute(sql)
            result = cursor.fetchall()
            works = [Work(id=row[0], img_url=row[1], description=row[2], title=row[3]) for row in result]
            return works
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/teams/")
async def upload_team(image_url: str, description: str, title: str):
    with connection.cursor() as cursor:
        try:

            insert_query = '''
            INSERT INTO team (img_url, description, title)
            VALUES (%s, %s, %s)
            RETURNING id
            '''
            cursor.execute(insert_query, (image_url, description, title))
            connection.commit()
            team_id = cursor.fetchone()[0]
        except Exception as e:
            connection.rollback()
            raise HTTPException(status_code=500, detail=str(e))
    
    return {"id": team_id, "image_url": image_url, "description": description, "title": title}

@app.get("/teams/", response_model=List[Team])
async def get_teams():
    try:
        with connection.cursor() as cursor:
            sql = "SELECT id, img_url, description, title FROM team"
            cursor.execute(sql)
            result = cursor.fetchall()
            teams = [Team(id=row[0], img_url=row[1], description=row[2], title=row[3]) for row in result]
            return teams
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    
@app.post("/contacts/")
async def create_contact(name: str, email: str, company: str,query:str):
    with connection.cursor() as cursor:
        try:

            insert_query = '''
            INSERT INTO quary (name, email, company, query)
            VALUES ( %s, %s, %s, %s)
            RETURNING id
            '''

            cursor.execute(insert_query, ( name,email, company,query))
            connection.commit()
            send_confirmation_email(email)
        except Exception as e:
            connection.rollback()
            raise HTTPException(status_code=500, detail=str(e))
    
    return {"message": "Contact created successfully"}


@app.post("/email/")
async def create_contact(email: str):
    with connection.cursor() as cursor:
        try:
            print(email)

            insert_query = '''
            INSERT INTO contactMail (email)
            VALUES (%s)
            RETURNING id
            '''

            cursor.execute(insert_query, (email,))
            connection.commit()
            send_confirmation_email(email)
        except Exception as e:
            connection.rollback()
            raise HTTPException(status_code=500, detail=str(e))
    
    return {"message": "email successfully"}
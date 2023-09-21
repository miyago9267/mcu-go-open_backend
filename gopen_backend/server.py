from fastapi import FastAPI
from routers import tests,auth,comment,course
from dotenv import load_dotenv
import uvicorn, os

load_dotenv()

app = FastAPI()
app.include_router(tests.router,prefix="/test",tags=["test"])
app.include_router(course.router,prefix="/course",tags=["course"])
app.include_router(auth.router,prefix="/auth",tags=["auth"])
app.include_router(comment.router,prefix="/comment",tags=["comment"])


@app.get("/PING")
def ping() -> str:
   return "PONG"

uvicorn.run(app, host='0.0.0.0', port=int(os.getenv("SERVER_PORT",8080)))
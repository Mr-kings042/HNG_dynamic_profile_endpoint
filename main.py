from fastapi import FastAPI
from routers import user_router
from fastapi.middleware.cors import CORSMiddleware
from middleware import add_request_id_and_process_time

app = FastAPI(title="User Profile API and Cat Facts", version="1.0.0")

# CORS configuration
app.add_middleware(CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)
app.middleware("http")(add_request_id_and_process_time) 
@app.get("/")
async def root():
    return {"message": "Welcome to the User Profile API and CatFActs"}

app.include_router(user_router, prefix="/me", tags=["User"])

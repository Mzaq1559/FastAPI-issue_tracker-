from fastapi import FastAPI
from app.routes.issues import router as issues_router
from app.middleware.timer import timer_middleware
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.middleware("http")(timer_middleware)
app.include_router(issues_router)
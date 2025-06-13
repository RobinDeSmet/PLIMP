from fastapi import APIRouter, FastAPI

from plimp.api.routes import todo


api_router = APIRouter()
api_router.include_router(todo.router)


app = FastAPI()
app.include_router(api_router)


@app.get("/health")
def health_check() -> bool:
    """
    Health check
    """
    return True

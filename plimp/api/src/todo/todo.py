from fastapi import APIRouter

router = APIRouter(tags=["todo"])


@router.get("/todo/health")
def health_check() -> bool:
    """
    Health check
    """
    return True

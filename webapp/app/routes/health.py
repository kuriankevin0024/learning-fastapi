from fastapi import APIRouter

router = APIRouter()

@router.get("/health")
def health():
    return {"message": "Health is running"}

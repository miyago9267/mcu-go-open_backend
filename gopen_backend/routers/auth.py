from fastapi import APIRouter

router = APIRouter()

@router.post('/login')
async def login():
    return {'login': True}

@router.post('/logout')
async def logout():
    return {'logout': True}
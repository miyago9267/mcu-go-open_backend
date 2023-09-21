from fastapi import APIRouter
from controllers import course

router = APIRouter()

@router.get('/')
async def get_all_courses(search: str = None):
    return course.get_all_courses(search=search)

@router.get('/all')
async def get_all_courses():
    return course.get_all_courses()

@router.get('/{teacher_id}/{course_id}')
async def get_all_courses(teacher_id: int, course_id: int):
    return {'course': {}}
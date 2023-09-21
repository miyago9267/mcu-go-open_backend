from utils import fake_data 

def get_all_courses(search: str = None):
    courses = fake_data.get_fake_courses(10)
    if search:
        # 此處使用 str.casefold() 以忽略大小寫進行搜索
        return [course for course in courses if search.casefold() in course.name.casefold()]
    
    return courses
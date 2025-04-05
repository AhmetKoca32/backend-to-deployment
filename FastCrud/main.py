from fastapi import FastAPI, Body

app = FastAPI()

#fake veritabanı oluşturma
courses_db = [
    {"id" : 1 , "instructor" : "Ahmet", "title":"Python" , "category":"Development"},
    {"id" : 2 , "instructor" : "Atil", "title":"Java" , "category":"Development"},
    {"id" : 3 , "instructor" : "Ahmet", "title":"Kubernates" , "category":"DEVOps"},
    {"id" : 4 , "instructor" : "Zeynep", "title":"Redis" , "category":"DEVOps"},
    {"id" : 5 , "instructor" : "Fatma", "title":"Celery" , "category":"DEVOps"},
    {"id" : 6 , "instructor" : "Atlas", "title":"Python" , "category":"AI"},
]




#endpoint = bir API'de bir kaynağa veya işleve ulaşmak için kullanılar URL veya ağ adresidir.

@app.get("/")
async def hello_world():
    return{"message": "Hello World"}

@app.get("/hello")
async def hello_world1():
    return{"detailed message": "Hello Ahmet"}

# projeyi denemek için terminale "uvicorn main:app --reload" kodunu kullan


#oluşturulan veritabanı üzerinde crud işlemleri
@app.get("/courses")
async def get_all_courses():
    return courses_db

###  Path Parameter  ####
@app.get("/courses/title/{course_title}")
async def get_course(course_title : str):
    for course in courses_db:
        if course.get('title').casefold() == course_title.casefold(): #casefold kullanımı ile büyük harf küçük harf duyarlılığı giderildi
            return course

@app.get("/courses/id/{course_id}")
async def get_course_by_id(course_id : int):
    for course in courses_db:
        if course.get('id') == course_id:
            return course

## Aynı endpoint urlde yer alan farklı çağırma yöntemlerinin ikisi de çalışmayacaktır en üstteki sisteme göre çalışır yani yukarıda gördüğünüz yapıya göre arama işlemi 'title' a göre yapılır

@app.get("/courses/byid/{course_id}")
async def get_course_by_id(course_id : int):
    for course in courses_db:
        if course.get('id') == course_id:
            return course

###  Query Parameters  ###
@app.get("/courses/")
async def get_category_by_query(category : str):
    courses_to_return = []
    for course in courses_db:
        if course.get('category').casefold() == category.casefold():
            courses_to_return.append(course)
    return courses_to_return


### Path ve Query aynı anda ###
@app.get("/courses/instructor/{course_instructor}/")
async def get_instructor_category_by_query(course_instructor: str , category: str):
    courses_to_return = []
    for course in courses_db:
        if (course.get('instructor').casefold() == course_instructor.casefold()
                and course.get('category').casefold() == category.casefold()):
            courses_to_return.append(course)
    return courses_to_return


@app.post("/courses/create_course")
async def create_course(new_course = Body()):
    courses_db.append(new_course)


@app.put("/courses/update_course")
async def update_course(updated_course=Body()):
    for index in range(len(courses_db)):
        if courses_db[index].get("id") == updated_course.get("id"):
         courses_db[index] = updated_course


@app.delete("/courses/delete_courses")
async def delete_course(course_id: int):
    for index in range(len(courses_db)):
        if courses_db[index].get("id") == course_id:
            courses_db.pop(index)
            break

#JSON -> Javascript Object Notation
#FastAPI nın en güzel özelliklerinden birisi de endpoint olarak '/docs' yazdığımızda tarayıcımızda şimdiye kadar yazdığımız bütün endpointleri gösterir

from fastapi import FastAPI, Body, Path, Query, HTTPException # httpexception bi istekte hata varsa onu nasıl döndüreceğimizi kendi statuslarımızı seçebiliyoruz
from typing import Optional # Opsiyonel olarak almak istedğimiz parametrelerde
from pydantic import BaseModel, Field #parametrelerin hangi veri tiğinde olacağını belirlerlemek için ekstra validasyonlar
from starlette import status #http status kodlarımızı oluşturacağız


app = FastAPI()

class Course():
     id: int
     title: str
     instructor: str
     rating: int
     published_date: int



     def __init__(self, id:int, title: str, instructor: str, rating: int, published_date: int):
         self.id = id
         self.title = title
         self.instructor = instructor
         self.rating = rating
         self.published_date = published_date

courses_db = [
    Course(1, "Python", "Ahmet", 5, 2029),
    Course(2, "Flutter", "Ahmet", 4, 2013),
    Course(3, "Jenkins", "Aslı", 3, 2024),
    Course(4, "Kubernates", "Sıla", 2, 2010),
    Course(5, "Docker", "Veli", 1, 2020),
    Course(6, "ML", "Ali", 4, 2021)
]


class CourseRequest(BaseModel):
    id: Optional[int] = Field(description="The id of the course", default=None)
    title: str = Field(min_length=3, max_length=20)
    instructor: str = Field(min_length=3)
    rating: int = Field(gt=0, lt=6)
    published_date: int = Field(ge=2000, le=2050) # yeni pydantic versiyonu ile greater than ve less than gösterimleri (gte,lte) den (ge,le) ye dönüştü

    model_config = {
        "json_schema_extra":{
            "example":{
                "title": "API Development",
                "instructor": "Ahmet",
                "rating": 5,
                "published_date": 2029
            }
        }
    }


@app.get("/courses",status_code=status.HTTP_200_OK)
async  def get_all_courses():
    return courses_db

@app.get("/courses/{course_id}",status_code=status.HTTP_200_OK)
async def get_course(course_id: int = Path(gt=0)):
    for course in courses_db:
        if course.id == course_id:
            return course
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='course not found')

@app.get("/courses/",status_code=status.HTTP_200_OK)
async def get_course_by_rating(course_rating: int = Query(gt=0 , lt=6)):
    courses_to_return = []
    for course in courses_db:
        if course.rating == course_rating:
            courses_to_return.append(course)
    return courses_to_return

@app.get("/courses/publish/", status_code=status.HTTP_200_OK)
async def get_course_by_published_date(course_published_date: int = Query(gt=2009 , lt=2050)):
    courses_to_return= []
    for course in courses_db:
        if course.published_date == course_published_date:
            courses_to_return.append(course)
    return courses_to_return


@app.post("/create-course",status_code=status.HTTP_201_CREATED)
async def create_course(course_request: CourseRequest):
    new_course = Course(**course_request.model_dump()) # Bu oluşturulan request modelinden gelen verileri almanın kısa yoludur ama id yi optional olarak atadığımız için burada sıkıntı çıkabilir
    courses_db.append(find_course_id(new_course))

def find_course_id(course : Course):
    course.id = 1 if len(courses_db) == 0 else courses_db[-1].id + 1
    return course

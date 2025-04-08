from fastapi import FastAPI, Body, Path, Query, HTTPException # httpexception bi istekte hata varsa onu nasıl döndüreceğimizi kendi statuslarımızı seçebiliyoruz
from typing import Optional # Opsiyonel olarak almak istedğimiz parametrelerde
from pydantic import BaseModel, Field #parametrelerin hangi veri tiğinde olacağını belirlerlemek için ekstra validasyonlar
from starlette import status #http status kodlarımızı oluşturacağız


app = FastAPI()

class Course:
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


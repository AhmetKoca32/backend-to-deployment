from fastapi import FastAPI

app = FastAPI()

#endpoint = bir API'de bir kaynağa veya işleve ulaşmak için kullanılar URL veya ağ adresidir.

@app.get("/")
async def hello_world():
    return{"message": "Hello World"}

@app.get("/hello")
async def hello_world1():
    return{"detailed message": "Hello Ahmet"}

# projeyi denemek için terminale "uvicorn main:app --reload" kodunu kullan
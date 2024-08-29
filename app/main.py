from fastapi import FastAPI
from handlers.book_handler import router as book_router

app = FastAPI()

app.include_router(book_router, prefix="/books")

@app.get('/')
def lobby():
    return {'message': 'Welcome to veri-blubuk awek awek gedagedigedagedao!'}
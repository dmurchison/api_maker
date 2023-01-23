from fastapi import FastAPI
from fastapi.responses import PlainTextResponse, JSONResponse


app = FastAPI()


@app.get('/', response_class=PlainTextResponse)
def home():
    return "Hello World, This is the home page"

@app.get('/test', response_class=JSONResponse)
def test_endpoint():
    return {
        "message": "Hello World, This is a test endpoint", 
        "status": "success", 
        "code": 200, 
        "data": [], 
        "error": [], 
        "meta": {
            "version": "1.0.0",
            "author": "Duncan Murch",
            "email": "something@email.com"
        }
    }




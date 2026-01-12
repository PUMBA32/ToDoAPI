from fastapi import FastAPI
from fastapi.responses import JSONResponse

import uvicorn


app = FastAPI()


@app.get('/')
def root():
    return JSONResponse({
        "message": "This is the main page."
    })


if __name__ == '__main__':
    uvicorn.run('app:app', reload=True)
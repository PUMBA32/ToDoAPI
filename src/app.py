from fastapi import FastAPI
from fastapi.responses import JSONResponse

from api.views import router as api_router

from database import *

import uvicorn

Base.metadata.create_all(bind=engine)


app = FastAPI()
app.include_router(api_router)


@app.get('/')
def root():
    return JSONResponse({
        "message": "This is the main page."
    })


if __name__ == '__main__':
    uvicorn.run('app:app', reload=True)
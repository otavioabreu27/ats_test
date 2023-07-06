from typing import Union
from fastapi import FastAPI
import logging

logging.basicConfig(
    level=logging.DEBUG,
    filename="app.log",
    filemode="w",
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)

app = FastAPI()


@app.get("/")
def hello_world():
    """
    Hello World!
    """
    logging.debug("Function hello_world from main.py")
    return {"Hello": "World"}

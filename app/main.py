# Este es el archivo principal de todo el programa
# Aqui vamos a definir el servidor de uvicorn
# Este servidor nos permitira hacerle consultas a la API
# Aqui importamos todas las rutas que va encontrar uvicorn
# uvicorn las podra hacer visibles a consultas de cualquier persona (cliente)

import logging

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Se importa la configuracion de la bd
import db
from config import config
# Se importan los modelos
# Se importan todas las rutas
from user import endpoint as user_endpoint
from user import modelo
from book import endpoint as book_endpoint
from book import modelo
from card import endpoint as card_endpoint
from card import modelo
from gender import endpoint as gender_endpoint
from gender import modelo
from order import endpoint as order_endpoint
from order import modelo

# Se crea la aplicacion de FastApi
app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=config.get("origins"),
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Se importan las rutas de la API:

# Ruta de clima
app.include_router(user_endpoint.router, prefix="/v1/user", tags=["users"])
app.include_router(book_endpoint.router, prefix="/v1/book", tags=["books"])
app.include_router(card_endpoint.router, prefix="/v1/card", tags=["cards"])
app.include_router(gender_endpoint.router, prefix="/v1/gender", tags=["genders"])
app.include_router(order_endpoint.router, prefix="/v1/order", tags=["orders"])


if __name__ == "__main__":
    db.Base.metadata.create_all(db.conn)
    uvicorn_arg = config.get("allowed_args_for_uvicorn")
    uvicorn.run(app="main:app", **uvicorn_arg)

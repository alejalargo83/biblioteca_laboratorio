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


if __name__ == "__main__":
    db.Base.metadata.create_all(db.conn)
    uvicorn_arg = config.get("allowed_args_for_uvicorn")
    uvicorn.run(app="main:app", **uvicorn_arg)

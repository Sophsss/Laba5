from fastapi import FastAPI
from uvicorn import Config, Server

from web_app import api_router

if __name__ == '__main__':
    # FastAPI - связующее звено между HTTP - сервером и кодом программиста.
    # В числе прочего отвечает за документацию (/docs).
    app = FastAPI()
    app.include_router(api_router)
    config = Config(
        app=app,
        host="localhost",
        port=8081
    )
    # Сам сервер. Принимает запрос, парсит аргументы,  заголовки и т.п.,
    # передает в FastAPI.
    # Собирает ответ (заголовки, куки, тело ответа в виде текста).
    server = Server(config)
    server.run()
from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from src.routes import routes

app = FastAPI()
app.router.include_router(routes.router)

register_tortoise(
    app,
    db_url="postgres://postgres:hd2biwnm@127.0.0.1:5431/tournament",
    modules={"models": ["src.models"]},
    generate_schemas=True,
    add_exception_handlers=True,
)

import uvicorn
from fastapi import FastAPI

# Импортируем роутер.
from app.api.routers import main_router
from app.core.config import settings
# Импортируем корутину для создания первого суперюзера.
from app.core.init_db import create_first_superuser

app = FastAPI(title=settings.app_title)

# Подключаем роутер.
app.include_router(main_router)


# При старте приложения запускаем корутину create_first_superuser.
@app.on_event('startup')
async def startup():
    await create_first_superuser()


if __name__ == '__main__':
    uvicorn.run(app, debug=True)

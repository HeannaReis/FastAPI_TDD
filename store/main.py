from fastapi import FastAPI
from store.core.config import settings
from store.routers import api_router

class App(FastAPI):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(
            *args,
            **kwargs,
            version="0.0.1",
            title=settings.PROJECT_NAME,
            # Remova o root_path temporariamente
            # root_path=settings.ROOT_PATH,
        )

app = App()

@app.get("/ping")
async def ping():
    return {"message": "pong"}

app.include_router(api_router)

print("Routes included:")
for route in app.routes:
    print(route.path, route.name)

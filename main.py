from fastapi import FastAPI
from routers.backend_api.server import backend_api_router
from routers.frontend_api.client import frontend_api_router


app = FastAPI()
app.include_router(frontend_api_router)
app.include_router(backend_api_router)
app.iclude_router(frontend_api_router)



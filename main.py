from fastapi import FastAPI
from config.server import server_settings
from api.controllers import account_router



app = FastAPI()
app.include_router(account_router)

from fastapi import FastAPI
import src.routers.pools as pool

app = FastAPI()
app.include_router(pool.router)

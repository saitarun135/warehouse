from fastapi import APIRouter

home_router = APIRouter(tags=['home-page'])

@home_router.get("/load-menus")
async def load_menus():
    return {"message": "Menus loaded successfully"}
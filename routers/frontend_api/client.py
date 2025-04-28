from fastapi import APIRouter, Depends, HTTPException, status, Request, Response 
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from security import verify_token, create_access_token, is_authenticated

frontend_api_router = APIRouter()
templates = Jinja2Templates(directory="./templates")


@frontend_api_router.get("/login")
async def login(request: Request, response: Response):
   token = request.cookies.get("access_token")
   if token:
    response = RedirectResponse(url="/dashboard", status_code=status.HTTP_302_FOUND)
    return response
   else:
      response = templates.TemplateResponse("login.html", {"request": request})
      response.set_cookie("access_token", create_access_token(data={"sub": "rafaellima"}))
      return response
   

@frontend_api_router.get("/dashboard")
async def login(request: Request, response: Response, dependencies: Depends = Depends(is_authenticated)):
   token = request.cookies.get("access_token")
   response = templates.TemplateResponse("dashboard.html", {"request": request})
   response.set_cookie("access_token", create_access_token(data={"sub": "rafaellima"}))
   return response

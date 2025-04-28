from fastapi import APIRouter, Depends, HTTPException, status, Request, Response, Form
from fastapi.responses import RedirectResponse
from fastapi.security import OAuth2PasswordBearer
from fastapi.security import OAuth2PasswordRequestForm
from security import verify_token, create_access_token, get_current_user_id
backend_api_router = APIRouter()


@backend_api_router.post("/login")
async def login(request: Request, response: Response, form = Form(...)):
    user = form.username
    password = form.password
    

    


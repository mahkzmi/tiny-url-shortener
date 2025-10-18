from fastapi import FastAPI, Depends, HTTPException, status,Request
from fastapi.responses import RedirectResponse
from sqlmodel import Session
from .database import create_db, get_session
from .schemas import ShortenRequest, ShortenResponse, StatsResponse
from .crud import create_link, get_link_by_code, increment_click, get_all_link
from .utils import generate_code, validate_custom_code
import os
from fastapi.templating import Jinja2Templates
from fastapi import Form


app = FastAPI(title="Tiny URL Shortener", version="0.1.0")

BASE_URL = os.getenv("BASE_URL", "http://localhost:8000")



templates = Jinja2Templates(directory="templates")

@app.get("/dashboard")
def dashboard(request: Request, session: Session = Depends(get_session)):
    links = get_all_link(session)
    return templates.TemplateResponse("dashboard.html", {"request": request, "links": links})



@app.post("/dashboard")
def create_link_from_dashboard(request: Request,
                                target_url: str = Form(...),
                                custom_code: str = Form(None),
                                title: str = Form(None),
                                session: Session = Depends(get_session)):
    if custom_code:
        code = custom_code.strip()
    if not validate_custom_code(code):
        raise HTTPException(status_code=400, detail="Invalid Custom Code Format")
    if get_link_by_code(session, code):
        raise HTTPException(status_code=409, detail="Custom Code already in use.")
    else:
        for _ in range(5):
            candidate = generate_code(6) 
            if not get_link_by_code(session, candidate):
                code = candidate
                break
            else:
                raise HTTPException(status_code=500, detail="Couldn't Generate unique Code.")
            
        create_link(session, code=code, target_url=target_url, title=title)
        links = get_all_link(session)
        return templates.TemplateResponse("dashboard.html", {"request": request, "links": links})    















@app.on_event("startup")
def on_startup():
    create_db()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/shorten", response_model=ShortenResponse, status_code=status.HTTP_201_CREATED)
def shorten(payload: ShortenRequest, session: Session = Depends(get_session)):
    # validate custom code if provided
    if payload.custom_code:
        code = payload.custom_code.strip()
        if not validate_custom_code(code):
            raise HTTPException(status_code=400, detail="invalid custom_code format")
        if get_link_by_code(session, code):
            raise HTTPException(status_code=409, detail="custom_code already in use")
    else:
        # generate unique code
        for _ in range(5):
            candidate = generate_code(6)
            if not get_link_by_code(session, candidate):
                code = candidate
                break
        else:
            raise HTTPException(status_code=500, detail="couldn't generate unique code, try again")

    link = create_link(session, code=code, target_url=str(payload.url), title=payload.title)
    short_url = f"{BASE_URL.rstrip('/')}/{link.code}"
    return ShortenResponse(code=link.code, short_url=short_url, target_url=link.target_url)

@app.get("/stats/{code}", response_model=StatsResponse)
def stats(code: str, session: Session = Depends(get_session)):
    link = get_link_by_code(session, code)
    if not link:
        raise HTTPException(status_code=404, detail="code not found")
    return StatsResponse(
        code=link.code,
        target_url=link.target_url,
        click_count=link.click_count or 0,
        created_at=link.created_at.isoformat(),
        title=link.title
    )

@app.get("/{code}")
def redirect(code: str, session: Session = Depends(get_session)):
    link = get_link_by_code(session, code)
    if not link:
        raise HTTPException(status_code=404, detail="not found")
    increment_click(session, link)
    return RedirectResponse(url=link.target_url, status_code=302)


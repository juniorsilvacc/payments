from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(
    directory='templates',
)

@app.get("/", response_class=HTMLResponse)
async def checkout_page(request: Request):
    return templates.TemplateResponse(
        name='checkout.html',
        context={'request': request},
    )

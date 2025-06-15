from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
app = FastAPI()
templates = Jinja2Templates(directory="templates")

# In-memory todo list
todos = []

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "todos": todos})

@app.post("/add")
async def add_todo(task: str = Form(...)):
    todos.append(task)
    return RedirectResponse(url="/", status_code=303)

@app.post("/delete/{task_id}")
async def delete_todo(task_id: int):
    if 0 <= task_id < len(todos):
        todos.pop(task_id)
    return RedirectResponse(url="/", status_code=303)

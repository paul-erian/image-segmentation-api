from fastapi import FastAPI, File, UploadFile, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from model import predict_class
import uuid
from fastapi.staticfiles import StaticFiles


app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def form(request: Request):
    return templates.TemplateResponse("form.html", {"request": request})

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.post("/predict", response_class=HTMLResponse)
async def predict(request: Request, file: UploadFile = File(...)):
    image_bytes = await file.read()

    # Créer un nom unique et sauvegarder l’image
    image_id = str(uuid.uuid4())
    image_path = f"static/{image_id}.jpg"
    with open(image_path, "wb") as f:
        f.write(image_bytes)

    # Prédiction
    prediction = predict_class(image_bytes)

    return templates.TemplateResponse("result.html", {
        "request": request,
        "prediction": prediction,
        "image_path": f"/static/{image_id}.jpg"
    })
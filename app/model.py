from torchvision import models, transforms
from PIL import Image
import torch
import io
import urllib.request

# Charger modèle ResNet50 préentraîné
model = models.resnet50(weights=models.ResNet50_Weights.IMAGENET1K_V2)
model.eval()

# Transformation d'entrée (taille, normalisation)
preprocess = transforms.Compose([
    transforms.Resize(224),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406],
                         std=[0.229, 0.224, 0.225])
])

# Charger labels ImageNet
LABELS_URL = "https://raw.githubusercontent.com/pytorch/hub/master/imagenet_classes.txt"
with urllib.request.urlopen(LABELS_URL) as f:
    labels = [line.decode("utf-8").strip() for line in f.readlines()]

def predict_class(image_bytes):
    image = Image.open(io.BytesIO(image_bytes)).convert("RGB")
    input_tensor = preprocess(image).unsqueeze(0)  # Ajouter batch dim
    with torch.no_grad():
        outputs = model(input_tensor)
        _, predicted_idx = torch.max(outputs, 1)
    return labels[predicted_idx.item()]

print("Modèle et transformations chargés avec succès.")
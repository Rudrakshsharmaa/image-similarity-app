import torch
import torchvision.models as models
import torchvision.transforms as transforms
from PIL import Image

# Load pretrained model
model = models.resnet50(pretrained=True)
model = torch.nn.Sequential(*list(model.children())[:-1])
model.eval()

transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
])

def extract_features(image):
    image = Image.fromarray(image)
    img = transform(image).unsqueeze(0)

    with torch.no_grad():
        features = model(img)

    return features.squeeze().numpy()
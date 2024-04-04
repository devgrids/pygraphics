from pygraphics.engine.components.component import Component
import torch
import torch.nn as nn

class CNN(nn.Module):
    def __init__(self):
        super(CNN, self).__init__()
        self.conv1 = nn.Conv2d(3, 32, kernel_size=3, stride=1, padding=1)
        self.pool = nn.MaxPool2d(kernel_size=2, stride=2)
        self.conv2 = nn.Conv2d(32, 32, kernel_size=3, stride=1, padding=1)
        self.fc1 = nn.Linear(32 * 16 * 16, 128)
        self.fc2 = nn.Linear(128, 1)
        self.sigmoid = nn.Sigmoid()

    def forward(self, x):
        x = self.pool(nn.functional.relu(self.conv1(x)))
        x = self.pool(nn.functional.relu(self.conv2(x)))
        x = x.view(-1, 32 * 16 * 16)
        x = nn.functional.relu(self.fc1(x))
        x = self.sigmoid(self.fc2(x))
        return x

class ConvolutionalNeuralNetwork(Component):
    def __init__(self):
        super().__init__()
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    
    def start(self):
        pass

    def update(self):
        pass

    def render(self):
        pass

    def load_model(self, model):
        pass

    def predict(self, image_path):
        import numpy as np
        from PIL import Image
        from torchvision import transforms

        test_image_path = image_path
        test_image = Image.open(test_image_path)

        test_transform = transforms.Compose([
            transforms.Resize((64, 64)),
            transforms.ToTensor(),
            lambda x: x[:3, :, :],
            transforms.Normalize(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5])
        ])
        test_image = test_transform(test_image)
        test_image = test_image.to(self.device)

        loaded_model = CNN()
        loaded_model.load_state_dict(torch.load('deep/cat_or_dog_predict.pth'))
        loaded_model.to(self.device)

        with torch.no_grad():
            loaded_model.eval()
            result = loaded_model(test_image.unsqueeze(0))
            prediction = 'dog' if result.item() > 0.5 else 'cat'
            print(prediction)


    
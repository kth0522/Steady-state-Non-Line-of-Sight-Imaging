from torchvision.datasets import MNIST
import torchvision.transforms as transforms

data_dir = './MNIST_DATASET'

transform = transforms.Compose([
		transforms.ToTensor(),
		transforms.Normalize((0.5,), (1.0,))
])

train_dataset = MNIST(data_dir, transform=transform, train=True, download=True)
valid_dataset = MNIST(data_dir, transform=transform, train=False, download=True)
test_dataset = MNIST(data_dir, transform=transform, train=False, download=True)

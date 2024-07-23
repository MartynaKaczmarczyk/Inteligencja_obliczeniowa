from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


# Funkcja do konwersji obrazu na szarość używając średniej arytmetycznej
def convert_to_gray_mean(image):
    image_array = np.array(image)
    gray_image = np.round(np.mean(image_array, axis=2)).astype(np.uint8)
    return Image.fromarray(gray_image)


# Funkcja do konwersji obrazu na szarość używając wzorca percepcyjnego
def convert_to_gray_perceptual(image):
    image_array = np.array(image)
    gray_image = np.round(
        0.299 * image_array[:, :, 0] + 0.587 * image_array[:, :, 1] + 0.114 * image_array[:, :, 2]).astype(np.uint8)
    return Image.fromarray(gray_image)


image_paths = [
    'img1.jpg',
    'img4.jpg',
    'img3.jpg'
]

# Przetwarzamy i porównujemy wyniki
for i, img_path in enumerate(image_paths):
    img = Image.open(img_path)
    gray_mean = convert_to_gray_mean(img)
    gray_perceptual = convert_to_gray_perceptual(img)

    plt.figure(figsize=(15, 5))

    plt.subplot(1, 3, 1)
    plt.imshow(img)
    plt.title('Oryginalny obrazek')

    plt.subplot(1, 3, 2)
    plt.imshow(gray_mean, cmap='gray')
    plt.title('Średnia arytmetyczna')

    plt.subplot(1, 3, 3)
    plt.imshow(gray_perceptual, cmap='gray')
    plt.title('Wzorzec percepcyjny')

    plt.show()

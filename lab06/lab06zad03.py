import cv2
import numpy as np
import os
import matplotlib.pyplot as plt

def load_images_from_folder(folder):
    images = []
    filenames = []
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder, filename))
        if img is not None:
            images.append(img)
            filenames.append(filename)
    return images, filenames

def preprocess_image(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    return blurred

def adaptive_threshold(image):
    return cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 11, 4)

def count_birds_in_images(folder):
    images, filenames = load_images_from_folder(folder)
    results = []
    for image, filename in zip(images, filenames):
        preprocessed = preprocess_image(image)
        thresholded = adaptive_threshold(preprocessed)
        num_labels, labels_im = cv2.connectedComponents(thresholded)
        bird_count = num_labels - 1  # subtract 1 to ignore the background label
        results.append((image, filename, bird_count))
    return results

# Specify the folder containing the images
folder_path = 'bird_miniatures/bird_miniatures'
bird_counts = count_birds_in_images(folder_path)

# Display images with bird count
for image, filename, count in bird_counts:
    plt.figure(figsize=(8, 6))
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title(f'{filename}: {count} birds')
    plt.axis('off')
    plt.show()

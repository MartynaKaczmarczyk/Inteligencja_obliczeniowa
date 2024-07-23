import tensorflow as tf
from tensorflow.keras.applications import Xception
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.optimizers import Adam
import os
#
# import os
# import shutil
#
# train_dir = 'dogs-cat/train'
# cat_dir = os.path.join(train_dir, 'cats')
# dog_dir = os.path.join(train_dir, 'dogs')
#
# # Utworzenie katalogów, jeśli nie istnieją
# os.makedirs(cat_dir, exist_ok=True)
# os.makedirs(dog_dir, exist_ok=True)
#
# # Przeniesienie plików do odpowiednich katalogów
# for filename in os.listdir(train_dir):
#     file_path = os.path.join(train_dir, filename)
#     if os.path.isfile(file_path):  # Sprawdzenie, czy to plik, a nie katalog
#         if filename.startswith('cat'):
#             shutil.move(file_path, os.path.join(cat_dir, filename))
#         elif filename.startswith('dog'):
#             shutil.move(file_path, os.path.join(dog_dir, filename))


train_dir = '../dogs-cat/train'
img_size = 299  # Rozmiar obrazów dla modelu Xception
batch_size = 64

train_datagen = ImageDataGenerator(
    rescale=1.0/255.0,
    validation_split=0.2,  # Użyjemy 20% danych jako zbiór walidacyjny
)

train_generator = train_datagen.flow_from_directory(
    train_dir,
    target_size=(img_size, img_size),
    batch_size=batch_size,
    class_mode='binary',
    subset='training'
)

validation_generator = train_datagen.flow_from_directory(
    train_dir,
    target_size=(img_size, img_size),
    batch_size=batch_size,
    class_mode='binary',
    subset='validation'
)

base_model = Xception(weights='imagenet', include_top=False, input_shape=(img_size, img_size, 3))

# Dodanie własnych warstw na szczycie modelu
x = base_model.output
x = GlobalAveragePooling2D()(x)
x = Dense(1024, activation='relu')(x)
predictions = Dense(1, activation='sigmoid')(x)  # Sigmoid dla klasyfikacji binarnej

# Zbudowanie całego modelu
model = Model(inputs=base_model.input, outputs=predictions)

# Zamrożenie warstw bazowego modelu
for layer in base_model.layers:
    layer.trainable = False

# Kompilacja modelu
model.compile(optimizer=Adam(learning_rate=0.001), loss='binary_crossentropy', metrics=['accuracy'])

epochs = 1

# Przetrenowanie modelu
history = model.fit(
    train_generator,
    epochs=epochs,
    validation_data=validation_generator,
    steps_per_epoch=train_generator.samples // batch_size,
    validation_steps=validation_generator.samples // batch_size
)

# Ewaluacja modelu
val_loss, val_accuracy = model.evaluate(validation_generator, steps=validation_generator.samples // batch_size)
print(f'Validation accuracy: {val_accuracy:.2f}, Validation loss: {val_loss:.2f}')

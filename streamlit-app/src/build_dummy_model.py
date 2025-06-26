from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from tensorflow.keras.optimizers import Adam

# Example input shape (adjust based on your preprocessing)
INPUT_SHAPE = (224, 224, 3)
NUM_CLASSES = 3  # Placeholder: e.g., ['W-2', 'Paystub', 'Bank Statement']

model = Sequential([
    Conv2D(16, (3, 3), activation='relu', input_shape=INPUT_SHAPE),
    MaxPooling2D(pool_size=(2, 2)),
    Flatten(),
    Dense(64, activation='relu'),
    Dense(NUM_CLASSES, activation='softmax')
])

model.compile(optimizer=Adam(), loss='categorical_crossentropy', metrics=['accuracy'])
model.summary()

# Save the model to a file
model.save('streamlit-app/models.h5')
print("Dummy model saved to streamlit-app/models.h5")

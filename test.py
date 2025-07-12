import tensorflow as tf
import numpy as np

# Создаем простую модель
model = tf.keras.Sequential([
    tf.keras.layers.Dense(100, input_shape=(10,), activation='relu'),
    tf.keras.layers.Dense(1)
])

model.compile(optimizer='adam', loss='mse')

# Создаем тестовые данные
X = np.random.randn(1000, 10)
y = np.random.randn(1000, 1)

# Обучаем модель
print("Начинаем обучение...")
history = model.fit(X, y, epochs=100, batch_size=32)  # Уменьшил эпохи для быстрой проверки
print("Обучение завершено!")

# Правильная проверка устройства выполнения
gpu_devices = tf.config.list_physical_devices('GPU')
if gpu_devices:
    print(f"\n✅ Модель выполнена на GPU: {gpu_devices[0].name}")
    for w in model.trainable_weights:
        print(f"Вес: {w.name} -> устройство: {w.handle.device}")
else:
    print("\n❌ Модель выполнена на CPU")
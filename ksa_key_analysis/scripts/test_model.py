import numpy as np
from tensorflow.keras.models import load_model

data_dir = "data/"
results_dir = "results/"

# Загрузка данных
keys = np.load(f"{data_dir}/keys.npz")
round_keys = np.load(f"{data_dir}/round_keys.npz")

# Нормализация данных
round_keys = round_keys.astype(np.float32) / (2**64 - 1)
keys = keys.astype(np.float32) / (2**80 - 1)

# Загрузка модели
model = load_model(f"{results_dir}/model_weights.h5")

# Оценка модели
loss, accuracy = model.evaluate(round_keys, keys)

# Сохранение результатов
with open(f"{results_dir}/test_results.txt", "w") as f:
    f.write(f"Loss: {loss}\nAccuracy: {accuracy}")

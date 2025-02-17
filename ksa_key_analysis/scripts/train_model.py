import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import numpy as np
from models.ksa_model import build_ksa_model

data_dir = "data/"
results_dir = "results/"

data = np.load(f"{data_dir}/keys.npz", allow_pickle=True)
keys = data["keys"]
round_keys = data["round_keys"]

# Нормализация данных
round_keys = round_keys.astype(np.float32) / (2**64 - 1)
keys = keys.astype(np.float32) / (2**80 - 1)

# Построение модели
model = build_ksa_model()

print(f"round_keys shape: {round_keys.shape}")
print(f"keys shape: {keys.shape}")
print(f"Example round_key: {round_keys[0]}")
print(f"Example key: {keys[0]}")

# Обучение
model.fit(round_keys, keys, epochs=20, batch_size=32, validation_split=0.2)

# Сохранение весов
os.makedirs(results_dir, exist_ok=True)
model.save(f"{results_dir}/model_weights.h5")

print(f"round_keys shape: {round_keys.shape}")
print(f"keys shape: {keys.shape}")

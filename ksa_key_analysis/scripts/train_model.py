import numpy as np
from models.ksa_model import build_ksa_model

data_dir = "data/"
results_dir = "results/"

# Загрузка данных
keys = np.load(f"{data_dir}/keys.npy")
round_keys = np.load(f"{data_dir}/round_keys.npy")

# Нормализация данных
round_keys = round_keys / (2**64 - 1)
keys = keys / (2**80 - 1)

# Построение модели
model = build_ksa_model()

# Обучение
model.fit(round_keys, keys, epochs=20, batch_size=32, validation_split=0.2)

# Сохранение весов
model.save(f"{results_dir}/model_weights.h5")

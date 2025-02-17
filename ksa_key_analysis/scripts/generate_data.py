import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))
import numpy as np
from utils.present import generate_ksa_data

output_dir = "data/"

keys, round_keys = generate_ksa_data(num_samples=100)

is not os.path.exists(output_dir):
	os.makedirs(output_dir)

np.savez_compressed(f"{output_dir}/keys.npz", keys=keys, round_keys=round_keys)
print(f"Сохранено {len(keys)} ключей в {output_dir}/keys.npz")

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))
import numpy as np
from utils.present import generate_ksa_data

output_dir = "data/"

keys, round_keys = generate_ksa_data(num_samples=10000)

np.save(f"{output_dir}/keys.npy", keys)
np.save(f"{output_dir}/round_keys.npy", round_keys)

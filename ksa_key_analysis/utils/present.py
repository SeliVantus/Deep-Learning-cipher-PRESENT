import numpy as np

# S-блок шифра PRESENT
SBOX = [
	0xC, 0x5, 0x6, 0xB, 0x9, 0x0, 0xA, 0xD,
	0x3, 0xE, 0xF, 0x8, 0x4, 0x7, 0x1, 0x2
]

# Обратный S-блок
SBOX_INV = [
	0x5, 0xE, 0xF, 0x8, 0xC, 0x1, 0x2, 0xD,
	0xB, 0x4, 0x6, 0x3, 0x0, 0x7, 0x9, 0xA
]

# P-блок для перестановок
PBOX = [
	0, 16, 32, 48, 1, 17, 33, 49,
	2, 18, 34, 50, 3, 19, 35, 51,
	4, 20, 36, 52, 5, 21, 37, 53,
	6, 22, 38, 54, 7, 23, 39, 55,
	8, 24, 40, 56, 9, 25, 41, 57,
	10, 26, 42, 58, 11, 27, 43, 59,
	12, 28, 44, 60, 13, 29, 45, 61,
	14, 30, 46, 62, 15, 31, 47, 63
]

# Функция генерации раундовых ключей
def generate_round_keys(master_key):
	"""Генерация 32 раундовых ключей из мастер-ключа (80 бит)."""
	round_keys = []
	key = master_key

	for i in range(32):
		round_keys.append(key >> 16)  # Берём старшие 64 бита
		key = ((key & 0x7FFFF) << 61) | (key >> 19)  # Циклический сдвиг влево на 61
		key = (SBOX[(key >> 76) & 0xF] << 76) | (key & 0x0FFFFFFFFFFFFFFFFFFF)
		key ^= i << 15  # XOR с номером раунда
	return round_keys

# Функция шифрования PRESENT
def present_encrypt(plaintext, round_keys):
	"""Шифрование одного блока данных (64 бита)."""
	state = plaintext
	for i in range(31):  # 31 раунд
		state ^= round_keys[i]  # XOR с раундовым ключом
		state = substitute(state)  # S-блоки
		state = permute(state)  # P-блоки
		state ^= round_keys[31]  # Финальный раундовый ключ
	return state

# Замена байтов через S-блоки
def substitute(state):
	"""Применение S-блоков к состоянию."""
	new_state = 0
	for i in range(16):
		new_state |= SBOX[(state >> (i * 4)) & 0xF] << (i * 4)
	return new_state

# Перестановка через P-блоки
def permute(state):
	"""Применение P-блока к состоянию."""
	new_state = 0
	for i in range(64):
		if (state >> i) & 1:
			new_state |= 1 << PBOX[i]
	return new_state

def generate_ksa_data(num_samples=100):
	keys = np.zeros((num_samples, ), dtype=np.object_)
	round_keys = np.zeros((num_samples, 32), dtype=np.uint64)

	for i in range(num_samples):
		master_key = int.from_bytes(np.random.bytes(10), "big")
		rk = generate_round_keys(master_key)

		keys[i] = master_key
		round_keys[i] = np.array(rk, dtype=np.uint64)
	return keys, round_keys
# Функция генерации данных для анализа
#def generate_ksa_data():
#	Генерация случайных данных для анализа ключей и раундовых ключей.
#	num_rounds = 32  # Количество раундов для PRESENT
#	key_length = 80  # Длина ключа
#	data_length = 64  # Длина данных для шифрования
#
#	# Генерация случайного мастер-ключа
#	master_key = np.random.randint(0, 2**key_length, dtype=np.object_)
#
#	# Генерация раундовых ключей из мастер-ключа
#	round_keys = generate_round_keys(master_key)
#
#	# Генерация случайного блока данных для шифрования
#	plaintext = np.random.randint(0, 2**data_length, dtype=np.uint64)
#
#	# Шифрование блока данных
#	ciphertext = present_encrypt(plaintext, round_keys)
#
#	# Сохранение сгенерированных данных в файлы
#	np.save('keys.npy', master_key)
#	np.save('round_keys.npy', round_keys)
#	np.save('plaintext.npy', plaintext)
#	np.save('ciphertext.npy', ciphertext)
#
#	print("Keys, round keys, plaintext, and ciphertext generated and saved.")
    
# Если скрипт запускается напрямую, то выполняется генерация данных
if __name__ == "__main__":
	generate_ksa_data()

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout

def build_ksa_model():
	model = Sequential([
		Dense(128, input_dim=64, activation='relu'),
		Dropout(0.2),
		Dense(256, activation='relu'),
		Dropout(0.2),
		Dense(80, activation='sigmoid')
	])
	model.compile(optimizer='adam', loss='mse', metrics=['accuracy'])
	return model

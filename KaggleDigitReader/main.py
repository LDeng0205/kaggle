import numpy as np
import tensorflow as tf
import numpy as np
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.optimizers import Adam
import pandas as pd

data = pd.read_csv("digit-recognizer/train.csv")
# print(data.head())
print(type(data))
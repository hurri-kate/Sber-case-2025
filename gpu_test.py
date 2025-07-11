import tensorflow as tf
print("TF Version:", tf.__version__)
print("GPU доступен:", tf.config.list_physical_devices('GPU'))
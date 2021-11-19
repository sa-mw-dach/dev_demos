# Uncomment the following 3 lines to get rid of the INFO-level log messages
# # Disable INFO log level (1: INFO messages are not printed)
# import os
# os.environ['TF_CPP_MIN_LOG_LEVEL'] = '1' 

# Import Tensorflow and enable logging 
import tensorflow as tf
tf.debugging.set_log_device_placement(True)

# List available GPUs
gpus = tf.config.list_physical_devices('GPU')

print('Available GPUs:')
print('***************************************************')
print(gpus)

# Place tensors on the CPU
with tf.device('/CPU:0'):
    a = tf.constant([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
    b = tf.constant([[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]])

# Run on the GPU
with tf.device('/GPU:0'):
    c = tf.matmul(a, b)

print('\nResult:')
print('***************************************************')
print(c)

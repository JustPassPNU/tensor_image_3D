import tensorflow as tf
import numpy as np

print(tf.__version__)

t1 = tf.Variable([1, 2, 3])
t2 = tf.constant([1, 2, 3])

print(t1)
print(t2)

print('===')
print(type(t1))
print(type(t2))




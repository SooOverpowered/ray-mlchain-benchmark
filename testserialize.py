import numpy as np
import pickle
import time

pickle.DEFAULT_PROTOCOL = 5

total_serialize = 0
total_deserialize = 0
for i in range(300):
    temp_object = np.random.rand(7680, 4320)
    start = time.time()
    x = pickle.dumps(temp_object)
    total_serialize += time.time()-start

    start = time.time()
    temp = pickle.loads(x)
    total_deserialize += time.time()-start

print(f"serialise 300 numpy array took: {total_serialize}s")
print(f"deserialise 300 numpy array took: {total_deserialize}s")

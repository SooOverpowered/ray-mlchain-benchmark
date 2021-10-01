from mlchain.client import Client
from mlchain.base import MsgpackSerializer, MsgpackBloscSerializer
import numpy as np
import time

model = Client(api_address='localhost:5000',
               serializer='json').model(check_status=False)

total = 0
img = np.random.rand(7680, 4320)
for i in range(1):
    start = time.time()
    res = model.predict(img)
    total += time.time()-start
print(f"time taken to serialize and send one by one is: {total}")


lst = [np.random.rand(7680, 4320) for i in range(8)]
start = time.time()
res = model.predict(lst)
print(f"time taken to serialize and send 2GB is: {time.time()-start}")

# total = 0
# for i in range(300):
#     img = np.random.rand(7680, 4320)
#     serialized = MsgpackSerializer().encode(img)
#     start = time.time()
#     deserialized = MsgpackSerializer().decode(serialized)
#     total += time.time()-start


# print(f"time taken to deserialize is: {total}")

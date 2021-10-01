import numpy as np
import time
import requests
import pickle


# This is what ray/pyarrow used, but they offer custom serializers as well so we can adapt to that
pickle.DEFAULT_PROTOCOL = 5


def send_once_x300():
    temp_object = np.random.rand(7680, 4320)
    total_seconds = 0
    for i in range(300):
        temp = pickle.dumps(temp_object)
        start = time.time()
        x = requests.post("http://127.0.0.1:5000", data=temp)
        total_seconds += time.time()-start+float(x.text)
        if x.status_code == 200:
            print("sent")
        else:
            print(x)
    print(f"total time taken: {total_seconds}s")


def send_batch_2gb():
    lst = [np.random.rand(7680, 4320) for i in range(8)]  # about 2gb of data
    temp = pickle.dumps(lst)
    start = time.time()
    x = requests.post("http://127.0.0.1:5000", data=temp)
    print(f"total time taken: {time.time()-start+float(x.text)}s")


# send_once_x300()
send_batch_2gb()

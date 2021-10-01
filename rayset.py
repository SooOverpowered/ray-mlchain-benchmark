import numpy as np
import ray
import time

ray.init()

refs = []


def rayset():
    total = 0
    for i in range(300):
        start = time.time()
        refs.append(ray.put(np.random.rand(7680, 4320)))
        total += time.time()-start
    print(f"Time taken to serialize 300 ndarray: {total}")


def rayget():
    total = 0
    for ids in refs:
        start = time.time()
        temp = ray.get(ids)
        elapsed = time.time()-start
        if type(temp) == np.ndarray:
            total += elapsed
        else:
            print("Error: ray.get() returned non-ndarray")
    print(f"Time taken to deserialize 300 ndarray: {total}")


def raycombined():
    total = 0
    for i in range(300):
        objecttostore = np.random.rand(7680, 4320)
        start = time.time()
        temp = ray.get(ray.put(objecttostore))
        total += time.time()-start
    print(f"Time taken for combined workload of 300 ndarray: {total}")


def raycombined2gb():
    total = 0
    lst = []
    for i in range(8):
        lst.append(np.random.rand(7680, 4320))
    start = time.time()
    temp = ray.get(ray.put(lst))
    total += time.time()-start
    print(f"Time taken for combined workload of 300 ndarray: {total}")


# rayset()
# rayget()
# raycombined()
raycombined2gb()

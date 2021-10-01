from flask import Flask, request
import numpy as np
import pickle
import time

app = Flask(__name__)


@app.route('/', methods=["POST"])
def receive():
    start = time.time()
    temp = pickle.loads(request.data)
    total = time.time()-start
    if type(temp) == np.ndarray or type(temp) == list:
        return str(total)
    else:
        print("failed")
        return "failed"


if __name__ == "__main__":
    app.run(debug=True)

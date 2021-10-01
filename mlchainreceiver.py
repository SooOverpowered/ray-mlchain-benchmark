import cv2
import numpy as np
from mlchain.base import ServeModel
from mlchain.client import Client


class Model():
    def predict(self, data):
        return "received"


# Define model
model = Model()

# Serve model
serve_model = ServeModel(model)

# Deploy model
if __name__ == '__main__':
    from mlchain.server import FlaskServer
    # Run flask model with upto 12 threads
    FlaskServer(serve_model).run(port=5000, threads=12)

import logging
from concurrent.futures import ThreadPoolExecutor
from math import sin, cos

import grpc
import numpy as np

from rawdata_pb2 import TransformResponse
from rawdata_pb2_grpc import RawDataServicer, add_RawDataServicer_to_server


class RawDataServer(RawDataServicer):
    def Transform(self, request, context):
        r_matrix = np.array(((cos(request.radian), -sin(request.radian)),
                             (sin(request.radian), cos(request.radian))))
        out = []
        for i in range(0, len(request.rawCoordinates)):
            vector = np.array((request.rawCoordinates[i].x, -request.rawCoordinates[i].y))
            vector_rotated = r_matrix.dot(vector)
            vector_as_list = vector_rotated.tolist()
            out.append({"x": vector_as_list[0], "y": vector_as_list[1]})
        resp = TransformResponse(transformedCoordinates=out)
        return resp


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )
    server = grpc.server(ThreadPoolExecutor())
    add_RawDataServicer_to_server(RawDataServer(), server)
    port = 3010
    server.add_insecure_port(f'[::]:{port}')
    server.start()
    logging.info("server ready on port %r", port)
    server.wait_for_termination()
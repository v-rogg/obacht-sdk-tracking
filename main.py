import logging
from concurrent.futures import ThreadPoolExecutor
from math import sin, cos

import grpc
import matplotlib.path as mpltPath
from sklearn.cluster import DBSCAN
import numpy as np

from rawdata_pb2 import TransformResponse, TrackResponse
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

    def TrackPersons(self, request, context):
        # print(request.scans)
        # print(request.zones)

        out = []

        scan_dict = {}
        zone_dict = {}

        for i in range(0, len(request.scans)):
            scan_points = []
            for j in range(0, len(request.scans[i].scanPoints)):
                scan_points.append([request.scans[i].scanPoints[j].x, request.scans[i].scanPoints[j].y])
            scan_dict[request.scans[i].address] = scan_points

        for i in range(0, len(request.zones)):
            zone_points = []
            for j in range(0, len(request.zones[i].zoneObjectCoordinates)):
                zone_points.append([request.zones[i].zoneObjectCoordinates[j].x, request.zones[i].zoneObjectCoordinates[j].y])
            zone_dict[request.zones[i].address] = zone_points

        combined_scan_points = []

        for key in scan_dict:
            if key in zone_dict:
                # Do something
                path = mpltPath.Path(zone_dict[key])
                inside = path.contains_points(scan_dict[key])
                # print(inside)

                for i, scanCoordinate in enumerate(scan_dict[key]):
                    if inside[i]:
                        combined_scan_points.append(scanCoordinate)

            else:
                for scanCoordinate in scan_dict[key]:
                    combined_scan_points.append(scanCoordinate)

        if len(combined_scan_points) > 0:
            x = np.array(combined_scan_points)
            clustering = DBSCAN(eps=100, min_samples=2).fit(x)

            clustered_dict = {}

            for i, label in enumerate(clustering.labels_.tolist()):
                if label in clustered_dict:
                    temp = clustered_dict[label]
                    temp.append(combined_scan_points[i])
                    clustered_dict[label] = temp
                else:
                    clustered_dict[label] = [combined_scan_points[i]]

            for values in clustered_dict.values():
                x = [p[0] for p in values]
                y = [p[1] for p in values]
                centroid = (sum(x) / len(values), sum(y) / len(values))
                out.append({"x": centroid[0], "y": centroid[1]})

        resp = TrackResponse(persons=out)
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
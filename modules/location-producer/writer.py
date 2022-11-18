import grpc
import location_pb2
import location_pb2_grpc

"""
Sample implementation of a writer that can be used to write messages to gRPC.
"""

print("Sending sample payload...")

channel = grpc.insecure_channel("localhost:5005")
stub = location_pb2_grpc.LocationServiceStub(channel)

# Update this with desired payload
location = location_pb2.LocationMessage(
    person_id=1,
    latitude='-420.6908829999',
    longitude='69.553629999',
    created_at='2022-11-18T12:00:00'
)


response = stub.Create(location)

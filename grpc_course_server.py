import grpc
from concurrent import futures
import course_service_pb2
import course_service_pb2_grpc

class CourseServiceServicer(course_service_pb2_grpc.CourseServiceServicer):
    def GetCourse(self, request, context):
        requested_course_id = request.course_id
        response = course_service_pb2.GetCourseResponse(
            course_id=requested_course_id,
            title="Автотесты API",
            description="Будем изучать написание API автотестов"
        )
        print(f"Received request for course ID: {requested_course_id}. Sending response.")
        return response


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    course_service_pb2_grpc.add_CourseServiceServicer_to_server(CourseServiceServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("gRPC сервер запушен на порту 50051...")
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
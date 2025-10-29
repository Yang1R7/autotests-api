from clients.courses.course_schema import CreateCourseRequestSchema
from clients.courses.courses_client import get_courses_client
from clients.exercises.exercises_client import get_exercise_client
from clients.exercises.exercises_schema import CreateExerciseRequestSchema
from clients.files.files_client import get_files_client
from clients.files.files_schema import CreateFileRequestSchema

from clients.private_http_builder import AuthenticationUserSchema
from clients.users.public_users_client import get_public_users_client
from clients.users.users_schema import CreateUserRequestSchema
from tools.fakers import get_random_email

public_user_client = get_public_users_client()

create_user_request = CreateUserRequestSchema(
    email=get_random_email(),
    password="test123",
    lastName="Max",
    firstName="Max",
    middleName="Max"
)
create_user_response = public_user_client.create_user(request=create_user_request)

authentication_user = AuthenticationUserSchema(
    email=create_user_request.email,
    password=create_user_request.password
)

files_client = get_files_client(user=authentication_user)
course_client = get_courses_client(user=authentication_user)

create_file_request = CreateFileRequestSchema(
    filename="image.png",
    directory="courses",
    upload_file="./testdata/files/image.png"
)

create_file_response = files_client.create_file(request=create_file_request)
print("Create file data:", create_file_response)

create_course_request = CreateCourseRequestSchema(
    title="Python",
    maxScore=100,
    minScore=10,
    description="Python API course",
    estimatedTime="2 weeks",
    previewFileId=create_file_response.file.id,
    createdByUserId=create_user_response.user.id
)
create_course_response = course_client.create_course(request=create_course_request)
print("Create course data:", create_course_response)

create_exercise_request = CreateExerciseRequestSchema(
    title="Home work 1",
    courseId=create_course_response.course.id,
    maxScore=10,
    minScore=5,
    orderIndex=1,
    description="HTTXP task",
    estimatedTime="1 day"
)

exercise_client = get_exercise_client(user=authentication_user)
create_exercise_response = exercise_client.create_exercise(request=create_exercise_request)
print("Create exercise data:", create_exercise_response)

import pytest
from pydantic import BaseModel

from clients.courses.course_schema import CreateCourseRequestSchema
from clients.exercises.exercises_client import get_exercise_client, CreateExerciseResponseSchema, \
    CreateExerciseRequestSchema, ExercisesClient
from fixtures.courses import CoursesFixture

from fixtures.users import UserFixture


class ExerciseFixture(BaseModel):
    request: CreateExerciseRequestSchema
    response: CreateExerciseResponseSchema


@pytest.fixture
def exercises_client(function_user: UserFixture) -> ExercisesClient:
    return get_exercise_client(user=function_user.authentication_user)


@pytest.fixture
def function_exercise(
        exercises_client: ExercisesClient,
        function_courses: CoursesFixture
) -> ExerciseFixture:

    request = CreateExerciseRequestSchema(courseId=function_courses.response.course.id)
    response = exercises_client.create_exercise(request=request)
    return ExerciseFixture(request=request, response=response)

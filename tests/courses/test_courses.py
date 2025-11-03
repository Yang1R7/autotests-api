from http import HTTPStatus

import pytest

from clients.courses.course_schema import UpdateCourseRequestSchema, UpdateCourseResponseSchema, GetCoursesQuerySchema, \
    GetCoursesResponseSchema, CreateCourseRequestSchema, CreateCourseResponseSchema
from clients.courses.courses_client import CoursesClient
from fixtures.courses import CoursesFixture
from fixtures.files import FileFixture
from fixtures.users import function_user, UserFixture
from tools.assertions.base import assert_status_code
from tools.assertions.courses import assert_update_course_response, assert_get_courses_response, \
    assert_create_course_response
from tools.assertions.schema import validate_json_schema


@pytest.mark.courses
@pytest.mark.regression
class TestCourses:
    def test_get_courses(
            self,
            courses_client: CoursesClient,
            function_user: UserFixture,
            function_courses: CoursesFixture
    ):
        query = GetCoursesQuerySchema(userId=function_user.response.user.id)
        response = courses_client.get_courses_api(query=query)
        response_data = GetCoursesResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_get_courses_response(get_courses_response=response_data,
                                    create_course_response=[function_courses.response])

        validate_json_schema(instance=response.json(), schema=response_data.model_json_schema())

    def test_update_course(self, courses_client: CoursesClient, function_courses: CoursesFixture):
        request = UpdateCourseRequestSchema()
        response = courses_client.update_course_api(function_courses.response.course.id, request=request)
        response_data = UpdateCourseResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_update_course_response(request=request, response=response_data)

        validate_json_schema(instance=response.json(), schema=response_data.model_json_schema())

    def test_create_course(self, courses_client: CoursesClient, function_file: FileFixture, function_user: UserFixture):
        request = CreateCourseRequestSchema(previewFileId=function_file.response.file.id,
                                            createdByUserId=function_user.response.user.id)
        response = courses_client.create_course_api(request=request)
        response_data = CreateCourseResponseSchema.model_validate_json(response.text)
        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_create_course_response(actual=response_data, expected=request)
        validate_json_schema(instance=response.json(), schema=response_data.model_json_schema())

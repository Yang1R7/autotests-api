from clients.courses.course_schema import UpdateCourseResponseSchema, UpdateCourseRequestSchema, CourseSchema, \
    GetCoursesResponseSchema, CreateCourseResponseSchema, CreateCourseRequestSchema
from tools.assertions.base import assert_equal, assert_length
from tools.assertions.files import assert_file
from tools.assertions.users import assert_user


def assert_update_course_response(
        request: UpdateCourseRequestSchema,
        response: UpdateCourseResponseSchema):
    """
    Проверяет, что ответ на обновление курса соответствует данным из запроса.

    :param request: Исходный запрос на обновление курса.
    :param response: Ответ API с обновленными данными курса.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    assert_equal(actual=response.course.title, expected=request.title, name="title")
    assert_equal(actual=response.course.max_score, expected=request.max_score, name="max_score")
    assert_equal(actual=response.course.min_score, expected=request.min_score, name="min_score")
    assert_equal(actual=response.course.description, expected=request.description, name="description")
    assert_equal(actual=response.course.estimated_time, expected=request.estimated_time, name="estimated_time")


def assert_courses(actual: CourseSchema, expected:CourseSchema):
    """
    Проверяет, что фактические данные курса соответствуют ожидаемым.

    :param actual: Фактические данные курса.
    :param expected: Ожидаемые данные курса.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    assert_equal(actual.id, expected.id, "id")
    assert_equal(actual.title, expected.title, "title")
    assert_equal(actual.max_score, expected.max_score, "max_score")
    assert_equal(actual.max_score, expected.max_score, "max_score")
    assert_equal(actual.description, expected.description, "description")
    assert_equal(actual.estimated_time, expected.estimated_time, "estimated_time")

    # Проверяем вложенные сущности
    assert_file(actual.preview_file, expected.preview_file)
    assert_user(actual.created_by_user, expected.created_by_user)





def assert_get_courses_response(
        get_courses_response: GetCoursesResponseSchema,
        create_course_response: list[CreateCourseResponseSchema]
):
    """
        Проверяет, что ответ на получение списка курсов соответствует ответам на их создание.

        :param get_courses_response: Ответ API при запросе списка курсов.
        :param create_course_response: Список API ответов при создании курсов.
        :raises AssertionError: Если данные курсов не совпадают.
        """
    assert_length(get_courses_response.courses, create_course_response, "courses")
    for index, create_course_response in enumerate(create_course_response):
        assert_courses(get_courses_response.courses[index], create_course_response.course)


def assert_create_course_response(actual: CreateCourseResponseSchema, expected:CreateCourseRequestSchema):
    """
    Проверяет, что ответ на создание курса соответствует данным из запроса.
    :param actual: Исходный запрос на создание курса.
    :param expected: Ответ API с созданным курсом.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    assert_equal(actual.course.title, expected.title, "title")
    assert_equal(actual.course.max_score, expected.max_score, "max_score")
    assert_equal(actual.course.min_score, expected.min_score, "min_score")
    assert_equal(actual.course.description, expected.description, "description")
    assert_equal(actual.course.estimated_time, expected.estimated_time, "estimated_time")
    # Проверяем соответствие preview_file_id
    assert_equal(actual.course.preview_file.id,expected.preview_file_id, "preview_file_id")
    # Проверяем соответствие created_by_user_id
    assert_equal(actual.course.created_by_user.id,expected.created_by_user_id, "created_by_user_id")



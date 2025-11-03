from clients.errors_schema import InternalErrorResponseSchema
from clients.exercises.exercises_schema import CreateExerciseRequestSchema, CreateExerciseResponseSchema, \
    ExercisesSchema, GetExerciseResponseSchema, UpdateExerciseResponseSchema, UpdateExerciseRequestSchema, \
    GetExercisesResponseSchema
from tools.assertions.base import assert_equal, assert_length
from tools.assertions.errors import assert_internal_error_response


def assert_create_exercise_response(
        actual: CreateExerciseResponseSchema,
        expected: CreateExerciseRequestSchema
):
    """
    Проверяет, что ответ на создание задания соответствует данным из запроса.
    :param actual: Ответ API с созданным заданием.
    :param expected: Исходный запрос на создание задания
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    assert_equal(actual.exercise.title, expected.title, "title")
    assert_equal(actual.exercise.course_id, expected.course_id, "course_id")
    assert_equal(actual.exercise.max_score, expected.max_score, "max_score")
    assert_equal(actual.exercise.min_score, expected.min_score, "min_score")
    assert_equal(actual.exercise.order_index, expected.order_index, "order_index")
    assert_equal(actual.exercise.description, expected.description, "description")
    assert_equal(actual.exercise.estimated_time, expected.estimated_time, "estimated_time")


def assert_exercise(
        actual: ExercisesSchema,
        expected: ExercisesSchema
):
    """
    Проверяет, что фактические данные задания соответствуют ожидаемым.

    :param actual: Фактические данные задания.
    :param expected: Ожидаемые данные задания.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    assert_equal(actual.id, expected.id, "id")
    assert_equal(actual.title, expected.title, "title")
    assert_equal(actual.course_id, expected.course_id, "course_id")
    assert_equal(actual.max_score, expected.max_score, "max_score")
    assert_equal(actual.min_score, expected.min_score, "min_score")
    assert_equal(actual.order_index, expected.order_index, "order_index")
    assert_equal(actual.description, expected.description, "description")
    assert_equal(actual.estimated_time, expected.estimated_time, "estimated_time")


def assert_get_exercise_response(
        get_exercise_response: GetExerciseResponseSchema,
        create_exercise_response: CreateExerciseResponseSchema
):
    """
    Проверяет, что ответ на получение задания соответствует ответу на его создание.

    :param get_exercise_response: Ответ API при запросе данных задания.
    :param create_exercise_response: Ответ API при создании задания.
    :raises AssertionError: Если данные задания не совпадают.
    """
    assert_exercise(actual=get_exercise_response.exercise, expected=create_exercise_response.exercise)


def assert_update_exercise_response(
        actual: UpdateExerciseResponseSchema,
        expected:UpdateExerciseRequestSchema
):
    """
        Проверяет, что ответ на обновление задания соответствует запросу.

        :param expected: Исходный запрос на обновление задания.
        :param actual: Ответ API с данными задания.
        :raises AssertionError: Если хотя бы одно поле не совпадает.
        """
    assert_equal(actual.exercise.title, expected.title,"title")
    assert_equal(actual.exercise.max_score, expected.max_score, "max_score")
    assert_equal(actual.exercise.min_score, expected.min_score, "min_score")
    assert_equal(actual.exercise.order_index, expected.order_index, "order_index")
    assert_equal(actual.exercise.description, expected.description, "description")
    assert_equal(actual.exercise.estimated_time, expected.estimated_time, "estimated_time")

def assert_exercise_not_found_response(actual: InternalErrorResponseSchema):
    """
    Функция для проверки ошибки, если задание не найдено на сервере.

    :param actual: Фактический ответ.
    :raises AssertionError: Если фактический ответ не соответствует ошибке "Exercise not found"
    """
    expected = InternalErrorResponseSchema(details="Exercise not found")
    assert_internal_error_response(actual=actual, expected=expected)


def assert_get_exercises_response(
        get_exercises_response: GetExercisesResponseSchema,
        create_exercise_response: list[CreateExerciseResponseSchema]
):
    """
       Проверяет, что ответ на получение списка заданий соответствует ответам на их создание.

       :param get_exercises_response: Ответ API при запросе списка заданий.
       :param create_exercise_response: Список API ответов при создании заданий.
       :raises AssertionError: Если данные заданий не совпадают.
       """
    assert_length(actual=get_exercises_response.exercises, expected=create_exercise_response, name="exercises")
    for index, create_exercise_response_item in enumerate(create_exercise_response):
        assert_exercise(get_exercises_response.exercises[index], create_exercise_response_item.exercise)


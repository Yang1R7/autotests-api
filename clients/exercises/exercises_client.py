import httpx
from typing import TypedDict

from httpx import Response

from clients.api_client import APIClient
from clients.private_http_builder import AuthenticationUserSchema, get_private_http_client

from clients.exercises.exercises_schema import (GetExercisesQuerySchema, GetExerciseResponseSchema
, GetExercisesResponseSchema, CreateExerciseRequestSchema, CreateExerciseResponseSchema, UpdateExerciseRequestSchema,
                                                UpdateExerciseResponseSchema)


class ExercisesClient(APIClient):
    """
    Клиент для работы с /api/v1/exercises
    """
    def get_exercises_api(self,query: GetExercisesQuerySchema) -> Response:
        """
    Метод получения всех упражнений курса.
    :query param: Словарь с courseid.
    :return: Ответ от сервера в виде объекта httpx.Response
    """
        return self.get("/api/v1/exercises",params=query.model_dump(by_alias=True))

    def get_exercise_api(self, exercise_id: str) -> Response:
        """
    Метод получения упражнения по exercise_id из курса.
    :path param: Словарь с  идентификатор  упражнения exercise_id.
    :return: Ответ от сервера в виде объекта httpx.Response
    """
        return self.get(f"/api/v1/exercises/{exercise_id}")

    def create_exercise_api(self, request: CreateExerciseRequestSchema) -> Response:
        """
    Метод создания упражнения курса.
    :param : request: Словарь с, title, courseId, maxScore, minScore ,orderIndex, description ,estimatedTime
    :return: Ответ от сервера в виде объекта httpx.Response
    """
        return self.post('/api/v1/exercises',json=request.model_dump(by_alias=True))

    def update_exercise_api(self,exercise_id: str, request:UpdateExerciseRequestSchema) -> Response:
        """
    Метод обновления упражнения курса по идентификатору  упражнения exercise_id.
    :param: request: Словарь с, title, maxScore, minScore ,orderIndex, description ,estimatedTime,
    :path param: exercise_id идентификатор упражнения
    :return: Ответ от сервера в виде объекта httpx.Response
    """
        return self.patch(f"/api/v1/exercises/{exercise_id}", json=request.model_dump(by_alias=True))

    def delete_exercise_api(self, exercise_id: str) -> Response:
        """
    Метод удаления упражнения курса по идентификатору  упражнения exercise_id .
    :param: Словарь с path параметром идентификатору упражнения exercise_id.
    :return: Ответ от сервера в виде объекта httpx.Response
    """
        return self.delete(f"/api/v1/exercises/{exercise_id}")

    def get_exercises(self,query: GetExercisesQuerySchema) -> GetExercisesResponseSchema:
        response = self.get_exercises_api(query=query)
        return GetExercisesResponseSchema.model_validate_json(response.text)

    def get_exercise(self,exercise_id: str) -> GetExerciseResponseSchema:
        response = self.get_exercise_api(exercise_id=exercise_id)
        return GetExerciseResponseSchema.model_validate_json(response.text)

    def create_exercise(self, request: CreateExerciseRequestSchema) -> CreateExerciseResponseSchema:
        response = self.create_exercise_api(request=request)
        return CreateExerciseResponseSchema.model_validate_json(response.text)

    def update_exercise(self,exercise_id: str, request:UpdateExerciseRequestSchema) -> UpdateExerciseResponseSchema:
        response = self.update_exercise_api(exercise_id=exercise_id, request=request)
        return UpdateExerciseResponseSchema.model_validate_json(response.text)


def get_exercise_client(user:AuthenticationUserSchema) -> ExercisesClient:
    """
    Функция создаёт экземпляр ExercisesClient с уже настроенным HTTP-клиентом.
    :return: Готовый к использованию ExercisesClient.
    """
    return ExercisesClient(client=get_private_http_client(user=user))
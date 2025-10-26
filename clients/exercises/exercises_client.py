import httpx
from typing import TypedDict

from httpx import Response

from clients.api_client import APIClient


class GetExercisesDict(TypedDict):
    """
    Описание структуры квери параметров для получение упражнений.
    """
    courseid : str


class CreateExerciseDict(TypedDict):
    """
    Описание структуры запроса для создания упражнения.
    """
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str


class UpdateExerciseDict(TypedDict):
    """
     Описание структуры запроса для апдейта упражнения.
     """
    title: str | None
    maxScore: int | None
    minScore: int | None
    orderIndex: int | None
    description: str | None
    estimatedTime: str | None

class ExercisesClient(APIClient):
    """
    Клиент для работы с /api/v1/exercises
    """
    def get_exercises_api(self,query: GetExercisesDict) -> Response:
        """
    Метод получения всех упражнений курса.
    :query param: Словарь с courseid.
    :return: Ответ от сервера в виде объекта httpx.Response
    """
        return self.get("/api/v1/exercises",params=query)

    def get_exercise_api(self, exercise_id: str) -> Response:
        """
    Метод получения упражнения по exercise_id из курса.
    :path param: Словарь с  идентификатор  упражнения exercise_id.
    :return: Ответ от сервера в виде объекта httpx.Response
    """
        return self.get(f"/api/v1/exercises{exercise_id}")

    def create_exercise_api(self, request: CreateExerciseDict) -> Response:
        """
    Метод создания упражнения курса.
    :param : request: Словарь с, title, courseId, maxScore, minScore ,orderIndex, description ,estimatedTime
    :return: Ответ от сервера в виде объекта httpx.Response
    """
        return self.post('/api/v1/exercises',json=request)

    def update_exercise_api(self,exercise_id: str, request:UpdateExerciseDict) -> Response:
        """
    Метод обновления упражнения курса по идентификатору  упражнения exercise_id.
    :param: request: Словарь с, title, maxScore, minScore ,orderIndex, description ,estimatedTime,
    :path param: exercise_id идентификатор упражнения
    :return: Ответ от сервера в виде объекта httpx.Response
    """
        return self.patch(f"/api/v1/exercises/{exercise_id}", json=request)

    def delete_exercise_api(self, exercise_id: str) -> Response:
        """
    Метод удаления упражнения курса по идентификатору  упражнения exercise_id .
    :param: Словарь с path параметром идентификатору упражнения exercise_id.
    :return: Ответ от сервера в виде объекта httpx.Response
    """
        return self.patch(f"/api/v1/exercises/{exercise_id}")

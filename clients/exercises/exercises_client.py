import httpx
from typing import TypedDict

from httpx import Response

from clients.api_client import APIClient
from clients.private_http_builder import AuthenticationUserDict, get_private_http_client


class Exercises(TypedDict):
    """
    Описание упражнений курса.
    """
    id: str
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str

class GetExercisesResponseDict(TypedDict):
    """
    Описание структуры ответа упражнений курса.
    """
    exercises: list[Exercises]

class GetExerciseResponseDict(TypedDict):
    """
    Описание структуры ответа конкретного упражнения курса.
    """
    exercises: Exercises

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

class CreateExerciseResponseDict(TypedDict):
    """
    Описание структуры ответа создания упражнения.
    """
    exercise: Exercises

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

class UpdateExerciseResponseDict(TypedDict):
    exercise: Exercises

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

    def get_exercises(self,query: GetExercisesDict) -> GetExercisesResponseDict:
        response = self.get_exercises_api(query=query)
        return response.json()

    def get_exercise(self,exercise_id: str) -> GetExerciseResponseDict:
        response = self.get_exercise_api(exercise_id=exercise_id)
        return response.json()

    def create_exercise(self, request: CreateExerciseDict) -> CreateExerciseResponseDict:
        response = self.create_exercise_api(request=request)
        return response.json()

    def update_exercise(self,exercise_id: str, request:UpdateExerciseDict) -> UpdateExerciseResponseDict:
        response = self.update_exercise_api(exercise_id=exercise_id, request=request)
        return response.json()


def get_exercise_client(user:AuthenticationUserDict) -> ExercisesClient:
    """
    Функция создаёт экземпляр ExercisesClient с уже настроенным HTTP-клиентом.
    :return: Готовый к использованию ExercisesClient.
    """
    return ExercisesClient(client=get_private_http_client(user=user))
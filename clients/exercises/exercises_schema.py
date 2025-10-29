from pydantic import BaseModel, Field, ConfigDict


class ExercisesSchema(BaseModel):
    """
    Описание упражнений курса.
    """
    model_config = ConfigDict(populate_by_name=True)

    id: str
    title: str
    courseId: str
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    order_index: int = Field(alias="orderIndex")
    description: str
    estimated_time: str = Field(alias="estimatedTime")


class GetExercisesResponseSchema(BaseModel):
    """
    Описание структуры ответа упражнений курса.
    """
    exercises: list[ExercisesSchema]


class GetExerciseResponseSchema(BaseModel):
    """
    Описание структуры ответа конкретного упражнения курса.
    """
    exercises: ExercisesSchema


class GetExercisesSchema(BaseModel):
    """
    Описание структуры квери параметров для получение упражнений.
    """
    courseid: str


class CreateExerciseRequestSchema(BaseModel):
    """
    Описание структуры запроса для создания упражнения.
    """
    model_config = ConfigDict(populate_by_name=True)

    title: str
    courseId: str
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    order_index: int = Field(alias="orderIndex")
    description: str
    estimated_time: str = Field(alias="estimatedTime")


class CreateExerciseResponseSchema(BaseModel):
    """
    Описание структуры ответа создания упражнения.
    """
    exercise: ExercisesSchema


class UpdateExerciseRequestSchema(BaseModel):
    """
     Описание структуры запроса для апдейта упражнения.
     """
    model_config = ConfigDict(populate_by_name=True)

    title: str | None
    max_score: int | None = Field(alias="maxScore")
    min_score: int | None = Field(alias="minScore")
    order_index: int | None = Field(alias="orderIndex")
    description: str | None
    estimated_time: str | None = Field(alias="estimatedTime")


class UpdateExerciseResponseSchema(BaseModel):
    exercise: ExercisesSchema

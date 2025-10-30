from pydantic import BaseModel, Field, ConfigDict

from tools.fakers import fake


class ExercisesSchema(BaseModel):
    """
    Описание упражнений курса.
    """
    model_config = ConfigDict(populate_by_name=True)

    id: str
    title: str
    course_id: str = Field(alias="courseId")
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

    title: str = Field(default_factory=fake.sentence)
    course_id: str = Field(alias="courseId", default_factory=fake.uuid4)
    max_score: int = Field(alias="maxScore", default_factory=fake.max_score)
    min_score: int = Field(alias="minScore", default_factory=fake.min_score)
    order_index: int = Field(alias="orderIndex", default_factory=lambda: fake.integer(1, 100))
    description: str = Field(default_factory=fake.text)
    estimated_time: str = Field(alias="estimatedTime", default_factory=fake.estimated_time)


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

    title: str | None = Field(default_factory=fake.sentence)
    max_score: int | None = Field(alias="maxScore", default_factory=fake.max_score)
    min_score: int | None = Field(alias="minScore", default_factory=fake.min_score)
    order_index: int = Field(alias="orderIndex", default_factory=lambda: fake.integer(1, 100))
    description: str | None = Field(default_factory=fake.text)
    estimated_time: str | None = Field(alias="estimatedTime", default_factory=fake.estimated_time)


class UpdateExerciseResponseSchema(BaseModel):
    exercise: ExercisesSchema

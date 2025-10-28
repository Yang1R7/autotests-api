from pydantic import BaseModel, Field, ConfigDict, computed_field, HttpUrl, EmailStr, ValidationError
from pydantic.alias_generators import to_camel
import uuid


# {
#   "course": {
#     "id": "string",
#     "title": "string",
#     "maxScore": 0,
#     "minScore": 0,
#     "description": "string",
#     "previewFile": {
#       "id": "string",
#       "filename": "string",
#       "directory": "string",
#       "url": "https://example.com/"
#     },
#     "estimatedTime": "string",
#     "createdByUser": {
#       "id": "string",
#       "email": "user@example.com",
#       "lastName": "string",
#       "firstName": "string",
#       "middleName": "string"
#     }
#   }
# }


class FileSchema(BaseModel):
    id: str
    filename: str
    directory: str
    url: HttpUrl


class UserSchema(BaseModel):
    id: str
    email: EmailStr
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")

    @computed_field()
    def username(self) -> str:
        return f"{self.first_name} {self.last_name}"

    def get_username(self):
        return f"{self.first_name} {self.last_name}"


class CourseSchema(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)

    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    title: str = "Max"
    max_score: int = Field(alias="maxScore", default=111)
    min_score: int = Field(alias="minScore", default=111)
    description: str = "Max"
    preview_file: FileSchema = Field(alias="previewFile")
    estimated_time: str = Field(alias="estimatedTime", default="Max")
    created_by_user: UserSchema = Field(alias="createdByUser")


course_default_model = CourseSchema(
    id="course_id",
    title="Playwright",
    maxScore=10,
    minScore=5,
    description="Playwright",
    previewFile=FileSchema(
        id="Max",
        filename="Max",
        directory="Max",
        url="http://google.com"
    ),
    estimatedTime="1 week",
    createdByUser=UserSchema(id="Maxim", email="maxim_single@example.com", lastName="Maxim", firstName="Maxim", middleName="Maxim")
)
print(course_default_model)

course_dict = {
    "id": "course_id",
    "title": "Playwright",
    "maxScore": 10,
    "minScore": 5,
    "description": "Playwright",
    "previewFile": {
        "id": "Max",
        "filename": "Max",
        "directory": "Max",
        "url": "http://google.com"
    },
    "estimatedTime": "1 week",
    "createdByUser": {
        "id": "Maxim",
        "email": "maxim_single@example.com",
        "lastName": "Maxim",
        "firstName": "Maxim",
        "middleName": "Maxim"
    }
}

# course_dict_model = CourseSchema(**course_dict)
# print(course_dict_model)

course_json = """
{
    "id": "course_id",
    "title": "Playwright",
    "maxScore": 10,
    "minScore": 5,
    "description": "Playwright",
    "previewFile": {
        "id": "Max",
        "filename": "Max",
        "directory": "Max",
        "url": "http://google.com"
    },
    "estimatedTime": "1 week",
    "createdByUser": {
        "id": "Maxim",
        "email": "maxim_single@example.com",
        "lastName": "Maxim",
        "firstName": "Maxim",
        "middleName": "Maxim"
    }
}
"""

course_json_model = CourseSchema.model_validate_json(course_json)
print(course_json_model)
# print(course_json_model.model_dump())
print(course_json_model.model_validate_json(by_alias=True))
user = UserSchema(id="11",email="maxim_single@example.com", lastName="Maxim", firstName="Maxim", middleName="Maxim")
print(user.get_username(), user.username)
try:
    file = FileSchema(
            id="Max",
            filename="Max",
            directory="Max",
            url="http//googlecom"
        )
except ValidationError as error:
    print(error)
    print(error.errors())


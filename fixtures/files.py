from clients.files.files_client import get_files_client, FilesClient
from fixtures.users import UserFixture
from clients.files.files_schema import CreateFileRequestSchema, CreateFileResponseSchema
import pytest
from pydantic import BaseModel


class FileFixture(BaseModel):
    request: CreateFileRequestSchema
    response: CreateFileResponseSchema


@pytest.fixture
def files_client(function_user: UserFixture) -> FilesClient:
    return get_files_client(function_user.authentication_user)


def function_file(files_client: FilesClient) -> FileFixture:
    request = CreateFileRequestSchema(upload_file="./testdata/files/image.png")
    response = files_client.create_file(request)
    return FileFixture(request=request, response=response)

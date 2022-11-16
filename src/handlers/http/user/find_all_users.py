import os
from src.domain.use_cases.FindAllUsers import FindAllUsers
from src.infra.repositories.Boto3UserResourceRepository import Boto3UserResourceRepository
from src.utils.json_response import json_response


def handler(event, context):
    repository = Boto3UserResourceRepository(os.environ["DYNAMODB_TABLE"])
    use_case = FindAllUsers(repository)
    users = use_case.execute()

    return json_response(users)

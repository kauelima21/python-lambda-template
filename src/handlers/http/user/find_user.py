from src.domain.use_cases.FindUser import FindUser
from src.infra.repositories.Boto3UserResourceRepository import Boto3UserResourceRepository
from src.utils.json_response import json_response


def handler(event, context):
    user_id = event['pathParameters']['user_id']
    repository = Boto3UserResourceRepository()
    use_case = FindUser(repository)
    user = use_case.execute(user_id)

    if not user:
        return json_response({
            "message": "There is no user with the specified user_id"
        }, 400)

    return json_response(user)

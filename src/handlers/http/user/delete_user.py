from src.domain.use_cases.DeleteUser import DeleteUser
from src.infra.repositories.Boto3UserResourceRepository import Boto3UserResourceRepository
from src.utils.json_response import json_response


def handler(event, context):
    user_id = event['pathParameters']['user_id']
    repository = Boto3UserResourceRepository()
    use_case = DeleteUser(repository)
    use_case.execute(user_id)

    return json_response({
        "message": "User deleted successfully"
    })

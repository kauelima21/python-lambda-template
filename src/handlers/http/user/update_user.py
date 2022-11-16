import os
import json
from src.utils.json_response import json_response
from src.domain.use_cases.UpdateUser import UpdateUser
from src.infra.repositories.Boto3UserResourceRepository import Boto3UserResourceRepository


def handler(event, context):
    data = json.loads(event["body"])
    user_id = event["pathParameters"]["user_id"]
    repository = Boto3UserResourceRepository(os.environ["DYNAMODB_TABLE"])
    use_case = UpdateUser(repository)
    user = use_case.execute(user_id, {
        "first_name": data["first_name"],
        "last_name": data["last_name"],
        "email": data["email"],
        "genre": data["genre"],
    })

    return json_response({
        "UpdatedUserData": user
    })

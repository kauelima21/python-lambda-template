import json
from src.utils.json_response import json_response
from src.domain.use_cases.CreateUser import CreateUser
from src.infra.repositories.Boto3UserResourceRepository import Boto3UserResourceRepository


def handler(event, context):
    data = json.loads(event["body"])
    repository = Boto3UserResourceRepository()
    use_case = CreateUser(repository)
    user = use_case.execute({
        "first_name": data["first_name"],
        "last_name": data["last_name"],
        "email": data["email"],
        "genre": data["genre"],
    })

    return json_response({
        "message": f"user {user.first_name} successfully created."
    }, 201)

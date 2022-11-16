def json_response(body: dict, status_code: int = 200) -> dict:
    return {
        "statusCode": status_code,
        "body": body,
        "headers": {
            "Access-Control-Allow-Origin": "*",
            "Content-Type": "application/json"
        }
    }

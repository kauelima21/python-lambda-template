import os
import boto3
from datetime import datetime
from src.domain.entities import User
from botocore.exceptions import ClientError
from src.domain.repositories.UserRepository import UserRepository


class Boto3UserResourceRepository(UserRepository):
    def __init__(self, table_name: str, primary: str = "id"):
        super().__init__()
        self._primary = primary
        self._table_name = table_name
        if 'LOCALSTACK_HOSTNAME' in os.environ:
            dynamodb_endpoint = 'http://%s:4566' % os.environ['LOCALSTACK_HOSTNAME']
            self._resource = boto3.resource('dynamodb', endpoint_url=dynamodb_endpoint)
        else:
            self._resource = boto3.resource('dynamodb')
        self.__create_table([
            {
                "AttributeName": self._primary,
                "KeyType": "HASH"
            }
        ], [
            {
                "AttributeName": self._primary,
                "AttributeType": "S"
            }
        ])
        self._table = self._resource.Table(self._table_name)

    def save(self, user: User) -> bool:
        try:
            self._table.put_item(Item={
                "id": user.id,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "email": user.email,
                "genre": user.genre,
                "created_at": user.created_at,
                "updated_at": user.updated_at,
            })

            return True
        except ClientError as error:
            raise error

    def find(self, count=False) -> dict:
        try:
            response = self._table.scan()
            if count:
                return {
                    "Items": response["Items"],
                    "Count": response["Count"]
                }

            return {
                "Items": response["Items"]
            }
        except ClientError as error:
            raise error

    def find_by_id(self, user_id: str) -> dict:
        try:
            response = self._table.query(
                KeyConditionExpression=f'{self._primary} = :user_id',
                ExpressionAttributeValues={
                    ':user_id': user_id
                }
            )

            if response["Count"] > 0:
                return {
                    'Item': response["Items"][0]
                }

            return None
        except ClientError as error:
            raise error

    def destroy(self, user_id: str) -> bool:
        try:
            self._table.delete_item(Key={
                "id": user_id
            })
            return True
        except ClientError as error:
            raise error

    def update(self, user: User) -> dict:
        update_expression = []
        expression_attribute_values = {}
        user_items = user.get_user_data
        for key in user_items:
            update_expression.append(f'{key} = :{key}')
            expression_attribute_values[f':{key}'] = user_items[key]

        update_expression.append('updated_at = :updated_at')
        expression_attribute_values[f':updated_at'] = datetime.now().isoformat()
        update_expression = 'SET ' + ', '.join(update_expression)

        try:
            response = self._table.update_item(
                Key={'id': user.id},
                UpdateExpression=update_expression,
                ExpressionAttributeValues=expression_attribute_values,
                ReturnValues="UPDATED_NEW"
            )
            return response['Attributes']
        except ClientError as error:
            raise error

    def __create_table(self, key_schema: list, attribute_definitions: list, throughput=5):
        existing_tables = [table.name for table in self._resource.tables.all()]
        if self._table_name in existing_tables:
            return

        params = {
            "TableName": self._table_name,
            "KeySchema": key_schema,
            "AttributeDefinitions": attribute_definitions,
            "ProvisionedThroughput": {
                "ReadCapacityUnits": throughput,
                "WriteCapacityUnits": throughput
            }
        }
        table = self._resource.create_table(**params)
        table.wait_until_exists()
        return table

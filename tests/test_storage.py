import pytest

from datalake_backend import DynamoDBStorage


def test_dynamodb_store(dynamodb_users_table, dynamodb_connection):
    storage = DynamoDBStorage(table_name='users',
                              connection=dynamodb_connection)
    expected_user = {'name': 'John', 'last_name': 'Muir'}
    storage.store(expected_user)
    user = dict(dynamodb_users_table.get_item(name='John', last_name='Muir'))
    assert dict(user) == expected_user
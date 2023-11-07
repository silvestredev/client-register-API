from chalice.test import Client
from app import app
import json

def test_create_user():
    with Client(app) as client:
        response = client.http.post(
            '/consumers/users',
            body = json.dumps({"name": "user1", "phone": "11999999991"}),
            headers = {"Content-Type": "application/json"} 
            )
        
        print(response.json_body)
        assert response.json_body["statusCode"] == 200

def test_update_user():
    with Client(app) as client:
        response = client.http.put(
            '/consumers/users',
            body = json.dumps({"name": "user1", "phone": "11999999991"}),
            headers = {"Content-Type": "application/json"} 
            )
        
        print(response.json_body)
        assert response.json_body["statusCode"] == 200

def test_delete_user():
    with Client(app) as client:
        response = client.http.delete(
            '/consumers/users',
            body = json.dumps({"name": "user1", "phone": "11999999991"}),
            headers = {"Content-Type": "application/json"} 
            )
        
        print(response.json_body)
        assert response.json_body["statusCode"] == 200

def test_get_user():
    with Client(app) as client:
        response = client.http.get('/consumers/users')
        
        print(response.json_body)
        assert response.json_body["statusCode"] == 200

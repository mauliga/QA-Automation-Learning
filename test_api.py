import requests

BASE_URL = "https://jsonplaceholder.typicode.com/posts"

def test_get_posts():
    response = requests.get(BASE_URL)
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_create_post():
    new_post = {"title": "foo", "body": "bar", "userId": 1}
    response = requests.post(BASE_URL, json=new_post)
    assert response.status_code == 201
    assert response.json()["title"] == "foo"

def test_update_post():
    updated_post = {"id": 1, "title": "updated title", "body": "new body", "userId": 1}
    response = requests.put(f"{BASE_URL}/1", json=updated_post)
    assert response.status_code == 200
    assert response.json()["title"] == "updated title"

def test_delete_post():
    response = requests.delete(f"{BASE_URL}/1")
    assert response.status_code == 200

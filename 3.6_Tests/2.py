import requests
import pytest

API_TOKEN = "your_api_token"


def test_create_folder_positive():
    headers = {
        "Authorization": f"OAuth {API_TOKEN}",
        "Content-Type": "application/json"
    }
    folder_name = "test_folder"
    url = f"https://cloud-api.yandex.net/v1/disk/resources?path=/&fields=items"
    response = requests.put(url, headers=headers, json={"path": folder_name})
    assert response.status_code == 201
    assert response.json()["path"] == f"/{folder_name}"


def test_create_folder_error():
    headers = {
        "Authorization": f"OAuth {API_TOKEN}",
        "Content-Type": "application/json"
    }
    folder_name = "test_folder"
    # Trying to create the same folder again should return an error
    url = f"https://cloud-api.yandex.net/v1/disk/resources?path=/&fields=items"
    response = requests.put(url, headers=headers, json={"path": folder_name})
    assert response.status_code == 409
    assert response.json()["message"] == "Resource already exists"

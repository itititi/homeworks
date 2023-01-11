import requests
import os


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {'Content-Type': 'aplication/json', 'Authorization': f'OAuth {self.token}'}

    def get_files_list(self):
        files_url = 'https://cloud-api.yandex.net/v1/disk/resources/files'
        headers = self.get_headers()
        response = requests.get(files_url, headers=headers)
        return response.json()

    def upload_link(self, path_to_file: str):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": path_to_file, "overwtite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        return response.json()

    def upload(self, path_to_file):
        results = self.upload_link(path_to_file=path_to_file)
        href = results.get("href", "")
        filename = os.path.basename(path_to_file)
        response = requests.put(href, data=open(filename, 'rb'))
        response.raise_for_status()
        if response.status_code == 210:
            print("Готово!")


if __name__ == '__main__':
    path_to_file = os.path.abspath('test.txt')
    token = ""
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)
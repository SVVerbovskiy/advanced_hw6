import requests

TOKEN_YADISK = 'AQAAAAAQ_hYTAADLW9pmC8q-xkv_gjQzXRuBd00'
mkdir_url = 'https://cloud-api.yandex.net:443/v1/disk/resources'


def create_folder(path: str):
    params = {'path': path}
    headers = {'Content-Type': 'application/json',
               'Authorization': TOKEN_YADISK}
    create_dir = requests.api.put(mkdir_url, headers=headers, params=params)
    return create_dir.status_code


def delete_folder(path: str):
    params = {'path': path}
    headers = {'Content-Type': 'application/json',
               'Authorization': TOKEN_YADISK}
    create_dir = requests.api.delete(mkdir_url, headers=headers, params=params)
    return create_dir.status_code


if __name__ == '__main__':
    create_folder('new')
    delete_folder('new')
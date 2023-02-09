# api_final
## Описание
Данный проект позволяет взаимодейстовать приложениям с сайтом Yatube через API.
## Установка
Клонируйте репозиторий к себе(fork), скачайте на свой пк(git clone). В терминале используйте pip install -r requirements.txt для установки всех необходимых библиотек.
## Примеры
api/v1/posts/
### POST:
{
  "text": "string",
  "image": "string",
  "group": 0
}
### GET:
{
"count": 123,
"next": "http://api.example.org/accounts/?offset=400&limit=100",
"previous": "http://api.example.org/accounts/?offset=200&limit=100",
"results": [
{}
]
}

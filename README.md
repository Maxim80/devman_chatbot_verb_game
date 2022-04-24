# Игра глаголов
Чатбот для месенджера Telegram и социальной сети Вконтакте. Чатбот с помощью сервиса для распознавания естественного языка DialogFlow от Google отвечает на типичные запросы пользователей. Перед использованием чатбота необходимо предворительно создать проект DialogFlow, группу Вконтакте, бота в Telegram.  
Пример работы для Telegram:  
![](./demo_tg_bot.gif)
Примера работы для Вконтакте:  
![](./demo_vk_bot.gif)  

## Как установить
```
git clone git@github.com:Maxim80/devman_chatbot_verb_game.git
pip install -r requirements.txt
```

## Как запустить
Перед запуском требуется установить следующие переменные окружени(либо добавить их в файл `.env`):  
`export TELERGAM_TOKEN=<Telegram bot api токен>`  
`export DIALOGFLOW_PROJECT_ID=<ID проекта DialogFlow>`  
`export VK_TOKEN=<API токен группы Вконтакте>`  
`GOOGLE_APPLICATION_CREDENTIALS=<путь к ключу для использования Google API>`  
`ADMIN_CHAT_ID=<ID чата администратора в Telegram, куда бот будет отправлять логи>`  

Запустить:  
`python3 tg_bot.py` запуск бота для Telegram.  
`python3 vk_bot.py` запуск бота для Вконтакте.  
`python3 neural_network_training.py` запуск скрипта для обучения нейросети DialogFlow.  

## Цели проекта
Проект написан в учебных целях в рамках курса по python-программированию на сайте [Devman](https://dvmn.org/).

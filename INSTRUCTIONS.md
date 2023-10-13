**Инструкция для тестирования функционала API**

1. **Регистрация**:
    - Отправьте POST-запрос на: `https://api.devops33.site/users/`
    - Тело запроса:
      ```json
      {
        "first_name": "Anatoliy",
        "username": "anatoliy",
        "password": "te12st34",
        "re_password": "te12st34"
      }
      ```

2. **Авторизация**:
    - Отправьте POST-запрос на: `https://api.devops33.site/auth/token/login/`
    - Тело запроса:
      ```json
      {
        "username": "anatoliy",
        "password": "te12st34"
      }
      ```

      После успешной авторизации вы получите токен, который будет использоваться в последующих запросах.


3. **Генерация токена для Telegram бота**:
    - Отправьте GET-запрос на: `https://api.devops33.site/telegram/token/`
    - Заголовок для авторизации:
      ```
      Authorization: Token 79babfa4a80572ae9ae534482d78062cfd693d2f
      ```

      В ответ вы получите токен, который будет использоваться для связи с вашим Telegram-ботом.


4. **Отправка сообщений**:
    - Отправьте POST-запрос на: `https://api.devops33.site/messages/`
    - Заголовок для авторизации:
      ```
      Authorization: Token 79babfa4a80572ae9ae534482d78062cfd693d2f
      ```
    - Тело запроса:
      ```json
      {
        "text": "Я первое сообщение!"
      }
      ```

5. **Выход из системы**:
    - Отправьте POST-запрос на: `https://api.devops33.site/auth/token/logout/`
    - Заголовок для авторизации:
      ```
      Authorization: Token 79babfa4a80572ae9ae534482d78062cfd693d2f
      ```

      После этого ваш текущий токен будет отозван, и вы больше не сможете использовать его для доступа к API.

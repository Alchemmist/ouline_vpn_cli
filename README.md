# OutlineVPN CLI

Этот скрипт позволяет управлять ключами Outline VPN через простой и понятный интерфейс командной строки. Он позволяет эффективно работать с ключами, их лимитами данных и получать информацию о сервере.

# Как использовать?

## Общий синтаксис команд

Все команды имеют следующий синтаксис:

```sh
python main.py <команда> [параметры]
```

## Команды

### 0. Быстрая справвка о командах

Для получения справки о том какие есть команды используйте `--help`:

```sh
python main.py --help
```

### 1. Получить информацию обо всех ключах

Для получения списка всех ключей используйте команду `get_keys`:

```sh
python main.py get_keys
```

Эта команда выведет список всех ключей, созданных в вашей системе.

### 2. Получить информацию о конкретном ключе

Для получения информации о конкретном ключе используйте команду `get_key` с параметром `key_id`:

```sh
python main.py get_key <key_id>
```

Замените `<key_id>` на ID ключа, информацию о котором вы хотите получить.

### 3. Создать новый ключ

Для создания нового ключа используйте команду `create_key`:

```sh
python main.py create_key --name <name> [--key_id <key_id>] [--data_limit <data_limit>]
```

`--name <name>` — имя нового ключа (обязательно).

`--key_id <key_id>` — уникальный идентификатор ключа (необязательно, если не указано, будет сгенерирован автоматически).

`--data_limit <data_limit>` — лимит данных для ключа в гигабайтах (необязательно).

Пример:

```sh
python main.py create_key --name TestKey --data_limit 5
```

### 4. Переименовать ключ

Для переименования ключа используйте команду `rename_key`:

```sh
python main.py rename_key <key_id> <new_key_name>
```

Замените `<key_id>` на ID ключа и `<new_key_name>` на новое имя ключа.

### 5. Установить лимит данных для ключа

Для установки лимита данных используйте команду `set_limit`:

```sh
python main.py set_limit <key_id> <data_limit>
```

`<key_id>` — ID ключа, для которого устанавливается лимит данных.
`<data_limit>` — новый лимит данных в гигабайтах.

Пример:

```sh
python main.py set_limit my_key_id 10
```

### 6. Удалить лимит данных для ключа

Для удаления лимита данных используйте команду `delete_limit`:

```sh
python main.py delete_limit <key_id>
```

Замените `<key_id>` на ID ключа, для которого нужно удалить лимит данных.

### 7. Удалить ключ

Для удаления ключа используйте команду `delete_key`:

```sh
python main.py delete_key <key_id>
```

Замените `<key_id>` на ID ключа, который вы хотите удалить.

### 8. Получить информацию о сервере

Для получения информации о сервере используйте команду `get_server_info`:

```sh
python main.py get_server_info
```

Эта команда выведет информацию о сервере, с которым подключен ваш Outline VPN.

### Пример использования

Получим список всех ключей:

```sh
python main.py get_keys
```

Создадим новый ключ с именем MyNewKey и лимитом данных 10 ГБ:

```sh
python main.py create_key --name MyNewKey --data_limit 10
```

Переименуем ключ:

```sh
python main.py rename_key <key_id> NewName
```

Установим новый лимит данных для ключа:

```sh
python main.py set_limit <key_id> 20
```

Удалим лимит данных для ключа:

```sh
python main.py delete_limit <key_id>
```

Удалим ключ:

```sh
python main.py delete_key <key_id>
```

Получим информацию о сервере:

```sh
python main.py get_server_info

```

# Как запустить?

1. Создаём и активируем виртуальное окружение:

```sh
python -m venv venv

# Для Linux
source venv/bin/activate

# Для Windows
.\venv\Scripts\activate
```

2. Устанавливаем зависимости:

```sh
pip install -r requirements.txt
```

3. Создаём файл `.env`:

```sh
cp .env.example .env
```

4. Заполняем файл `.env` совими данными

# Как собрать?

1. Попробуем запустить проект по инструкции выше и проверяем что всё работает

2. Открываем файл `config.py` и находим там эти строки:

```python
api_url = config("API_URL")
cert_sha256 = config("CERT_SHA")
```

3. Заменяем их на:

```python
api_url = "<your-api-url>"
cert_sha256 = "<your-cert>"
```

4. Выполняем сборку под ту ОС, на которой сейчас находимся
```sh
pyinstaller --onefile --add-data ".env:." --hidden-import decouple --hidden-import outline-vpn-api main.py
```

5. После этого создастся папка `dist` в которой будет лежать бинарник `main` для Linux или `main.exe` для Windows

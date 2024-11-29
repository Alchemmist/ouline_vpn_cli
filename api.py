from config import client
from utils import gb_to_bytes
from openpyxl import Workbook


def dump_keys_to_excel(keys, filename="keys_dump.xlsx"):
    workbook = Workbook()
    sheet = workbook.active
    sheet.title = "Keys"

    headers = [
        "ID",
        "Name",
        "Password",
        "Port",
        "Method",
        "Access URL",
        "Used Bytes",
        "Data Limit",
    ]
    sheet.append(headers)

    for key in keys:
        sheet.append([
            key.key_id,
            key.name,
            key.password,
            key.port,
            key.method,
            key.access_url,
            key.used_bytes,
            key.data_limit,
        ])

    workbook.save(filename)
    print(f"Данные о ключах успешно сохранены в файл: {filename}")


def get_keys():
    """Получает все ключи, связанные с сервером Outline VPN.

    Эта функция извлекает список всех ключей с сервера Outline VPN.

    Возвращает
    -------
    List[Dict]
        Список словарей, каждый из которых представляет ключ VPN.
        Каждый словарь содержит информацию о ключе, такую как `key_id`, `name`,
        `access_url`, `used_bytes`, `data_limit` и т.д.

    Пример
    -------
    >>> get_keys()
    [{'key_id': '6', 'name': 'HabrKey', 'access_url': 'vpn://example', 'used_bytes': 1048576, 'data_limit': 1610612736}]
    """
    return client.get_keys()


def get_key_info(key_id: str):
    """Получает подробную информацию о конкретном ключе VPN.

    Эта функция извлекает подробную информацию о конкретном ключе
    с помощью его уникального идентификатора (`key_id`).

    Параметры
    ----------
    key_id : str
        Уникальный идентификатор ключа для получения информации.

    Возвращает
    -------
    Dict
        Словарь, содержащий подробную информацию о ключе.
        Включает такие поля, как `key_id`, `name`, `access_url` и т.д.

    Пример
    -------
    >>> get_key_info('6')
    {'key_id': '6', 'name': 'HabrKey', 'access_url': 'vpn://example'}
    """
    return client.get_key(key_id)


def create_new_key(key_id: str = None, name: str = None, data_limit_gb: float = None):
    """Создает новый ключ VPN на сервере.

    Эта функция позволяет создать новый ключ с необязательными параметрами:
    `key_id`, `name` и `data_limit`. Если `key_id` не предоставлен, он будет
    автоматически сгенерирован. Параметр `data_limit` указывается в гигабайтах,
    который затем преобразуется в байты.

    Параметры
    ----------
    key_id : str, optional
        Уникальный идентификатор ключа (по умолчанию None, в этом случае Outline генерирует его).
    name : str, optional
        Название ключа, которое поможет его идентифицировать (по умолчанию None).
    data_limit_gb : float, optional
        Лимит данных для ключа в гигабайтах (по умолчанию None).

    Возвращает
    -------
    Dict
        Словарь, содержащий информацию о созданном ключе.

    Пример
    -------
    >>> create_new_key(name="HabrKey", data_limit_gb=1.5)
    {'key_id': '6', 'name': 'HabrKey', 'access_url': 'vpn://new-key', 'data_limit': 1610612736}
    """
    return client.create_key(
        key_id=key_id, name=name, data_limit=gb_to_bytes(data_limit_gb)
    )


def rename_key(key_id: str, new_key_name: str):
    """Переименовывает существующий ключ VPN.

    Эта функция позволяет переименовать существующий ключ, предоставив
    его уникальный `key_id` и новое название (`new_key_name`).

    Параметры
    ----------
    key_id : str
        Уникальный идентификатор ключа для переименования.
    new_key_name : str
        Новое имя для ключа.

    Возвращает
    -------
    Dict
        Словарь, содержащий результат операции переименования.

    Пример
    -------
    >>> rename_key('6', 'NewKeyName')
    {'status': 'success'}
    """
    return client.rename_key(key_id, new_key_name)


def set_data_limit(key_id: str, data_limit_gb: float):
    """Обновляет лимит данных для существующего ключа.

    Эта функция позволяет обновить лимит данных для существующего ключа,
    предоставив его `key_id` и новый лимит в гигабайтах. Лимит данных преобразуется
    из гигабайт в байты перед обновлением.

    Параметры
    ----------
    key_id : str
        Уникальный идентификатор ключа, для которого нужно обновить лимит.
    data_limit_gb : float
        Новый лимит данных для ключа в гигабайтах.

    Возвращает
    -------
    Dict
        Словарь, содержащий результат операции обновления.

    Пример
    -------
    >>> upd_limit('6', 5)
    {'status': 'success'}
    """
    return client.add_data_limit(key_id, gb_to_bytes(data_limit_gb))


def delete_data_limit(key_id: str):
    """Удаляет лимит данных для существующего ключа.

    Эта функция позволяет удалить лимит данных с существующего ключа,
    предоставив его `key_id`.

    Параметры
    ----------
    key_id : str
        Уникальный идентификатор ключа, для которого нужно удалить лимит.

    Возвращает
    -------
    Dict
        Словарь, содержащий результат операции удаления лимита.

    Пример
    -------
    >>> delete_limit('6')
    {'status': 'success'}
    """
    return client.delete_data_limit(key_id)


def delete_key(key_id: str):
    """Удаляет ключ VPN с сервера.

    Эта функция позволяет удалить существующий ключ с сервера,
    предоставив его `key_id`.

    Параметры
    ----------
    key_id : str
        Уникальный идентификатор ключа, который нужно удалить.

    Возвращает
    -------
    Dict
        Словарь, содержащий результат операции удаления.

    Пример
    -------
    >>> delete_key('6')
    {'status': 'success'}
    """
    return client.delete_key(key_id)


def get_server_info():
    """Получает техническую информацию о сервере.

    Эта функция извлекает общую информацию о сервере, который
    выполняет службу Outline VPN.

    Возвращает
    -------
    Dict
        Словарь, содержащий техническую информацию о сервере.

    Пример
    -------
    >>> get_service_info()
    {'version': '1.0.0', 'uptime': '72 hours'}
    """
    return client.get_server_information()


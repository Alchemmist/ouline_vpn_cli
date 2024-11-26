import argparse
from api import (
    delete_data_limit,
    delete_key,
    get_keys,
    get_key_info,
    get_server_info,
    rename_key,
    create_new_key,
    set_data_limit,
    delete_data_limit,
)


def create_parser():
    parser = argparse.ArgumentParser(description="Управление ключами Outline VPN.")

    # Подсистема для работы с ключами
    subparsers = parser.add_subparsers(
        dest="command", help="Команды для управления ключами"
    )

    # Команда для получения всех ключей
    subparsers.add_parser("get_keys", help="Получить информацию обо всех ключах")

    # Команда для получения информации о ключе
    get_key_parser = subparsers.add_parser(
        "get_key", help="Получить информацию о ключе"
    )
    get_key_parser.add_argument("key_id", help="ID ключа для получения информации")

    # Команда для создания нового ключа
    create_key_parser = subparsers.add_parser("create_key", help="Создать новый ключ")
    create_key_parser.add_argument(
        "--key_id", help="Уникальный идентификатор для нового ключа", default=None
    )
    create_key_parser.add_argument("--name", help="Имя нового ключа", required=True)
    create_key_parser.add_argument(
        "--data_limit", type=float, help="Лимит данных в гигабайтах", default=None
    )

    # Команда для переименования ключа
    rename_key_parser = subparsers.add_parser("rename_key", help="Переименовать ключ")
    rename_key_parser.add_argument("key_id", help="ID ключа для переименования")
    rename_key_parser.add_argument("new_key_name", help="Новое имя для ключа")

    # Команда для установки лимита данных
    set_limit_parser = subparsers.add_parser(
        "set_limit", help="Установить лимит данных для ключа"
    )
    set_limit_parser.add_argument("key_id", help="ID ключа")
    set_limit_parser.add_argument(
        "data_limit", type=float, help="Новый лимит данных в гигабайтах"
    )

    # Команда для удаления лимита данных
    delete_limit_parser = subparsers.add_parser(
        "delete_limit", help="Удалить лимит данных для ключа"
    )
    delete_limit_parser.add_argument(
        "key_id", help="ID ключа для удаления лимита данных"
    )

    # Команда для удаления ключа
    delete_key_parser = subparsers.add_parser("delete_key", help="Удалить ключ")
    delete_key_parser.add_argument("key_id", help="ID ключа для удаления")

    # Команда для получения информации о сервере
    subparsers.add_parser("get_server_info", help="Получить информацию о сервере")

    return parser

def process_args(args):
    try:
        if args.command == "get_keys":
            keys = get_keys()
            if keys:
                print("Список всех ключей:\n")
                for key in keys:
                    print(f"ID: {key.key_id}")
                    print(f"Имя: {key.name or 'Без имени'}")
                    print(f"Пароль: {key.password}")
                    print(f"Порт: {key.port}")
                    print(f"Метод шифрования: {key.method}")
                    print(f"URL доступа: {key.access_url}")
                    print(f"Использованные байты: {key.used_bytes or 'Нет данных'}")
                    print(f"Лимит данных: {key.data_limit or 'Не установлен'}")
                    print("-" * 40)
            else:
                print("Ключи не найдены.")
        
        elif args.command == "get_key":
            try:
                key_info = get_key_info(args.key_id)
                if key_info:
                    print("Информация о ключе:")
                    print(f"ID: {key_info.key_id}")
                    print(f"Имя: {key_info.name or 'Без имени'}")
                    print(f"Пароль: {key_info.password}")
                    print(f"Порт: {key_info.port}")
                    print(f"Метод шифрования: {key_info.method}")
                    print(f"URL доступа: {key_info.access_url}")
                    print(f"Использованные байты: {key_info.used_bytes or 'Нет данных'}")
                    print(f"Лимит данных: {key_info.data_limit or 'Не установлен'}")
                else:
                    raise AttributeError
            except (Exception, AttributeError):
                print(f"Ошибка: Ключ с ID '{args.key_id}' не найден.")
        
        elif args.command == "create_key":
            new_key = create_new_key(
                key_id=args.key_id, name=args.name, data_limit_gb=args.data_limit
            )
            print("Создан новый ключ:")
            print(f"ID: {new_key.key_id}")
            print(f"Имя: {new_key.name or 'Без имени'}")
            print(f"Пароль: {new_key.password}")
            print(f"Порт: {new_key.port}")
            print(f"Метод шифрования: {new_key.method}")
            print(f"URL доступа: {new_key.access_url}")
        
        elif args.command == "rename_key":
            try:
                renamed_key = rename_key(args.key_id, args.new_key_name)
                if renamed_key:
                    print("Ключ успешно переименован:")
                    print(f"ID: {args.key_id}")
                    print(f"Новое имя: {args.new_key_name}")
                else:
                    raise AttributeError
            except AttributeError:
                print(f"Ошибка: Ключ с ID '{args.key_id}' не найден.")
        
        elif args.command == "set_limit":
            try:
                updated_limit = set_data_limit(args.key_id, args.data_limit)
                if updated_limit:
                    print("Лимит данных обновлен:")
                    print(f"ID ключа: {args.key_id}")
                    print(f"Новый лимит: {args.data_limit} ГБ")
                else:
                    raise AttributeError
            except AttributeError:
                print(f"Ошибка: Ключ с ID '{args.key_id}' не найден.")
        
        elif args.command == "delete_limit":
            try:
                removed_limit = delete_data_limit(args.key_id)
                if removed_limit:
                    print("Лимит данных удален.")
                    print(f"ID ключа: {args.key_id}")
                else:
                    raise AttributeError
            except AttributeError:
                print(f"Ошибка: Ключ с ID '{args.key_id}' не найден.")
        
        elif args.command == "delete_key":
            deleted = delete_key(args.key_id)
            if deleted:
                print(f"\nКлюч с ID '{args.key_id}' успешно удален.")
            else:
                print(f"Ошибка: Не удалось удалить ключ с ID '{args.key_id}'. Возможно, он не существует.")
        elif args.command == "get_server_info":
            try:
                server_info = get_server_info()
                print("Информация о сервере:")
                print(f"Имя сервера: {server_info.get('name', 'Нет информации')}")
                print(f"ID сервера: {server_info.get('serverId', 'Нет информации')}")
                print(f"Метрики включены: {'Да' if server_info.get('metricsEnabled') else 'Нет'}")
                print(f"Дата создания: {server_info.get('createdTimestampMs', 'Нет информации')}")
                print(f"Версия: {server_info.get('version', 'Нет информации')}")
                print(f"Порт для новых ключей доступа: {server_info.get('portForNewAccessKeys', 'Нет информации')}")
                print(f"Хостнейм для ключей доступа: {server_info.get('hostnameForAccessKeys', 'Нет информации')}")
            except Exception as e:
                print(f"Произошла ошибка при получении информации о сервере: {e}")
        else:
            print("Ошибка: Команда не распознана. Воспользуйтесь --help для получения справки")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

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
    # Обработка команд
    if args.command == "get_keys":
        keys = get_keys()
        if keys:
            for key in keys:
                print(key)
        else:
            print("Ключи не найдены.")

    elif args.command == "get_key":
        key_info = get_key_info(args.key_id)
        print(key_info)

    elif args.command == "create_key":
        new_key = create_new_key(
            key_id=args.key_id, name=args.name, data_limit_gb=args.data_limit
        )
        print(f"Создан новый ключ: {new_key}")

    elif args.command == "rename_key":
        renamed_key = rename_key(args.key_id, args.new_key_name)
        print(f"Ключ переименован: {renamed_key}")

    elif args.command == "set_limit":
        updated_limit = set_data_limit(args.key_id, args.data_limit)
        print(f"Лимит данных обновлен: {updated_limit}")

    elif args.command == "delete_limit":
        removed_limit = delete_data_limit(args.key_id)
        print(f"Лимит данных удален: {removed_limit}")

    elif args.command == "delete_key":
        deleted = delete_key(args.key_id)
        print(f"Ключ удален: {deleted}")

    elif args.command == "get_server_info":
        server_info = get_server_info()
        print(f"Информация о сервере: {server_info}")

    else:
        print("Команда не распознана.")


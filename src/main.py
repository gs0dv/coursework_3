from src.utils.functions import load_file


def main():
    """
        Точка входа
    """
    path = r'.\data\operations.json'

    # список всех транзакций
    transactions = load_file(path)

    if transactions:
        # словарь транзакций {дата_транзакции: данные_транзакции}
        dict_sec_id_from_transaction = {}

        for item in transactions:
            if item.get_state() == "EXECUTED":
                dict_sec_id_from_transaction[item.convert_date_in_sec()] = item

        list_sec_from_transaction = list(dict_sec_id_from_transaction.keys())
        list_sec_from_transaction.sort(reverse=True)
        list_sec_from_transaction = list_sec_from_transaction[:5]

        for item in list_sec_from_transaction:
            print(dict_sec_id_from_transaction[item].show_transaction_details())
            print()

    else:
        return


if __name__ == '__main__':
    main()

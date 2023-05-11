import json

from src.modules.transaction import Transaction


def load_file(path):
    """
        Загружает данные из файла json
    """
    try:
        with open(path, 'r', encoding='utf-8') as file:
            transaction_list = []
            file_json = json.load(file)

            for line in file_json:
                if line:
                    id_ = line['id']
                    state = line['state']
                    date = line['date']
                    operation_amount = line['operationAmount']
                    description = line['description']
                    from_ = line['from'] if 'from' in line.keys() else 'Opening_deposit'
                    to = line['to']

                    transaction_list.append(Transaction(
                        id_=id_,
                        state=state,
                        date=date,
                        operation_amount=operation_amount,
                        description=description,
                        from_=from_,
                        to=to
                    ))

            return transaction_list
    except FileNotFoundError:
        print("Файл не найден!")
        return
    except json.decoder.JSONDecodeError:
        print("Невозможно преобразовать файл из json!")
        return

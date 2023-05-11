from src.modules.errors import NumberAccountValueError, NumberCardValueError
import datetime


class Transaction:

    def __init__(self, id_, date, state, operation_amount, description, from_, to):
        # id транзакциии
        self.id_ = id_
        # информация о дате совершения операции
        self.date = date
        # статус перевода
        self.state = state
        # сумма операции и валюта
        self.operation_amount = operation_amount
        # описание типа перевода
        self.description = description
        # откуда
        self.from_ = from_
        # куда
        self.to = to

    def show_transaction_details(self):
        """
            Показывает подробности транзакции в формате:
                14.10.2018 Перевод организации
                Visa Platinum 7000 79** **** 6361 -> Счет **9638
                82771.72 руб.
        """
        # отформатированная дата
        formated_date = None
        try:
            formated_date = self.format_date(self.date)
        except ValueError:
            print('Неверный формат даты')

        if self.description == "Открытие вклада":
            data_from = "Открытие вклада"
        else:
            # исходящие данные
            data_from = None
            try:
                data_from = self.convert_data(self.from_)
            except NumberAccountValueError:
                print("Неверный формат исходящего счета")
            except NumberCardValueError:
                print("Неверный формат исходящего номера карты")

        # входящие данные
        data_to = None
        try:
            data_to = self.convert_data(self.to)
        except NumberAccountValueError:
            print("Неверный формат входящего счета")
        except NumberCardValueError:
            print("Неверный формат входящего номера карты")

        # сумма валюты
        amount_currency = None
        try:
            amount_currency = self.get_amount_currency()
        except KeyError:
            print("Отсутствуют данные суммы перевода/валюты")

        return f"{formated_date} {self.description}\n" \
               f"{data_from} -> {data_to}\n" \
               f"{amount_currency}\n" \
               f"{self.get_state()}"

    def convert_data(self, data):
        """
            Преобразует данные из форматов:
            Visa Classic 4040551273087672  ->  Visa Classic 4040 55** **** 7672
            Счет 86675623828180311969      ->  Счет **1969
            MasterCard 9175985085449563    ->  MasterCard 9175 98** **** 9563
        """
        if not data:
            return

        if "Счет" in data:
            name_account, number_account = data.split()

            if len(number_account) == 20 and number_account.isdigit():
                return name_account + " " + "**" + number_account[-4:]

            raise NumberAccountValueError("Неверный формат счета")

        else:
            name_card, number_card = data[:-16].strip(), data[-16:].strip()

            if number_card.isdigit() and len(number_card) == 16:
                number_card = "".join([number_card[:6], '*' * 6, number_card[-4:]])
                number_card = number_card[:4] + " " + number_card[4:8] + " " + number_card[8:12] + " " + number_card[
                                                                                                         12:16]
                return name_card + " " + number_card

            raise NumberCardValueError("Неверный формат номера карты")

    def get_amount_currency(self):
        """
            Возвращает количество валюты в формате  82771.72 руб. , 16872.46 USD
        """
        return self.operation_amount['amount'] + " " + self.operation_amount['currency']['name']

    def format_date(self, date_time_str):
        """
            Форматирует дату из формата Y-%m-%dT%H:%M:%S.%f в формат %d.%m.%Y
        """
        if not date_time_str:
            return

        date_time_obj = datetime.datetime.strptime(date_time_str, "%Y-%m-%dT%H:%M:%S.%f")
        date = date_time_obj.date()
        return date.strftime("%d.%m.%Y")

    def convert_date_in_sec(self):
        formated_date = datetime.datetime.strptime(self.date, "%Y-%m-%dT%H:%M:%S.%f")
        return (formated_date - datetime.datetime(1970, 1, 1)).total_seconds()

    def get_id(self):
        return self.id_

    def get_state(self):
        return self.state

    def __repr__(self):
        return f"Transaction (id_={self.id_},date={self.date}, state={self.state}, " \
               f"operation_amount={self.operation_amount}, description={self.description}, " \
               f"from_={self.from_}, to={self.to})"

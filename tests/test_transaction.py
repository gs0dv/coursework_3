from src.modules.errors import NumberAccountValueError, NumberCardValueError
from src.modules.transaction import Transaction
import pytest

id_ = 720751477
state = "EXECUTED"
date = "2018-11-08T08:21:45.902633"
date_3 = "2018-11-08 08:21:45.902633"
operation_amount = {"amount": "16872.46", "currency": {"name": "USD", "code": "USD"}}
operation_amount_1 = {"amount": "16872.46", "currency": {"code": "USD"}}
operation_amount_2 = {"currency": {"code": "USD"}}
operation_amount_9 = {"currency": {"name": "USD", "code": "USD"}}
description = "Перевод организации"
description_4 = "Открытие вклада"
from_ = "Счет 75743795418434298755"
from_5 = "Счет 757437954184342987"
from_6 = "Maestro 159683786870519"
to = "Счет 80785963509390811744"
to_7 = "Счет 8078596350939081174"
to_8 = "Maestro 159683786870519"

transaction = Transaction(id_=id_, state=state, date=date, operation_amount=operation_amount, description=description,
                          from_=from_, to=to)

transaction_1 = Transaction(id_=id_, state=state, date=date, operation_amount=operation_amount_1,
                            description=description, from_=from_, to=to)

transaction_2 = Transaction(id_=id_, state=state, date=date, operation_amount=operation_amount_2,
                            description=description, from_=from_, to=to)

transaction_3 = Transaction(id_=id_, state=state, date=date_3, operation_amount=operation_amount,
                            description=description, from_=from_, to=to)

transaction_4 = Transaction(id_=id_, state=state, date=date, operation_amount=operation_amount,
                            description=description_4, from_=from_, to=to)

transaction_5 = Transaction(id_=id_, state=state, date=date, operation_amount=operation_amount,
                            description=description, from_=from_5, to=to)

transaction_6 = Transaction(id_=id_, state=state, date=date, operation_amount=operation_amount,
                            description=description, from_=from_6, to=to)

transaction_7 = Transaction(id_=id_, state=state, date=date, operation_amount=operation_amount,
                            description=description, from_=from_, to=to_7)

transaction_8 = Transaction(id_=id_, state=state, date=date, operation_amount=operation_amount,
                            description=description, from_=from_, to=to_8)

transaction_9 = Transaction(id_=id_, state=state, date=date, operation_amount=operation_amount_9,
                            description=description, from_=from_, to=to)

transaction_repr = Transaction(id_="id_", state="state", date="date", operation_amount="operation_amount",
                               description="description", from_="from_", to="to")

str_1 = '08.11.2018 Перевод организации\n' \
        'Счет **8755 -> Счет **1744\n' \
        '16872.46 USD'

str_3 = 'None Перевод организации\n' \
        'Счет **8755 -> Счет **1744\n' \
        '16872.46 USD'

str_4 = '08.11.2018 Открытие вклада\n' \
        'Открытие вклада -> Счет **1744\n' \
        '16872.46 USD'

str_5 = '08.11.2018 Перевод организации\n' \
        'None -> Счет **1744\n' \
        '16872.46 USD'

str_6 = '08.11.2018 Перевод организации\n' \
        'None -> Счет **1744\n' \
        '16872.46 USD'

str_7 = '08.11.2018 Перевод организации\n' \
        'Счет **8755 -> None\n' \
        '16872.46 USD'

str_8 = str_7

str_9 = '08.11.2018 Перевод организации\n' \
        'Счет **8755 -> Счет **1744\n' \
        'None'


def test_convert_data():
    assert transaction.convert_data('Visa Classic 4040551273087672') == 'Visa Classic 4040 55** **** 7672'
    assert transaction.convert_data('Счет 86675623828180311969') == 'Счет **1969'
    assert transaction.convert_data('MasterCard 9175985085449563') == 'MasterCard 9175 98** **** 9563'
    assert transaction.convert_data('') == None


def test_convert_data__NumberAccountValueError():
    with pytest.raises(NumberAccountValueError):
        transaction.convert_data('Счет 8667562382818031196')
        transaction.convert_data('Счет 866')
        transaction.convert_data('')


def test_convert_data__NumberCardValueError():
    with pytest.raises(NumberCardValueError):
        transaction.convert_data('Visa Classic 404055127308767')
        transaction.convert_data('Visa Classic 404055')
        transaction.convert_data('')


def test_get_amount_currency():
    assert transaction.get_amount_currency() == '16872.46 USD'


def test_get_amount_currency__KeyError():
    with pytest.raises(KeyError):
        assert transaction_1.get_amount_currency()
        assert transaction_2.get_amount_currency()


def test_show_transaction_details():
    assert transaction.show_transaction_details() == str_1
    assert transaction_3.show_transaction_details() == str_3
    assert transaction_4.show_transaction_details() == str_4
    assert transaction_5.show_transaction_details() == str_5
    assert transaction_6.show_transaction_details() == str_6
    assert transaction_7.show_transaction_details() == str_7
    assert transaction_8.show_transaction_details() == str_8
    assert transaction_9.show_transaction_details() == str_9


def test_format_date():
    assert transaction.format_date('2019-07-13T18:51:29.313309') == '13.07.2019'
    assert transaction.format_date('') == None


def test_test_format_date__ValueError():
    with pytest.raises(ValueError):
        assert transaction.format_date('2019-07-13T18:51:29. 313309')


def test_convert_date_in_sec():
    assert transaction.convert_date_in_sec() == 1541665305.902633


def test_get_id():
    assert transaction.get_id() == 720751477


def test_repr():
    assert repr(transaction_repr) == 'Transaction (id_=id_,date=date, state=state, ' \
                                     'operation_amount=operation_amount, description=description, ' \
                                     'from_=from_, to=to)'


def test_get_state():
    assert transaction.get_state() == "EXECUTED"

from src.utils.functions import load_file

path = r"C:\Users\admin\PycharmProjects\coursework_3\tests\test_data\test_operations.json"
path_2 = r"C:\Users\admin\PycharmProjects\coursework_3\tests\test_data\test_operations_2.json"


def test_load_file():
    assert isinstance(load_file(path), list) == True
    assert load_file("") == None
    assert load_file(path_2) == None

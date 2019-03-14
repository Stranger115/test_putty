from SoftLibrary.data_generate import DataGenerate


def test_enter_message():
    test_data = {
            'user': '112',
            'password': '18cD2',
            'command': '09k'
}
    except_result = {
        'user': ['', '1', '1', '2', 'enter'],
        'password': ['', '1', '8', 'c', 'D', '2', 'enter'],
        'command': ['', '0', '9', 'k', 'enter']
    }
    data = DataGenerate()
    assert data.enter_message(test_data) == except_result
import pytest
pytest.main()
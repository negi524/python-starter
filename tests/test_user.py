import pytest
from user import User


def test_user_constructor():
    """正常系テスト"""
    user = User(id=1, name="Sample")
    assert user.id == 1
    assert user.name == "Sample"


def test_invalid_user_constructor():
    """例外系テスト"""
    with pytest.raises(ValueError) as exception:
        user = User(id="abc", name="Sample")

    assert "Input should be a valid integer" in str(exception.value)

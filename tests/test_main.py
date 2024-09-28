# from src.main import add_one
import src.main as main


def test_add_one():
    assert main.add_one(1) == 2

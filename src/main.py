from pydantic import BaseModel
import application_setting.my_logger as mylogger
from logging import Logger
import application_setting.my_credential as mycredential
from typing import Optional

# loggerを取得
logger: Logger = mylogger.get_logger("main")


class User(BaseModel):
    id: int
    name: str


def main():
    logger.info("hello, world.")
    user = User(id="1", name="Hoge")
    logger.info(user)
    print(mycredential.KEY)


def add_one(number: int) -> int:
    return number + 1


if __name__ == "__main__":
    main()

import application_setting.my_logger as mylogger
from logging import Logger
import application_setting.my_credential as mycredential
from typing import Optional

# loggerを取得
logger: Logger = mylogger.get_logger("main")

# credential情報を取得
credential: Optional[dict] = mycredential.read_credential()


def main():
    logger.info("hello, world.")
    print(credential)


def add_one(number: int) -> int:
    return number + 1


if __name__ == "__main__":
    main()

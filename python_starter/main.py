import application_setting.my_logger as my_logger


def main():
    print(my_logger.get_logger())
    print("hello, world.")


def add_one(number: int) -> int:
    return number + 1


if __name__ == "__main__":
    main()

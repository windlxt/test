from loguru import logger

logger.info("Hello, World!")

logger.add("logfile.log", format="{time} {level} {message}", level="DEBUG")


@logger.catch
def main():
    1 / 0


if __name__ == "__main__":
    main()

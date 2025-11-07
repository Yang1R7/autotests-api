import logging


def get_logger(name: str) -> logging.Logger:
    # Создаём логгер с именем "AUTOTEST"
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)  # Устанавливаем уровень логгирования на DEBUG, чтобы захватывать все сообщения

    # Создаём консольный обработчик для вывода логов в консоль
    handler = logging.StreamHandler()
    handler.setLevel(logging.DEBUG)  # Устанавливаем уровень для обработчика

    # Создаём форматтер для задания формата лог-сообщений
    formatter = logging.Formatter('%(asctime)s | %(name)s | %(levelname)s | %(message)s')
    handler.setFormatter(formatter)  # Привязываем форматтер к обработчику

    # Добавляем обработчик к логгеру
    logger.addHandler(handler)

    return logger


logger = get_logger("INPUT")

logger.info("Make API request")
logger.info("Code 200 response")

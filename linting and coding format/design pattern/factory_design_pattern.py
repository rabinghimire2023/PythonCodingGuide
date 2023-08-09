"""Builder Design pattern
"""
import logging
import datetime

class FileLogger:
    """File Logger
    """
    def __init__(self) -> None:
        print("File Logging")

    def logging(self, msg):
        """Logging

        Args:
            msg (str): message.
        """
        return logging.info("File Logging %s at %s", msg, datetime.datetime.now())

class ConsoleLogger:
    """Console Logger
    """
    def __init__(self) -> None:
        print("Console Logging")

    def logging(self, msg):
        """logging

        Args:
            msg (str): Message.
        """
        return logging.warning("Console Logging %s at %s", msg, datetime.datetime.now())

class DatabaseLogger:
    """Database Logger
    """
    def __init__(self) -> None:
        print("Database Logging")

    def logging(self, msg):
        """Logging
        """
        return logging.info("Database Logging %s at %s", msg, datetime.datetime.now())
class LoggerFactory:
    """Logger Factory
    """
    def __init__(self,logger_type: str)->None:
        self.logger_type=logger_type
    def factory_logger(self):
        """
        Factory logger
        """
        loggers = {
        "File": FileLogger,
        "Console": ConsoleLogger,
        "Database": DatabaseLogger
    }
        return loggers[self.logger_type]()


logging.basicConfig(level=logging.INFO)

MESSAGE = "secret"
file = LoggerFactory.factory_logger("File")
console = LoggerFactory.factory_logger("Console")
database = LoggerFactory.factory_logger("Database")

file.logging(MESSAGE)
console.logging(MESSAGE)
database.logging(MESSAGE)

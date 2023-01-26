import enum

from .exception import LogPyException


class LogLevel:
    class Level(enum.IntEnum):
        DEBUG = 1
        INFO = 2
        WARNING = 3
        ERROR = 4
        CRITICAL = 5

    @staticmethod
    def get_log_level(level: int) -> Level:
        match level:
            case 1:
                return LogLevel.Level.DEBUG
            case 2:
                return LogLevel.Level.INFO
            case 3:
                return LogLevel.Level.WARNING
            case 4:
                return LogLevel.Level.CRITICAL
            case 5:
                return LogLevel.Level.ERROR
            case _:
                raise LogPyException(f"log level not found - {level}")


class LoggerFormatConfig:
    class Attribute(enum.IntEnum):

        LEVEL_NAME = 1
        DATE_TIME = 2
        # MODULE = 3
        MESSAGE = 4
        LOGGER_NAME = 5
        LEVEL_NUMBER = 6
        # PATH_NAME = 7
        # FILE_NAME = 8
        # LINE_NUMBER = 9
        # FUNCTION_NAME = 10
        Request_Id = 11

    __enum_to_value_map = {
        1: "%(levelname)s",
        2: "%(asctime)s",
        3: "%(module)s",
        4: "%(message)s",
        5: "%(name)s",
        6: "%(levelno)s",
        7: "%(pathname)s",
        8: "%(filename)s",
        9: "%(lineno)d",
        10: "%(funcName)s",
        11: "%(request_id)s",
    }

    __SEPERATOR = "-::-"
    __LOG_STYLE = "%"
    __DEFAULT_FORMAT = [
        Attribute.LEVEL_NAME,
        Attribute.DATE_TIME,
        Attribute.Request_Id,
        Attribute.MESSAGE,
    ]

    @classmethod
    def get_log_style(cls):
        return cls.__LOG_STYLE

    @classmethod
    def get_seperator(cls):
        return cls.__SEPERATOR

    @classmethod
    def get_default_format(cls) -> list[Attribute]:
        return cls.__DEFAULT_FORMAT

    @classmethod
    def convert_to_format(cls, attrs: list[Attribute]) -> str:
        value: str = ""
        if not attrs:
            attrs = cls.__DEFAULT_FORMAT

        for attr in attrs:
            map_value = cls.__enum_to_value_map[attr.value]
            map_value += f" {cls.__SEPERATOR} "
            value += map_value

        value = value[:-5]
        return value


class LogConfig:
    log_level: LogLevel.Level
    log_name: str
    log_path: str

    def __init__(self, level, name, path) -> None:
        self.log_level=level,
        self.log_name=name,
        self.log_path=path



class LogConfigs:
    def __init__(self, level: LogLevel.Level, log_name: str, log_path: str) -> None:
        self.__config = LogConfig(level, log_name, log_path)

    @property
    def log_config(self):
        return self.__config

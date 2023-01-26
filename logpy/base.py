import logging
import os

from starlette_context import context

from .poco import LogConfig, LogLevel, LoggerFormatConfig
from .exception import LogPyException
from starlette_context.plugins.request_id import RequestIdPlugin


class RequestIdFilter(logging.Filter):
    def filter(self, record: logging.LogRecord):
        record.request_id = context[RequestIdPlugin.key]
        return True


class _LoggerBase:
    def __init__(
        self, log_config: LogConfig, format: list[LoggerFormatConfig.Attribute]
    ):
        formatter = logging.Formatter(
            fmt=LoggerFormatConfig.convert_to_format(format),
            style=LoggerFormatConfig.get_log_style(),
            datefmt="%d-%b-%y %H:%M:%S",
        )
        self.__create_dir(log_config.log_path)
        handler = logging.FileHandler(log_config.log_path + log_config.log_name)
        handler.setFormatter(formatter)
        self._logger = logging.getLogger(self._type())
        self._logger.setLevel(self.__get_log_level(log_config.log_level))
        self._logger.addHandler(handler)
        self._logger.addFilter(RequestIdFilter())

    def __create_dir(self, path: str):
        if path:
            if not os.path.exists(path):
                if not path.endswith("/"):
                    path += "/"
                os.makedirs(path)

    def _type(self):
        return self.__class__.__name__

    def _add_debug_log(self, message: str):
        self._logger.debug(message)

    def _add_info_log(self, message: str):
        self._logger.info(message)

    def _add_warning_log(self, message: str):
        self._logger.warning(message)

    def _add_critical_log(self, message: str):
        self._logger.critical(message)

    def _add_error_log(self, message: str):
        self._logger.error(message)

    def __get_log_level(self, level: LogLevel.Level) -> int:
        match level:
            case LogLevel.Level.DEBUG:
                return logging.DEBUG
            case LogLevel.Level.INFO:
                return logging.INFO
            case LogLevel.Level.WARNING:
                return logging.WARNING
            case LogLevel.Level.CRITICAL:
                return logging.CRITICAL
            case LogLevel.Level.ERROR:
                return logging.ERROR
            case _:
                raise LogPyException(f"log level not found - {level.name}")

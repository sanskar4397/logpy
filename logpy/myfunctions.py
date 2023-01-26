

from .poco import LogLevel, LoggerFormatConfig, LogConfig
from .base import _LoggerBase



def singleton(cls, *args, **kw):
    instances = {}
    def _singleton(*args, **kw):
        if cls not in instances:
                instances[cls] = cls(*args, **kw)
        return instances[cls]
    return _singleton


@singleton
class LogPy(_LoggerBase):
    def __init__(self, log_config: LogConfig=None, format: list[LoggerFormatConfig.Attribute]=[]):
        config = log_config if log_config else self.__get_default_log_config()
        format = format if format else self.__get_default_format()
        super().__init__(config, format)
    
    def __get_default_log_config(self):
        return LogConfig(
            LogLevel.Level.INFO,
            "myapplogs_logpy.log",
            ""
        )
    def __get_default_format(self):
        return LoggerFormatConfig.get_default_format()
    
    def debug(msg):
        super()._add_debug_log(msg)
    
    def info(msg):
        super()._add_info_log(msg)
    
    def error(msg):
        super()._add_error_log(msg)
    
    def critical(msg):
        super()._add_critical_log(msg)
    
    def warning(msg):
        super()._add_warning_log(msg)

    

    
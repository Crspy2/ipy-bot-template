import logging


class CustomFormatter(logging.Formatter):
    """Custom formatter class"""

    grey = "\x1b[90m"
    green = "\x1b[32m"
    blue = "\033[34m"
    yellow = "\x1b[33m"
    red = "\x1b[31m"
    white = "\x1b[37m"
    underline = "\x1b[4m"
    bold = "\x1b[1m"
    reset = "\x1b[0m"

    def format(self, record):

        log_fmt = f"{self.grey}[%(asctime)s] [%(filename)s] [%(name)s] › "

        # Dynamic Spacing
        record.asctime = self.formatTime(record, "%d-%m-%Y] [%H:%M:%S")
        real_len = len(log_fmt % record.__dict__)        
        prefered_len = 60
        remaining_len = prefered_len - real_len

        if remaining_len <= 0:
            remaining_len = 5
        gap = remaining_len * ' '

        # Render the log based on the log_type
        match record.levelno:
            case logging.DEBUG:
                log_fmt += f"{self.green}{self.underline}✔ debug{self.reset}{gap}%(message)s"
            case logging.INFO:
                log_fmt += f"{self.blue}{self.underline}ℹ info{self.reset} {gap}%(message)s"
            case logging.WARN:
                log_fmt += f"{self.yellow}{self.underline}⚠ warning{self.reset}{gap}%(message)s"
            case logging.ERROR:
                log_fmt += f"{self.red}{self.underline}✖ error{self.reset}{gap}%(message)s"
            case logging.FATAL:
                log_fmt += f"\x1b[41m{self.white}{self.bold}  💀 Fatal  {self.reset}{gap}%(message)s"
            case 99:  # LOG
                log_fmt += f"{self.white}{self.underline}📝 log{self.reset}{gap}%(message)s"
            case 100:  # START
                log_fmt += f"{self.green}{self.underline}▶ start{self.reset}{gap}%(message)s"
            case _:
                log_fmt += f"{self.white}{self.underline} unknown {self.reset}{gap}%(message)s"
                

        formatter = logging.Formatter(log_fmt, datefmt="%d-%m-%Y] [%H:%M:%S")
        return formatter.format(record)


def overwrite_ipy_loggers():
    for k, v in logging.Logger.manager.loggerDict.items():
        print(k, v)
        if k in ["mixin", "dispatch", "http", "gateway", "client", "context"]:
            for h in v.handlers:
                h.setFormatter(CustomFormatter)


def get_logger(name):
    """Function to get a logger
    Useful for modules that have already initialized a logger, such as discord.py
    """
    __logger = logging.getLogger(name)
    __logger.setLevel(logging.DEBUG)
    __ch = logging.StreamHandler()
    __ch.setFormatter(CustomFormatter())
    __logger.addHandler(__ch)
    return __logger




def init_logger(name="Altera"):
    """Function to create a designated logger for separate modules"""
    __logger = logging.Logger(name)
    __ch = logging.StreamHandler()
    __ch.setLevel(logging.DEBUG)
    __ch.setFormatter(CustomFormatter())
    __logger.addHandler(__ch)
    __logger.say = lambda msg: __logger.log(99, msg)
    __logger.start = lambda msg: __logger.log(100, msg)
    return __logger
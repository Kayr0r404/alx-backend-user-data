#!/usr/bin/env python3
"""Task 1: log Class"""

import re
import logging
from typing import List


class RedactingFormatter(logging.Formatter):
    """Redacting Formatter class"""

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """format log record to string"""
        msg: str = super(RedactingFormatter, self).format(record)
        txt = filter_datum(self.fields, self.REDACTION, msg, self.SEPARATOR)
        return txt


def filter_datum(
    fields: List[str],
    redaction: str,
    message: str,
    separator: str,
) -> str:
    """returns the log message obfuscated:"""
    message_list: list = message.split(separator)
    for field in message_list:
        if field.split("=")[0] in fields:
            message_list[message_list.index(field)] = re.sub(
                "^" + field, field.split("=")[0] + "=" + redaction, field
            )

    return separator.join(message_list)

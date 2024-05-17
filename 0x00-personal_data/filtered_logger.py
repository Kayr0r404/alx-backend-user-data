#!/usr/bin/env python3
"""Task 1: log Class"""

import re
import logging
from datetime import datetime


class RedactingFormatter(logging.Formatter):
    """Redacting Formatter class"""

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: tuple):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """format log record to string"""
        message = record.getMessage().split(self.SEPARATOR)
        filtered = filter_datum(
            self.fields,
            self.REDACTION,
            f"{self.SEPARATOR} ".join(message),
            self.SEPARATOR,
        )
        timestamp = datetime.utcfromtimestamp(record.created).strftime(
            "%Y-%m-%d %H:%M:%S"
        )
        return f"[HOLBERTON] {record.name} INFO {timestamp} {filtered}"


def filter_datum(fields, redaction, message, separator):
    """returns the log message obfuscated:"""
    message_list = message.split(separator)
    for field in message_list:
        if field.split("=")[0] in fields:
            message_list[message_list.index(field)] = re.sub(
                "^" + field, field.split("=")[0] + "=" + redaction, field
            )

    return separator.join(message_list)


filter_datum(
    ["password", "date_of_birth"],
    "xxxx",
    "name=egg;email=eggmin@eggsample.com;password=eggcellent;date_of_birth=12/12/198",
    ";",
)

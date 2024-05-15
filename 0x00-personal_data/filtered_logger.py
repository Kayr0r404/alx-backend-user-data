#!/usr/bin/env python3

import re


def filter_datum(fields, redaction, message, separator):
    message_list = message.split(separator)
    for field in message_list:
        if field.split("=")[0] in fields:
            index = message_list.index(field)
            message_list[index] = re.sub(
                "^" + field, field.split("=")[0] + "=" + redaction, field
            )

    return separator.join(message_list)


filter_datum(
    ["password", "date_of_birth"],
    "xxxx",
    "name=egg;email=eggmin@eggsample.com;password=eggcellent;date_of_birth=12/12/198",
    ";",
)

# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import logging


class Logger(object):

    def __init__(self, file_path, name="logger"):
        """
        Initialize the log class
        :param file_path: Log file path
        """
        self.logger = logging.getLogger(name)
        handler = logging.FileHandler(filename=file_path)
        self.logger.setLevel(logging.INFO)
        handler.setLevel(logging.INFO)
        formatter = logging.Formatter('%(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def out_print(self, in_list, separator=","):
        """
        Print output to file
        :param in_list: Input data list
        :param separator: Separator for each item
        :return: None
        """
        self.logger.info("[{}]".format(separator.join(list(map(str, in_list)))))


if __name__ == "__main__":
    print(get_images_from_path("./"))

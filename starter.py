'''
Python accessibility checker
Created by Matteus Sthefano Leite da Silva - 2016-12-28
'''

from checker.checker import Checker
from utils.printer import print_warn, print_header, print_not_found
import os


class Starter(object):
    def __init__(self, current_dir):
        self.__checker = Checker(current_dir)

    def start(self):
        warnings = self.__checker.find_warnings()
        print_header()

        if warnings:
            for warn in warnings:
                print_warn(warn)
        else:
            print_not_found()

if __name__ == "__main__":
    starter = Starter(os.getcwd())
    starter.start()

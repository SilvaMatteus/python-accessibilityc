from utils import constants as const
from utils.roles import ROLES
import os


class Checker(object):
    ''' Checker
    Entity that finds elements of html without
    good accessibility practices.
    '''

    def __init__(self, dir):
        self.__directory = dir

    def find_warnings(self):
        ''' Find warnings
        Method that looks for warnings in html files.
        It aggregates the warnings by html element or tag using a dictionary.

        :return: A list of warnings(to define warning in this context see the docs).
        '''

        warnings = []
        files = self.__find_html(self.__directory)

        for file in files:
            file_warnings = self.__check_html(file)
            if file_warnings:
                warnings.extend(file_warnings)

        return warnings

    def __find_html(self, dir):
        ''' Recursive function
        to find each html in the web project.

        :param dir: project home directory
        :return: a list with all html paths
        '''

        directories = []

        for item in os.listdir(dir):
            if os.path.isfile(os.path.join(dir, item)):
                if item.lower().endswith(const.HTML_EXTENSION):
                    directories.append(os.path.join(dir, item))
            else:
                directories.extend(self.__find_html(os.path.join(dir, item)))

        return directories

    def __check_html(self, file):
        '''
        Retrieve all the warnings of a html.
        :param file: The current html.
        :return: All the warnings of a html.
        '''
        warnings = []
        try:
            html = open(file, const.READ_ONLY_MODE)
            lines = html.readlines()
            for i in xrange(len(lines)):
                line_warnings = self.__read_line(lines[i])
                if line_warnings:
                    self.__insert_file_info(line_warnings, i +1, file)
                    warnings.extend(line_warnings)

        except IOError as exception:
            raise exception

        finally:
            html.close()
        return warnings

    def __read_line(self, line):
        '''
        Read one single line looking for warnings.
        :param line:
        :return: All the warnings of the line.
        '''
        warnings = []
        for role in ROLES:
            if self.__has_warning(role, line):
                warning = {'content': role['content'], 'explanation': role['explanation']}
                warnings.append(warning)
        return warnings

    def __insert_file_info(self, line_warnings, i, html):
        '''
        Insert the line number of the warning occurrence.
        :param line_warnings: List with warnings of the line.
        :param i: Line number.
        :param html: Path to html file.
        '''
        for warn in line_warnings:
            warn['local'] = html + ' at line: ' + str(i)

    def __has_warning(self, role, line):
        '''
        Verify if a line has a element that needs a warning.
        :param role: The role to analise.
        :param line: The line to analise.
        :return: True or False.
        '''
        return role['identifier'] in line and not role['content'] in line

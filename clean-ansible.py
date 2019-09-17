#!/usr/bin/python3

"""
Clean-Ansible is the tool to find the unnecessary variables declared in Ansible automation.
To search these variables run it with `python3` with specific option (dvars / gvars).

USAGE:
python3 clean-ansible.py dvars - to find unnecessary defaults variables
python3 clean-ansible.py gvars - to find unnecessary group variables

Author:
https://wrogrammer.com

Contact:
wrogrammer@gmail.com

https://github.com/wrogrammer/clean-ansible
"""

from dependencies.core import find_unused_defaults_vars, find_unused_groups_vars

import sys
from termcolor import colored


"""
Consts explanation:
MAIN_PATH - points to Ansible roles location
GROUP_VARS_PATH - points to Ansible group_vars location
EXCLUDE_VARS - variables to exclude
"""


MAIN_PATH = './roles/**/defaults/*.yml'
GROUP_VARS_PATH = './inventory/group_vars/*.yml'
EXCLUDE_VARS = ()


if __name__ == '__main__':
    try:
        if str(sys.argv[1]) == 'dvars':
            find_unused_defaults_vars(MAIN_PATH)
            find_unused_groups_vars(MAIN_PATH, GROUP_VARS_PATH)
        elif str(sys.argv[1]) == 'gvars':
            find_unused_groups_vars(MAIN_PATH, GROUP_VARS_PATH, EXCLUDE_VARS)
        else:
            print(colored("Please specify option to run.\nTo find unused defaults variables: dvars\n"
                  "To find unused group variables: gvars\nFor example: 'python3 clean-ansible.py dvars'", 'red'))
    except Exception as error:
        print("Something went wrong!!!\n", error)

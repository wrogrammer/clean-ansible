#!/usr/bin/python3

import glob
import os
import re

from pprint import pprint
from termcolor import colored
from unipath import Path


ANSIBLE_CONFIG_FILE_NAME = "ansible.cfg"
ANSIBLE_ROLES_PATH_VARIABLE_NAME = "roles_path"
ANSIBLE_SUBPATH_DEFAULTS = "**/defaults/*.yaml"
ANSIBLE_SUBPATH_TASKS = "tasks/*.yaml"
ANSIBLE_SUBPATH_TEMPLATES = "templates/**/*?.j2"


def read_ansible_configuration_file():
    # ARGPARSE to path ansible.cfg
    with open(ANSIBLE_CONFIG_FILE_NAME, "r") as f:
        for i, line in enumerate(f):
            if ANSIBLE_ROLES_PATH_VARIABLE_NAME in line:
                line = re.sub(r"\s+", "", line, flags=re.UNICODE)
                roles_path = re.split('=', line)[-1]
                return roles_path
            else:
                # TODO -> Get from argparse path -> PRIORITY.
                # TODO -> Separation roles func.
                continue
        return 0


def get_ansible_defaults_path(roles_path_from_config_file):
    roles_path_from_config_file = Path(roles_path_from_config_file)
    path_to_defaults = os.path.join(roles_path_from_config_file, ANSIBLE_SUBPATH_DEFAULTS)
    print("DEFAULTS_PATH:", colored(path_to_defaults, 'red'))
    return path_to_defaults


def get_ansible_tasks_path(general_path_to_all_defaults):
    general_path_to_all_defaults = Path(general_path_to_all_defaults).parent.parent
    path_to_tasks = os.path.join(general_path_to_all_defaults, ANSIBLE_SUBPATH_TASKS)
    print("TASKS_PATH:", colored(path_to_tasks, 'red'))
    return path_to_tasks


def get_ansible_templates_path(general_path_to_all_defaults):
    general_path_to_all_defaults = Path(general_path_to_all_defaults).parent.parent
    path_to_templates = os.path.join(general_path_to_all_defaults, ANSIBLE_SUBPATH_TEMPLATES)
    print("TEMPLATES_PATH:", colored(path_to_templates, 'red'))
    return path_to_templates


def get_ansible_files(path):
    paths_to_files = []
    for f in glob.iglob(path, recursive=True):
        paths_to_files.append(f)
    pprint(paths_to_files)
    return paths_to_files

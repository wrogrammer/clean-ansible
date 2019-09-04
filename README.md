![Clean Ansible Logo](/logos/clean_ansible_logo.png)

------------
## Contents
* [Links](https://github.com/wrogrammer/clean-ansible#Links)
* [Description](https://github.com/wrogrammer/clean-ansible#Description)
* [Features](https://github.com/wrogrammer/clean-ansible#Features)
* [Installation](https://github.com/wrogrammer/clean-ansible#Installation)
* [Questions / Help?](https://github.com/wrogrammer/clean-ansible#questions--help)
* [Bug reporting](https://github.com/wrogrammer/clean-ansible#bug-reporting)
* [Authors](https://github.com/wrogrammer/clean-ansible#Authors)
* [Supported Python Versions](https://github.com/wrogrammer/clean-ansible#supported-python-versions)


------------
### Links
- Website: [wrogrammer.com/](https://wrogrammer.com/ "wrogrammer.com/")

------------
### Description
**Clean Ansible** is the tool to detect incorrect variables before the provisioning process with use [Ansible](https://github.com/ansible/ansible "Ansible") automation tool.

The [Ansible](https://github.com/ansible/ansible "Ansible") doesn’t have functionality to check variables before running deployment.

------------
### Features
- find undefined Ansible variables

  `clean-ansible` is able to find undefined variables declared in Ansible: `tasks`, `playbooks`, and `templates`.

- find redundant Ansible variables

  `clean-ansible` is able to show the repeated Ansible variables based on Ansible variables precedence.

------------
### Installation

To use `clean-ansible` run:

```pip3 install clean-ansible```

------------
### Examples

------------
### Questions / Help?

Feel free to contact me:
`wrogrammer@gmail.com`
 
------------
### Bug reporting
Just open a Github issue.

------------
### Authors
- [Michał Janik](https://www.linkedin.com/in/michal-janik/ "Michał Janik") (@wrogrammer)

------------
### Supported Python Versions
`clean-ansible` is supported on Python 3.4+.

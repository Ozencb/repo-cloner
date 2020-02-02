# Repo Cloner

## Description
A command-line tool for cloning starred or created repositories of a user.
It requires Python 3.0+

---

## Installation
Make sure that setuptools is installed on your system before running setup.

Linux:
`sudo apt-get install python3-setuptools`

Windows:
`pip install setuptools`

Then you can run `python setup.py install` to install YTS-Scraper on your system.

## Usage

| Description                                               | Command                                                                     |
|-----------------------------------------------------------|-----------------------------------------------------------------------------|
| Help                                                      | `repo-cloner --help`                                                    |
| Clone created repositories of a user                      | `repo-cloner --user user1 --mode repos`                                 |
| Clone starred repositories of a user                      | `repo-cloner --user user1 --mode starred`                                 |
| Specify output directory                                  | `repo-cloner --user user1 --mode starred --output "Downloads"`            |
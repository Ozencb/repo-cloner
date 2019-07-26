# Repo Cloner
A command-line tool for cloning starred or created repositories of a user.
It requires Python 3.0+
---

## Installation
`python setup.py install`

## Usage

| Description                                               | Command                                                                     |
|-----------------------------------------------------------|-----------------------------------------------------------------------------|
| Help                                                      | `repocloner --help`                                                    |
| Clone created repositories of a user                      | `repocloner --user user1 --mode repos`                                 |
| Clone starred repositories of a user                      | `repocloner --user user1 --mode stars`                                 |
| Specify output directory                                  | `repocloner --user user1 --mode stars --output "Downloads"`            |

If you wish to use the tool without installing you can cd into script's directory and use the commands below:

| Description                                               | Command                                                                     |
|-----------------------------------------------------------|-----------------------------------------------------------------------------|
| Help                                                      | `./repocloner.py --help`                                                    |
| Clone created repositories of a user                      | `./repocloner.py --user user1 --mode repos`                                 |
| Clone starred repositories of a user                      | `./repocloner.py --user user1 --mode stars`                                 |
| Specify output directory                                  | `./repocloner.py --user user1 --mode stars --output "Downloads"`            |
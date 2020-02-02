from setuptools import setup, find_packages

setup(  name="Repo Cloner",
        version="0.1",
        packages=find_packages(),
        install_requires=[  'requests',
                            'gitpython',
                            'argparse',
                            'gitdb'],
        entry_points={'console_scripts': ['repo-cloner = repo_cloner.main:main']},
        author="Ozencb",
        description="A command-line tool to clone starred or created repositories of a user",
        license=open('LICENSE').read()
    )
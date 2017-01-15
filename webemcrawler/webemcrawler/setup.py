import sys
from cx_Freeze import setup, Executable

build_exe_options = {"packages": ["BeautifulSoup"]}
executables = [
    Executable('newy.py')
]

setup(name='hello', version='0.1', description='1', executables=executables)

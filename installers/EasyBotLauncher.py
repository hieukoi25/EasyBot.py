from sys import platform
from os import system, listdir, chdir, path, remove
import wget
#dependancies
if platform == 'win32':
    system('python --version')
system('pip install discord image qrcode wget')
BRANCH = 'testing'
chdir(path.dirname(path.abspath(__file__)))
#install eb
directory = listdir(path.dirname(path.abspath(__file__)))
wget.download(f'https://github.com/chisaku-dev/EasyBot.py/archive/refs/heads/{BRANCH}.zip', path.dirname(path.abspath(__file__)))
from shutil import unpack_archive
unpack_archive(f'Easybot.py-{BRANCH}.zip', path.expanduser("~"))
remove(f'Easybot.py-{BRANCH}.zip')
system('cls')
print(f'Files stored at: {path.expanduser("~")}\Easybot.py-{BRANCH}')
#start eb
system(f'python {path.expanduser("~")}/EasyBot.py-{BRANCH}/eb_control.py')
!pip install gitpython

!git config --global http.sslverify false

import os
import sys
import shutil
from getpass import getpass

import git

# ------------------------------------------------------------------------------
# Define project's name and owner and git provider
# ------------------------------------------------------------------------------
OWNER = 'claverru'
P_NAME = 'git-python'
GIT_PROV = 'github.com'
# ------------------------------------------------------------------------------

user = input('Git user:      ')
passw = getpass('Git password:  ')

if P_NAME in os.listdir():
  print('Removing old folder.')
  shutil.rmtree(P_NAME)

if P_NAME in sys.path:
  print('Removing old path.')
  sys.path.remove(P_NAME)

url = 'https://{0}:{1}@{2}/{3}/{4}'.format(user, passw, GIT_PROV, OWNER, P_NAME)

try:
  git.Git().clone(url)
  print('Repository {} cloned succesfully'.format(P_NAME))
  sys.path.append(P_NAME)
except git.GitCommandError:
  print('Access Denied, check authentication.')

del user, passw

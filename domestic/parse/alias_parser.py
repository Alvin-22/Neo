import os

from domestic.utility.read_file import *
from domestic.global_state import *


def alias_parser(data):
  if os.path.isfile(f'{state["root"]}/{state["settings"]["folders"]["parent"]}/alias.txt'):
    filesize = os.path.getsize(f'{state["root"]}/{state["settings"]["folders"]["parent"]}/alias.txt')

    if filesize != state['settings']['dynamic']['alias-size']:
      state['settings']['dynamic']['alias-data'] = read_file(f'{state["root"]}/{state["settings"]["folders"]["parent"]}/alias.txt').decode(state['settings']['encoding']).strip().split('\n')
      state['settings']['dynamic']['alias-size'] = filesize

    for alias in state['settings']['dynamic']['alias-data']:
      key_value = alias.split('=')

      if len(key_value) == 2:
        if data == key_value[0]:
          return key_value[1]
    
  return data
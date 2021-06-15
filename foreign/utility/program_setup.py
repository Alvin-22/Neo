import argparse

from foreign.global_state import *


def program_setup():
  parser = argparse.ArgumentParser()
  parser.add_argument('-ip', '--ipv4', default='localhost', help='IP address of host.')
  parser.add_argument('-p', '--port', type=int, default=1200, help='Socket port of host.')
  args = parser.parse_args()

  state['ip'], state['port'] = args.ipv4, args.port
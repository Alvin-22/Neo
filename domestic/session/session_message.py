from domestic.utility.validate_dict_key import *
from domestic.utility.status_message import *
from binary.data_handling.send_data import *
from binary.data_handling.recv_data import *
from domestic.utility.delete_client import *
from domestic.utility.text_to_image import *
from domestic.session.session_wait import *
from domestic.utility.write_error import *
from domestic.make.make_image import *
from domestic.make.make_file import *
from domestic.global_state import *


def session_message(message, piped_data=True, loading_text='loading...'):
  data = session_wait((state['session']['socket'], message, True), loading_text)

  text_mode = validate_dict_key(data, 'text_mode')
  text_extras = validate_dict_key(data, 'text_extras')

  if state['options']['information-gathering']['backup']['text']:
    make_file(['backup', 'backup/text'], 'txt', bytes(data['message'], state['settings']['encoding']))

  if state['options']['information-gathering']['backup']['image']:
    make_image(['backup', 'backup/image'], text_to_image(data['message']), False)
  
  if piped_data:
    if text_mode is None:
      status_message(data['message'], 'pure')
    else:
      if text_extras:
        status_message(data['message'], text_mode, text_extras)
      else:
        status_message(data['message'], text_mode)
  else:
    return data
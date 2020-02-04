import sys
from requests_toolbelt.multipart.encoder import MultipartEncoder
import os
import random
argvstr = sys.argv[1:]
print(argvstr)
argv_dict = {
    'name': 'file',
    'file': 'C:\\Users\湛子\Desktop\黄建test.txt',
    'filename': '黄建test.txt'
}
for argv in argvstr:
    argv = str(argv).replace("\r\n", "")
    DICT = eval(argv)
    argv_dict.update(DICT)
print(argv_dict)
multipart_encoder = MultipartEncoder(
    fields={
        'name': argv_dict['name'],
        'type': 'txt',
        'filename': argv_dict['filename'],
        'file': (os.path.basename(argv_dict['file']), open(argv_dict['file'], 'rb'), 'application/octet-stream')
        # file为路径
    },
    boundary='-----------------------------' + str(random.randint(1e28, 1e29 - 1))
)
print(argv_dict)

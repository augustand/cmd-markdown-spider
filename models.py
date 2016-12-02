# -*- coding:utf-8 -*-
from tinydb import TinyDB

from config import DB_PATH

tdb = TinyDB(DB_PATH)


class TbName(object):
    Tags = 'tags'
    Headers = 'headers'



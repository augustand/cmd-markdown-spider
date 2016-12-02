# -*- coding:utf-8 -*-
import sys

from bs4 import BeautifulSoup

from config import BLOG_PAGE
from models import tdb, TbName

reload(sys)
sys.setdefaultencoding('utf-8')

import requests


def get_tags():
    res = requests.get(BLOG_PAGE)
    bs = BeautifulSoup(res.text, 'lxml')
    tags = bs.select('#file-list .tag-list')
    for tag in tags:
        links = tag.select('.file-item.item a')
        yield dict(
            tag_name=tag.select_one('.tag-item.item .tag-name').text,
            tag_count=tag.select_one('.tag-item.item .tag-count').text,
            tag_links=[dict(link_href=link.attrs.get("href"), link_name=link.text.strip(' " "|\n|\b')) for link in
                       links]
        )


if __name__ == '__main__':
    tdb.purge_table(TbName.Tags)
    tdb.table(TbName.Tags).insert_multiple(list(get_tags()))
    pass

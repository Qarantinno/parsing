import logging
import os
from util.utils import write_json


if __name__ == '__main__':
    from sources.parsers import gg
    store = 'Алми'
    gg(store)

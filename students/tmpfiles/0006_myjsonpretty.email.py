#!/usr/bin/env python3


import codecs
import json
import argparse
from pytils.translit import slugify
from random import randint

parser = argparse.ArgumentParser(
                    prog='myjsonpretty',
                    description='Transform the input json-file APPEND EMAIL and create the pretty json output',
                    epilog='Warning: rewrite the same file')
parser.add_argument('FileName')


args = parser.parse_args()
FileName = args.FileName


with codecs.open(FileName, 'r', encoding='utf-8') as fp:
    data = json.load(fp)

for item in data:
    if item['model'] == 'students.student':
        email = "{}.{}.{}_{:03d}@mail.ru".format( slugify(item['fields']['last_name']), slugify(item['fields']['first_name'][0]), slugify(item['fields']['patronymic'][0]), randint(2005,2008) )
        item['fields']['email'] = email
        item['fields']['is_active'] = not randint(0,1)

with codecs.open(FileName, 'w', encoding='utf-8') as fp:
    json.dump(data, fp, ensure_ascii=False,indent=4)

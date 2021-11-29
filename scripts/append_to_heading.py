#!/usr/bin/python3
# encoding: utf-8

import re, sys, os, unicodedata    

original_content = os.environ['original_content']
heading = os.environ['heading']
entry = os.environ['entry']
block = re.compile(r'^((- )?## '+re.escape(heading)+r'(\n(\t|(  )+)-.*)*)', flags = re.MULTILINE)
replace = '\\1\n\t- '+entry

# r'^(- ## '+re.escape(heading)+r'(\n(\t|(  )+)-.*)*)'
# r'^(- ## '+re.escape(heading)+r'(\n  -.*)*)'

if re.findall(block, original_content) == []:
	new_content = original_content + '\n- ## ' + heading + '\n\t- ' + entry
else:
	new_content = re.sub(block, replace, original_content)

sys.stdout.write(unicodedata.normalize("NFC",new_content))
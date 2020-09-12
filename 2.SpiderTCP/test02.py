# -*- coding: utf-8 -*-
import re

string="A1.45，b5，6.45，8.82"
regex = re.compile(r"\d+\.?\d*")
print(regex.findall(string))

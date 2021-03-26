#!/usr/local/bin/python3

import sys
import json
from ruamel.yaml import YAML
from pprint import pprint as pp

import random
import string

characters = string.ascii_lowercase + string.digits

yaml=YAML()
yaml.default_flow_style = False

configConfig = yaml.load(open("FoxyProxy.yaml"))

# pp(configConfig)

for i, rule in enumerate(configConfig['rules']):
    rule['blackPatterns'] = rule['denyPatterns']
    rule['whitePatterns'] = rule['allowPatterns']

    if rule['title'] != "Default no proxy":
        rule['blackPatterns'] += configConfig['commonDenyPatterns']
    rule = configConfig['defaultRuleValues'] | rule

    for j, pattern in enumerate(rule['blackPatterns']):
        rule['blackPatterns'][j] = configConfig['defaultPatternValues'] | pattern
    for j, pattern in enumerate(rule['whitePatterns']):
        rule['whitePatterns'][j] = configConfig['defaultPatternValues'] | pattern

    configConfig.insert(i, ''.join(random.choice(characters) for i in range(20)), rule)

del configConfig["commonDenyPatterns"]
del configConfig["rules"]
del configConfig["defaultRuleValues"]
del configConfig["defaultPatternValues"]

json.dump(configConfig, sys.stdout)

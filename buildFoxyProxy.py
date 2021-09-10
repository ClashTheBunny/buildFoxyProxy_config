#!/usr/bin/env python3

"""Build a FoxyProxy Config programatically

Usage:
  buildFoxyProxy.py [FILE]
  buildFoxyProxy.py (-h | --help)

Arguments:
  [FILE] YAML file describing your proxy setup

Options:
  -h, --help     Show this screen.

"""
from docopt import docopt

import sys
import json
from ruamel.yaml import YAML
from pprint import pprint as pp

import random
import string

characters = string.ascii_lowercase + string.digits

yaml=YAML()
yaml.default_flow_style = False

def buildConfig(fileName):
	configConfig = yaml.load(open(fileName))

	for i, rule in enumerate(configConfig['rules']):
		rule['blackPatterns'] = rule['denyPatterns']
		rule['whitePatterns'] = rule['allowPatterns']
		rule['index'] = i
		rule['active'] = True

		if rule['title'] != "Default no proxy":
			rule['blackPatterns'] += configConfig['commonDenyPatterns']
		final_rule = configConfig['defaultRuleValues'].copy()
		final_rule.update(rule)
		rule = final_rule

		for j, pattern in enumerate(rule['blackPatterns']):
			final_pattern = configConfig['defaultPatternValues'].copy()
			final_pattern.update(pattern)
			rule['blackPatterns'][j] = final_pattern
		for j, pattern in enumerate(rule['whitePatterns']):
			final_pattern = configConfig['defaultPatternValues'].copy()
			final_pattern.update(pattern)
			rule['whitePatterns'][j] = final_pattern

		configConfig.insert(i, ''.join(random.choice(characters) for i in range(20)), rule)

	del configConfig["commonDenyPatterns"]
	del configConfig["rules"]
	del configConfig["defaultRuleValues"]
	del configConfig["defaultPatternValues"]

	return configConfig


if __name__ == '__main__':
    arguments = docopt(__doc__, version='Build a FoxyProxy Config Programatically')
    output = buildConfig(arguments['FILE'])
    json.dump(output, sys.stdout)

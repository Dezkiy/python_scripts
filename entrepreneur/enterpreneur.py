#!/bin/python
# -*- coding: utf-8 -*-
'''


С помощью функции parse_cdp_neighbors из modul_parse
и функции draw_topology из файла draw_network_graph.py
сгенерировать топологию, которая соответствует выводу
команды sh cdp neighbor из файла 

Не копировать код функций parse_cdp_neighbors и draw_topology.

В итоге, должен быть сгенерировано изображение топологии.
'''
from pprint import pprint
from modul_parse import parse_cdp_neighbors
from draw_network_graph import draw_topology

infiles = ['routers.txt']

topology = {}

for file in infiles:
	with open(file) as show_command:
		parsed = parse_cdp_neighbors(show_command)
		for pk,pv in parsed.items():
			if not pk in topology.values():
				topology[pk]=pv

pprint(topology)

draw_topology(topology)

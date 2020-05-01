# Cílem této úlohy je vložit cizí slovník do našeho hlavního slovníku.

# Tady je náš hlavní slovník: databaze = {'id123': {},'id124': {},'id125': {},'id126': {}}

# A tady jsou ostatní:
# PrvniSlovnik = {'jmeno': 'Thomas', 'vek': 45, 'zeme': 'Czechia', 'mesto': 'Brno'}
# DruhySlovnik = {'jmeno': 'Daniel', 'vek': 34, 'zeme': 'Czechia', 'mesto': 'Prague'}
# TretiSlovnik = {'jmeno': 'Eva', 'vek': 43, 'zeme': 'Czechia', 'mesto': 'Olomouc'}

from pprint import pprint as pp

databaze = {'id123': {},'id124': {},'id125': {},'id126': {}}
PrvniSlovnik = {'jmeno': 'Thomas', 'vek': 45, 'zeme': 'Czechia', 'mesto': 'Brno'}
DruhySlovnik = {'jmeno': 'Daniel', 'vek': 34, 'zeme': 'Czechia', 'mesto': 'Prague'}
TretiSlovnik = {'jmeno': 'Eva', 'vek': 43, 'zeme': 'Czechia', 'mesto': 'Olomouc'}

databaze.update(id123 = PrvniSlovnik)
databaze.update(id124 = DruhySlovnik)
databaze.update(id125 = TretiSlovnik)

pp(databaze)
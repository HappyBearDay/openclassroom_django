#!/usr/bin/env python3.7
#from  store.models  import Artist, Album


ARTISTS = {
  'francis-cabrel': {'name': 'Francis Cabrel'},
  'lej': {'name': 'Elijay'},
  'rosana': {'name': 'Rosana'},
  'maria-dolores-pradera': {'name': 'María Dolores Pradera'},
}

ALBUMS = [
  {'title': 'Sarbacane', 'artists': [ARTISTS['francis-cabrel']]},
  {'title': 'La Dalle', 'artists': [ARTISTS['lej']]},
  {'title': 'Luna Nueva', 'artists': [ARTISTS['rosana'], ARTISTS['maria-dolores-pradera']]}
]





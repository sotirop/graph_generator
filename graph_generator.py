#! /usr/bin/env python3

import argparse
import random
from datetime import datetime
Directed = False
Loop = False

def main(vertices, density, max_d, seed):
  random.seed(seed)
  
  for i in range(0, vertices):
    for j in range(0, vertices):
      if Directed or (i <= j):
        if Loop or (i != j):
            if random.uniform(0.0, 1.0) <= density:
                dis =  random.uniform(0.0, 1.0*max_d)
                print("%4d %4d %10f" % (i, j, dis))


if __name__ == "__main__":
  parser = argparse.ArgumentParser(description = 'Generate a random undirected graph')
  parser.add_argument('-v', '--vertices', type=int,
    default=5, help='the number of vertices, default: 5')
  parser.add_argument('-d', '--density', type=float,
    default=0.4, help='probability of an edge to be created, default 0.4')
  parser.add_argument('-md', '--max_d', type=float,
    default=10.0, help='max distance of an edge, default: 10.0')
  parser.add_argument('-s', '--seed', default=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    help='seed string, input to random.seed funtion, default: datetime.now() value')
  parser.add_argument('-dir', '--directed', action='store_true',
    help='assume directed graph, default is undirected')
  parser.add_argument('-l', '--loop', action='store_true',
    help='permit loops, default loops are not permitted')
  args = parser.parse_args()
  Directed = args.directed
  Loop = args.loop
  # print(args)
  main(args.vertices, args.density, args.max_d, args.seed)

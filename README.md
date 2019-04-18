# graph_generator

A simple graph generator in Python.

## help
```
user> ./graph_generator.py -h
usage: graph_generator.py [-h] [-v VERTICES] [-d DENSITY] [-md MAX_D]
                          [-s SEED] [-dir] [-l]

Generate a random undirected graph

optional arguments:
  -h, --help            show this help message and exit
  -v VERTICES, --vertices VERTICES
                        the number of vertices, default: 5
  -d DENSITY, --density DENSITY
                        probability of an edge to be created, default 0.4
  -md MAX_D, --max_d MAX_D
                        max distance of an edge, default: 10.0
  -s SEED, --seed SEED  seed string, input to random.seed funtion, default:
                        datetime.now() value
  -dir, --directed      assume directed graph, default is undirected
  -l, --loop            permit loops, default loops are not permitted
  ```

## usage

### number of vertices
Create a graph with 5 vertices and probability 1 that any edge exists. Default density probability is 0.40.
```
user> ./graph_generator.py -v 5 -d 1
   0    1   8.241189
   0    2   4.117791
   0    3   6.369332
   0    4   2.315471
   1    2   2.389442
   1    3   3.020105
   1    4   7.396298
   2    3   8.626766
   2    4   0.984170
   3    4   7.679901
```
Create a graph with 10 vertices and probability 0.40 that any edge exists.
```
user> ./graph_generator.py -v 10
   0    4   1.856113
   0    5   9.167582
   0    7   4.295258
   1    4   1.199899
   1    6   0.371146
   1    9   4.633235
   2    4   8.496948
   2    6   9.353413
   2    9   2.615050
   3    5   3.202757
   3    6   1.779892
   3    8   0.043698
   5    7   2.369914
   6    8   8.740469
   7    9   0.864979
```
### max distance
Create a graph with 4 vertices and probability 1 that any edge exists, with each edge length between 0.0 and 24.0.
```
user> ./graph_generator.py -v 4 -d 1 -md 24.0
   0    1   9.036901
   0    2  19.743478
   0    3  20.234961
   1    2  23.784967
   1    3  13.496640
   2    3   8.423459
```
### directed graph
Create a directed graph with 4 vertices and probability 1 that any edge exists, with each edge length between 0.0 and 5.0.
```
user> ./graph_generator.py -v 4 -d 1 -md 5.0 -dir
   0    1   3.404863
   0    2   3.213175
   0    3   3.053851
   1    0   4.751465
   1    2   0.518659
   1    3   3.239149
   2    0   2.242328
   2    1   1.474554
   2    3   2.505322
   3    0   0.347947
   3    1   2.859499
   3    2   3.876708
```
### loops (edge from vertex to itself)
Create a directed graph with 3 vertices and probability 1 that any edge exists, with each edge length between 0.0 and 10.0, where loops are permitted.
```
user> ./graph_generator.py -v 3 -d 1 -md 10.0 -dir -l
   0    0   7.545652
   0    1   2.331990
   0    2   6.899898
   1    0   8.483664
   1    1   3.025699
   1    2   6.373641
   2    0   1.872887
   2    1   4.078114
   2    2   1.067111
```
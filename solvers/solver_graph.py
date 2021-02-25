import argparse
import random
import sys
sys.path.extend(['..', '.'])
from collections import *
from queue import PriorityQueue
from dataparser import parse
from util import get_in_file_content

# inp is an input file as a single string
# return your output as a string
def solve(inp, args):
    # TODO: Solve the problem
    random.seed(args['seed'])
    ns = parse(inp)
    left = set([pizza['id'] for pizza in ns.pizzas])
    adj_mat = [[0 for _ in range(ns.M)] for _ in range(ns.M)]
    for pizza1 in ns.pizzas:
        for pizza2 in ns.pizzas:
            adj_mat[pizza1['id']][pizza2['id']] = len(pizza1['ingredients'].intersection(pizza2['ingredients']))
    teams = []
    
    def pop_mat (v):
        for i in range(ns.M):
            adj_mat[v][i] = float('inf')
            adj_mat[i][v] = float('inf')
        
    def find_best_list(team_size):
        if len(left) < team_size:
            return None
        else:
            L = []
            v = left.pop()
            pq = PriorityQueue()
            L.append(v)
            for i in left:
                pq.put((adj_mat[v][i], i))
            for _ in range(team_size-1):
                popped = pq.get()
                L.append(popped[1])
                left.remove(popped[1])
            for v in L:
                pop_mat(v)
        return L
    team_pizzas = []
    for _ in range(ns.T4):
        # pick pizzas
        pizza_list = find_best_list(team_size=4)
        if pizza_list==None:
            break
        team_pizzas.append(pizza_list)
    for _ in range(ns.T3):
        # pick pizzas
        pizza_list = find_best_list(team_size=3)
        if pizza_list==None:
            break
        team_pizzas.append(pizza_list)
    for _ in range(ns.T2):
        # pick pizzas
        pizza_list = find_best_list(team_size=2)
        if pizza_list==None:
            break
        team_pizzas.append(pizza_list)
    out = []
    out.append(str(len(team_pizzas)))
    for row in team_pizzas:
        out.append(' '.join(map(str, [len(row)]+row)))
    res = '\n'.join(out)
    return res

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('in_file')
    args = parser.parse_args()
    inp = get_in_file_content(args.in_file)
    out = solve(inp, {'seed': 0})
    print('\n'.join(['OUT:', '=========', out]))

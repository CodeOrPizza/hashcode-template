import argparse
import random
import sys
sys.path.extend(['..', '.'])
from collections import *
from dataparser import parse
from util import get_in_file_content

# inp is an input file as a single string
# return your output as a string
def solve(inp, args):
    # TODO: Solve the problem
    random.seed(args['seed'])
    ns = parse(inp)
    left = [pizza['id'] for pizza in ns.pizzas]
    team_pizzas = []
    left = sorted(left, key=lambda p_id: len(ns.pizzas[p_id]['ingredients']))
    
    for _ in range(ns.T3):
        # pick pizzas
        if len(left)<3:
            break
        pizza_list = []
        for _ in range(3):
            pizza_list.append(left.pop())
        team_pizzas.append(pizza_list)
    
    for _ in range(ns.T4):
        # pick pizzas
        if len(left)<4:
            break
        pizza_list = []
        for _ in range(4):
            pizza_list.append(left.pop())
        team_pizzas.append(pizza_list)
    for _ in range(ns.T2):
        # pick pizzas
        if len(left)<2:
            break
        pizza_list = []
        for _ in range(2):
            pizza_list.append(left.pop()) 
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

"""
    =====> Sample Input

    Enter number of Nodes: 7
    Enter Node_Name space separated:
    NOTE: Enter Node names in Capital Letters:
    ==> A B C D E F G


    Enter Edges: Format(First_Node_Name Second_Node_Name Edge_Cost) space separated:
    NOTE: Enter edge as (0 0 0) to stop entering more edges
    NOTE: Enter Node names in Capital Letters
    Edge: A B 2
    Edge: A C 5
    Edge: B C 6
    Edge: B D 1
    Edge: B E 3
    Edge: C F 8
    Edge: D E 4
    Edge: E G 9
    Edge: F G 9
    Edge: 0 0 0

    Name of Start Node: A
"""


import math


class GraphNode:
    def __init__(self, name, index):
        self.name = name
        self.index = index
        self.distance = math.inf
        self.neighbours = []
        self.weight_map = {}
        self.parent = None


def add_edge(source, destination, edge_cost):
    first = node_list[source]
    second = node_list[destination]

    first.neighbours.append(second)
    first.weight_map[second] = edge_cost


def path_print(node):
    if node.parent:
        path_print(node.parent)
    print(node.name + " ", end="")


def bellman_ford(start_node):
    start_node.distance = 0
    for i in range(len(node_list)):
        for current_node in node_list:
            for neighbour in current_node.neighbours:
                if neighbour.distance > current_node.distance + current_node.weight_map[neighbour]:
                    neighbour.distance = current_node.distance + current_node.weight_map[neighbour]
                    neighbour.parent = current_node

    # optional code - to check for negative cycle
    for current_node in node_list:
        for neighbour in current_node.neighbours:
            if neighbour.distance > current_node.distance + current_node.weight_map[neighbour]:
                print('WARNING: Negative cycle found.')
                print('\t Vertex name: ' + neighbour.name)
                print('\t Old cost: ' + neighbour.distance)
                new_distance = current_node.distance + current_node.weight_map[neighbour]
                print('\t New cost: ' + new_distance)

    print('Negative cycle not found.')

    for node_to_check in node_list:
        print("Node {}, distance: {}, Path: ".format(node_to_check.name, str(node_to_check.distance)), end="")
        path_print(node_to_check)
        print()


node_list = []


def main():
    no_of_nodes = int(input("Enter number of Nodes: "))
    mapp = {}

    print('Enter Node_Name space separated:\nNOTE: Enter Node names in Capital Letters: ')
    names = input('==> ').split(' ')
    for i in range(no_of_nodes):
        node = GraphNode(names[i], i)
        node_list.append(node)
        mapp[names[i]] = i

    print('\n\nEnter Edges: Format(First_Node_Name Second_Node_Name Edge_Cost) space separated:')
    print('NOTE: Enter edge as (0 0 0) to stop entering more edges')
    print('NOTE: Enter Node names in Capital Letters')
    while True:
        row = input('Edge: ').split(' ')
        first, second = row[0], row[1]
        edge_cost = int(row[2])

        if first == second == '0':
            break

        add_edge(mapp[first], mapp[second], edge_cost)

    start = input("\nName of Start Node: ")

    bellman_ford(node_list[mapp[start]])


main()


import sys
input = sys.stdin.readline

n = int(input())

dic = dict()
maze = []
for _ in range(n):
    node = input().strip().split()
    maze.append(node)
    dic[node[0]] = (node[1], node[2])

def inorder(node):
    if node != '.':
        inorder(dic[node][0])
        print(node, end='')
        inorder(dic[node][1])


def preorder(node):
    if node != '.':
        print(node, end='')
        preorder(dic[node][0])
        preorder(dic[node][1])

def postorder(node):
    if node != '.':
        postorder(dic[node][0])
        postorder(dic[node][1])
        print(node, end='')

preorder('A')
print()
inorder('A')
print()
postorder('A')
print()
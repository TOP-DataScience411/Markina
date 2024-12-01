import random

def tree_generator():
    def generate_branch():
        num_leaves = random.randrange(0, 4)
        num_branches = random.randrange(0, 3)
        branch = []
        for _ in range(num_leaves):
            branch.append('leaf')
        for _ in range(num_branches):
            branch.append(generate_branch())
        return branch
    tree = generate_branch()
    while not tree or (len(tree) == 1 and isinstance(tree[0], list) and not tree[0]):
        tree = generate_branch()
    
    return tree
    
    
    
    
# C:\Users\Админ\Scripts\Markina\2024.11.24>python -i 4.py
#>>> tree_generator()
#['leaf', 'leaf', 'leaf', ['leaf', 'leaf', 'leaf'], ['leaf', 'leaf']]
#>>> tree_generator()
#['leaf', 'leaf', 'leaf', ['leaf', 'leaf', 'leaf']]
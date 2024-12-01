def tree_leaf(tree):
    count = 0
    for leaf in tree:
        if isinstance(leaf, list):
            count += tree_leaf(leaf)
        elif leaf == 'leaf':
            count += 1
        else:
            count += 0
    return count
    
    
#C:\Users\Админ\Scripts\Markina\2024.11.24>python -i 3.py
#>>> tree = [[[['leaf', 'leaf', 'leaf', 'leaf'], 'leaf', 'leaf', 'leaf'], [['leaf', 'leaf'], 'leaf', 'leaf'], ['leaf', '\leaf', 'leaf']], [['leaf', 'leaf'], ['leaf', 'leaf', 'leaf', 'leaf', 'leaf', 'leaf'], 'leaf', 'leaf', 'leaf'], [['leaf'\], ['leaf', 'leaf', ['leaf', 'leaf', 'leaf']], 'leaf', 'leaf'], ['leaf', 'leaf', ['leaf', 'leaf'], 'leaf']]
#>>> tree_leaf(tree)
#38
#>>>
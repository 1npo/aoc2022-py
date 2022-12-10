import re
from anytree import AnyNode, RenderTree, Resolver, PostOrderIter 
from anytree.resolver import ChildResolverError


# Thanks apio 😄
# https://stackoverflow.com/questions/69379301/adding-new-nodes-by-id-in-anytree
class FSTree:
    def __init__(self):
        self.root = AnyNode(id='/', size=0, isdir=True)

    def add_node(self, parent_id, child_id, size=0, isdir=False):
        r = Resolver('id')
        parent_node = r.get(self.root, parent_id)
        try:
            node = r.get(parent_node, child_id)
        except ChildResolverError:
            AnyNode(id=child_id,
                    parent=parent_node,
                    size=size,
                    isdir=isdir)

    def display(self):
        for pre, _, node in RenderTree(self.root):
            if node.size != 0:
                print(f'{pre}{node.id} ({node.size}) {node.isdir=}')
            else:
                print(f'{pre}{node.id} {node.isdir=}')


CMD_RE = re.compile('^\$ (ls|cd) ?(.*)?')
OUT_RE = re.compile('^(dir|\d.*) (.*)')


def parse_line(line: str) -> tuple:
    cmd = CMD_RE.findall(line)
    out = OUT_RE.findall(line)

    if cmd:
        return cmd[0]
    if out:
        if out[0][0].isdigit():
            return (int(out[0][0]), out[0][1])
        else:
            return out[0]


def build_fs_tree(fs_tree, content):
    current_tree_pos = ''

    for l in content:
        if l[0] == 'cd':
            if l[1] == '/':
                continue
            elif l[1] == '..':
                if current_tree_pos.count('/') == 1:
                    current_tree_pos = ''
                else:
                    current_tree_pos = current_tree_pos.rsplit('/', 2)[0] + '/'
            else:
                current_tree_pos += f'{l[1]}/'
            continue

        if l[0] == 'ls':
            continue

        if l[0] == 'dir':
            fs_tree.add_node(current_tree_pos, l[1], isdir=True)

        if isinstance(l[0], int):
            fs_tree.add_node(current_tree_pos, l[1], size=l[0])


def sum_children(node):
    if len(node.children) == 1 and node.children[0].isdir:
        return node.children[0].size
    else:
        return sum([child.size for child in node.children])


def solve(filepath: str):
    with open(filepath, 'r') as f:
        content = [parse_line(line.strip()) for line in f]
        
        fs_tree = FSTree()
        build_fs_tree(fs_tree, content)

        part1_sum = 0

        # First pass - sum all the child files
        dirs_summed = []
        for node in PostOrderIter(fs_tree.root):
            if node.isdir:
                node.size = sum_children(node)
 
        # Second pass - sum all the dirs <= 100000
        for node in PostOrderIter(fs_tree.root):
            if node.isdir and node.size <= 100_000:
                part1_sum += node.size
        
        disk_space_max = 70_000_000
        disk_space_unused = 30_000_000
        disk_space_cur = disk_space_max - fs_tree.root.size
        disk_space_needed = disk_space_unused - disk_space_cur
        
        # Third pass - get all the dirs that can be removed to free up the needed space
        suitable_dirs = []
        for node in PostOrderIter(fs_tree.root):
            if node.isdir and node.size >= disk_space_needed:
                suitable_dirs.append(node.size)
            
        # fs_tree.display()
        
        print(f'[+] Part 1 solution: {part1_sum}')
        print(f'[+] Part 2 solution: {min(suitable_dirs)}')

class TreeNode:
    def __init__(self, key, value, left=None, right=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right
        self.size = 0


class Tree:
    def __init__(self):
        self.root = None

    def is_empty(self):
        return self.root.size == 0

    def put(self, key, value):
        def put_rec(node):
            if node is None:
                return TreeNode(key, value)
            if node.key < key:
                node.left = put_rec(node.left)
            else:
                node.right = put_rec(node.right)

        self.root = put_rec(self.root)

    def get(self, key):
        def get_rec(node):
            if node.key == key:
                return node.value
            if node.key < key:
                return get_rec(node.left) if node.left else None
            return get_rec(node.right) if node.right else None

        return get_rec(self.root)

    def is_bst(self):
        def _is_bst(node, _min, _max):
            if node is None: return True
            if _min is not None and node.key >= _min: return False
            if _max is not None and node.key >= _max: return False
            return True

        return _is_bst(self.root, None, None)

    def pre_order(self):
        result = []

        def traverse(node):
            if node:
                result.append((node.key, node.value))
                traverse(node.left)
                traverse(node.right)

        traverse(self.root)
        return result

    def post_order(self):
        result = []

        def traverse(node):
            if node:
                traverse(node.left)
                traverse(node.right)
                result.append((node.key, node.value))

        traverse(self.root)
        return result

    def in_order(self):
        result = []

        def traverse(node):
            if node:
                traverse(node.left)
                result.append((node.key, node.value))
                traverse(node.right)

        traverse(self.root)
        return result

    def level_order(self):
        queue = [self.root]
        result = []
        while queue:
            node = queue.pop(0)
            result.append((node.key, node.value))
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return result

    def height(self):
        def height_helper(node):
            if node is None:
                return -1
            return 1 + max(height_helper(node.left), height_helper(node.right))

        return height_helper(self.root)

    def is_mirror_at_root(self):
        pass
   
from collections import deque, Counter


class Node:
    def __init__(self, symbol=None, weight=None, left=None, right=None):
        self.symbol = symbol
        self.weight = weight
        self.left = left
        self.right = right


def travel_down(code, node, label):
    if node is None:
        return

    if node.symbol is not None:
        # we reached a leaf!
        code[node.symbol] = label
        return

    # travel down the tree calling recursively the function
    # left children gets a 0, right children gets a 1
    travel_down(code, node.left, label + "0")
    travel_down(code, node.right, label + "1")


def huffman_code(text):
    # one queue for leaves and one for internal nodes
    leaves = deque()
    internals = deque()

    # start by filling the leaves with the sorted probabilities
    # lowest probabilities go to the front of the queue
    counts = dict(sorted(Counter(text).items(), key=lambda x: x[1]))
    for c in counts:
        leaves.append(Node(c, counts[c]))

    while len(leaves) + len(internals) > 1:
        # compare the heads of the queues to get the next children
        if len(internals) > 0 and (
            len(leaves) == 0 or leaves[0].weight > internals[0].weight
        ):
            child1 = internals.popleft()
        else:
            child1 = leaves.popleft()

        # the test is the same for the second child (the queues have changed)
        if len(internals) > 0 and (
            len(leaves) == 0 or leaves[0].weight > internals[0].weight
        ):
            child2 = internals.popleft()
        else:
            child2 = leaves.popleft()

        # create parent node and add it to the internal nodes queue
        parent = Node(None, child1.weight + child2.weight, child1, child2)
        internals.append(parent)

    # the only node left is the Huffman tree
    root = internals[0]

    code = {}
    travel_down(code, root, "")

    return code

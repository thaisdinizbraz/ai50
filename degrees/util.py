class Node():
    def __init__(self, state, parent, action):
        self.state = state
        self.parent = parent
        self.action = action


class StackFrontier():
    def __init__(self):
        self.frontier = []
        self.frontierSet = set()

    def add(self, node):
        self.frontier.append(node)
        self.frontierSet.add(node.state)

    def contains_state(self, state):
        # Guarantee O(1) lookup
        return state in self.frontierSet

    def empty(self):
        return len(self.frontier) == 0

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.pop()
            self.frontierSet.remove(node.state)
            return node


class QueueFrontier(StackFrontier):

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[0]
            self.frontier = self.frontier[1:]
            return node

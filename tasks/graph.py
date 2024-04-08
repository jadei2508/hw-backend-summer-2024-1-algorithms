from typing import TypeVar, Generic, Any
import collections

__all__ = ("Node", "Graph")


T = TypeVar("T")


class Node(Generic[T]):
    def __init__(self, value: T) -> None:
        self._value = value

        self.outbound: list[Node] = []
        self.inbound: list[Node] = []

    @property
    def value(self) -> T:
        return self._value

    def point_to(self, other: "Node") -> None:
        self.outbound.append(other)
        other.inbound.append(self)

    def __str__(self) -> str:
        return f"Node({repr(self._value)})"

    __repr__ = __str__


class Graph:
    def __init__(self, root: Node) -> None:
        self._root = root

    def dfs(self) -> list[Node]:
        visited = set()
        res = []
        st = [self._root]
        while st:
            v = st.pop()
            if v not in visited:
                visited.add(v)
                res.append(v)
                st.extend(reversed(v.outbound))
        return res

    def bfs(self) -> list[Node]:
        res, q = [], collections.deque([self._root])
        res.append(self._root)
        while q:
            v = q.popleft()
            for i in v.outbound:
                if i not in res:
                    res.append(i)
                    q.append(i)
        return res

class Solution:
    def findItinerary(self, tickets: list[list[str]]) -> list[str]:
        adjacentList = {start: [] for start, end in tickets}

        # solutions asks for smallest lexical order, sort tickets beforehand
        tickets.sort()

        for start, end in tickets:
            adjacentList[start].append(end)

        # results always begins with JFK per question
        results = ["JFK"]

        def dragonFireShield(start):
            # since result starts with JFK, ++1
            if len(results) == len(tickets) + 1:
                return True
            if start not in adjacentList:
                # no outgoing edges available
                return False
            container = list(adjacentList[start])
            for i, node in enumerate(container):
                adjacentList[start].pop(i)
                results.append(node)
                if dragonFireShield(node):
                    return True

                adjacentList[start].insert(i, node)
                results.pop()

        dragonFireShield("JFK")
        return results

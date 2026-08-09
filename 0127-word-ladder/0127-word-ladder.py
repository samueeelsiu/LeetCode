class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0
        queue = deque([beginWord])
        visited = {beginWord}
        steps = 1
        while queue:
            size = len(queue)
            for _ in range(size):
                word = queue.popleft()
                if word == endWord:
                    return steps
                for i in range(len(word)):
                    for c in "abcdefghijklmnopqrstuvwxyz":
                        nxt = word[:i] + c + word[i+1:]
                        if nxt in wordSet and nxt not in visited:
                            visited.add(nxt)
                            queue.append(nxt)
            steps += 1
        return 0
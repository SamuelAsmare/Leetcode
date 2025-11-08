class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0 
        # impossible
        # hash table to store the nextwords
        # BFS
        wordList.append(beginWord)
        graph = defaultdict(list)  
        for word in wordList: 
            for i in range(len(word)):
                graph[word[:i] + "*" + word[i+1:]].append(word) # finding all patterns
        q = deque([(beginWord,1)])
        visited_words = set([beginWord])
        while q: # start BFS
            word , ans = q.popleft()
            if word == endWord:
                return ans
            # find all patterns of the word
            for i in range(len(word)):
                for nei in graph[word[:i] + "*" + word[i+1:]]:
                    if nei not in visited_words:
                        q.append((nei, ans+1))
                        visited_words.add(nei)
        return 0








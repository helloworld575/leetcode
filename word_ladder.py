import collections
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]

def word_ladder(beginWord,endWord,wordList):
    wordSet = set(wordList)
    queue = collections.deque([[beginWord, 1]])
    while queue:
        word,length = queue.popleft()
        if word == endWord:
            return length
        for i in range(len(word)):
            for chr in "qwertyuiopasdfghjklzxcvbnm":
                new_word = word[:i]+chr+word[i+1:]
                if new_word in wordSet:
                    queue.append((new_word,length+1))
                    wordSet.remove(new_word)
    return 0
print(word_ladder(beginWord,endWord,wordList))

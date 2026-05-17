class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        storage = {}

        for word in strs:
            sortedWord = "".join(sorted(word))
            if sortedWord in storage:
                storage[sortedWord].append(word)
            else:
                storage[sortedWord] = [word]
        
        return list(storage.values())
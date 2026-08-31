class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        pointWord1,pointWord2 = 0 , 0
        count = 0
        mergeWord = []

        while count < len(word1) + len(word2) :

            if pointWord1 < len(word1):
                mergeWord.append(word1[pointWord1])
                pointWord1 +=1
            if pointWord2 < len(word2):
                mergeWord.append(word2[pointWord2])
                pointWord2 +=1
            count +=1
        
        return "".join(mergeWord)
            
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:


        if not words or k <= 0:
            return []


        # create dict
        wordsDict = {}
        for word in words:
            if word in wordsDict:
                wordsDict[word] += 1
            else:
                wordsDict[word] = 1

        # create heap
        heap = [(-freq, word) for word, freq in wordsDict.items()]
        heapq.heapify(heap)

        # return top k results from heap

        '''
        output = []
        for i in range(k):
            item.heapq.heappop(heap)
            output.append(item[1])
        return output
        '''

        return [heapq.heappop(heap)[1] for _ in range(k)]

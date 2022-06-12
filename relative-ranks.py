class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:


        out = []

        medals = {1: "Gold Medal", 2: "Silver Medal", 3: "Bronze Medal"}
        order = {}

        heap = [] #min heap

        for i in score:
            heappush(heap, -1 * i)
            # heappush(heap, i)

        # print('heap:', (heap))


        position = 1

        while heap:
            s = -1 * heappop(heap)
            # s = heappop(heap)

            # if s >

            # if s in hashmap:
                # out.append(hashmap[s])


            # if counter in hashmap:
            #     out.append(hashmap[counter])
            # else:
            #     out.append(str(s))

            # counter += 1

            if position in medals:
                # out.append(hashmap[position])
                order[s] = medals[position]
            else:
                # out.append(str(s))
                order[s] = str(position)

            position += 1

            # print('heap:', (heap))

        # print(order)

        for s in score:

            out.append(order[s])

        return out

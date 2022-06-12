class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        print(tasks)
        print(n)

        heap = []



        for i in tasks:
            heappush(heap, i)

        print(heap)


        unique_tasks = 0
        last_task = None

        hashmap = {}

        while heap:

            i = heappop(heap)

            # if i == last_task:
                # unique_tasks += 1
            # else:
                # last_task = i

            if i not in hashmap:
                hashmap[i] = 1
            else:
                hashmap[i] += 1

            # hashmap[i] += 1
            unique_tasks = max(unique_tasks, hashmap[i])

            # print(i)

        print(unique_tasks)
        print(hashmap)

        sleep = 0

        result = (unique_tasks - 1) * (n + 1)

        for k, v in enumerate(hashmap):
            # print(k, v)
            # print(hashmap[v])

            if sleep >= n:
                break

            # hold = ceil(hashmap[v] / 2)
            hold = hashmap[v] - 1
            # if hold > 0:
                # sleep += hold
            # else:
                # sleep += 1

            if hashmap[v] == unique_tasks:
                result += 1


        # print(ceil(3 / 2))

        print(sleep)

        # return len(hashmap) + sleep

        return max(result, len(tasks))

        return len(tasks) + sleep

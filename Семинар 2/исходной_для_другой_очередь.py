import queue

def is_subsequence(a, b):
    q = queue.Queue()
    for char in a:
        q.put(char)

    for char in b:
        if not q.empty() and q.queue[0] == char:
            q.get()

    return q.empty()

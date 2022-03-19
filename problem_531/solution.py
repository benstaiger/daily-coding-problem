
# This problem was asked Microsoft.
# 
# Using a read7() method that returns 7 characters from a file, implement
# readN(n) which reads n characters.
# 
# For example, given a file with the content “Hello world”, three read7()
# returns “Hello w”, “orld” and then “”.

def mock_read7():
    data = "this is a kind of long string of text."
    idx = 0
    while idx + 7 < len(data):
        yield data[idx:idx+7]
        idx += 7
    yield data[idx:]


def readN(n, read7):
    output = []
    total_read = 0
    if hasattr(readN, "buffer") and readN.buffer:
        total_read += len(readN.buffer)
        output.append(readN.buffer)
        readN.buffer = None
    while (total_read + 7) <= n:
        try:
            output.append(next(read7))
            total_read += 7
        except StopIteration:
            return "".join(output)
    
    if total_read < n:
        try:
            leftover = next(read7)
            output.append(leftover[:n - total_read])
            readN.buffer = leftover[n - total_read:]
        except Exception:
            pass
    return "".join(output)

gen =  mock_read7()
for i in range(15):
    print(readN(8, gen))
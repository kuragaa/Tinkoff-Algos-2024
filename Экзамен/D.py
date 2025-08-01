def check_tests(count, computers, tl):
    completed = 0
    for process_t, sent_count, setup_t in computers:
        dur = sent_count * process_t + setup_t
        full = tl // dur
        completed += full * sent_count + min(sent_count, (tl % dur) // process_t)
        if completed >= count:
            return True
    return False


def bin_search(tc, comps):
    left, right = 0, 10 ** 18
    while left < right:
        mid = (left + right) // 2
        if check_tests(tc, comps, mid):
            right = mid
        else:
            left = mid + 1
    return left


test_count, count = map(int, input().split())
comps = [tuple(map(int, input().split())) for _ in range(count)]
ot = bin_search(test_count, comps)
dist = [0] * count
for i, (process_t, sent_count, setup_t) in enumerate(comps):
    if test_count == 0:
        break
    dur = sent_count * process_t + setup_t
    full = ot // dur
    mpt = full * sent_count + min(sent_count, (ot % dur) // process_t)
    dist[i] = min(mpt, test_count)
    test_count -= dist[i]
print(ot)
print(' '.join(map(str, dist)))
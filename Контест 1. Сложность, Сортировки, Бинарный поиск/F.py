def merge_sort(a, b, count):
    res = []
    i = 0  # два указателя
    j = 0

    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            res.append(a[i])
            i += 1
        else:
            count += len(a) - i 
            res.append(b[j])
            j += 1
    res += a[i:] + b[j:]  
    return res, count


def split_list(arr, count):
    mid = len(arr) // 2  
    a = arr[:mid]  
    b = arr[mid:]  

    if len(a) > 1:  
        a, count = split_list(a, count)
    if len(b) > 1:
        b, count = split_list(b, count)

    res, count = merge_sort(a, b, count)  
    return res, count


n = int(input())
a = [int(i) for i in input().split()]
count = 0
res, count = split_list(a, count)
print(count)
print(*res)
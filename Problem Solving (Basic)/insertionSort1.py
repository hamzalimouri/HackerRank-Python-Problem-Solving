def insertionSort1(n, arr):
    for i in range(len(arr) - 1, 0, -1):
        x = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > x:
            arr[j + 1] = arr[j]
            j -= 1
            print(' '.join(map(str, arr)))
        arr[j + 1] = x
    print(' '.join(map(str, arr)))
    

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)

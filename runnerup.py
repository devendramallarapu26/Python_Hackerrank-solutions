    # Given list is[2,3,6,6,5] . The maximum score is 6, second maximum is 5. Hence, we print 5 as the runner-up score.
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    arr = list(set(arr))
    print(arr[-2])


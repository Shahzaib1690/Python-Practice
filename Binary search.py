list = [5,2,1,6,7,3,4,8,9,0]

list.sort()
print(list)
pos = 0
def binary(list):
    n = int(input("Enter a number you wanna search"))
    min = 0
    max = len(list) -1

    while min <= max:
        mid = (min + max) // 2

        if list[mid] == n:
            print("You Searched number is ",list[mid] ," at Position ",mid+1)
            break
        else:
            if list[mid] > n:
                max = mid-1
            else:
                min = mid+1
    else:
        print("Not Found")


binary(list)
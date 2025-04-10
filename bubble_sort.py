#Write a program in python to implement Bubble sort using functions.
# Branch: Computer Engineering
# Year: 2nd year
# Sem: IV
# Subject : SKL Python
# Name: Shaikh Tasneem Azharul
# UIN: 231P043
# Roll No: 41

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def main():
    arr = list(map(int, input("Enter the elements of the array separated by space: ").split()))
    print("Original array:", arr)
    bubble_sort(arr)
    print("Sorted array:", arr)

if __name__ == "__main__":
    main()
print("Name: Shaikh Tasneem Azharul\nUIN: 231P043\nRoll No: 41")
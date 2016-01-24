__author__ = 'parvez'
def sort():
    array_a = [1, 20, 31, 45, 50]
    array_b = [10, 12, 17, 70]
    for element in array_b:
        last_index = len(array_a)-1
        if element >= array_a[last_index]:
            array_a.append(element)
        else:
            index = last_index
            # insert element at the last
            array_a.append(None)
            # insertion sort
            while index > 0 and array_a[index] >= element:
                array_a[index+1] = array_a[index]
                index -= 1
            array_a[index+1] = element
    print(array_a)

def main():
   sort()

if __name__ == "__main__":
    main()


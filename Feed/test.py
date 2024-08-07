
def palinderome(string):
    
    for i in range(len(string)//2):
        if string[i] == string[len(string)-i-1]:
            return True
        else:
            False


print(palinderome("MalayalaM"))


def revers_array(array):
    
    for i in range(len(array)//2):
        
        array[i],array[len(array)-1-i] = array[len(array)-1-i],array[i]
        
    return array


print(revers_array([1,2343,23,23,123]))


def Middle(array):
    
    for i in range(len(array)):
        
        if i == len(array)//2:
            return array[i]
        
    return False


print(Middle([1,2,3,4,5,6]))


def remove_dublicate(array):
    return list(set(array))

print(remove_dublicate([1,2,3,4,5,2,3,21]))


def large(array):
    
    largest=array[0]
    
    for i in array:
        if i > largest:
            largest = i
    return largest


print(large([1,2,3,4,5,6,33,4]))

def sum_of_the_array(array):
    sum_of = 0
    
    for i in array:
        sum_of += i
        
    return sum_of

print(sum_of_the_array([1,2]))

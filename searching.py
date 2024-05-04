def linear_search(l, item, issorted=False):
    if type(item) == float or int and type(l) == type(list):   
        for i in range(len(l)):
            if l[i] == item:
                return i
    else: 
        return None


def binary_search(l, item, issorted=False):
    if type(item) == float or int and type(l) == type(list):
        min = 0 
        max = len(l)-1
        if issorted == False:
            return(linear_search(l, item, issorted = False)) 
        while (min <= max):
            mean = (max + min)//2
            if l[mean] == item:
                return mean
            elif l[mean] > item:
                max = mean -1
            else:
                min = mean + 1
    else:
        return None

'''
Created on 2016-4-5

@author: huikeli
'''

def decomposeEven(path):
    first = []
    second = []
    
    for index in range(len(path)/2):
        first.append(path[index]+path[index+1]);
        
    for index in range(len(path)/2+1, len(path))[::-1]:
        second.append(path[index]+path[index-1]);
    
    result = [first, second]
#     print result
    return result

def decomposeOdd(path):
    first = []
    second = []
    
    a = ''
    if len(path)/2-1 <= 0:
        a = path[0]
    for index in range(len(path)/2-1):
        first.append(path[index]+path[index+1]);
        a = path[index+1]
    first.append(a+'*')
    
    if len(path)/2-1 <= 0:
        a = path[1]    
    for index in range(len(path)/2+1, len(path))[::-1]:
        second.append(path[index]+path[index-1]);
        a = path[index-1]
        
    second.append(a+'*')
    
    result = [first, second]
#     print result
    return result

def decompose(path):
    if (len(path) % 2) == 0:
       return decomposeOdd(path)
    else:
       return decomposeEven(path)
if __name__ == '__main__':
    decompose('MA')
    decompose('AMKADA')
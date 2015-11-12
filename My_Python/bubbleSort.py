def bubbleSort(alist):
    for j in range(len(alist)-1,0,-1):
        #print(len(alist))
        #print(passnum) 
        for i in range(j):
            if alist[i] > alist[i+1]:
                alist[i] , alist[i+1] = alist[i+1] , alist[i]
            print alist

def main():
        alist = [10003,77,3,123,12]
        print(bubbleSort(alist))

if __name__ == '__main__':
        main()
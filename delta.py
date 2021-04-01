import sys
import os

#probe = ./ + argv[2] + correct_list_string

# os.system(is-interesting())

def dd(P, candidate, interesting_function):

    if(len(candidate) == 1):
        return candidate #THIS HAS TO BE A SET

    candidate = list(candidate)

    p1 = candidate[0:len(candidate)//2]
    p2 = candidate[len(candidate)//2:] #-1?

    # print("p1: ", p1) 
    # print("p2: ", p2)

    P1 = set(p1)
    P2 = set(p2)

    # print("P: ", P)
    # print("P1: ", P1)
    # print("P2: ", P2)

    union1 = P.union(P1)
    P1_as_string = " ".join( map(str, union1))
    # if interesting(P U P1)=yes return dd(P,P1)
    if (os.system(interesting_function + " " + P1_as_string) != 0):
        return dd(P,P1, interesting_function)
        
    union2 = P.union(P2)
    P2_as_string = " ".join( map(str, union2))
    #if interesting(P U P2)=yes return dd(P, P2)
    if (os.system(interesting_function + " " + P2_as_string) != 0):
        return dd(P, P2, interesting_function)

    # else return dd(P U P2, P1) U dd(P U P1, P2)
    else:
        return dd(P.union(P2), P1, interesting_function).union(dd(P.union(P1), P2, interesting_function))

def main():
    size_of_set = sys.argv[1]
    interesting = sys.argv[2]

    starting_list = list( range (int(size_of_set)))
  
    p = []
    P = set(p)

    nums = dd(P, starting_list, interesting)
    numslist = list(nums)
    numslist.sort()

    print(numslist)

if __name__ == '__main__':
    main()

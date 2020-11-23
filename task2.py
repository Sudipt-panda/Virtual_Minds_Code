#####
def jumps(A,B,D):
    s=A
    c=0
    while True:
       s+=D
       c+=1
       if s>=B:
           break
    return c
######
def main():
    print(jumps(10,85,30))
######
main()
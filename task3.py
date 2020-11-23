def zeros(n):
    s=bin(n)[2:]
    prev=0
    a=[]
    for i in range(len(s)):
        if s[i]=='1':
            #print(s[prev+1:i])
            #print(len(s[prev+1:i]))
            a.append(len(s[prev+1:i]))
            prev=i
    return max(a)
    
########
def main():
    print(zeros(168000))
########
main()
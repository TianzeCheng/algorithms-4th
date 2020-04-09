class ShellSort (object):
    @staticmethod
    def sort(a):
        N = len(a)
        h = 1
        while h < N / 3:
            h = h * 3 + 1
        while h>=1:
            h=int(h)
            for i in range(h,N):
                j=i
                while j>=h:
                    if a[j]<a[j-h]:
                        temp=a[j]
                        a[j]=a[j-h]
                        a[j-h]=temp
                    j-=h
            h=h/3
    
if __name__=='__main__':
    a=[2,3,5,2,56,7,3,7,4,2,90,1]
    print(a)
    ShellSort.sort(a)
    print(a)

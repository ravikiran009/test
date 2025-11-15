from random import randint
class window:
    def __init__(self):
        self.len=10
        self.wid=10
        self.arr=list()
        self.score=0
    def h_block(self):
        l=randint(1,self.wid//2)
        print(f'len---{l}')
        idx = int(input("Enter index: "))
        idx=min(idx,self.wid-l)
        l=self.wid-idx if idx+l>self.wid else l
        for i in range(len(self.arr)):
            if self.arr[i][idx:idx+l]==list('*')*l:
                for j in range(idx,idx+l):
                    self.arr[i][j]='1'
                return []
        ls=['*' for _ in range(idx)]
        l=min(self.wid-idx,l)
        ls.extend(['1' for _ in range(l)])
        if self.wid-idx-l>0:
            ls.extend(['*' for _ in range(self.wid-idx-l)])
        return ls
    def v_block(self):
        l=randint(1,self.wid//2)
        print(f'len---{l}')
        idx = int(input("Enter index: "))
        idx=min(idx,9)
        for i in range(len(self.arr)):
            if l and self.arr[i][idx]=='*':
                while i<len(self.arr) and l:
                    self.arr[i][idx]='1'
                    i+=1
                    l-=1
        ls=['*' for _ in range(self.wid)]
        ls[idx]='1'
        return [ls.copy() for _ in range(l)]
    def block(self):
        i=randint(0,10)
        print('Insert horizontal') if i%2==0 else print('Insert vertical')
        block = self.h_block() if i%2==0 else self.v_block()
        if not block:
            return
        self.arr.append(block) if i%2==0 else self.arr.extend(block)
    def print(self):
        ids=[i for i in range(self.wid)]
        for i in ids:
            print(i,end=" ")
        ids=[]
        r=len(self.arr)-1
        print()
        print(('# '*self.wid).rstrip(' '))
        for i in self.arr[-1::-1]:
            for j in i:
                if j=='1' and len(set(i))==1:
                    ids.append(r)
                    self.score+=100
                    continue
                print(f'{j}',end=" ")
            r-=1
            print()
        print(f'-------Rows-------{len(self.arr)}-------Score-------{self.score}')
        

if __name__=="__main__":
    w = window()
    w.print()
    while True:
        w.block()
        if len(w.arr)>=w.len:
            print("Game Over!!!")
            break
        w.print()
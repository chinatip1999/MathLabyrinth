# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 19:18:47 2020
@author: Chinatip
"""

"""
This is Math Labyrinth Game implementation
Rules:
    - there is start region ('0' blocks)
    - there is end region ('-1' blocks)
    - try to create path from start region to end region
    - next block in path must higher than current block by 1
    -------------------------
    | 0 | 0 | 0 | 0 | 1 | 2 |
    -------------------------
    | 1 | 1 | 3 | 4 | 4 | 3 |
    -------------------------
    | 2 | 3 | 4 | 4 | 2 | 6 |
    -------------------------
    | 3 | 6 | 5 | 5 | 6 | 5 |
    -------------------------
    | 1 | 7 | 4 | 8 | 7 | 8 |
    -------------------------
    | -1| -1| -1| 9 | 3 | 4 |
    -------------------------
"""

"""
This part is an implementation of each block in the game
Each contains:
- data of itself as data
- its neighbors
- possible block
"""
class block:
    data=0
    u=0
    d=0
    l=0
    r=0
    init=0
    nxt=0
    before=0
    def __init__(self,data,u,d,l,r):
        self.data=data
        self.u=u
        try:
            u.d=self
        except:
            print('',end='')
        self.d=d
        try:
            d.u=self
        except:
            print('',end='')
        
        self.l=l
        try:
            l.r=self
        except:
            print('',end='')
        
        self.r=r
        try:
            r.l=self
        except:
            print('',end='')
    def __repr__(self):
        return str(self.data)
    def path(self):
        p=[]
        try:
            if self.u.data-self.data==1:
                p.append(self.u)
        except:
            print('',end='')
        try:
            if self.d.data-self.data==1:
                p.append(self.d)
        except:
            print('',end='')
        try:
            if self.l.data-self.data==1:
                p.append(self.l)
        except:
            print('',end='')
        try:
            if self.r.data-self.data==1:
                p.append(self.r)
        except:
            print('',end='')
        self.nxt=p
        return p
        
class MathL:
    data=[]
    m=[]
    def __init__(self,n):
        self.data=n
        self.m=[]
        for i in range(len(n)):
            l=[]
            for j in range(len(n[i])):
                if n[i][j]==0:
                    a=block(0,-99,-99,-99,-99);
                    a.init=True
                else:
                    a=block(n[i][j],-99,-99,-99,-99)
                    a.init=False
                try:
                    a.l=l[-1]
                except:
                    print('xl')
                try:
                    l[-1].r=a
                except:
                    print('xll')
                try:
                    a.u=self.m[i-1][j]
                except:
                    print('xu')
                try:
                    self.m[i-1][j].d=a
                except:
                    print('xuu')
                l.append(a)
            self.m.append(l)
        
test=[[ 0, 0, 0, 0, 1, 2],
      [ 1, 1, 3, 4, 4, 3],
      [ 2, 3, 4, 4, 2, 6],
      [ 3, 6, 5, 5, 6, 5],
      [ 1, 7, 4, 8, 7, 8],
      [-1,-1,-1, 9, 3, 4]]
a=MathL(test)
r=[]
for i in test:
    l=[]
    for j in i:
        if j==0:
            l.append(1)
        elif j==-1:
            l.append(1)
        else:
            l.append(0)
    r.append(l)
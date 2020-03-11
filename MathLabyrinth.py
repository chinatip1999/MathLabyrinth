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
    |*0*|*0*|*0*|*0*| 1 | 2 |
    -------------------------
    ||1|| 1 | 3 | 4 | 4 | 3 |
    -------------------------
    ||2||=3=||4|| 4 | 2 | 6 |
    -------------------------
    | 3 |=6=||5|| 5 | 6 | 5 |
    -------------------------
    | 1 ||7|| 4 | 8 | 7 | 8 |
    -------------------------
    |*-1|*-1|*-1| 9 | 3 | 4 |
    -------------------------
"""

"""
This part is an implementation of each block in the game
Each contains:
- data of itself as data
- its neighbors as u,d,l,r
- possible block as nxt
"""
import time
class stack:
    d=[]
    def __init__(self):
        self.d=[]
    def push(self,a):
        self.d.insert(0,a)
    def pop(self):
        return
class block:
    """
    data field
    """
    data=0
    u=0
    d=0
    l=0
    r=0
    nxt=0
    visited=0
    valid=0
    parent=0
    def __init__(self,data,u,d,l,r):
        """
        Block object initialization
        """
        """ defines self data"""
        self.data=data
        """
        insert upper block and check if set lower block of
        the upper is possible then set. else, then discard.
        and apply to down left and right as well
        """
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
        """ to print the block"""
        return str(self.data)
    
    def path(self):
        p=[]
        """ in case of starting block, add all possible
        (neighbor and not 0 (start block))
        """
        if self.data==0:
            if type(self.u)==block and self.u.data!=0:
                p.append(self.u)
            if type(self.d)==block and self.d.data!=0:
                p.append(self.d)
            if type(self.l)==block and self.l.data!=0:
                p.append(self.l)
            if type(self.r)==block and self.r.data!=0:
                p.append(self.r)
            self.nxt=p
            return p
        
        """check if there is a possible way to walk by 
        check neighbor's data (n+1 blocks is u,d,l,r)
        if d(n+1)-d(n)=k then add n+1 block to path list"""
        k=1
        try:
            if self.u.data-self.data==k or self.u.data==-1:
                p.append(self.u)
        except:
            print('',end='')
        try:
            if self.d.data-self.data==k or self.d.data==-1:
                p.append(self.d)
        except:
            print('',end='')
        try:
            if self.l.data-self.data==k or self.l.data==-1:
                p.append(self.l)
        except:
            print('',end='')
        try:
            if self.r.data-self.data==k or self.r.data==-1:
                p.append(self.r)
        except:
            print('',end='')
        self.nxt=p
        return p
    
    def detail(self):
        """ represent data of each block in path """
        txt=''
        txt+='data: '+str(self.data)+'\nvisited: '+str(self.visited)
        print(txt)
        for i in self.nxt:
            i.detail()
        
            
    def walk(self):
        """
        walk recursively to define each block wether 
        it's valid or invalid block in path
        """
        print(self.data)
        self.path()
        print(self.nxt)
        if self.data==-1:
            self.visited=1
            self.valid=1
            self.addpath(self)
            print('reached')
            return -1
        
        if self.nxt==[]:
            self.visited=1
            self.valid=0
            print('can\'t move anymore')
            return 0
        else:
            v=0
            self.visited=1
            for i in self.nxt:
                a=i.walk()
                if a==0:
                    print(str(i.data)+'is invalid')
                elif a==-1:
                    self.addpath(i)
                    v=1
                    print(str(i.data)+'is valid')
            if v==0:
                self.valid=0
                print(str(self.data)+'(self) is invalid')
                return 0
            else:
                self.valid=1
                print(str(self.data)+'(self) is valid')
                return -1
            
    
    way=[]
    tmp=[]
    def addpath(self,a):
        """
        under development
        """
        self.tmp.insert(0,a)
        print(self.tmp)
        if a.data==0:
            self.way.append([self.tmp])
            print(self.tmp)
            self.tmp=[]
            
        
        
class MathL:
    data=[]
    m=[]
    start=[]
    def __init__(self,n):
        """
        add list data and convert to map
        in case of edge, -99 will be replaced instead of block
        """
        self.data=n
        self.m=[]
        for i in range(len(n)):
            l=[]
            for j in range(len(n[i])):
                if n[i][j]==0:
                    a=block(0,-99,-99,-99,-99);
                    a.init=True
                    self.start.append(a)
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
            
    def path(self):
        """
        start find path
        """
        a=time.time_ns()
        for i in self.start:
            i.walk()
        b=time.time_ns()
        print(b-a)
            
    def visit(self):
        """
        show visited block
        """
        for i in self.m:
            for j in i:
                print(j.visited,end=' ')
            print('')
    def valid(self):
        """
        show valid block (valid is a part of path)
        """
        for i in self.m:
            for j in i:
                print(j.valid,end=' ')
            print('')
            
    def result(self):
        """
        show valid path (valid is a part of path)
        """
        for i in self.m:
            for j in i:
                if j.valid==1:
                    txt='{:2d}'.format(j.data)
                    print(txt,end=' ')
                else:
                    print('  ',end=' ')
            print('')
    def explain(self):
        """
        show valid path (valid is a part of path)
        """
        for i in self.m:
            for j in i:
                if j.visited==1:
                    txt='{:2d}'.format(j.data)
                    print(txt,end=' ')
                else:
                    print('  ',end=' ')
            print('')
test=[[ 0, 0, 0, 0, 1, 2],
      [ 1, 1, 5, 6, 7, 3],
      [ 2, 3, 4, 4, 8, 6],
      [ 3, 6, 5, 5, 9, 10],
      [ 1, 7, 4, 8, 7, 11],
      [-1,-1,-1, 14, 13, 12]]
#test=[[0,0,1,3,4,7,10,4,13,11],
#      [1,2,3,5,5,9,12,6,17,15],
#      [3,5,7,7,9,11,14,7,12,14],
#      [5,7,9,13,11,13,16,8,15,17],
#      [7,11,12,15,16,15,18,9,12,16],
#      [9,9,10,17,18,17,19,13,8,14],
#      [11,13,11,16,20,23,21,23,25,12],
#      [13,15,25,27,29,25,23,24,27,29],
#      [15,2,23,15,31,27,24,27,30,31],
#      [17,19,21,25,33,35,37,39,-1,-1]]
a=MathL(test)
a.path()
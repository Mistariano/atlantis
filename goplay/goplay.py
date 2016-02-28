#coding=utf8

__author__ = 'MisT'

from gopoint import GoPoint
import os
import copy

class GoPlay:
    MAXC=1000
    def __init__(self, size):
        self.cntC=0
        # self.bestFriend=BloomFilter(capacity=GoPlay.MAXC)
        self.valueSet=set([])
        self.size = size
        self.MIN=0
        self.MAX=self.size+1
        self.isPass=0
        self.nextPlayer=True
        self.board=[[GoPoint(x=i,y=j,color=GoPoint.NULL) for j in range(0,self.MAX+1)]for i in range(0,self.MAX+1)]
        for i in range(self.MIN,self.MAX+1):
            self.board[self.MIN][i].become_wall()
            self.board[self.MAX][i].become_wall()
            self.board[i][self.MAX].become_wall()
            self.board[i][self.MIN].become_wall()

    def loop(self):
        while not self.end():
            # self.output()
            self.getXY()
            i=0
            while self.move():
                i+=1
                if i > 1000:
                    print'move too much'
                    os.system('pause')
                self.getXY()
            if self.isPass:
                if self.x==-1:
                    self.isPass+=1
                else:
                    self.isPass=0
            self.cleanFrbidn()
            self.nextPlayer=not self.nextPlayer

    def getX(self,x):
        self.x=x

    def getY(self,y):
        self.y=y

    def getXY(self):
        self.getX()
        self.getY()

    def move(self):
    #判断虚手：
        if self.x==-1:
            if not self.isPass:
                self.isPass=1
            return 0
    #判断落子合法性：
        if self.board[self.x][self.y].color!=GoPoint.NULL:
            print 'You can not move here'
            return 1
    #确定当前颜色：
        if self.nextPlayer:
            color=GoPoint.BLACK
        else:
            color=GoPoint.WHITE
    #禁止自填真眼：
        cnt1=0
        cnt2=0
        for i in[[self.x+1,self.y],[self.x-1,self.y],[self.x,self.y+1],[self.x,self.y-1]]:
            if self.board[i[0]][i[1]].color==color:
                cnt1+=1
            elif self.board[i[0]][i[1]].color==GoPoint.WALL:
                cnt2+=1
        if cnt1+cnt2==4:
            for i in [[self.x+1,self.y+1],[self.x-1,self.y-1],[self.x-1,self.y+1],[self.x+1,self.y-1]]:
                if self.board[i[0]][i[1]].color==color:
                    cnt1+=1
                elif self.board[i[0]][i[1]].color==GoPoint.WALL:
                    cnt2+=1
            if (not cnt2) and (cnt1>=7):
                self.board[self.x][self.y].become_frbidn()
                return 1
            elif cnt2+cnt1==8:
                self.board[self.x][self.y].become_frbidn()
                return 1
    #备份：
        safeCopy=copy.deepcopy(self.board)
    #着子：
        self.board[self.x][self.y].move(color=color)
    #数气：
        for i in [[self.x+1,self.y],[self.x-1,self.y],[self.x,self.y+1],[self.x,self.y-1]]:
            if self.board[i[0]][i[1]].qi==-1:
                self.board[self.x][self.y].qi+=1
                self.board[self.x][self.y].qiGroup+=1
    #紧气：
        for i in [[self.x+1,self.y],[self.x-1,self.y],[self.x,self.y+1],[self.x,self.y-1]]:
            if self.board[i[0]][i[1]].qi>0:
                self.board[i[0]][i[1]].qi-=1
                f=self.groupFind(g=i)
                self.board[f[0]][f[1]].qiGroup-=1
        someoneDie=False
        for i in [[self.x+1,self.y],[self.x-1,self.y],[self.x,self.y+1],[self.x,self.y-1]]:
            if self.board[i[0]][i[1]].qi>=0:
            #连子：
                if self.board[i[0]][i[1]].color==color:
                    self.groupUnion(g1=[self.x,self.y],g2=i)
            #提子：
                else:
                    if not self.groupQi(g=i):
                        self.groupGoDie(g=self.groupFind(g=i))
                        someoneDie=True
    #检查合法性：
        if not (someoneDie or self.groupCheck(g=[self.x,self.y])):
            self.board=copy.deepcopy(safeCopy)
            self.board[self.x][self.y].become_frbidn()
            return 1
    #禁全局同形：
        v=self.boardValue()
        # self.copyValue(copy=safeCopy)
        # if v in self.bestFriend:
        if v in self.valueSet:
            self.board=copy.deepcopy(safeCopy)
            self.board[self.x][self.y].become_frbidn()
            return 1
        # self.bestFriend.add(v)
        self.valueSet.add(v)
        # self.cntC+=1
        # if self.cntC>=GoPlay.MAXC:
        #     print 'bf is too little,continue?'
        #     os.system('pause')
        #     self.MAXC*=2
        #     new=BloomFilter(capacity=GoPlay.MAXC)
        #     self.bestFriend=new.union(other=self.bestFriend)
    #结束：
        return 0

    def cleanFrbidn(self):
        for i in range(1,self.MAX):
            for j in range(1,self.MAX):
                if self.board[i][j].qi==-1:
                    self.board[i][j].color=GoPoint.NULL

    def end(self):
        if self.isPass!=4:
            return 0
        self.res_cnt={GoPoint.BLACK:0,GoPoint.WHITE:0}
        for i in range(1,self.MAX):
            for j in range(1,self.MAX):
                if self.board[i][j].qi>=0:
                    self.res_cnt[self.board[i][j].color]+=1
                else:
                    tmp=-1
                    flag=True
                    for p in [[i+1,j],[i,j+1],[i-1,j],[i,j-1]]:
                        if self.board[p[0]][p[1]].qi>0:
                            c=self.board[p[0]][p[1]].color
                            if tmp==-1:
                                tmp=c
                                continue
                            if tmp!=c:
                                flag=False
                                break
                    if tmp!=-1 and flag:
                        self.res_cnt[tmp]+=1
        if self.res_cnt[GoPoint.BLACK]>self.res_cnt[GoPoint.WHITE]:
            self.win=1
        else:
            self.win=0
        return 1


    def groupQi(self,g):
        g=self.groupFind(g=g)
        return self.board[g[0]][g[1]].qiGroup

    def groupFind(self,g):
        if self.board[g[0]][g[1]].group==g:
            return g
        self.board[g[0]][g[1]].group=self.groupFind(self.board[g[0]][g[1]].group)
        return self.board[g[0]][g[1]].group


    def groupUnion(self,g1,g2):
        group1=self.groupFind(g=self.board[g1[0]][g1[1]].group)
        group2=self.groupFind(g=self.board[g2[0]][g2[1]].group)
        father1=self.board[group1[0]][group1[1]]
        father2=self.board[group2[0]][group2[1]]
        if group2!=group1:
            if father1.groupRank<father2.groupRank:
                father1.group=group2
                father2.member.append(group1)
                father2.qiGroup+=father1.qiGroup
            if father1.groupRank>father2.groupRank:
                father2.group=group1
                father1.member.append(group2)
                father1.qiGroup+=father2.qiGroup
            if father1.groupRank==father2.groupRank:
                father1.group=group2
                father2.groupRank+=1
                father2.member.append(group1)
                father2.qiGroup+=father1.qiGroup

    def groupCheck(self,g):
        if not self.groupQi(g=g):
            return 0
        if self.groupQi(g=g)<=4 and self.groupFind(g=g)!=[self.x,self.y]:
            points=[]
            if self.groupBadmove(g=g,points=points):
                return 0
        return 1

    def groupBadmove(self,g,points):
        if self.board[g[0]][g[1]].qi>1:
            return 0
        if self.board[g[0]][g[1]].qi==1:
            for i in [[g[0],g[1]+1],[g[0]+1,g[1]],[g[0],g[1]-1],[g[0]-1,g[1]]]:
                if self.board[i[0]][i[1]].qi==-1:
                    if not (i in points):
                        if len(points):
                            return 0
                        points.append(i)
        for member in self.board[g[0]][g[1]].get_member():
            if not self.groupBadmove(g=member,points=points):
                return 0
        return 1


    def groupGoDie(self,g):
        for member in self.board[g[0]][g[1]].get_member():
            self.groupGoDie(g=member)
        self.board[g[0]][g[1]].die()
        done=self
        for i in [[g[0]+1,g[1]],[g[0]-1,g[1]],[g[0],g[1]+1],[g[0],g[1]-1]]:
                if self.board[i[0]][i[1]].qi>=0:
                    self.board[i[0]][i[1]].qi+=1
                    f=self.groupFind(g=i)
                    self.board[f[0]][f[1]].qiGroup+=1


    def draw(self):
        return [[self.board[i][j].output() for j in range(1,self.MAX)]for i in range(1,self.MAX)]

    def boardValue(self):
        ans=0
        for i in range(1,self.MAX):
            for j in range(1,self.MAX):
                ans+=self.board[i][j].output()
                ans<<=2
        #print ans
        return ans
    def copyValue(self,copy):
        ans=0
        for i in range(1,self.MAX):
            for j in range(1,self.MAX):
                ans+=copy[i][j].output()
                ans<<=2
        #print ans
        return ans
    def output(self):
        print self.draw()

if __name__ == '__main__':
    a=GoPlay(19)
    a.output()
    a.loop()


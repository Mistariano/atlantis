#coding=utf8

__author__ = 'MisT'

from gopoint import GoPoint
from pybloom import BloomFilter
import os
import copy

class GoPlay:

    def __init__(self, size):
        self.MAXC=1000
        self.cnt_c=0
        self.bf=BloomFilter(capacity=self.MAXC)
        self.size = size
        self.MIN=0
        self.MAX=self.size+1
        self.is_pass=0
        # self.board=[[0 for j in range(0,size+2)]for i in range(0,size+2)]
        self.board=[[GoPoint(x=i,y=j,color=GoPoint.NULL) for j in range(0,self.MAX+1)]for i in range(0,self.MAX+1)]
        #print board
        for i in range(self.MIN,self.MAX+1):
            # self.board[self.MIN][i] = GoPlay.WALL
            # self.board[self.MAX][i] = GoPlay.WALL
            # self.board[i][self.MAX] = GoPlay.WALL
            # self.board[i][self.MIN] = GoPlay.WALL
            self.board[self.MIN][i].become_wall()
            self.board[self.MAX][i].become_wall()
            self.board[i][self.MAX].become_wall()
            self.board[i][self.MIN].become_wall()
        # self.group=[[[i,j]for j in range(1,self.MAX)]for i in range(1,self.MAX)]

    def loop(self):
        self.nextPlayer=True
        while not self.end():

            self.get_xy()
            # self.get_x()
            # self.get_y()
            i=0
            # print 'moving...'
            while self.move():
                i+=1
                if i > 1000:
                    print'move too much'
                    os.system('pause')
                self.get_xy()
            # print self.nextPlayer,'to',self.x,self.y
            if self.is_pass:
                if self.x==-1:
                    self.is_pass+=1
                else:
                    self.is_pass=0
            self.clean_frbidn()
            # self.scan()
            # self.output()
            self.nextPlayer=not self.nextPlayer

    def get_x(self,x):
        self.x=x

    def get_y(self,y):
        self.y=y

    def get_xy(self):
        self.get_x()
        self.get_y()

    def move(self):
    #判断虚手：
        if self.x==-1:
            if not self.is_pass:
                self.is_pass=1
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
        safe_copy=copy.deepcopy(self.board)
    #着子：
        self.board[self.x][self.y].move(color=color)
    #数气：
        for i in [[self.x+1,self.y],[self.x-1,self.y],[self.x,self.y+1],[self.x,self.y-1]]:
            if self.board[i[0]][i[1]].qi==-1:
                self.board[self.x][self.y].qi+=1
                self.board[self.x][self.y].qi_group+=1
    #紧气：
        for i in [[self.x+1,self.y],[self.x-1,self.y],[self.x,self.y+1],[self.x,self.y-1]]:
            if self.board[i[0]][i[1]].qi>0:
                self.board[i[0]][i[1]].qi-=1
                f=self.group_find(g=i)
                self.board[f[0]][f[1]].qi_group-=1
        someone_die=False
        for i in [[self.x+1,self.y],[self.x-1,self.y],[self.x,self.y+1],[self.x,self.y-1]]:
            if self.board[i[0]][i[1]].qi>=0:
            #连子：
                if self.board[i[0]][i[1]].color==color:
                    self.group_union(g1=[self.x,self.y],g2=i)
            #提子：
                else:
                    if not self.group_qi(g=i):
                        self.group_godie(g=self.group_find(g=i))
                        someone_die=True
    #检查合法性：
        #print 'now checking',[self.x,self.y]
        if not (someone_die or self.group_check(g=[self.x,self.y])):
            self.board=copy.deepcopy(safe_copy)
            self.board[self.x][self.y].become_frbidn()
            return 1
        #print 'allright.'
        #print 'qi:',self.board[self.x][self.y].qi
    #禁全局同形：
        v=self.board_value()
        self.copy_value(copy=safe_copy)
        if v in self.bf:
            self.board=copy.deepcopy(safe_copy)
            self.board[self.x][self.y].become_frbidn()
            return 1
        self.bf.add(v)
        self.cnt_c+=1
        if self.cnt_c>=self.MAXC:
            print 'bf is too little,continue?'
            os.system('pause')
            self.MAXC*=2
            new=BloomFilter(capacity=self.MAXC)
            self.bf=new.union(other=self.bf)
    #结束：
        return 0

    # def scan(self):
    #     pass
    def clean_frbidn(self):
        for i in range(1,self.MAX):
            for j in range(1,self.MAX):
                if self.board[i][j].qi==-1:
                    self.board[i][j].color=GoPoint.NULL

    def end(self):
        if self.is_pass!=4:
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
        # print 'BLACK:',self.res_cnt[GoPoint.BLACK]
        # print 'WHITE:',self.res_cnt[GoPoint.WHITE]
        if self.res_cnt[GoPoint.BLACK]>self.res_cnt[GoPoint.WHITE]:
            self.win=1
            # print 'BLACK is winner.'
        else:
            self.win=0
            # print 'WHITE is winner.'
        return 1


    def group_qi(self,g):
        g=self.group_find(g=g)
        return self.board[g[0]][g[1]].qi_group

    def group_find(self,g):
        if self.board[g[0]][g[1]].group==g:
            return g
        self.board[g[0]][g[1]].group=self.group_find(self.board[g[0]][g[1]].group)
        return self.board[g[0]][g[1]].group


    def group_union(self,g1,g2):
        group1=self.group_find(g=self.board[g1[0]][g1[1]].group)
        group2=self.group_find(g=self.board[g2[0]][g2[1]].group)
        if group2!=group1:
            self.board[group1[0]][group1[1]].group=group2
            self.board[group2[0]][group2[1]].member.append(group1)
            self.board[group2[0]][group2[1]].qi_group+=self.board[group1[0]][group1[1]].qi_group

    def group_check(self,g):
        if not self.group_qi(g=g):
            return 0
        if self.group_qi(g=g)<=4 and self.group_find(g=g)!=[self.x,self.y]:
            points=[]
            if self.group_badmove(g=g,points=points):
                return 0
        return 1



    # def group_union(self,g1,g2):
    #     group1=self.group_find(g=self.board[g1[0]][g1[1]].group)
    #     group2=self.group_find(g=self.board[g2[0]][g2[1]].group)
    #     self.board[group1[0]][group1[1]].group=group2
    #     self.board[group2[0]][group2[1]].member.append(group1)

    def group_badmove(self,g,points):
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
            if not self.group_badmove(g=member,points=points):
                return 0
        return 1


    def group_godie(self,g):
        for member in self.board[g[0]][g[1]].get_member():
            self.group_godie(g=member)
        self.board[g[0]][g[1]].die()
        done=self
        for i in [[g[0]+1,g[1]],[g[0]-1,g[1]],[g[0],g[1]+1],[g[0],g[1]-1]]:
                if self.board[i[0]][i[1]].qi>=0:
                    self.board[i[0]][i[1]].qi+=1
                    f=self.group_find(g=i)
                    self.board[f[0]][f[1]].qi_group+=1


    def draw(self):
        return [[self.board[i][j].output() for j in range(1,self.MAX)]for i in range(1,self.MAX)]

    def board_value(self):
        ans=0
        for i in range(1,self.MAX):
            for j in range(1,self.MAX):
                ans+=self.board[i][j].output()
                ans<<=2
        #print ans
        return ans
    def copy_value(self,copy):
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


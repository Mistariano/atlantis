#coding=utf8

__author__ = 'MisT'

from goplay.goplay import GoPlay
from goplay.gopoint import GoPoint
from operator import itemgetter

class UnitPlay(GoPlay):
    def loadUnit(self,ub,uw):
        self.unitBlack=ub
        self.unitWhite=uw

    def end(self):
        self.toGet=True
        return GoPlay.end(self)

    def getXY(self):
        if self.toGet:
            self.toGet=False
            if self.nextPlayer:
                color=GoPoint.BLACK
            else:
                color=GoPoint.WHITE
            inputs=[]
            for xx in range(1,self.MAX):
                for yy in range(1,self.MAX):
                    if self.board[xx][yy].qi>=0:
                        if self.board[xx][yy].color==color:
                            inputs.append(0.5)
                        else:
                            inputs.append(1)
                    else:
                        inputs.append(self.board[xx][yy].color)
            if self.nextPlayer:
                ans = self.unitBlack.startDash(inputs=inputs)
            else:
                ans = self.unitWhite.startDash(inputs=inputs)
            self.allowed=[]
            for i in range(0,len(ans)):
                if self.board[i/self.size+1][i%self.size+1].color==GoPoint.NULL:
                    self.allowed.append([i,ans[i]])
            self.allowed.sort(key=itemgetter(1),reverse=True)
            # print'[DEBUG]=============================='
        # print '[DEBUG]',self.allowed
        if not len(self.allowed):
            self.x=-1
            self.y=-1
        else:
            self.x=self.allowed[0][0]/self.size+1
            self.y=self.allowed[0][0]%self.size+1
            del self.allowed[0]
        # max=-1
        # index=-1
        # for i in range(0,len(self.ans)):
        #     if self.board[i/self.size+1][i%self.size+1].color==GoPoint.NULL:
        #         if max<self.ans[i]:
        #             max=self.ans[i]
        #             index=i
        # if max==-1:
        #     self.x=-1
        #     self.y=-1
        # else:
        #     self.x=index/self.size+1
        #     self.y=index%self.size+1

    def output(self):
        draw=self.draw()
        print
        print' ',
        for i in range(1,self.MAX):
            print 10+i,
        print
        cnt=11
        for i in draw:
            print cnt,
            cnt+=1
            for j in i:
                if j==1:
                    print u'○',
                if j==2:
                    print u'●',
                if j==0:
                    print '..',
            print

    def loop(self):
        GoPlay.loop(self)
        # print 'Result:'
        # print 'B:',self.res_cnt[GoPoint.BLACK],'W:',self.res_cnt[GoPoint.WHITE]
        # if self.res_cnt[GoPoint.BLACK]+self.res_cnt[GoPoint.WHITE]!=self.size**2:
        # self.output()

__author__ = 'MisT'

from goplay.goplay import GoPlay
from goplay.gopoint import GoPoint

class UnitPlay(GoPlay):
    def loadUnit(self,ub,uw):
        self.unitBlack=ub
        self.unitWhite=uw

    def end(self):
        self.to_get=True
        return GoPlay.end(self)

    def get_xy(self):
        if self.to_get:
            self.to_get=False
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
                self.ans = self.unitBlack.startDash(inputs=inputs)
            else:
                self.ans = self.unitWhite.startDash(inputs=inputs)
            # print self.ans
            # print 'here'
        max=-1
        index=-1
        for i in range(0,len(self.ans)):
            if self.board[i/self.size+1][i%self.size+1].color==GoPoint.NULL:
                if max<self.ans[i]:
                    max=self.ans[i]
                    index=i
        if max==-1:
            self.x=-1
            self.y=-1
        else:
            self.x=index/self.size+1
            self.y=index%self.size+1

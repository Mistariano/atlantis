__author__ = 'MisT'

class GoPoint:
    NULL=0
    BLACK=1
    WHITE=2
    # BLACK_FORBIDDENED=3
    # WHITE_FORBIDDENED=4
    # ALL_FORBIDDENED=5
    FORBIDDENED=3
    WALL=6

    def __init__(self,x,y,color):
        self.x=x
        self.y=y
        self.color=color
        self.group=[self.x,self.y]
        self.member=[[self.x,self.y]]
        self.qi=-1
        self.qi_group=0
        # self.NEXT=[self.x,self.y]
        # self.LAST=[self.x,self.y]

    def move(self,color):
        self.color=color
        self.qi=0
        self.qi_group=0

    def get_member(self):
        for g in self.member:
            if g[0]!=self.x or g[1]!=self.y:
                yield g

    def die(self):
        self.qi=-1
        self.color=GoPoint.NULL
        self.group=[self.x,self.y]
        self.member=[[self.x,self.y]]

    def become_wall(self):
        self.color=GoPoint.WALL
        self.qi=-666

    def become_frbidn(self):
        self.color=GoPoint.FORBIDDENED
        self.qi=-1
        self.group=[self.x,self.y]
        self.member=[[self.x,self.y]]

    def output(self):
        if self.color!=GoPoint.BLACK and self.color!=GoPoint.WHITE:
            return GoPoint.NULL
        else:
            return self.color





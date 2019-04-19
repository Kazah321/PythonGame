class levels:
    def __init__(self):
        level_0 =["xxxxxxxxxxxxxxxxxxxx",
                  "x                  x",
                  "x                  x",
                  "x         G        x",
                  "x                  x",
                  "x   C              x",
                  "x                  x",
                  "x       C          x",
                  "x                  x",
                  "x  C               x",
                  "x                  x",
                  "x C                x",
                  "x                  x",
                  "x                  x",
                  "x   c              x",
                  "x                  x",
                  "x                  x",
                  "x                  x",
                  "x       XEX        x",
                  "xxxxxxxxxxxxxxxxxxxx",]
        level_1 =["xxxxxxxxxxxxxxxxxxxx",
                  "xX     XXXXXXX     x",
                  "xX XX  XC X TX     x",
                  "xX CX  X  X  X     x",
                  "xXXXX XXX   XX     x",
                  "x                  x",
                  "x     CXX  xxxxx   x",
                  "x    XXXX  xxxExXXXx",
                  "x    X  c  xC  xg  x",
                  "x    X     xx  xXXXx",
                  "x    XXXX          x",
                  "x                  x",
                  "x   T              x",
                  "x        T         x",
                  "x                T x",
                  "x XXX    C         x",
                  "x   XX        XXX  x",
                  "xT  CX          X  x",
                  "x             XGX  x",
                  "xxxxxxxxxxxxxxxxxxxx",]
        level_2 =["xxxxxxxxxxxxxxxxxxxx",
                  "x              XCg x",
                  "x    XXXXXXX X X XXx",
                  "x    X     XXX X  Xx",
                  "x   XXXXX    X XX  x",
                  "x   X   X c  XEX   x",
                  "x   XCX X  XXXXX   x",
                  "x   XXX X  X   X   x",
                  "x       X  X   X   x",
                  "x              X   x",
                  "x                  x",
                  "x           c      x",
                  "x                  x",
                  "x                  x",
                  "x                  x",
                  "x        C    XXXXXx",
                  "x     C       d    x",
                  "x             X X Tx",
                  "x             XGXCtx",
                  "xxxxxxxxxxxxxxxxxxxx",]
        level_3 =["xxxxxxxxxxxxxxxxxxxx",
                  "x    CX         xGxx",
                  "x T XXX  X      x xx",
                  "x   XEX CX         x",
                  "x   XDXXXXDX       x",
                  "x   X Xt   X       x",
                  "x   X XXXXXX       x",
                  "x                  x",
                  "x                  x",
                  "x            c     x",
                  "x                  x",
                  "x                  x",
                  "x          XXDX    x",
                  "x     c    X CX    x",
                  "x          XCCX    x",
                  "xxx        XCTX    x",
                  "xtx        XCCXX XXx",
                  "x          XXXXX XXx",
                  "x    c      C Xt Xgx",
                  "xxxxxxxxxxxxxxxxxxxx",]
        level_4 =["xxxxxxxxxxxxxxxxxxxx",
                  "x G d   X          x",
                  "xX XXXX X  XXXX    x",
                  "xT TXTX X  X CX    x",
                  "xXtXXC  XC X       x",
                  "xXXXXXX XXXXXX     x",
                  "x      c    X      x",
                  "x XXXXX XX  X      x",
                  "x X C X X   d      x",
                  "x X   X X  XX      x",
                  "x XXX XXX  X  XXX  x",
                  "x       X  XXXXtX  x",
                  "x  XXXXXX  X    X  x",
                  "x    XC      X  XXXx",
                  "x    X    X  X  XC x",
                  "x    X XXXX  X  X  x",
                  "x    XCX     XXXXX x",
                  "x    XXX           x",
                  "x        E         x",
                  "xxxxxxxxxxxxxxxxxxxx",]
        level_5 =["xxxxxxxxxxxxxxxxxxxx",
                  "x                  x",
                  "x                  x",
                  "x         G        x",
                  "x                  x",
                  "x                  x",
                  "x                  x",
                  "x                  x",
                  "x                  x",
                  "x                  x",
                  "x                  x",
                  "x                  x",
                  "x                  x",
                  "x                  x",
                  "x                  x",
                  "x                  x",
                  "x                  x",
                  "x                  x",
                  "x        E         x",
                  "xxxxxxxxxxxxxxxxxxxx",]

        self.Tab =[ level_0,level_1,level_2,level_3,level_4,level_5]
    @property
    def get_level(self):
        return self.Tab
        

    
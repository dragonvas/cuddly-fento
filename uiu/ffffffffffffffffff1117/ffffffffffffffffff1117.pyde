 o=0
 oo=0
 x=0
 xx=0
 c=0
 z=0
 def setup():
     size (1000 ,1000)
 def draw():
     global o,oo,x,xx,c,z
     background (255,255,255)
     fill (oo,0,0)
     ellipse (700 ,700 ,50 ,50)
     это красный шaр
     fill (0,x,0)
     ellipse (100 ,100 ,50 ,50)
     это зелёный шaр
     fill (0,0,o)
     ellipse (900 ,700 ,30 ,30)
     это синий шaр
     fill (xx,xx,0)
     ellipse (200 ,700 ,50 ,50)
     это жёлтый шaр
     fill (0,c,c)
     ellipse (10 ,600 ,50 ,50)
     это голубой шaр
     fill (z,0,z)
     ellipse (700 ,800 ,50 ,50)
     это pозовый шaр
     o=o+1
     oo=oo+2
     x=x+3
     xx=xx+4
     c=c+5
     z=z+6
     if oo >= 255:
         oo=0
     if o >= 255:
         o=0
     if x >= 255:
         x=0
     if xx >= 255:
         xx=0
     if c >= 255:
         c=0
     if z >= 255:
         z=0
     if o > 255*60:
    noLoop()

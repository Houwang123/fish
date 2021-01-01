def fish(a,b,c,d,e,f,g,h,*args,**kwargs):
    cc=lambda x:(100*x**2)
    l=0
    m=0
    n=0
    o=0
    p=cc(e)
    s = 1.4 if not a else kwargs['s']
    def gg(c,d):
        u=c
        y=0
        for i in range(60):
            v=c*0.02*min([d/p,1])
            if d<=0:
                v=0
            y=y+v
            w=v*(1-c/p)
            x=max(0,c*0.001*1.5*(2-d/p))
            d=max(0,d-v)
            c=max(c+w-x,0)
        return c-u-y*f
    def eg(c,i,j):
        ii=gg(c,i)
        jj=gg(c,j)
        if abs(i-j)<p*0.01:
            return [ii,i]
        elif jj>ii:
            return eg(c,max((j+i)//2,i+1),j)
        else:
            return eg(c,i,min((j+i)//2,j-1))
    def ee(i,j):
        ii=0
        fi=0
        jj=0
        fj=0
        z=p*s
        if z < d//1+(b+j-i-1)//f:
            ii = gg(i,z)
            fi = z
            jj = gg(j,z)
            fj = z
        else:
            res=eg(i,0,d//1+(b+c-i-1)//f)
            ii=res[0]
            fi=res[1]
            res=eg(j,0,d//1+(b+c-j-1)//f)
            jj=res[0]
            fj=res[0]
        if abs(i-j)<p*0.01:
            return [i, fi]
        if jj>ii:
            return ee(max((j+i)//2,i+1),j)
        else:
            return ee(i,min((j+i)//2,j-1))
    if not c:
        n=b/g/1.5
        b=b-g*n
        res=eg(n,0,min(p*5,(b-1)//f))
        q=res[0]
        m=res[1]
    else:
        if d < p*2:
            s=s+0.05
        elif d > p*2.1:
            s=s-0.04
        res=ee(0,c//1)
        q=res[0]
        r=res[1]
        l=max(0,c-q)
        m=max(0,r-d)
        b=b+l-n*m
        if a<140:
            if e < 6:
                if b>h*cc(e+1)*1.2:
                    o=1
            elif e < 16:
                if b>h*cc(e+2)*1.1:
                    o=2
            else:
                if b>h*cc(e+3)*1.05:
                    o=3
    return [l,m,n,o], [], {'s':s}
def fish(a,b,c,d,e,f,g,h,*args,**kwargs):
    cc=lambda x:(100*x**2)
    def gg(c,d):
        u,y=c,0
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
        if i>=j:
            return ii,i
        elif jj>ii:
            return eg(c,max((j+i)//2,i+1),j)
        else:
            return eg(c,i,min((j+i)//2,j-1))
    def ee(i,j):
        ii,fi, jj, fj=0,0,0,0
        z=p*(1.2+e*0.12)
        if z < d//1+(b+j-i-1)//f:
            ii = gg(i,z)
            fi = z
            jj = gg(j,z)
            fj = z
        else:
            ii,fi=eg(i,0,d//1+(b+j-i-1)//f)
            jj,fj=eg(j,0,d//1+(b+j-i-1)//f)
        if i>=j:
            return i, fi
        if jj>ii:
            return ee(max((j+i)//2,i+1),j)
        else:
            return ee(i,min((j+i)//2,j-1))
    l,m,n,o,p = 0,0,0,0,cc(e)
    if not c:
        n=b/g/1.5 if not c else 0
        b=b-g*n
        q,m=eg(n,0,min(p*5,(b-1)//f))
    else:
        q,r=ee(0,c//1)
        l,m=max(0,c-q),max(0,r-d)
        b=b+l-n*m
        if a<140:
            if e < 6:
                if b>h*cc(e+1)*1.5:
                    o=1
            elif e < 16:
                if b>h*cc(e+2)*1.2:
                    o=2
    return [l,m,n,o], [], {}


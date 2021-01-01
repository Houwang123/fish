from RestrictedPython import compile_restricted, Eval, Guards, safe_globals, utility_builtins

def make_policy():
    p_globals = {**safe_globals, **utility_builtins}
    p_globals['__builtins__']['__metaclass__'] = type
    p_globals['__builtins__']['__name__'] = type

    p_globals['__builtins__']['min'] = min
    p_globals['__builtins__']['max'] = max

    p_globals['_getattr_'] = Guards.safer_getattr
    p_globals['_write_'] = Guards.full_write_guard
    p_globals['_getiter_'] = Eval.default_guarded_getiter
    p_globals['_getitem_'] = Eval.default_guarded_getitem
    p_globals['_iter_unpack_sequence_'] = Guards.guarded_iter_unpack_sequence

    return p_globals

source = '''
def fish(a,b,c,d,e,f,g,h,*args,**kwargs):
    cc=lambda x:(100*x**2)
    l=0
    m=0
    n=0
    o=0
    p=cc(e)
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
        if i>=j:
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
        z=p*(1.2+e*0.12)
        if z < d//1+(b+j-i-1)//f:
            ii = gg(i,z)
            fi = z
            jj = gg(j,z)
            fj = z
        else:
            res=eg(i,0,d//1+(b+j-i-1)//f)
            ii=res[0]
            fi=res[1]
            res=eg(j,0,d//1+(b+j-i-1)//f)
            jj=res[0]
            fj=res[0]
        if i>=j:
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
        res=ee(0,c//1)
        q=res[0]
        r=res[1]
        l=max(0,c-q)
        m=max(0,r-d)
        b=b+l-n*m
        if a<140:
            if e < 6:
                if b>h*cc(e+1)*1.5:
                    o=1
            elif e < 16:
                if b>h*cc(e+2)*1.2:
                    o=2
            else:
                if b>h*cc(e+3)*1.1:
                    o=3
    return [l,m,n,o], [], {}
    '''

loc={}
byte_code = compile_restricted(source, '<inline>', 'exec')
exec(byte_code, make_policy(),loc)
loc['fish'](2,50,100,200,1,0.1,0.1,0.7)
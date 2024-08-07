from sympy import*
r=Symbol('r')
t=Symbol('t')
u=sin(r*cos(t))*cosh(r*sin(t))
print("u=",u)
v=cos(r*cos(t))*sinh(r*sin(t))
print("v=",v)
ur=diff(u,r).simplify()
ut=diff(u,t).simplify()
vr=diff(v,r).simplify()
vt=diff(v,t).simplify()
if(ur==simplify((1/r)*vt)) &(ut==simplify((-r)*vr)):
    print("Cauchy-Rieman's equation is satisfied")
else:
    print("Cauchy-Reiman's equation is satisfied")    
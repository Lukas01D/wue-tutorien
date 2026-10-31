import math, itertools
from nachrechnen_koord import lauf
from nachrechnen_nichtlinear import fall, n43
res = []
for tau, thKT, thG in itertools.product((20, 30, 41, 75), (5.0, 7.0, 10.0), (13.0, 17.0, 20.0)):
    thm = 20 + 60*math.exp(-10/tau)
    o2 = lauf(t_end=2400.0, C_T=255.0, thmess=thm, thM2=thKT)
    o3 = lauf(t_end=2400.0, C_T=255.0, thmess=thm, thM2=thG)
    res.append((tau, thKT, thG, o2[2], o2[0]-o3[1], o3[1]-o2[1]))
for tau in (20, 30, 41, 75):
    sub = [x for x in res if x[0] == tau]
    print(f"tau {tau}: B1-B2 {min(x[3] for x in sub):.2f}..{max(x[3] for x in sub):.2f}, "
          f"B1-B3 {min(x[4] for x in sub):.2f}..{max(x[4] for x in sub):.2f}, B3-B2 {min(x[5] for x in sub):.2f}..{max(x[5] for x in sub):.2f}")
sub = [x for x in res if x[0] in (30, 41) and x[1] in (5.0, 7.0) and x[2] in (13.0, 17.0, 20.0)]
print(f"typisch (tau 30-41, Kühltasche 5-7, Glas 13-20): B1-B2 {min(x[3] for x in sub):.2f}..{max(x[3] for x in sub):.2f}, "
      f"B1-B3 {min(x[4] for x in sub):.2f}..{max(x[4] for x in sub):.2f}, B3-B2 {min(x[5] for x in sub):.2f}..{max(x[5] for x in sub):.2f}")

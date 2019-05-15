import sys
from CProbe import ConductivityProbe
from TProbes import TemperatureProbes
from Scale import Scale

def fprintf(stream, format_spec, *args):
    stream.write(format_spec % args)

con = ConductivityProbe(9600)
con.whosmans()
con.helpme()
con.changeB(80000)
con.changeP()
con.whosmans()
#con.openC()
#l = con.line()
#print(l)

T = TemperatureProbes(8909890)
T.whosmans()
T.helpme()
T.changeB(80000)
T.changeP()
T.whosmans()
#T.openC()
#l = T.line()
#print(l)

S = Scale(8909890)
S.whosmans()
S.helpme()
S.changeB(80000)
S.changeP()
S.whosmans()
#S.openC()
#l = S.line()
#print(l)

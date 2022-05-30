
# # print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# from matplotlib.pyplot import phase_spectrum


from regex import P


Math=80;
physics=76;
Computer=60;
English=60;
pak=50;
total=100;
m_p= Math/total *100;
P_P=physics/total*100;
c_p=Computer/total*100;
e_p=English/total*100;
p_p=pak/total*100;
t_p=(Math+physics+Computer+English+pak)/500*100
print(t_p)
if Math <33:
 m="pass"
else:
 m="fail"
 if physics <33:
  P="fail"
 else:
  P="pass"
 if Computer <33:
   c="fail"
 else:
  c="pass"
 if English <33:  
  e="fail"
 else:
  e="pass"
 if P <33:
  P="fail"
 else:
  P="pass"
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
print("  Subject           Obtain.Marks              Total.Marks               Pass/Fail        Persentage  ")
print("   Maths             30                        100                        ",m,"          ", m_p   )
print("   Physics           76                        100                        ",P,"           ", P_P )
print("   Computer          60                        100                         ",c,"          ",c_p )
print("   English           60                        100                        ",e,"            ",e_p )
print("   Pakistan_stdy     76                        100                        ",P,"           ",p_p)
print("This candidate paseed the exam with the percentagr of",t_p)



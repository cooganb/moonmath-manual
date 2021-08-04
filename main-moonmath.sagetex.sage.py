## -*- encoding: utf-8 -*-

# This file was *autogenerated* from the file /home/mirco/Leastauthority/MMM/moonmath-manual/main-moonmath.sagetex.sage
from sage.all_cmdline import *   # import sage library

_sage_const_509 = Integer(509); _sage_const_852 = Integer(852); _sage_const_505 = Integer(505); _sage_const_907 = Integer(907); _sage_const_695 = Integer(695); _sage_const_171 = Integer(171); _sage_const_294 = Integer(294); _sage_const_768 = Integer(768); _sage_const_763 = Integer(763); _sage_const_767 = Integer(767); _sage_const_530 = Integer(530); _sage_const_535 = Integer(535); _sage_const_537 = Integer(537); _sage_const_13 = Integer(13); _sage_const_12 = Integer(12); _sage_const_11 = Integer(11); _sage_const_10 = Integer(10); _sage_const_17 = Integer(17); _sage_const_16 = Integer(16); _sage_const_15 = Integer(15); _sage_const_14 = Integer(14); _sage_const_908 = Integer(908); _sage_const_826 = Integer(826); _sage_const_19 = Integer(19); _sage_const_18 = Integer(18); _sage_const_822 = Integer(822); _sage_const_583 = Integer(583); _sage_const_588 = Integer(588); _sage_const_737 = Integer(737); _sage_const_323 = Integer(323); _sage_const_733 = Integer(733); _sage_const_732 = Integer(732); _sage_const_326 = Integer(326); _sage_const_738 = Integer(738); _sage_const_213 = Integer(213); _sage_const_139 = Integer(139); _sage_const_138 = Integer(138); _sage_const_882 = Integer(882); _sage_const_721 = Integer(721); _sage_const_805 = Integer(805); _sage_const_390 = Integer(390); _sage_const_74 = Integer(74); _sage_const_77 = Integer(77); _sage_const_71 = Integer(71); _sage_const_430 = Integer(430); _sage_const_710 = Integer(710); _sage_const_715 = Integer(715); _sage_const_80 = Integer(80); _sage_const_494 = Integer(494); _sage_const_30 = Integer(30); _sage_const_793 = Integer(793); _sage_const_794 = Integer(794); _sage_const_472 = Integer(472); _sage_const_392 = Integer(392); _sage_const_48 = Integer(48); _sage_const_157 = Integer(157); _sage_const_154 = Integer(154); _sage_const_465 = Integer(465); _sage_const_469 = Integer(469); _sage_const_468 = Integer(468); _sage_const_787 = Integer(787); _sage_const_58 = Integer(58); _sage_const_144 = Integer(144); _sage_const_141 = Integer(141); _sage_const_898 = Integer(898); _sage_const_143 = Integer(143); _sage_const_652 = Integer(652); _sage_const_148 = Integer(148); _sage_const_3 = Integer(3); _sage_const_2 = Integer(2); _sage_const_1 = Integer(1); _sage_const_0 = Integer(0); _sage_const_7 = Integer(7); _sage_const_6 = Integer(6); _sage_const_5 = Integer(5); _sage_const_4 = Integer(4); _sage_const_9 = Integer(9); _sage_const_8 = Integer(8); _sage_const_28 = Integer(28); _sage_const_29 = Integer(29); _sage_const_877 = Integer(877); _sage_const_22 = Integer(22); _sage_const_23 = Integer(23); _sage_const_20 = Integer(20); _sage_const_21 = Integer(21); _sage_const_26 = Integer(26); _sage_const_27 = Integer(27); _sage_const_24 = Integer(24); _sage_const_25 = Integer(25); _sage_const_665 = Integer(665); _sage_const_664 = Integer(664); _sage_const_705 = Integer(705); _sage_const_571 = Integer(571); _sage_const_442 = Integer(442); _sage_const_215 = Integer(215); _sage_const_518 = Integer(518); _sage_const_845 = Integer(845); _sage_const_38 = Integer(38); _sage_const_689 = Integer(689); _sage_const_31 = Integer(31); _sage_const_686 = Integer(686); _sage_const_33 = Integer(33); _sage_const_32 = Integer(32); _sage_const_35 = Integer(35); _sage_const_34 = Integer(34); _sage_const_37 = Integer(37); _sage_const_36 = Integer(36); _sage_const_166 = Integer(166); _sage_const_287 = Integer(287); _sage_const_902 = Integer(902); _sage_const_675 = Integer(675); _sage_const_679 = Integer(679); _sage_const_564 = Integer(564); _sage_const_774 = Integer(774)## This file (main-moonmath.sagetex.sage) was *autogenerated* from main-moonmath.tex with sagetex.sty version 2019/01/09 v3.2.
import sagetex
_st_ = sagetex.SageTeXProcessor('main-moonmath', version='2019/01/09 v3.2', version_check=True)
try:
 _st_.current_tex_line = _sage_const_48 
 _st_.commandline(_sage_const_0 , r"""
sage: ZZ # A sage notation for the integer type
sage: NN # A sage notation for the counting number type
sage: ZZ(5) # Get an element from the Ring of integers
sage: ZZ(5) + ZZ(3)
sage: ZZ(5) * NN(3)
sage: ZZ.random_element(10**50)
sage: ZZ(27713).str(2) # Binary string representation
sage: NN(27713).str(2) # Binary string representation
sage: ZZ(27713).str(16) # Hexadecimal string representation
""", globals(), locals(), True)
except:
 _st_.goboom(_sage_const_58 )
try:
 _st_.current_tex_line = _sage_const_77 
 _st_.commandline(_sage_const_1 , r"""
sage: n = NN(19214758032624000)
sage: factor(n)
""", globals(), locals(), True)
except:
 _st_.goboom(_sage_const_80 )
try:
 _st_.current_tex_line = _sage_const_138 
 _st_.commandline(_sage_const_2 , r"""
sage: ZZ(-17) // ZZ(4) # Integer quotient
sage: ZZ(-17) % ZZ(4) # remainder
sage: ZZ(4).divides(ZZ(-17)) # self divides other
sage: ZZ(4).divides(ZZ(12))
""", globals(), locals(), True)
except:
 _st_.goboom(_sage_const_143 )
try:
 _st_.current_tex_line = _sage_const_154 
 _st_.commandline(_sage_const_3 , r"""
sage: ZZ(143785).quo_rem(ZZ(17)) # Euclidean Division
sage: ZZ(143785) == ZZ(8457)*ZZ(17) + ZZ(16) # check
""", globals(), locals(), True)
except:
 _st_.goboom(_sage_const_157 )
try:
 _st_.current_tex_line = _sage_const_213 
 _st_.commandline(_sage_const_4 , r"""
sage: ZZ(12).xgcd(ZZ(5)) # (gcd(a,b),s,t)
""", globals(), locals(), True)
except:
 _st_.goboom(_sage_const_215 )
try:
 _st_.current_tex_line = _sage_const_287 
 _st_.commandline(_sage_const_5 , r"""
sage: ZZ(137).gcd(ZZ(64))
sage: ZZ(64)** ZZ(137) % ZZ(137) == ZZ(64) % ZZ(137)
sage: ZZ(64)** ZZ(137-1) % ZZ(137) == ZZ(1) % ZZ(137)
sage: ZZ(1918).gcd(ZZ(137))
sage: ZZ(1918)** ZZ(137) % ZZ(137) == ZZ(1918) % ZZ(137)
sage: ZZ(1918)** ZZ(137-1) % ZZ(137) == ZZ(1) % ZZ(137)
""", globals(), locals(), True)
except:
 _st_.goboom(_sage_const_294 )
try:
 _st_.current_tex_line = _sage_const_323 
 _st_.commandline(_sage_const_6 , r"""
sage: (ZZ(7)* (ZZ(2)*ZZ(4) + ZZ(21)) + ZZ(11))  % ZZ(6) == (ZZ(4) - ZZ(102))  % ZZ(6)
sage: (ZZ(7)* (ZZ(2)*ZZ(76) + ZZ(21)) + ZZ(11))  % ZZ(6) == (ZZ(76) - ZZ(102))  % ZZ(6)
""", globals(), locals(), True)
except:
 _st_.goboom(_sage_const_326 )
try:
 _st_.current_tex_line = _sage_const_390 
 _st_.commandline(_sage_const_7 , r"""
sage: CRT_list([4,1,3,0], [7,3,5,11])
""", globals(), locals(), True)
except:
 _st_.goboom(_sage_const_392 )
try:
 _st_.current_tex_line = _sage_const_465 
 _st_.commandline(_sage_const_8 , r"""
sage: Z6 = Integers(6)
sage: Z6(2) + Z6(5)
sage: Z6(7)*(Z6(2)*Z6(4)+Z6(21))+Z6(11) == Z6(4) - Z6(102)
""", globals(), locals(), True)
except:
 _st_.goboom(_sage_const_469 )
try:
 _st_.current_tex_line = _sage_const_535 
 _st_.commandline(_sage_const_9 , r"""
sage: ZZ(6).xgcd(ZZ(5))
""", globals(), locals(), True)
except:
 _st_.goboom(_sage_const_537 )
try:
 _st_.current_tex_line = _sage_const_583 
 _st_.commandline(_sage_const_10 , r"""
sage: Z5 = Integers(5)
sage: Z5(3)**(5-2)
sage: Z5(3)**(-1)
sage: Z5(3)**(5-2) == Z5(3)**(-1)
""", globals(), locals(), True)
except:
 _st_.goboom(_sage_const_588 )
try:
 _st_.current_tex_line = _sage_const_652 
 _st_.commandline(_sage_const_11 , r"""
sage: Zx = ZZ['x'] # integer polynomials with indeterminate x
sage: Zt.<t> = ZZ[] # integer polynomials with indeterminate t
sage: Zx
sage: Zt
sage: p1 = Zx([17,-4,2])
sage: p1
sage: p1.degree()
sage: p1.leading_coefficient()
sage: p2 = Zt(t^23)
sage: p2
sage: p6 = Zx([0])
sage: p6.degree()
""", globals(), locals(), True)
except:
 _st_.goboom(_sage_const_665 )
try:
 _st_.current_tex_line = _sage_const_686 
 _st_.commandline(_sage_const_12 , r"""
sage: Z6 = Integers(6)
sage: Z6x = Z6['x']
sage: Z6x
sage: p1 = Z6x([5,-4,2])
sage: p1
sage: p1 = Z6x([17,-4,2])
sage: p1
sage: Z6x(x-2)*Z6x(x+3)*Z6x(x-5) == Z6x(x^3 + 2*x^2 + x)
""", globals(), locals(), True)
except:
 _st_.goboom(_sage_const_695 )
try:
 _st_.current_tex_line = _sage_const_715 
 _st_.commandline(_sage_const_13 , r"""
sage: Zx = ZZ['x']
sage: p1 = Zx([17,-4,2])
sage: p7 = Zx(x-2)*Zx(x+3)*Zx(x-5)
sage: p1(ZZ(2))
sage: p7(ZZ(-6)) == ZZ(-264)
""", globals(), locals(), True)
except:
 _st_.goboom(_sage_const_721 )
try:
 _st_.current_tex_line = _sage_const_732 
 _st_.commandline(_sage_const_14 , r"""
sage: Z6 = Integers(6)
sage: Z6x = Z6['x']
sage: p1 = Z6x([5,-4,2])
sage: p1(Z6(2)) == Z6(5)
""", globals(), locals(), True)
except:
 _st_.goboom(_sage_const_737 )
try:
 _st_.current_tex_line = _sage_const_768 
 _st_.commandline(_sage_const_15 , r"""
sage: Zx = ZZ['x']
sage: P = Zx([2,-4,5])
sage: Q = Zx([5,0,-2,1])
sage: P+Q == Zx(x^3 +3*x^2 -4*x +7)
sage: P*Q == Zx(5*x^5 -14*x^4 +10*x^3+21*x^2-20*x +10)
""", globals(), locals(), True)
except:
 _st_.goboom(_sage_const_774 )
try:
 _st_.current_tex_line = _sage_const_787 
 _st_.commandline(_sage_const_16 , r"""
sage: Z6x = Integers(6)['x']
sage: P = Z6x([2,-4,5])
sage: Q = Z6x([5,0,-2,1])
sage: P+Q == Z6x(x^3 +3*x^2 +2*x +1)
sage: P*Q == Z6x(5*x^5 +4*x^4 +4*x^3+3*x^2+4*x +4)
""", globals(), locals(), True)
except:
 _st_.goboom(_sage_const_793 )
try:
 _st_.current_tex_line = _sage_const_845 
 _st_.commandline(_sage_const_17 , r"""
sage: Zx = ZZ['x']
sage: A = Zx([-9,0,0,2,0,1])
sage: B = Zx([-1,4,1])
sage: M = Zx([-80,19,-4,1])
sage: R = Zx([-89,339])
sage: A == M*B + R
""", globals(), locals(), True)
except:
 _st_.goboom(_sage_const_852 )
try:
 _st_.current_tex_line = _sage_const_877 
 _st_.commandline(_sage_const_18 , r"""
sage: Zx = ZZ['x']
sage: p = Zx(x^2-3)
sage: p.roots()
sage: p.factor()
""", globals(), locals(), True)
except:
 _st_.goboom(_sage_const_882 )
try:
 _st_.current_tex_line = _sage_const_902 
 _st_.commandline(_sage_const_19 , r"""
sage: Zx = ZZ['x']
sage: p = Zx(x^7 + 3*x^6 + 3*x^5 + x^4 - x^3 - 3*x^2 - 3*x - 1)
sage: p.roots()
sage: p.factor()
""", globals(), locals(), True)
except:
 _st_.goboom(_sage_const_907 )
try:
 _st_.current_tex_line = _sage_const_71 
 _st_.commandline(_sage_const_20 , r"""
sage: CommutativeRings()
sage: CommutativeRings().super_categories()
""", globals(), locals(), True)
except:
 _st_.goboom(_sage_const_74 )
try:
 _st_.current_tex_line = _sage_const_139 
 _st_.commandline(_sage_const_21 , r"""
sage: Fields()
""", globals(), locals(), True)
except:
 _st_.goboom(_sage_const_141 )
try:
 _st_.current_tex_line = _sage_const_144 
 _st_.commandline(_sage_const_22 , r"""
sage: QQ
sage: QQ(1/5) # Get an element from the field of rational numbers
sage: QQ(1/5) / QQ(3) # Division
""", globals(), locals(), True)
except:
 _st_.goboom(_sage_const_148 )
try:
 _st_.current_tex_line = _sage_const_166 
 _st_.commandline(_sage_const_23 , r"""
sage: GF(2)
sage: GF(2)(1) # Get an element from GF(2)
sage: GF(2)(1) + GF(2)(1) # Addition
sage: GF(2)(1) / GF(2)(1) # Division
""", globals(), locals(), True)
except:
 _st_.goboom(_sage_const_171 )
try:
 _st_.current_tex_line = _sage_const_29 
 _st_.commandline(_sage_const_24 , r"""
sage: EllipticCurve(GF(5),[1,0])
sage: EllipticCurve(GF(5),[1,0]).trace_of_frobenius()
""", globals(), locals(), True)
except:
 _st_.goboom(_sage_const_32 )
try:
 _st_.current_tex_line = _sage_const_430 
 _st_.commandline(_sage_const_25 , r"""
sage: F43 = GF(43)
sage: F43t.<t> = F43[]
sage: F43_6.<v> = GF(43^6, name='v', modulus=t^6+6) # t^6+6 irreducible
sage: BLS6 = EllipticCurve (F43_6,[0 ,6])
sage: INF = BLS6(0) # point at infinity
sage: for P in INF.division_points(13): # PI(P) == [q]P
....:     if P.order() == 13: # exclude point at infinity
....:         PiP = BLS6([a.frobenius() for a in P])
....:         qP = 43*P
....:         if PiP == qP:
....:             print(P.xy())
""", globals(), locals(), True)
except:
 _st_.goboom(_sage_const_442 )
try:
 _st_.current_tex_line = _sage_const_468 
 _st_.commandline(_sage_const_26 , r"""
sage: g1 = BLS6([13,15])
sage: g2 = BLS6([7*v^2, 16*v^3])
sage: g1.weil_pairing(g2,13)
""", globals(), locals(), True)
except:
 _st_.goboom(_sage_const_472 )
try:
 _st_.current_tex_line = _sage_const_494 
 _st_.commandline(_sage_const_27 , r"""
sage: F13 = GF(13)
sage: for A in xrange(3, 13):
....:     if (A-2) % 4 != 0:
....:         continue
....:     try:
....:         E = EllipticCurve(F13, [0, A, 0, 1, 0]) # Montgomery form
....:         E
....:         E.order()
....:     except:
....:         continue
""", globals(), locals(), True)
except:
 _st_.goboom(_sage_const_505 )
try:
 _st_.current_tex_line = _sage_const_509 
 _st_.commandline(_sage_const_28 , r"""
sage: for d in F13:
....:     j= ZZ(0)
....:     for x in F13:
....:         for y in F13:
....:             if x^2+y^2 == 1+d*x^2*y^2:
....:                 j=j+1
....:     print('d=',d)
....:     print('order=',j)
""", globals(), locals(), True)
except:
 _st_.goboom(_sage_const_518 )
try:
 _st_.current_tex_line = _sage_const_530 
 _st_.commandline(_sage_const_29 , r"""
sage: for x in F13:
....:     for y in F13:
....:         if x^2+y^2 == F13(1)+F13(7)*x^2*y^2:
....:             print(x,y)
""", globals(), locals(), True)
except:
 _st_.goboom(_sage_const_535 )
try:
 _st_.current_tex_line = _sage_const_564 
 _st_.commandline(_sage_const_30 , r"""
sage: def Edwards_add((x1,y1),(x2,y2),d):
....:     x3 = F13((F13(x1)*F13(y2)+F13(y1)*F13(x2))/((F13(1)+F13(d)*F13(x1)*F13
....: (x2)*F13(y1)*F13(y2))))
....:     y3 = F13((F13(y1)*F13(y2)-F13(x1)*F13(x2))/((F13(1)-F13(d)*F13(x1)*F13
....: (x2)*F13(y1)*F13(y2))))
....:     return (x3,y3)
""", globals(), locals(), True)
except:
 _st_.goboom(_sage_const_571 )
try:
 _st_.current_tex_line = _sage_const_664 
 _st_.commandline(_sage_const_31 , r"""
sage: F13 = GF(13)
sage: for A in xrange(3, 13):
....:     if (A-2) % 4 != 0:
....:         continue
....:     try:
....:         E = EllipticCurve(F13, [0, A, 0, 1, 0]) # Montgomery form
....:         E
....:         E.order()
....:     except:
....:         continue
""", globals(), locals(), True)
except:
 _st_.goboom(_sage_const_675 )
try:
 _st_.current_tex_line = _sage_const_679 
 _st_.commandline(_sage_const_32 , r"""
sage: j = ZZ(0)
sage: for a in F13:
....:     for d in F13:
....:         j = 0
....:         for x in F13:
....:             for y in F13:
....:                 if a*x^2 + y^2 == 1+d*x^2*y^2:
....:                     j=j+1
....:         print('curve: a=',a,'d=',d,'order:',j)
""", globals(), locals(), True)
except:
 _st_.goboom(_sage_const_689 )
try:
 _st_.current_tex_line = _sage_const_705 
 _st_.commandline(_sage_const_33 , r"""
sage: for x in F13:
....:     for y in F13:
....:         if F13(2)*x^2+y^2 == F13(1)+F13(11)*x^2*y^2:
....:             print(x,y)
""", globals(), locals(), True)
except:
 _st_.goboom(_sage_const_710 )
try:
 _st_.current_tex_line = _sage_const_733 
 _st_.commandline(_sage_const_34 , r"""
sage: def Edwards_add((x1,y1),(x2,y2),a,d):
....:     x3 = F13((F13(x1)*F13(y2)+F13(y1)*F13(x2))/((F13(1)+F13(d)*F13(x1)*F13(x2)*F13(y1)*F13(y2))))
....:     y3 = F13((F13(y1)*F13(y2)-F13(a)*F13(x1)*F13(x2))/((F13(1)-F13(d)*F13(x1)*F13(x2)*F13(y1)*F13(y2))))
....:     return (x3,y3)
""", globals(), locals(), True)
except:
 _st_.goboom(_sage_const_738 )
try:
 _st_.current_tex_line = _sage_const_763 
 _st_.commandline(_sage_const_35 , r"""
sage: F7 = GF(7)
sage: MNT4 = EllipticCurve (F7,[4 ,1])
sage: [P.xy() for P in MNT4.points() if P.order() > 1]
""", globals(), locals(), True)
except:
 _st_.goboom(_sage_const_767 )
try:
 _st_.current_tex_line = _sage_const_794 
 _st_.commandline(_sage_const_36 , r"""
sage: F7t.<t> = F7[]
sage: F7_4.<u> = GF(7^4, name='u', modulus=t^4+t+1) # embedding degree is 4
sage: MNT4 = EllipticCurve (F7_4,[4 ,1])
sage: INF = MNT4(0) # point at infinity
sage: for P in INF.division_points(5): # PI(P) == [q]P
....:     if P.order() == 5: # exclude point at infinity
....:         PiP = MNT4([a.frobenius() for a in P])
....:         qP = 7*P
....:         if PiP == qP:
....:             print(P.xy())
""", globals(), locals(), True)
except:
 _st_.goboom(_sage_const_805 )
try:
 _st_.current_tex_line = _sage_const_822 
 _st_.commandline(_sage_const_37 , r"""
sage: g1 = MNT4([0,1])
sage: g2 = MNT4(2*u^3 + 5*u^2 + 4*u + 2, 2*u^3 + 3*u + 5)
sage: g1.weil_pairing(g2,5)
""", globals(), locals(), True)
except:
 _st_.goboom(_sage_const_826 )
try:
 _st_.current_tex_line = _sage_const_898 
 _st_.commandline(_sage_const_38 , r"""
sage: G.<x> = GF(5^6) # embedding degree is 6
sage: MNT6 = EllipticCurve (G,[2 ,1])
sage: INF = MNT6(0) # point at infinity
sage: for P in INF.division_points(7): # PI(P) == [q]P
....:     if P.order() == 7: # exclude point at infinity
....:         PiP = MNT6([a.frobenius() for a in P])
....:         qP = 5*P
....:         if PiP == qP:
....:             print(P.xy())
""", globals(), locals(), True)
except:
 _st_.goboom(_sage_const_908 )
_st_.endofdoc()

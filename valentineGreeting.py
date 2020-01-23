#Name: Alex Pierce 
#valentinegreeting.py
#Purpose:Valentines greeting card
#Inputs:clicks from user 
#Outputs:valentines greeting card to monitor

from graphics import *
from time import sleep

def main():
    winWidth = 1000
    winHeight = 1000
    win = GraphWin("Valentines Greeting Card", winWidth, winHeight)
    win.setBackground("Red")
    #Instructions
    instPt=Point(winWidth/2, winHeight-20)
    inst=Text(instPt,"Shoot heart to open card")
    inst.setSize(24)
    inst.setTextColor("White")
    inst.draw(win)
    #Heart
    heart=Polygon(Point(499,325), Point(502,319), Point(505,309), Point(509,298),
                  Point(516,286), Point(523,273), Point(533,263), Point(544,251),
                  Point(552,243), Point(565,235), Point(579,226), Point(594,219),
                  Point(607,216), Point(620,212), Point(635,209), Point(647,207),
                  Point(660,206), Point(671,207), Point(687,206), Point(704,209),
                  Point(718,213), Point(735,219), Point(746,225), Point(758,232),
                  Point(769,241), Point(780,252), Point(790,264), Point(799,276),
                  Point(807,289), Point(813,301), Point(817,318), Point(820,336),
                  Point(821,347), Point(820,361), Point(818,375), Point(816,385),
                  Point(814,396), Point(811,407), Point(809,418), Point(805,427),
                  Point(800,439), Point(797,451), Point(792,462), Point(787,470),
                  Point(781,482), Point(776,491), Point(770,499), Point(765,508),
                  Point(759,515), Point(752,524), Point(746,531), Point(739,537),
                  Point(732,546), Point(724,552), Point(714,565), Point(706,572),
                  Point(695,582), Point(683,591), Point(673,599), Point(660,610),
                  Point(647,620), Point(639,628), Point(625,639), Point(616,648),
                  Point(609,654), Point(601,661), Point(592,670), Point(585,677),
                  Point(576,685), Point(569,692), Point(559,702), Point(552,710),
                  Point(543,722), Point(536,731), Point(527,741), Point(521,750),
                  Point(514,760), Point(506,770), Point(500,784), Point(494,777),
                  Point(490,769), Point(485,763), Point(480,755), Point(474,746),
                  Point(468,737), Point(461,728), Point(455,721), Point(445,709),
                  Point(432,694), Point(421,683), Point(410,672), Point(397,660),
                  Point(384,649), Point(373,638), Point(359,628), Point(348,618),
                  Point(335,607), Point(326,601), Point(315,591), Point(305,584),
                  Point(298,575), Point(291,569), Point(283,564), Point(274,555),
                  Point(266,546), Point(257,536), Point(249,526), Point(241,516),
                  Point(232,505), Point(226,494), Point(217,478), Point(209,465),
                  Point(202,449), Point(200,438), Point(189,415), Point(184,391),
                  Point(181,367), Point(180,344), Point(183,321), Point(188,303),
                  Point(194,287), Point(203,272), Point(213,259), Point(225,247),
                  Point(243,232), Point(259,223), Point(278,216), Point(299,210),
                  Point(316,208), Point(333,207), Point(351,209), Point(366,211),
                  Point(378,212), Point(390,216), Point(401,220), Point(416,226),
                  Point(426,232), Point(437,238), Point(449,246), Point(462,257),
                  Point(471,268), Point(479,281), Point(487,298), Point(493,306),
                  Point(495,313))
    heart.setFill("Hot Pink")
    heart.setOutline("White")
    heart.draw(win)
    #cupid
    cupid=Polygon(Point(765,764), Point(760,760), Point(757,757), Point(755,753),
                  Point(749,751), Point(742,748), Point(738,743), Point(734,736),
                  Point(728,734), Point(722,730), Point(721,736), Point(719,741),
                  Point(718,748), Point(716,754), Point(714,761), Point(712,768),
                  Point(709,774), Point(706,778), Point(699,782), Point(695,780),
                  Point(693,778), Point(695,775), Point(699,778), Point(703,774),
                  Point(706,768), Point(708,762), Point(709,754), Point(710,747),
                  Point(711,738), Point(713,730), Point(717,723), Point(717,719),
                  Point(719,712), Point(726,708), Point(728,700), Point(735,695),
                  Point(743,689), Point(752,684), Point(762,679), Point(769,672),
                  Point(773,667), Point(770,664), Point(774,660), Point(779,665),
                  Point(778,673), Point(773,679), Point(768,684), Point(761,689),
                  Point(754,693), Point(748,698), Point(741,703), Point(738,709),
                  Point(737,717), Point(743,725), Point(751,729), Point(761,736),
                  Point(770,740), Point(781,742), Point(792,747), Point(792,744),
                  Point(788,744), Point(786,739), Point(785,735), Point(783,733),
                  Point(785,731), Point(784,729), Point(782,726), Point(783,724),
                  Point(784,721), Point(783,718), Point(783,715), Point(786,715),
                  Point(788,714), Point(791,711), Point(793,707), Point(794,701),
                  Point(795,695), Point(799,690), Point(805,686), Point(809,685),
                  Point(808,682), Point(811,673), Point(814,671), Point(819,667),
                  Point(820,672), Point(822,678), Point(827,680), Point(832,683),
                  Point(843,687), Point(852,691), Point(857,698), Point(862,708),
                  Point(866,719), Point(865,734), Point(858,742), Point(850,747),
                  Point(848,749), Point(848,754), Point(842,756), Point(838,756),
                  Point(832,756), Point(835,760), Point(829,760), Point(823,759),
                  Point(819,760), Point(824,764), Point(829,768), Point(835,765),
                  Point(842,765), Point(852,769), Point(856,769), Point(855,764),
                  Point(855,757), Point(861,754), Point(870,756), Point(878,762),
                  Point(884,766), Point(894,769), Point(893,769), Point(905,769),
                  Point(909,775), Point(904,778), Point(898,777), Point(889,775),
                  Point(894,780), Point(900,782), Point(897,786), Point(891,783),
                  Point(886,781), Point(891,786), Point(893,789), Point(890,790),
                  Point(885,786), Point(879,784), Point(883,789), Point(880,791),
                  Point(878,788), Point(872,784), Point(874,791), Point(872,793),
                  Point(868,793), Point(864,789), Point(865,793), Point(865,795),
                  Point(862,797), Point(860,794), Point(857,791), Point(858,794),
                  Point(857,798), Point(854,797), Point(852,797), Point(851,803),
                  Point(849,811), Point(842,813), Point(835,810), Point(826,804),
                  Point(812,792), Point(807,795), Point(798,800), Point(791,800),
                  Point(788,800), Point(783,806), Point(784,814), Point(785,821),
                  Point(783,829), Point(779,836), Point(778,842), Point(779,853),
                  Point(775,861), Point(773,867), Point(777,871), Point(784,877),
                  Point(785,887), Point(783,896), Point(783,906), Point(785,917),
                  Point(790,924), Point(788,933), Point(781,937), Point(773,937),
                  Point(765,941), Point(755,941), Point(751,934), Point(751,928),
                  Point(760,927), Point(768,920), Point(766,908), Point(763,899),
                  Point(759,885), Point(754,879), Point(749,873), Point(751,866),
                  Point(747,859), Point(741,847), Point(739,837), Point(733,835),
                  Point(725,830), Point(726,836), Point(725,847), Point(724,853),
                  Point(726,861), Point(729,867), Point(727,872), Point(724,878),
                  Point(718,878), Point(715,881), Point(709,885), Point(702,885),
                  Point(698,884), Point(692,877), Point(693,870), Point(701,873),
                  Point(703,865), Point(699,823), Point(698,812), Point(708,803),
                  Point(721,798), Point(734,797), Point(739,786), Point(746,777),
                  Point(752,770), Point(759,764))
    cupid.setFill("Black")
    cupid.setOutline("Light Pink")
    cupid.draw(win)
    line1=Line(Point(798,762), Point(777,675))
    line1.draw(win)
    line2=Line(Point(798,765), Point(705,778))
    line2.draw(win)
    arrow=Polygon(Point(705,705), Point(707,707), Point(708,710), Point(704,712),
                  Point(698,712), Point(694,707), Point(693,700), Point(692,693),
                  Point(698,693), Point(704,693), Point(711,694), Point(715,698),
                  Point(712,705), Point(705,705), Point(775,754), Point(780,767),
                  Point(781,758), Point(791,755), Point(777,752), Point(705,705),)
    arrow.setFill("Deep Pink")
    arrow.setOutline("Black")
    arrow.draw(win)
    #shoot arrow loop
    win.getMouse()
    for i in range(20):
        arrow.move(-10,-10)
        sleep(.05)
    #open card
    win.setBackground("Light Pink")
    heart.undraw()
    cupid.undraw()
    arrow.undraw()
    line1.undraw()
    line2.undraw()
    inst.undraw()
    #right border
    heartr1=Polygon(Point(951,64), Point(954,57), Point(958,51), Point(962,47),
                   Point(967,43), Point(970,38), Point(974,34), Point(978,28),
                   Point(980,21), Point(979,16), Point(977,12), Point(974,8),
                   Point(969,6), Point(964,5), Point(960,7), Point(956,10),
                   Point(952,15), Point(950,21), Point(947,14), Point(944,10),
                   Point(938,7), Point(933,7), Point(927,10), Point(922,15),
                   Point(920,20), Point(922,28),Point(927,34), Point(932,38),
                   Point(936,44), Point(939,50), Point(945,54), Point(947,60))
    heartr1.setFill("Red")
    heartr1.setOutline("White")
    heartr1.draw(win)
    heartr2=Polygon(Point(952,110), Point(954,105), Point(958,100), Point(963,97),
                    Point(970,97), Point(977,99), Point(980,104), Point(980,110),
                    Point(980,117), Point(977,121), Point(974,125), Point(970,129),
                    Point(967,132), Point(963,135), Point(960,139), Point(957,143),
                    Point(953,147), Point(952,152), Point(949,147), Point(946,144),
                    Point(942,139), Point(939,137), Point(936,134), Point(932,130),
                    Point(928,125), Point(925,120), Point(921,114), Point(921,108),
                    Point(924,101), Point(930,97), Point(937,96), Point(943,99),
                    Point(948,105))
    heartr2.setFill("Hot Pink")
    heartr2.setOutline("White")
    heartr2.draw(win)
    heartr3=Polygon(Point(951,182), Point(953,176), Point(957,171), Point(963,168),
                    Point(971,168), Point(978,173), Point(980,181), Point(980,189),
                    Point(976,194), Point(972,198), Point(968,204), Point(963,208),
                    Point(959,213), Point(956,217), Point(952,223), Point(948,219),
                    Point(946,216), Point(943,212), Point(939,210), Point(935,205),
                    Point(930,201), Point(927,196), Point(925,192), Point(923,187),
                    Point(923,180), Point(926,173), Point(929,169), Point(937,168),
                    Point(943,170), Point(946,173))
    heartr3.setFill("Red")
    heartr3.setOutline("White")
    heartr3.draw(win)
    heartr4=Polygon(Point(952,251), Point(954,244), Point(960,240), Point(968,238),
                    Point(975,241), Point(979,247), Point(981,254), Point(979,259),
                    Point(976,263), Point(972,269), Point(969,273), Point(965,276),
                    Point(961,280), Point(958,283), Point(955,288), Point(953,293),
                    Point(951,297), Point(947,288), Point(944,284), Point(939,278),
                    Point(936,277), Point(930,271), Point(926,267), Point(924,264),
                    Point(922,258), Point(922,252), Point(923,246), Point(927,240),
                    Point(936,238), Point(942,240), Point(946,245))
    heartr4.setFill("Hot Pink")
    heartr4.setOutline("White")
    heartr4.draw(win)
    heartr5=Polygon(Point(951,322), Point(955,316), Point(959,310), Point(965,308),
                    Point(971,308), Point(977,312), Point(981,317), Point(981,324),
                    Point(979,330), Point(974,336), Point(970,340), Point(967,344),
                    Point(964,347), Point(960,350), Point(957,355), Point(953,359),
                    Point(953,365), Point(949,360), Point(945,355), Point(942,351),
                    Point(936,347), Point(931,341), Point(927,336), Point(923,329),
                    Point(922,323), Point(924,315), Point(930,310), Point(938,307),
                    Point(946,313))
    heartr5.setFill("Red")
    heartr5.setOutline("White")
    heartr5.draw(win)
    heartr6=Polygon(Point(952,400), Point(954,394), Point(959,388), Point(967,386),
                    Point(974,387), Point(979,392), Point(981,401), Point(978,408),
                    Point(974,414), Point(969,419), Point(962,425), Point(959,429),
                    Point(956,434), Point(953,440), Point(951,443), Point(949,437),
                    Point(945,432), Point(940,428), Point(934,422), Point(930,418),
                    Point(926,413), Point(923,408), Point(922,401), Point(924,392),
                    Point(929,388), Point(936,386), Point(941,387), Point(946,391),
                    Point(949,397))
    heartr6.setFill("Hot Pink")
    heartr6.setOutline("White")
    heartr6.draw(win)
    heartr7=Polygon(Point(952,479), Point(954,473), Point(958,469), Point(965,467),
                    Point(970,467), Point(977,471), Point(980,476), Point(981,481),
                    Point(979,486), Point(976,491), Point(972,495), Point(969,499),
                    Point(966,502), Point(962,505), Point(958,509), Point(955,513),
                    Point(952,518), Point(951,522), Point(949,517), Point(946,513),
                    Point(944,510), Point(940,506), Point(936,504), Point(933,501),
                    Point(930,496), Point(926,490), Point(923,485), Point(922,480),
                    Point(923,475), Point(927,469), Point(934,466), Point(942,467),
                    Point(948,474))
    heartr7.setFill("Red")
    heartr7.setOutline("White")
    heartr7.draw(win)
    heartr8=Polygon(Point(952,566), Point(955,559), Point(958,555), Point(965,554),
                    Point(971,554), Point(977,557), Point(981,562), Point(981,569),
                    Point(978,574), Point(974,579), Point(969,586), Point(966,591),
                    Point(961,595), Point(956,599), Point(954,605), Point(952,610),
                    Point(949,603), Point(944,598), Point(941,596), Point(937,591),
                    Point(933,587), Point(929,582), Point(925,578), Point(922,571),
                    Point(922,563), Point(925,557), Point(931,553), Point(938,552),
                    Point(945,556), Point(949,563))
    heartr8.setFill("Hot Pink")
    heartr8.setOutline("White")
    heartr8.draw(win)
    heartr9=Polygon(Point(952,652), Point(954,646), Point(958,642), Point(965,638),
                    Point(973,639), Point(980,646), Point(981,653), Point(979,661),
                    Point(975,666), Point(971,670), Point(966,674), Point(963,679),
                    Point(959,682), Point(955,687), Point(954,690), Point(952,695),
                    Point(949,689), Point(946,683), Point(941,679), Point(938,677),
                    Point(934,674), Point(932,670), Point(929,667), Point(925,663),
                    Point(923,659), Point(922,653), Point(923,647), Point(928,641),
                    Point(934,638), Point(938,638), Point(945,641), Point(948,647))
    heartr9.setFill("Red")
    heartr9.setOutline("White")
    heartr9.draw(win)
    heartr10=Polygon(Point(952,727), Point(954,720), Point(958,714), Point(963,711),
                     Point(970,711), Point(977,714), Point(981,719), Point(981,725),
                     Point(981,731), Point(977,736), Point(973,741), Point(968,745),
                     Point(963,750), Point(959,754), Point(956,758), Point(954,762),
                     Point(952,768), Point(950,763), Point(946,758), Point(941,753),
                     Point(937,749), Point(933,745), Point(929,740), Point(926,736),
                     Point(923,731), Point(922,723), Point(925,717), Point(931,711),
                     Point(938,711), Point(944,713), Point(950,720))
    heartr10.setFill("Hot Pink")
    heartr10.setOutline("White")
    heartr10.draw(win)
    heartr11=Polygon(Point(952,794), Point(956,786), Point(962,783), Point(969,783),
                     Point(976,785), Point(980,792), Point(980,801), Point(975,806),
                     Point(971,813), Point(966,818), Point(961,822), Point(956,827),
                     Point(952,834), Point(952,839), Point(948,830), Point(944,826),
                     Point(938,820), Point(934,816), Point(930,812), Point(926,807),
                     Point(924,803), Point(921,797), Point(924,791), Point(927,786),
                     Point(934,782), Point(941,782), Point(948,789))
    heartr11.setFill("Red")
    heartr11.setOutline("White")
    heartr11.draw(win)
    heartr12=Polygon(Point(952,866), Point(953,860), Point(957,855), Point(962,853),
                     Point(968,852), Point(974,853), Point(979,858), Point(982,865),
                     Point(979,872), Point(976,877), Point(972,882), Point(967,886),
                     Point(963,890), Point(959,894), Point(955,898), Point(953,901),
                     Point(952,906), Point(948,900), Point(946,897), Point(943,894),
                     Point(938,890), Point(933,886), Point(932,882), Point(927,878),
                     Point(924,873), Point(923,868), Point(923,861), Point(928,855),
                     Point(933,851), Point(941,852), Point(947,858))
    heartr12.setFill("Hot Pink")
    heartr12.setOutline("White")
    heartr12.draw(win)
    heartr13=Polygon(Point(952,942), Point(953,936), Point(958,933), Point(962,930),
                     Point(970,930), Point(977,933), Point(981,940), Point(981,946),
                     Point(979,952), Point(975,957), Point(971,961), Point(966,965),
                     Point(961,970), Point(957,975), Point(954,978), Point(952,984),
                     Point(949,979), Point(947,975), Point(942,971), Point(937,966),
                     Point(932,962), Point(929,957), Point(925,953), Point(922,946),
                     Point(923,938), Point(926,933), Point(933,929), Point(939,929),
                     Point(945,932), Point(948,939))
    heartr13.setFill("Red")
    heartr13.setOutline("White")
    heartr13.draw(win)
    #leftborder
    heartl1=Polygon(Point(45,18), Point(46,14), Point(49,10), Point(52,7),
                    Point(55,4), Point(61,4), Point(66,5), Point(70,9),
                    Point(74,14), Point(74,18), Point(72,25), Point(70,29),
                    Point(67,32), Point(63,36), Point(60,40), Point(56,43),
                    Point(54,46), Point(50,50), Point(47,54), Point(46,58),
                    Point(45,63), Point(44,57), Point(42,54), Point(39,51),
                    Point(37,49), Point(34,45), Point(30,42), Point(27,39),
                    Point(24,36), Point(21,32), Point(18,28), Point(16,24),
                    Point(14,20), Point(15,14), Point(19,9), Point(25,5),
                    Point(30,5), Point(36,7), Point(40,12))
    heartl1.setFill("Red")
    heartl1.setOutline("White")
    heartl1.draw(win)
    heartl2=Polygon(Point(45,88), Point(46,83), Point(49,79), Point(54,76),
                    Point(59,75), Point(65,75), Point(70,78), Point(73,83),
                    Point(75,89), Point(72,95), Point(69,99), Point(65,104),
                    Point(62,107), Point(57,112), Point(53,116), Point(49,120),
                    Point(47,124), Point(45,130), Point(42,124), Point(39,121),
                    Point(34,116), Point(30,112), Point(27,108), Point(23,104),
                    Point(19,100), Point(17,96), Point(16,92), Point(16,89),
                    Point(17,81), Point(22,76), Point(29,74), Point(34,74),
                    Point(40,79), Point(43,84))
    heartl2.setFill("Hot Pink")
    heartl2.setOutline("White")
    heartl2.draw(win)
    heartl3=Polygon(Point(46,166), Point(47,162), Point(48,157), Point(52,153),
                    Point(57,152), Point(62,151), Point(68,153), Point(72,159),
                    Point(74,165), Point(74,172), Point(70,177), Point(66,182),
                    Point(62,186), Point(58,190), Point(54,193), Point(50,197),
                    Point(47,201), Point(45,206), Point(43,203), Point(40,200),
                    Point(38,197), Point(35,193), Point(31,191), Point(28,188),
                    Point(26,185), Point(22,181), Point(19,177), Point(16,173),
                    Point(15,168), Point(15,163), Point(17,157), Point(21,153),
                    Point(27,151), Point(35,152), Point(40,157), Point(43,162))
    heartl3.setFill("Red")
    heartl3.setOutline("White")
    heartl3.draw(win)
    heartl4=Polygon(Point(45,245), Point(47,240), Point(50,235), Point(55,232),
                    Point(61,231), Point(66,232), Point(72,236), Point(73,240),
                    Point(75,246), Point(72,253), Point(67,258), Point(64,262),
                    Point(59,267), Point(55,271), Point(51,275), Point(48,279),
                    Point(45,284), Point(44,289), Point(42,282), Point(39,277),
                    Point(36,275), Point(33,271), Point(29,268), Point(26,265),
                    Point(21,260), Point(19,256), Point(17,253), Point(15,248),
                    Point(15,242), Point(17,238), Point(21,235), Point(25,233),
                    Point(32,233), Point(37,236), Point(41,240))
    heartl4.setFill("Hot Pink")
    heartl4.setOutline("White")
    heartl4.draw(win)
    heartl5=Polygon(Point(46,332), Point(46,327), Point(49,323), Point(53,321),
                    Point(57,319), Point(63,319), Point(69,322), Point(73,326),
                    Point(74,331), Point(74,337), Point(71,342), Point(68,345),
                    Point(64,350), Point(60,354), Point(56,357), Point(52,361),
                    Point(48,365), Point(46,370), Point(44,375), Point(42,369),
                    Point(39,365), Point(36,362), Point(33,359), Point(31,356),
                    Point(27,353), Point(24,349), Point(21,346), Point(18,343),
                    Point(17,339), Point(16,335), Point(16,329), Point(18,324),
                    Point(23,320), Point(29,319), Point(35,319), Point(40,324),
                    Point(43,328))
    heartl5.setFill("Red")
    heartl5.setOutline("White")
    heartl5.draw(win)
    heartl6=Polygon(Point(45,409), Point(47,403), Point(50,398), Point(55,395),
                    Point(60,395), Point(65,395), Point(70,397), Point(73,402),
                    Point(74,407), Point(74,411), Point(71,418), Point(68,422),
                    Point(65,425), Point(62,429), Point(58,432), Point(55,435),
                    Point(53,439), Point(49,441), Point(46,447), Point(45,451),
                    Point(42,445), Point(39,443), Point(36,439), Point(33,436),
                    Point(31,434), Point(28,431), Point(25,428), Point(21,424),
                    Point(19,420), Point(17,417), Point(15,413), Point(15,408),
                    Point(16,403), Point(20,398), Point(25,395), Point(31,395),
                    Point(36,396), Point(41,401), Point(43,406))
    heartl6.setFill("Hot Pink")
    heartl6.setOutline("White")
    heartl6.draw(win)
    heartl7=Polygon(Point(45,482), Point(46,477), Point(50,472), Point(53,469),
                    Point(58,468), Point(62,468), Point(68,469), Point(72,472),
                    Point(74,477), Point(74,481), Point(74,486), Point(72,490),
                    Point(69,493), Point(65,498), Point(62,501), Point(59,505),
                    Point(55,507), Point(51,511), Point(48,515), Point(46,518),
                    Point(44,524), Point(43,518), Point(39,514), Point(37,511),
                    Point(33,508), Point(31,505), Point(27,502), Point(24,499),
                    Point(22,496), Point(19,493), Point(17,490), Point(16,487),
                    Point(14,482), Point(14,479), Point(16,475), Point(19,471),
                    Point(24,469), Point(29,469), Point(35,470), Point(40,475))
    heartl7.setFill("Red")
    heartl7.setOutline("White")
    heartl7.draw(win)
    heartl8=Polygon(Point(45,551), Point(47,547), Point(50,543), Point(53,540),
                    Point(60,539), Point(66,539), Point(71,542), Point(73,547),
                    Point(74,553), Point(72,559), Point(70,563), Point(66,566),
                    Point(63,571), Point(59,574), Point(55,578), Point(52,581),
                    Point(48,585), Point(45,589), Point(43,594), Point(41,586),
                    Point(39,583), Point(34,580), Point(30,576), Point(27,572),
                    Point(23,568), Point(19,564), Point(16,560), Point(16,556),
                    Point(15,548), Point(18,543), Point(23,539), Point(27,538),
                    Point(32,538), Point(37,539), Point(41,545))
    heartl8.setFill("Hot Pink")
    heartl8.setOutline("White")
    heartl8.draw(win)
    heartl9=Polygon(Point(45,622), Point(47,618), Point(50,613), Point(55,610),
                    Point(61,609), Point(67,610), Point(71,615), Point(73,621),
                    Point(73,628), Point(69,634), Point(64,638), Point(60,643),
                    Point(56,647), Point(52,650), Point(48,656), Point(46,660),
                    Point(44,664), Point(42,659), Point(40,656), Point(37,652),
                    Point(34,650), Point(32,647), Point(28,644), Point(25,641),
                    Point(22,637), Point(19,634), Point(17,629), Point(15,626),
                    Point(15,623), Point(15,620), Point(15,618), Point(16,616),
                    Point(20,612), Point(23,610), Point(27,609), Point(33,610),
                    Point(38,612), Point(42,617))
    heartl9.setFill("Red")
    heartl9.setOutline("White")
    heartl9.draw(win)
    heartl10=Polygon(Point(45,699), Point(47,693), Point(50,688), Point(56,685),
                     Point(62,685), Point(68,687), Point(71,691), Point(74,697),
                     Point(74,703), Point(73,708), Point(69,711), Point(66,715),
                     Point(62,719), Point(58,723), Point(53,727), Point(50,732),
                     Point(47,736), Point(44,743), Point(42,737), Point(39,733),
                     Point(35,728), Point(31,725), Point(28,721), Point(23,717),
                     Point(19,713), Point(17,708), Point(15,703), Point(15,696),
                     Point(17,691), Point(20,688), Point(25,686), Point(30,686),
                     Point(37,687), Point(41,691), Point(43,696))
    heartl10.setFill("Hot Pink")
    heartl10.setOutline("White")
    heartl10.draw(win)
    heartl11=Polygon(Point(45,779), Point(47,775), Point(50,770), Point(54,767),
                     Point(60,766), Point(64,766), Point(70,769), Point(72,773),
                     Point(74,778), Point(73,782), Point(71,787), Point(68,790),
                     Point(65,794), Point(61,798), Point(57,802), Point(53,806),
                     Point(50,809), Point(47,814), Point(45,820), Point(43,816),
                     Point(39,812), Point(36,808), Point(32,805), Point(28,800),
                     Point(24,796), Point(20,792), Point(18,789), Point(16,785),
                     Point(15,781), Point(16,773), Point(18,768), Point(23,766),
                     Point(29,765), Point(35,765), Point(40,771), Point(43,776))
    heartl11.setFill("Red")
    heartl11.setOutline("White")
    heartl11.draw(win)
    heartl12=Polygon(Point(46,867), Point(47,862), Point(49,856), Point(54,853),
                     Point(60,852), Point(66,852), Point(71,855), Point(73,860),
                     Point(73,866), Point(72,871), Point(69,877), Point(66,882),
                     Point(62,885), Point(58,889), Point(55,893), Point(51,896),
                     Point(48,899), Point(46,904), Point(44,910), Point(43,903),
                     Point(39,898), Point(35,894), Point(31,891), Point(28,888),
                     Point(25,885), Point(22,882), Point(18,877), Point(16,874),
                     Point(15,869), Point(15,863), Point(18,857), Point(22,853),
                     Point(28,852), Point(32,852), Point(37,854), Point(41,858),
                     Point(43,863))
    heartl12.setFill("Hot Pink")
    heartl12.setOutline("White")
    heartl12.draw(win)
    heartl13=Polygon(Point(45,948), Point(47,943), Point(51,936), Point(57,935),
                     Point(62,935), Point(67,935), Point(72,939), Point(73,946),
                     Point(73,953), Point(70,958), Point(65,963), Point(62,966),
                     Point(59,970), Point(55,973), Point(52,976), Point(49,979),
                     Point(47,984), Point(45,988), Point(42,985), Point(39,981),
                     Point(37,978), Point(33,975), Point(29,971), Point(27,969),
                     Point(24,966), Point(21,963), Point(18,957), Point(15,951),
                     Point(15,946), Point(17,940), Point(21,936), Point(25,936),
                     Point(30,935), Point(36,935), Point(40,939), Point(43,944))
    heartl13.setFill("Red")
    heartl13.setOutline("White")
    heartl13.draw(win)
    #happy valentines day
    textPt=Point(winWidth/2,winHeight/2)
    text=Text(textPt,"HAPPY VALENTINES DAY!")
    text.setSize(36)
    text.setTextColor("White")
    text.draw(win)
    
    #update instructions
    instPt=Point(winWidth/2, winHeight-20)
    inst=Text(instPt,"Click again to close")
    inst.setSize(24)
    inst.setTextColor("White")
    inst.draw(win)
    win.getMouse()
    win.close()
    

def getClicks():
    win = GraphWin("Valentines Greeting Card", 1000, 1000)
    image = Image(Point(1000,1000),"border.ppm")
    image.draw(win)
    points=[]
    for i in range (400):
        pt=win.getMouse()
        pt.draw(win)
        points.append(pt)
        x=pt.getX()
        y=pt.getY()
        print("Point("+str(x)+","+str(y)+")",end= ", ")

main()
#getClicks()


    

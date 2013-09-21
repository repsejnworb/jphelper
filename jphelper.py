import os
import sys
import pyperclip

try:
	with open(r'jplist.txt') as handle:
		the_list = handle.read(1024)
except IOError:
	print 'Loading default list'
	the_list = """Urmaugs Secret [&BDIEAAA=]
	Pig Iron Quarry [&BBkCAAA=]
	Demongrub Pits [&BPwAAAA=]
	King Jaliss Refuge [&BMAAAAA=]
	Spelunkers Delve [&BP4FAAA=]
	Crimson Plateau [&BMYDAAA=]
	Grendich Gamble [&BNoAAAA=]
	Wall Breach Blitz [&BGEBAAA=]
	Loreclaw Expanse [&BMcDAAA=]
	Viziers Tower [&BPcCAAA=]
	Buried Archives [&BCIDAAA=]
	Shamans Rookery [&BHcBAAA=]
	Behem Gauntlet [&BP0BAAA=]
	Under New Management [&BNUGAAA=]"""
the_list = the_list.splitlines()

for puzzle in the_list:
	if puzzle.startswith('#') or len(puzzle.strip()) == 0:
		pass
	else:
		puzzle_name = puzzle.split()[:-1]
		puzzle_location = puzzle.split()[-1]
		print "Next up is %s" % ' '.join(puzzle_name)
		pyperclip.copy(puzzle)
		raw_input("Press Enter to continue...")

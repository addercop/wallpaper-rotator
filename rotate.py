#!/usr/bin/python

#Script to tint a wallpaper through the RGB color space
#with a period of one hour.
#Has a hard dependency on hsetroot.

import colorsys
import os
import random
import sys
import time

def hue_to_rgb(hue):
	(r,g,b) = colorsys.hsv_to_rgb(float(hue)/360.0,1,1)
	r = int(r*255)
	g = int(g*255)
	b = int(b*255)
	s = "%02x%02x%02x" % (r,g,b)
	return s

def main():
	if len(sys.argv) < 2:
		print "usage: rotate [FILE]"
		return
	image = sys.argv[1]
	color = random.randint(1,360)
	while True:
		color = (color + 1) % 360
		rgb = hue_to_rgb(color)
		print "Changing to #%s" % rgb
		os.spawnl(os.P_WAIT,"/usr/bin/hsetroot","hsetroot","-center",image,"-tint","#%s"%rgb)
		time.sleep(10)

if __name__ == "__main__":
	main()

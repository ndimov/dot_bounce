import sys, pygame
import random
import math
import itertools

pygame.init()
width,height = 1366,768
size = width,height
maxSpeed = 9
dotSize = 4
numDots = 20
lineWidth = 3

#speed = [2,2]
black = 0,0,0
white = 255,255,255
webColor = white

screen = pygame.display.set_mode((width,height),pygame.FULLSCREEN)
pygame.display.set_caption("My Game")

dots = [] #x,y,movex,movey,color

init = True
lineDraw = True
webbed = False
coloredWeb = True
paused = False

screen.fill(black)

#several buttons on top (also Hide) which look like (Toggle web [W])

def randSpeed():
	n = random.randint(-maxSpeed,maxSpeed)
	if n <=1: n = 2
	return n

for i in range(numDots):
	x = random.randint(0,width)
	y = random.randint(0,height)
	sx = randSpeed()
	sy = randSpeed()
	color = []
	sum = 0
	for i in range(3):
		c = random.randint(0,255)
		color.append(c)
		sum += c
	if sum < 100:
		for c in color:
			c = c + 50
	dots.append([x,y,sx,sy,color])

while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE: sys.exit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				lineDraw = not lineDraw
			if event.key == pygame.K_LALT:
				webbed = not webbed
				lineDraw = False
			if event.key == pygame.K_x:
				coloredWeb = not coloredWeb
			if event.key == pygame.K_p:
				paused = not paused
				
		
	if webbed or not lineDraw: screen.fill(black)
	
	if webbed:
		for a,b in itertools.combinations(dots,2):
			lColor = webColor
			#print(lColor)
			if coloredWeb:
				lColor=[]
				for i in range(3):
					lColor.append(int((a[4][i] + b[4][i])/2))
				#print(color)
			pygame.draw.line(screen, lColor, [a[0],a[1]], [b[0],b[1]], lineWidth)
	#else:
	for data in dots:
		(x,y,sx,sy,color) = data
		if not webbed: pygame.draw.circle(screen, color, [x,y], dotSize)
		if not paused:
			data[0]=x+sx
			data[1]=y+sy
			if x<=dotSize: data[2]=abs(sx)
			if x>=width-dotSize: data[2]=-abs(sx)
			if y<=dotSize: data[3]=abs(sy)
			if y>=height-dotSize: data[3]=-abs(sy)	
	
	font = pygame.font.SysFont("freesansbold.ttf", 25)
	text = font.render("ESC to quit. SPACE to toggle line draw. ALT to toggle web. X to toggle multicolor web. P to pause.",1,white)
	textpos = text.get_rect()
	screen.blit(text, textpos)
	pygame.display.flip()
	pygame.time.Clock().tick(60)
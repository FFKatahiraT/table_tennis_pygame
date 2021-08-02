import pygame
import random

def ball_spawn():
	global x_ball, y_ball, x_ball_change, y_ball_change
	x_ball=display_width*0.5
	y_ball=display_height*0.5
	x_ball_change=random.randint(-v_init,v_init)
	y_ball_change=random.randint(-v_init,v_init)

def blit(step):
	gameDisplay.fill(yellow)
	gameDisplay.blit(booster_left[step], booster_left_xy)
	gameDisplay.blit(booster_right[step], booster_right_xy)
	gameDisplay.blit(racket1, (x[0]-10,y[0]-100))
	gameDisplay.blit(racket2, (x[1]-10,y[1]-100))
	gameDisplay.blit(ball, (x_ball-40,y_ball-40))
	gameDisplay.blit(counter_textsurface_1,(display_width*0.4,display_height*0.1))
	gameDisplay.blit(counter_textsurface_2,(display_width*0.6,display_height*0.1))

def read(name):
	file=open(name+'.txt', 'r')
	return file.read()
	
def save_results(player1_name, player2_name):
	prev_records=read('records')
	file=open('records.txt', 'w')
	file.write(prev_records)
	file.write(player1_name+': '+str(win_counter[0])+'\t')
	file.write(player2_name+': '+str(win_counter[1])+'\n')
	file.close()

def get_player_name(color):
	global crashed
	running=True
	player_name=''
	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:	#выход из программы
				pygame.quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_BACKSPACE:	#удаление последнего символа
					if len(player_name)>0:
						player_name = player_name[:-1]
				elif event.key == pygame.K_RETURN: 	#конец записи K_RETURN -- кнопка Enter
					running=False
				else:
					player_name += event.unicode	#Ввод текста

		p_name_textsurface = myfont.render('Enter player name: '+player_name, False, color)	#Соберем текст для вывода на экран 
		blit(step)	#Выводим все окружение, что у нас было
		win_textsurface = myfont.render('Game Over!', False, green)	#Собираем текст 'Game over!'
		gameDisplay.blit(win_textsurface,(display_width*0.5,display_height*0.8))	#выводим текст 'Game over!' на экран 
		gameDisplay.blit(p_name_textsurface,(display_width*0.3,display_height*0.3))	#выводим набираемое имя игрока на экран
		pygame.display.update()	#обновляем экран
		clock.tick(60)	#FPS
	return player_name
	
def button_hovered(button_xy, textsurface):
	button_xy_centered=[]
	for i in range(len(button_xy)):
		button_xy_centered.append(button_xy[i]-button_size[i]/2)
	mouse = pygame.mouse.get_pos()
	if 0<=mouse[0]-button_xy_centered[0]<=button_size[0] and 0<=mouse[1]-button_xy_centered[1]<=button_size[1]:
		pygame.draw.rect(gameDisplay,green,button_xy_centered+button_size)
	else:
		pygame.draw.rect(gameDisplay,yellow,button_xy_centered+button_size)	
	gameDisplay.blit(textsurface, button_xy_centered)
		

def menu():
	global button_size
	running=True
	button_start_xy = [display_width*0.5,display_height*0.3]
	button_records_xy = [display_width*0.5,display_height*0.5]
	button_author_xy = [display_width*0.5,display_height*0.7]
	button_quit_xy = [display_width*0.5,display_height*0.9]
	button_size = [150, 50]

	start_textsurface = myfont.render('START', False, white)
	records_textsurface = myfont.render('RECORDS', False, white)
	author_textsurface = myfont.render('AUTHOR', False, white)
	quit_textsurface = myfont.render('QUIT', False, white)

	while running:
		mouse = pygame.mouse.get_pos()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:	#выход из программы
				pygame.quit()
			if event.type == pygame.MOUSEBUTTONDOWN:
				if -button_size[0]/2<=mouse[0]-button_start_xy[0]<=button_size[0]/2 and -button_size[1]/2<=mouse[1]-button_start_xy[1]<=button_size[1]/2:
					game()
				elif -button_size[0]/2<=mouse[0]-button_records_xy[0]<=button_size[0]/2 and -button_size[1]/2<=mouse[1]-button_records_xy[1]<=button_size[1]:
					records()
				elif -button_size[0]/2<=mouse[0]-button_author_xy[0]<=button_size[0]/2 and -button_size[1]/2<=mouse[1]-button_author_xy[1]<=button_size[1]/2:
					author()
				elif -button_size[0]/2<=mouse[0]-button_quit_xy[0]<=button_size[0]/2 and -button_size[1]/2<=mouse[1]-button_quit_xy[1]<=button_size[1]/2:
					pygame.quit()
		
		gameDisplay.blit(menu_background, (display_width*0.5-960,display_height*0.5-540))
		gameDisplay.blit(logo, (display_width*0.5-300,display_height*0.1-32))
		button_hovered(button_start_xy,start_textsurface)
		button_hovered(button_records_xy,records_textsurface)
		button_hovered(button_author_xy,author_textsurface)
		button_hovered(button_quit_xy, quit_textsurface)
		pygame.display.update()	#обновляем экран
		clock.tick(60)	#FPS			

def author():
	button_back_xy = [display_width*0.2,display_height*0.9]
	back_textsurface = myfont.render('BACK', False, white)
	running=True
	while running:
		mouse = pygame.mouse.get_pos()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:	#выход из программы
				pygame.quit()
			if event.type == pygame.MOUSEBUTTONDOWN:
					if -button_size[0]/2<=mouse[0]-button_back_xy[0]<=button_size[0]/2 and -button_size[1]/2<=mouse[1]-button_back_xy[1]<=button_size[1]/2:
						return
		gameDisplay.blit(author_img, (display_width*0.5-254,display_height*0.5-250))
		button_hovered(button_back_xy, back_textsurface)
		pygame.display.update()	#обновляем экран
		clock.tick(60)	#FPS				

def records():
	records_textsurface=[]
	button_back_xy = [display_width*0.2,display_height*0.9]
	button_next_xy = [display_width*0.8,display_height*0.9]
	back_textsurface = myfont.render('BACK', False, white)
	next_textsurface = myfont.render('NEXT', False, white)
	running=True
	data=read('records').replace('\t', '    ').split('\n')
	for i in range(len(data)):
		records_textsurface.append(myfont.render(str(i)+') '+data[i], False, white))

	while running:
		mouse = pygame.mouse.get_pos()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:	#выход из программы
				pygame.quit()
			if event.type == pygame.MOUSEBUTTONDOWN:
					if -button_size[0]/2<=mouse[0]-button_back_xy[0]<=button_size[0]/2 and -button_size[1]/2<=mouse[1]-button_back_xy[1]<=button_size[1]/2:
						return
					elif -button_size[0]/2<=mouse[0]-button_next_xy[0]<=button_size[0]/2 and -button_size[1]/2<=mouse[1]-button_next_xy[1]<=button_size[1]/2:
						records_textsurface=records_textsurface[i:]
		gameDisplay.fill(blue)
		button_hovered(button_back_xy, back_textsurface)
		for i in range(len(records_textsurface)):
			if 0.2+0.1*i<=0.8:
				gameDisplay.blit(records_textsurface[i],(display_width*0.25, display_height*(0.1+0.1*i)))
			else:
				button_hovered(button_next_xy, next_textsurface)
				break_record=i
				break
		pygame.display.update()	#обновляем экран
		clock.tick(60)	#FPS				

def game():
	global crashed, x, y, x_ball, y_ball, x_change, y_ball, x_ball_change, y_ball_change
	global counter_textsurface_1, counter_textsurface_2, win_counter
	global booster_right_xy, booster_left_xy, step
	x=[display_width*0.8, display_width*0.2]
	y=[display_height*0.5, display_height*0.5]
	booster_right_xy = [display_width*0.5-120,display_height*0.2-40]
	booster_left_xy = [display_width*0.5-120,display_height*0.8-40]
	x_change=[0,0]
	y_change=[0,0]
	win_counter=[0,0]
	spawn_timer=0
	step=0

	ball_spawn()
	running = True
	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
			############################
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					x_change[0] = -5
				elif event.key == pygame.K_RIGHT:
					x_change[0] = 5
				elif event.key == pygame.K_UP:
					y_change[0] = -5
				elif event.key == pygame.K_DOWN:
					y_change[0] = 5
				if event.key == pygame.K_a:
					x_change[1] = -5
				elif event.key == pygame.K_d:
					x_change[1] = 5
				elif event.key == pygame.K_w:
					y_change[1] = -5
				elif event.key == pygame.K_s:
					y_change[1] = 5
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
					x_change[0] = 0
				elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
					y_change[0] = 0
				if event.key == pygame.K_a or event.key == pygame.K_d:
					x_change[1] = 0
				elif event.key == pygame.K_w or event.key == pygame.K_s:
					y_change[1] = 0
			############################
		
		if spawn_timer<=0:	#Неприкосновенность мяча после спавна
			for i in range(len(x)):
				length = ((x_ball-x[i])**2+(y_ball-y[i])**2)**0.5
				x_ball_change += 10**1*(x_ball-x[i])/sigma*2.718**(-0.001*(length/sigma)**2)
				y_ball_change += 10**1*(y_ball-y[i])/sigma*2.718**(-0.001*(length/sigma)**2)
		else:
			spawn_timer-=1

		x_ball_change/=1.05	#Торможение мяча
		y_ball_change/=1.05

		if 0<=x_ball-booster_left_xy[0]<=240 and 0<=y_ball-booster_left_xy[1]<=80 and x_ball_change>0:
			x_ball_change*=1.2
		elif 0<=x_ball-booster_right_xy[0]<=240 and 0<=y_ball-booster_right_xy[1]<=80  and x_ball_change<0:
			x_ball_change*=1.2	#Условие ускореня бустерами
			
		for i in range(len(x)):
			x[i]+=x_change[i]
			y[i]+=y_change[i]
		x_ball+=x_ball_change
		y_ball+=y_ball_change

		for i in range(len(x)):
			if x[i]>=display_width:
				x[i]=display_width-10
			elif x[i]<=0:
				x[i]=10
			if y[i]>=display_height:
				y[i]=display_height-10
			elif y[i]<=0:
				y[i]=10
		if x_ball>=display_width:
			ball_spawn()
			spawn_timer=180
			win_counter[0]+=1
		elif x_ball<=0:
			ball_spawn()
			spawn_timer=180
			win_counter[1]+=1
		if y_ball>=display_height-40:
			y_ball=display_height-41
			y_ball_change*=-1
		elif y_ball<=40:
			y_ball=41
			y_ball_change*=-1

		counter_textsurface_1 = myfont.render(str(win_counter[0]), False, blue)
		counter_textsurface_2 = myfont.render(str(win_counter[1]), False, red)

		if pygame.time.get_ticks()%100==0:	#Каждую 0.1 с step будет изменятся на 1
			step+=1
		if step>=3:	#Если step 3 (у нас только 3 кадра в booster), то сбрасываем step на 0
			step=0
		blit(step)	#Отрисовываем элементы игры

		for i in range(len(win_counter)):
			if win_counter[i] >=11:
				player1_name=get_player_name(blue)
				player2_name=get_player_name(red)
				save_results(player1_name, player2_name)
				running=False

		pygame.display.update()
		clock.tick(60)

pygame.init()
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 36)

display_width = 800
display_height = 600
gameDisplay = pygame.display.set_mode((display_width,display_height))

pygame.display.set_caption('Table_tennis_game')

black = (0,0,0)
white = (255,255,255)
yellow = (255,255,0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

clock = pygame.time.Clock()

racket1 = pygame.image.load('racket1.png')
racket2 = pygame.image.load('racket2.png')
ball = pygame.image.load('ball.png')
booster_left=[]
for i in range(3):
	booster_left.append(pygame.image.load('booster'+str(i+1)+'.png'))	#Подгружаем картинки ускорителя в список
booster_right=[]
for i in range(3):
	booster_right.append(pygame.image.load('booster'+str(i+1)+'_right.png'))	#Подгружаем картинки ускорителя в список
logo = pygame.image.load('logo.png')
menu_background = pygame.image.load('background.jpeg')
author_img = pygame.image.load('author.jpg')

sigma=1
v_init=13

menu()
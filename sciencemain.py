import pygame,sys,random,time

pygame.init()



#이미지 불러오기
fire = pygame.image.load("Simple-Flame-PNG-HD-Quality.png")
fire = pygame.transform.scale(fire,(30,50))

font_text = pygame.font.SysFont(None,30)
temperature_text = pygame.font.SysFont(None,30) 

#마우스 위치
x_pos_mouse = 0
y_pos_mouse = 0
mouse_pos = 0

fire_rect_size = 0


#처음위치 지정
ball_pos_x = []
ball_pos_y = []

for i in range(0,10):
    ball_pos_x.append(random.randrange(170,700))
    ball_pos_y.append(random.randrange(190,370))


#처음 속도,방향 지정
ball_speed_x=[]
ball_speed_y=[]
for x in range(0,10):
    ball_speed_x.append(1)
    ball_speed_y.append(1)

fbx = 0
fby = 0
rect = pygame.Rect(410,450,100,20)
#마우스가 검정 색을  클릭했을때
def click(pos):
    global fire_rect_size
    global fbx
    global fby
    if rect.collidepoint(pos):
        print("fire")
        fire_rect_size =fire_rect_size+10
        print(fire_rect_size)


#색상
Blue = 0,0,255
White = 255,255,255
Black = 0,0,0

r = 10
print(ball_pos_y)
compare = []
compare.append(190)
compare.append(370)
compare.append(700)
compare.append(170)

ballspeedx = 1
ballspeedy = 1

ballspeedx1 = 1
ballspeedy1 = 1

ballspeedx2 = 1
ballspeedy2 = 1

ballspeedx3 = 1
ballspeedy3 = 1

ballspeedx4 = 1
ballspeedy4 = 1

enter = 0

def first():
    global fbx
    global enter

    
    fbx +=0.0001
    enter = 0
  


temperature = 255
start_input = 0
start_time = time.time()    
print("사용설명서: 샤를의 법칙 시뮬레이션 온도를 높이고 싶을떄 검정색 사각형을 클릭한뒤 0을 누른다. 그럼 온도가 높아져서 입자의 속도가 빨라진다.")
start_input = input("계속하려면 y키를 누르시오")
if start_input == 'y':
    run = True
    display = pygame.display.set_mode((900,500))
while run:##################################################################################################
    pygame.display.flip()
    mouse_pos = None
    end_time = time.time()
    Time = end_time - start_time
    result_time = round(Time,0)

    
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            run = False
        
        #마우스 위치
        if event.type == pygame.MOUSEMOTION:
            x_pos_mouse,y_pos_mouse = pygame.mouse.get_pos()
            x_pos_mouse = x_pos_mouse -25
            y_pos_mouse = y_pos_mouse -25
        #마우스 클릭 위치   
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            print(mouse_pos)
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_0:
                enter = 1


        #불 크기 +30까지 제한    
    if fire_rect_size == 40:
        fire_rect_size = 0
        fbx = 0
        fby = 0
    if enter == 1:
        first()
        print("okok")
        

        
    #공의 처음 움직임
    ball_pos_x[0] += ballspeedx
    ball_pos_y[0] += ballspeedy

    ball_pos_x[1] += ballspeedx1
    ball_pos_y[1] += ballspeedy1

    ball_pos_x[2] += ballspeedx2
    ball_pos_y[2] += ballspeedy2

    ball_pos_x[3] += ballspeedx3
    ball_pos_y[3] += ballspeedy3

    ball_pos_x[4] += ballspeedx4
    ball_pos_y[4] += ballspeedy4










   #compare 
   #0:190,1:170,2:700
    if ball_pos_x[0] <= compare[3]+r:
        ballspeedx = -ballspeedx

        ball_pos_x[0] = 170+r 
        
    
    elif ball_pos_x[0] >= compare[2]-r:
        ballspeedx = -ballspeedx

        ball_pos_x[0] = 700-r
       
        

    if ball_pos_y[0] >= compare[1]:
        ballspeedy = -ballspeedy
        fby = -fby
        ball_pos_y[0] = 370-r
        

    elif ball_pos_y[0] <= compare[0]:
        ballspeedy = -ballspeedy
        fby = -fby
        ball_pos_y[0] = 190+r 




    if ball_pos_x[1] <= compare[3]+r:
        ballspeedx1 = -ballspeedx1
        ball_pos_x[1] = 170+r 

    
    elif ball_pos_x[1] >= compare[2]-r:
        ballspeedx1 = -ballspeedx1
        ball_pos_x[1] = 700-r

       
        

    if ball_pos_y[1] >= compare[1]-r:
        ballspeedy1 = -ballspeedy1
        ball_pos_y[1] = 370-r
        fby = -fby
        
        

    elif ball_pos_y[1] <= compare[0]+r:
        ballspeedy1 = -ballspeedy1
        ball_pos_y[1] = 190+r 
        fby = -fby
       




    if ball_pos_x[2] <= compare[3]+r: 
        ballspeedx2 = -ballspeedx2

        ball_pos_x[2] = 170+r 
        
    
    elif ball_pos_x[2] >= compare[2]-r:
        ballspeedx2 = -ballspeedx2

        ball_pos_x[2] = 700-r
       
        

    if ball_pos_y[2] >= compare[1]-r:
        ballspeedy2 = -ballspeedy2
        fby = -fby
        ball_pos_y[2] = 370-r
        

    elif ball_pos_y[2] <= compare[0]+r:
        ballspeedy2 = -ballspeedy2
        fby = -fby
        ball_pos_y[2] = 190+r 



    if ball_pos_x[3] <= compare[3]+r:
        ballspeedx3 = -ballspeedx3

        ball_pos_x[3] = 170+r 
        
    
    elif ball_pos_x[3] >= compare[2]-r:
        ballspeedx3 = -ballspeedx3

        ball_pos_x[3] = 700-r
       
        

    if ball_pos_y[3] >= compare[1]-r:
        ballspeedy3 = -ballspeedy3
        fby = -fby
        ball_pos_y[3] = 370-r
        

    elif ball_pos_y[3] <= compare[0]+r:
        ballspeedy3 = -ballspeedy3
        fby = -fby
        ball_pos_y[3] = 190+r 


    if ball_pos_x[4] <= compare[3]+r:
        ballspeedx4 = -ballspeedx4

        ball_pos_x[4] = 170+r 
        
    
    elif ball_pos_x[4] >= compare[2]-r:
        ballspeedx4 = -ballspeedx4

        ball_pos_x[4] = 700-r
       
        

    if ball_pos_y[4] >= compare[1]-r:
        ballspeedy4 = -ballspeedy4
        fby = -fby
        ball_pos_y[4] = 370-r
        

    elif ball_pos_y[4] <= compare[0]+r:
        ballspeedy4 = -ballspeedy4
        fby = -fby
        ball_pos_y[4] = 190+r 

    if result_time % 5 == 0:     
        
        if ballspeedx < 0:
            ballspeedx -= 0.0001+fbx

        else:
            ballspeedx += 0.0001+fbx

        if ballspeedy < 0:    
            ballspeedy -= 0.0001+fbx
        else:
            ballspeedy += 0.0001+fbx



        
        
        if ballspeedx1 < 0:
            ballspeedx1 -= 0.0001+fbx
        else:
            ballspeedx1 += 0.0001+fbx
        if ballspeedy1 < 0:    
            ballspeedy1 -= 0.0001+fbx
        else:
            ballspeedy1 += 0.0001+fbx

        
        
        
        if ballspeedx2 < 0:
            ballspeedx2 -= 0.0001+fbx
        else:
            ballspeedx2 += 0.0001+fbx
        if ballspeedy2 < 0:    
            ballspeedy2 -= 0.0001+fbx
        else:
            ballspeedy2 += 0.0001+fbx

        
        
        
        if ballspeedx3 < 0:
            ballspeedx3 -= 0.0001+fbx
        else:
            ballspeedx3 += 0.0001+fbx
        if ballspeedy3 < 0:    
            ballspeedy3 -= 0.0001+fbx
        else:
            ballspeedy3 += 0.0001+fbx


        if ballspeedx4 < 0:
            ballspeedx4 -= 0.0001+fbx
        else:
            ballspeedx4 += 0.0001+fbx
        if ballspeedy4 < 0:    
            ballspeedy4 -= 0.0001+fbx
        else:
            ballspeedy4 += 0.0001+fbx


        temperature += 1+fbx*1000
        
        



            

    if mouse_pos:
        click(mouse_pos)




    fire_rect = pygame.image.load("Simple-Flame-PNG-HD-Quality.png")
    fire_rect = pygame.transform.scale(fire_rect,(30+fire_rect_size,50+fire_rect_size))
    
    #화면 띄우기
 
    display.fill((255,255,255))
    pygame.draw.rect(display,Black,(410,450,100,20))
    pygame.draw.rect(display,(255,0,0),(800,450,20,temperature))



    pygame.draw.circle(display,Blue,(ball_pos_x[0],ball_pos_y[0]),10)
    pygame.draw.circle(display,Blue,(ball_pos_x[1],ball_pos_y[1]),10)
    pygame.draw.circle(display,Blue,(ball_pos_x[2],ball_pos_y[2]),10)
    pygame.draw.circle(display,Blue,(ball_pos_x[3],ball_pos_y[3]),10)
    pygame.draw.circle(display,Blue,(ball_pos_x[4],ball_pos_y[4]),10)


    pygame.draw.line(display,Black,(170,370),(700,370))#아레쪽
    pygame.draw.line(display,Black,(170,370),(170,190))#왼쪽
    pygame.draw.line(display,Black,(700,370),(700,190))#오른쪽
    pygame.draw.line(display,Black,(170,190),(700,190))#위쪽
    display.blit(fire,(x_pos_mouse,y_pos_mouse)) 
    display.blit(fire_rect,(430,400))            
    pygame.display.update()
pygame.quit()
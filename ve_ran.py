#Thư viện pygame
#Câu lệnh bắt buộc có khi setting pygame.
import pygame
import random
import sys
pygame.init()

#BIẾN
##font chữ của game 
fontchu1="04B_19.TTF"
fontchu2="Lobster-Regular.ttf"
font_menu=pygame.font.Font(fontchu1,50)# Chọn font và cỡ chữ
font_mode=pygame.font.Font(fontchu2,30)# Chọn font và cỡ chữ
##Khởi tạo giá trị x ,y ban đầu để sử dụng di chuyển 
dis_rong=800
dis_cao=600
##Tạo thuộc tính người chơi 
###người chơi 1
player1_x1=dis_rong/2
player1_y1=dis_cao/2
###người chơi 2
player2_x1=dis_rong/2
player2_y1=dis_cao/2
##Tạo các biến mới x1_change và y1_change để giữ các giá trị cập nhật của tọa độ x và y.
###giá trị tọa độ mới của người chơi 1
x1_change=0
y1_change=0
###giá trị tọa độ mới của người chơi 2
x2_change=0
y2_change=0

snake_block1=20#Tạo khối thân rắn
snake_block2=20#Tạo khối thân rắn
snake_speed1=20
snake_speed2=20
body_list_1=[]#lưu lại phần thân rắn 
body_list_2=[]#lưu lại phần thân rắn 
length_body_snake1=1#độ dài của rắn 
length_body_snake2=1#độ dài của rắn 
score_choi1=0
score_show1=0
score_choi2=0
score_show2=0
hscore=0#Điểm cao nhất
##khởi biến bg_x=o để thực hiện di chuyển background cho game
bg_x=0

#XỬ LÝ MÀN HÌNH GAME
##Tạo cửa số game và tiêu đề game
screen=pygame.display.set_mode((dis_rong,dis_cao))
pygame.display.set_caption("Game Snakes")
##Khởi tạo hàm điều chỉnh tốc độ hiển thị(điều khiển của user) của rắn  
clock = pygame.time.Clock()
##Tạo icon game
###sử dung image.load để tải icon snake.png từ file theo path
icon=pygame.image.load(r"snake.png")
pygame.display.set_icon(icon)
##Thêm background cho game
bg=pygame.image.load(r"desktop-wallpaper-snake-game-cool-green-gaming.png")
bg=pygame.transform.scale2x(bg)

#XỬ LÝ 
##Tạo food cho snake
foodx = round(random.randrange(0, (dis_rong - snake_block1)/20.0)) * 20.0
foody = round(random.randrange(20, (dis_cao - snake_block1)/20.0)) * 20.0
# Biến để xác định chế độ chơi (1 người hoặc 2 người)
modechoi=0
##Vòng lặp xử lý hiển thị game
###Tạo biến running để kiểm tra xem game còn chạy hay dừng rồi
running=False # Ban đầu không chạy game
show_menu = True
while True :
    #cho biết thông tin về hành động của user từ hàm event.get() diễn ra trên màn hình 
    for event in pygame.event.get():
        #nếu người dùng click nút thoát(x) trên cửa sổ game thì dừng game 
        if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        if event.type==pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            # Kiểm tra xem người dùng có nhấn vào nút "1 Player" không
            if button_Mode1.collidepoint(mouse_pos):
                modechoi = 1
                running = True
                show_menu=False
               
            # Kiểm tra xem người dùng có nhấn vào nút "2 Players" không
            elif button_Mode2.collidepoint(mouse_pos):
                modechoi = 2
                running = True
                show_menu=False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if not running:  # Nếu trạng thái chơi là False (đang không chơi)
                    running = True  # Bắt đầu trạng thái chơi
                    # Khởi tạo lại các biến cần thiết cho trò chơi ở đây (tùy vào chế độ chơi)
            elif event.key == pygame.K_m:
                if not running:  # Nếu trạng thái chơi là False (đang không chơi)
                    ##vẽ đối tượng lên trên màn hình dùng blit
                    screen.blit(bg,(bg_x,0))
                    show_menu=True# trở về menu game
                    # Khởi tạo lại các biến cần thiết cho trò chơi ở đây (tùy vào chế độ chơi)        
    if show_menu:
            #Menu game
            menu_text=font_menu.render("Menu game Snakes",True,(255,0,0))# Tạo hình ảnh chứa văn bản
            menu_rect = menu_text.get_rect(center=(dis_rong // 2, dis_cao // 2 - 50))#để lấy hình chữ nhật (rectangle) bao quanh văn bản
            screen.blit(menu_text,menu_rect)    # Hiển thị hình ảnh chứa văn bản lên màn hình
            ##Vẽ mode 1 người chơi
            button_Mode1=pygame.Rect(dis_rong // 2 - 100, dis_cao // 2, 250, 50)#khởi tạo button 
            pygame.draw.rect(screen,(255,255,255),button_Mode1)#vẽ khung button
            Mode1_text=font_mode.render("Chế độ 1 người",True,(255,0,0))# Tạo hình ảnh chứa văn bản
            Mode1_rect = Mode1_text.get_rect(center=button_Mode1.center)#để lấy hình chữ nhật (rectangle) bao quanh văn bản
            screen.blit(Mode1_text,Mode1_rect)    # Hiển thị hình ảnh chứa văn bản lên màn hình
            ##Vẽ mode 2 người chơi
            button_Mode2=pygame.Rect(dis_rong // 2 - 100, dis_cao // 2 +70, 250, 50)#khởi tạo button 
            pygame.draw.rect(screen,(255,255,255),button_Mode2)
            Mode2_text=font_mode.render("Chế độ 2 người",True,(255,0,0))# Tạo hình ảnh chứa văn bản
            Mode2_rect = Mode2_text.get_rect(center=button_Mode2.center)#để lấy hình chữ nhật (rectangle) bao quanh văn bản
            screen.blit(Mode2_text,Mode2_rect)    # Hiển thị hình ảnh chứa văn bản lên màn hình
    pygame.display.update()
    font_score=pygame.font.Font(fontchu1,20)
    if running:
        # Xử lý logic game khi đang chạy
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if modechoi == 1:
                # Xử lý điều khiển và logic cho chế độ 1 người chơi
                #di chuyển 
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_UP:
                        x1_change=0
                        y1_change=-snake_block1
                    elif event.key==pygame.K_DOWN:
                        x1_change=0
                        y1_change=snake_block1
                    elif event.key==pygame.K_RIGHT:
                        x1_change=snake_block1
                        y1_change=0
                    elif event.key==pygame.K_LEFT:
                        x1_change=-snake_block1
                        y1_change=0
                    elif event.key==pygame.K_SPACE:#Nếu bấm space thì sẽ chơi lại 
                        running=True
                ##di chuyển background từ phải về trái tới lề bên trái là -800 thì gán bg_x=0 để thực hiện nối thêm background vào game
                bg_x-=1
                ##vẽ đối tượng lên trên màn hình dùng blit
                screen.blit(bg,(bg_x,0))
                ##xử lý background chạy vô tận
                if(bg_x==-800):
                    bg_x=0
                screen.blit(bg,(bg_x+800,0))  
                #cập nhật lại thông tin màn hình 
                #Thực hiện di chuyển cập nhật vị trí x1 và y1
                player1_x1+=x1_change
                player1_y1+=y1_change
                #Thêm thân cho snake (xử lý List)
                body_list_1.append((player1_x1,player1_y1))
                #vẽ Food (hình chữ nhật)
                pygame.draw.rect(screen,(255,0,0),[foodx,foody,snake_block1,snake_block1])
                #Sau khi dùng for thì phần thân rắn sẽ tự động thêm vào chúng ta cần xử lý sự kiện này 
                if len(body_list_1)>length_body_snake1:
                    del body_list_1[0] #Nếu phần thân của rắn lớn hơn độ dài rắn thì xóa phần đầu 
                #Tạo hình dạng snake1
                for player1_x1,player1_y1 in body_list_1:
                    #draw.rect( , ,[x,y,dài,rộng]) rect: vẽ hình chữ nhật
                    pygame.draw.rect(screen,(255,255,255),[player1_x1,player1_y1,snake_block1,snake_block1])#Đầu
                #xử lý thức ăn 
                if player1_x1==foodx and player1_y1==foody:
                    #Thêm phần thân rắn vào list body_list
                    length_body_snake1+=1
                    #tính điểm
                    score_choi1+=1
                    score_show1=score_choi1
                    if score_choi1>hscore:
                        hscore=score_choi1
                    #Random lại thức ăn 
                    foodx = round(random.randrange(0, (dis_rong - snake_block1)/20.0)) * 20.0
                    foody = round(random.randrange(20, (dis_cao - snake_block1)/20.0)) * 20.0
                #Kiểm tra va chạm
                if player1_x1>=dis_rong or player1_x1<0 or player1_y1>=dis_cao or player1_y1<20 or (player1_x1,player1_y1)in body_list_1[:-1]:
                    running=False
                #Hiển thị điểm chế độ 1 người 
                if running:
                    score_txt=font_score.render(f'_____________________________Your score: {score_choi1}________________________________',True,(65,105,255))#Print score lên màn hình
                    screen.blit(score_txt,(0,0))#position hiển thị
                else:
                    score_txt1=font_score.render(f'Your score: {score_show1}',True,(64,224,208))#Print score lên màn hình
                    screen.blit(score_txt1,(350,360))#position hiển thị
                    hscore_txt=font_score.render(f'High score: {hscore}',True,(64,224,208))
                    screen.blit(hscore_txt,(350,390))
                    note_txt=font_score.render(f'Press space to play again or press m to go back to game menu  !!!',True,(255,0,0))
                    screen.blit(note_txt,(80,320))
                     #reset game
                    player1_x1 = dis_rong / 2
                    player1_y1 = dis_cao / 2
                    x1_change = 0
                    y1_change = 0
                    body_list_1 = []
                    length_body_snake1 = 1
                    score_choi1 = 0
                    score_show1 = 0
                #Thời gian càng nhỏ thì răn di chuyển càng chậm có thể dùng để tăng độ khó của game 
                clock.tick(snake_speed1)#snake_speed fps
            elif modechoi == 2:
                # Xử lý điều khiển và logic cho chế độ 2 người chơi
                # Điều khiển rắn của người chơi 1 trong chế độ chơi 2 người
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_UP:
                        x1_change=0
                        y1_change=-snake_block2
                    elif event.key==pygame.K_DOWN:
                        x1_change=0
                        y1_change=snake_block2
                    elif event.key==pygame.K_RIGHT:
                        x1_change=snake_block2
                        y1_change=0
                    elif event.key==pygame.K_LEFT:
                        x1_change=-snake_block2
                        y1_change=0
                    elif event.key==pygame.K_SPACE:#Nếu bấm space thì sẽ chơi lại 
                        running=True
            # Điều khiển rắn của người chơi 2 trong chế độ chơi 2 người       
                    elif event.key==pygame.K_w:
                        x2_change=0
                        y2_change=-snake_block2
                    elif event.key==pygame.K_s:
                        x2_change=0
                        y2_change=snake_block2
                    elif event.key==pygame.K_d:
                        x2_change=snake_block2
                        y2_change=0
                    elif event.key==pygame.K_a:
                        x2_change=-snake_block2
                        y2_change=0
                    elif event.key==pygame.K_SPACE:#Nếu bấm space thì sẽ chơi lại 
                        running=True
                
                ##di chuyển background từ phải về trái tới lề bên trái là -800 thì gán bg_x=0 để thực hiện nối thêm background vào game
                bg_x-=1
                ##vẽ đối tượng lên trên màn hình dùng blit
                screen.blit(bg,(bg_x,0))
                ##xử lý background chạy vô tận
                if(bg_x==-800):
                    bg_x=0
                screen.blit(bg,(bg_x+800,0))  
                #Kiểm tra va chạm
                if (player1_x1 >= dis_rong or player1_x1 < 0 or player1_y1 >= dis_cao or player1_y1 < 20) or ((player1_x1, player1_y1) in body_list_1[:-1]) or \
                (player2_x1 >= dis_rong or player2_x1 < 0 or player2_y1 >= dis_cao or player2_y1 < 20) or ((player2_x1, player2_y1) in body_list_2[:-1]) or \
                ((player1_x1, player1_y1) in body_list_2[:-1] or (player2_x1, player2_y1) in body_list_1[:-1]):
                    running = False
                #cập nhật lại thông tin màn hình 
                #Thực hiện di chuyển cập nhật vị trí x1 và y1
                player1_x1+=x1_change
                player1_y1+=y1_change
                #Thực hiện di chuyển cập nhật vị trí x2 và y2
                player2_x1+=x2_change
                player2_y1+=y2_change
                #Thêm thân cho snake (xử lý List)
                body_list_1.append((player1_x1,player1_y1))
                body_list_2.append((player2_x1,player2_y1))
                #vẽ Food (hình chữ nhật)
                pygame.draw.rect(screen,(255,0,0),[foodx,foody,snake_block2,snake_block2])
                #Sau khi dùng for thì phần thân rắn sẽ tự động thêm vào chúng ta cần xử lý sự kiện này 
                if len(body_list_1)>length_body_snake1:
                    del body_list_1[0] #Nếu phần thân của rắn lớn hơn độ dài rắn thì xóa phần đầu 
                if len(body_list_2)>length_body_snake2:
                    del body_list_2[0] #Nếu phần thân của rắn lớn hơn độ dài rắn thì xóa phần đầu 
                #Tạo hình dạng snake1
                for player1_x1,player1_y1 in body_list_1:
                    #draw.rect( , ,[x,y,dài,rộng]) rect: vẽ hình chữ nhật
                    pygame.draw.rect(screen,(255,255,255),[player1_x1,player1_y1,snake_block2,snake_block2])#Đầu
                #Tạo hình dạng snake2
                for player2_x1,player2_y1 in body_list_2:
                    #draw.rect( , ,[x,y,dài,rộng]) rect: vẽ hình chữ nhật
                    pygame.draw.rect(screen,(255,255,255),[player2_x1,player2_y1,snake_block2,snake_block2])#Đầu
                #xử lý thức ăn 
                if player1_x1==foodx and player1_y1==foody:
                    #Thêm phần thân rắn vào list body_list
                    length_body_snake1+=1
                    #tính điểm
                    score_choi1+=1
                    score_show1=score_choi1
                    if score_choi1>hscore:
                        hscore=score_choi1
                    #Random lại thức ăn 
                    foodx = round(random.randrange(0, (dis_rong - snake_block2)/20.0)) * 20.0
                    foody = round(random.randrange(20, (dis_cao - snake_block2)/20.0)) * 20.0
                elif player2_x1==foodx and player2_y1==foody:
                    length_body_snake2+=1
                    #tính điểm
                    score_choi2+=1
                    score_show2=score_choi2
                    if score_choi2>hscore:
                        hscore=score_choi2
                    #Random lại thức ăn 
                    foodx = round(random.randrange(0, (dis_rong - snake_block2)/20.0)) * 20.0
                    foody = round(random.randrange(20, (dis_cao - snake_block2)/20.0)) * 20.0
                 #Hiển thị điểm chế độ 2 người 
                if running:
                    score_txt=font_score.render(f'___________________Player1 score: {score_choi1} | Player2 score: {score_choi2}___________________',True,(65,105,255))#Print score lên màn hình
                    screen.blit(score_txt,(0,0))#position hiển thị
                else:
                    score_txt1=font_score.render(f'Player1 score: {score_show1}',True,(64,224,208))#Print score lên màn hình
                    screen.blit(score_txt1,(350,360))#position hiển thị
                    score_txt1=font_score.render(f'Player2 score: {score_show2}',True,(64,224,208))#Print score lên màn hình
                    screen.blit(score_txt1,(350,380))#position hiển thị
                    hscore_txt=font_score.render(f'High score: {hscore}',True,(64,224,208))
                    screen.blit(hscore_txt,(350,400))
                    note_txt=font_score.render(f'Press space to play again or press m to go back to game menu!!!',True,(255,0,0))
                    screen.blit(note_txt,(80,320))
                    #reset game
                    player1_x1 = dis_rong / 2
                    player1_y1 = dis_cao / 2
                    player2_x1 = dis_rong / 2 
                    player2_y1 = dis_cao / 2 
                    x1_change = 0
                    y1_change = 0
                    x2_change = 0
                    y2_change = 0
                    body_list_1 = []
                    body_list_2 = []
                    length_body_snake1 = 1
                    length_body_snake2 = 1
                    score_choi1 = 0
                    score_show1 = 0
                    score_choi2 = 0
                    score_show2 = 0   
                #Thời gian càng nhỏ thì răn di chuyển càng chậm có thể dùng để tăng độ khó của game 
                clock.tick(snake_speed2)#snake_speed fps
            pygame.display.update()

    


    
            

#Thư viện pygame
#Câu lệnh bắt buộc có khi setting pygame.
import pygame
import random
pygame.init()

#BIẾN
##Khởi tạo giá trị x ,y ban đầu để sử dụng di chuyển 
dis_rong=800
dis_cao=600
x1=dis_rong/2
y1=dis_cao/2
##Tạo các biến mới x1_change và y1_change để giữ các giá trị cập nhật của tọa độ x và y.
x1_change=0
y1_change=0
snake_block=20#Tạo khối thân rắn
snake_speed=10
body_list=[]#lưu lại phần thân rắn 
length_body_snake=1#độ dài của rắn 
score_choi=0
score_show=0
hscore=0#Điểm cao nhất
##khởi biến bg_x=o để thực hiện di chuyển background cho game
bg_x=0
running=True

#XỬ LÝ MÀN HÌNH GAME
##Tạo cửa số game và tiêu đề game
screen=pygame.display.set_mode((dis_rong,dis_cao))
pygame.display.set_caption("Game Snakes")
##Khởi tạo hàm điều chỉnh tốc độ hiển thị(điều khiển của user) của rắn  
clock = pygame.time.Clock()
##Tạo icon game
###sử dung image.load để tải icon snake.png từ file theo path
icon=pygame.image.load(r"C:\Users\DELL\OneDrive - Trường ĐH CNTT - University of Information Technology\Máy tính\python\gameran\snake.png")
pygame.display.set_icon(icon)
##Thêm background cho game
bg=pygame.image.load(r"C:\Users\DELL\OneDrive - Trường ĐH CNTT - University of Information Technology\Máy tính\python\gameran\desktop-wallpaper-snake-game-cool-green-gaming.png")
bg=pygame.transform.scale2x(bg)

#HÀM DEF
##Hàm hiển thị điểm 
def Diem(score_choi, score_show):
    font_score=pygame.font.Font("04B_19.TTF",20)
    if running:
        score_txt=font_score.render(f'_____________________________Your score: {score_choi}________________________________',True,(65,105,255))#Print score lên màn hình
        screen.blit(score_txt,(0,0))#position hiển thị
    else:
        score_txt1=font_score.render(f'Your score: {score_show}',True,(119,136,153))#Print score lên màn hình
        screen.blit(score_txt1,(350,360))#position hiển thị
        hscore_txt=font_score.render(f'High score: {hscore}',True,(119,136,153))
        screen.blit(hscore_txt,(350,390))
        note_txt=font_score.render(f'Press space to play again!!!',True,(255,0,0))
        screen.blit(note_txt,(300,300))
##Hàm check va chạm vào tường và phần đầu rắn đụng vào thân rắn 
def Check_va_cham():
    if x1>=dis_rong or x1<0 or y1>=dis_cao or y1<20 or (x1,y1)in body_list[:-1]:
        return False
    return True

   
#XỬ LÝ 
##Tạo food cho snake
foodx = round(random.randrange(0, (dis_rong - snake_block)/20.0)) * 20.0
foody = round(random.randrange(20, (dis_cao - snake_block)/20.0)) * 20.0
    
##Vòng lặp xử lý hiển thị game
###Tạo biến running để kiểm tra xem game còn chạy hay dừng rồi
running=True
while True:
    #cho biết thông tin về hành động của user từ hàm event.get() diễn ra trên màn hình 
    for event in pygame.event.get():
        #nếu người dùng click nút thoát(x) trên cửa sổ game thì dừng game 
        if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        #di chuyển 
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_UP:
                x1_change=0
                y1_change=-snake_block
            elif event.key==pygame.K_DOWN:
                x1_change=0
                y1_change=snake_block
            elif event.key==pygame.K_RIGHT:
                x1_change=snake_block
                y1_change=0
            elif event.key==pygame.K_LEFT:
                x1_change=-snake_block
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
   
    Diem(score_choi,score_show)
    if running:
        #Thực hiện di chuyển cập nhật vị trí x1 và y1
        x1+=x1_change
        y1+=y1_change
        #Thêm thân cho snake (xử lý List)
        body_list.append((x1,y1))
        #vẽ Food (hình chữ nhật)
        pygame.draw.rect(screen,(255,0,0),[foodx,foody,snake_block,snake_block])
        #Sau khi dùng for thì phần thân rắn sẽ tự động thêm vào chúng ta cần xử lý sự kiện này 
        if len(body_list)>length_body_snake:
            del body_list[0] #Nếu phần thân của rắn lớn hơn độ dài rắn thì xóa phần đầu 
        #Tạo hình dạng snake
        for x1,y1 in body_list:
            #draw.rect( , ,[x,y,dài,rộng]) rect: vẽ hình chữ nhật
            pygame.draw.rect(screen,(255,255,255),[x1,y1,snake_block,snake_block])#Đầu
        #xử lý thức ăn 
        if x1==foodx and y1==foody:
            #Thêm phần thân rắn vào list body_list
            length_body_snake+=1
            #tính điểm
            score_choi+=1
            score_show=score_choi
            if score_choi>hscore:
                hscore=score_choi
            #Random lại thức ăn 
            foodx = round(random.randrange(0, (dis_rong - snake_block)/20.0)) * 20.0
            foody = round(random.randrange(20, (dis_cao - snake_block)/20.0)) * 20.0
        running=Check_va_cham()#nếu Fasle sẽ hiển thị chơi lại 
        #Thời gian càng nhỏ thì răn di chuyển càng chậm có thể dùng để tăng độ khó của game 
        clock.tick(snake_speed)#snake_speed fps
    else:
        #reset lại game
        #khởi tạo lại
        x1=dis_rong/2
        y1=dis_cao/2
        x1_change=0
        y1_change=0
        body_list=[]
        length_body_snake=1
        score_choi=0
    #cập nhật lại thông tin màn hình 
    pygame.display.update()

    


    
            
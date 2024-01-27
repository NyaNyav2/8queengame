import pygame
import random
from itertools import permutations, combinations

pygame.init()
img = pygame.image.load('queen.png')# Load ảnh con hậu
# Thiết lập màu sắc
white = (255,255,255)
black = (0,0,0)

#Thiết lập kích thước màn hình 640 : 80 =8
height=640
width=640

gameDisplay = pygame.display.set_mode((width,height))
pygame.display.set_caption('Chess_Board                press s to checkout different solutions')



size = 80 # Kích thước cạnh ô vuông


boxlist=[]
queenlist=[]
#Biến count được sử dụng để đếm số ô trong quá trình tạo bàn cờ.
#Danh sách boxlist sẽ lưu trữ tọa độ của các ô đen cần được vẽ lên màn hình.

def reset_board():
    count =0
    for i in range(0,width,size):
        for j in range(0,height+size,size):
            boxes=[]
            if count % 2 == 1:   # Kiểm tra nếu ô hiện tại là ô đen            
                boxes.append(i)  # Lưu tọa độ x của ô đen vào danh sách boxes
                boxes.append(j)  # Lưu tọa độ y của ô đen vào danh sách boxes
                boxlist.append(boxes) # Thêm danh sách boxes vào danh sách boxlist
            count += 1
#Vòng lặp for lồng nhau để duyệt qua tất cả các ô trên màn hình với kích thước size x size
#Biến count được sử dụng để quyết định ô hiện tại là đen hay trắng. Nếu count lẻ, ô hiện tại sẽ là ô đen.
#Đối với các ô đen, tọa độ x và y của ô sẽ được lưu vào danh sách boxes và sau đó thêm vào danh sách boxlist.
    print(boxlist)
    gameDisplay.fill(white) #tô màu nền trắng cho màn hình
    for XnY in boxlist:
            pygame.draw.rect(gameDisplay,black, [XnY[0],XnY[1],size,size])
            
    pygame.display.update()
    
def solution():
    sol =[]
    count = 0 #Biến đếm số lượng lời giải tìm được
    text = 8 #Số quân hậu cần xếp
    n = int(text)
    x = range(1, n+1) #Tạo một dãy số từ 1 đến n (tức là 1 đến 8) để biểu diễn các cột trên bàn cờ.

    for permuation in permutations(range(1, n+1)):
        #Sử dụng hàm permutations() để tạo ra tất cả các hoán vị có thể có của các số từ 1 đến n. Mỗi hoán vị đại diện cho một cách sắp xếp các quân hậu theo thứ tự cột.
        y = permuation #Lưu trữ hoán vị hiện tại vào biến y
        all_permutations = list(zip(x,y)) #Nối các giá trị trong x (cột) với các giá trị trong y (hàng) để tạo thành các tọa độ (x, y) của các quân hậu.
        list_of_permutations.append(all_permutations)

    for possible_solution in list_of_permutations:
        solutions = []
        for piece1, piece2 in combinations(possible_solution, 2): # Lấy từng cặp quân hậu từ possible_solution để kiểm tra.
            solutions.append(is_diagonal(piece1, piece2)) #Gọi hàm is_diagonal() để kiểm tra xem hai quân hậu có nằm trên đường chéo hay không, và lưu kết quả vào solutions.

        if True not in solutions: # Nếu không có cặp quân hậu nào nằm trên đường chéo (tức là tất cả đều là False), thì đây là một lời giải hợp lệ.
            sol.append(possible_solution)
            count += 1
         
    
    return (sol,count)                    
      

def is_diagonal(point1, point2): #Kiểm tra xem hai điểm point1 và point2 có nằm trên cùng một đường chéo hay không
    x1 = point1[0]
    y1 = point1[1]
    x2 = point2[0]
    y2 = point2[1]
    gradient = (y2-y1)/(x2-x1) #Nếu gradient bằng 1 hoặc -1, nghĩa là hai điểm nằm trên cùng một đường chéo
    if gradient == -1 or gradient == 1:
        return(True)
    else:
        return(False)

list_of_permutations = []


def render_solution(solution_tuple): #hiển thị lời giải của bài toán tám quân hậu lên màn hình, sử dụng thư viện Pygame.
    print("=============")
    print(solution_tuple)
    for element in solution_tuple:
        x_val = (element[0]-1)*80 +5
        y_val = (element[1]-1)*80 +5
        queen=pygame.image.load('queen.png')
        gameDisplay.blit(queen,[int(x_val),int(y_val)])
                        
    pygame.display.update()
        
    

def gameloop():
    gameExit = False
    sol=[] #Danh sách trống để lưu trữ các lời giải cho bài toán tám quân hậu
    prev_key = "no_sol" #Biến lưu trữ phím trước đó được nhấn, ban đầu là "no_sol"
    
    
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                 gameExit=True
            if event.type == pygame.KEYDOWN:#nhấn phím
                if event.key == pygame.K_s:
                    if prev_key != "sol": #tránh gọi hàm solution() liên tục
                        sol,count=solution()
                    random_number=round(random.randrange(0,count))  #chọn ngẫu nhiên một lời giải từ danh sách các lời giải tìm được  
                    print(sol[random_number])
                    #update board
                    del queenlist[:]
                    reset_board()
                    render_solution(sol[random_number])
                    prev_key = "sol"
                if event.key == pygame.K_c: #Xóa các quân hậu và vòng tròn hiện có trên bàn cờ (nếu có)
                    del queenlist[:]                   
                    reset_board()
                    gameloop()        
           
reset_board()            
gameloop()
pygame.quit()
quit()

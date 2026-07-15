# Mối quan hệ đã được học trong Database : 

# 1-1 : 1 học sinh - 1 mã định danh (CCCD)
# 1-n : 1 Tùng - yêu nhiều anh 
# n-n : 1 học sinh - học nhiều khóa học <=> 1 khóa học có thể được đăng ký bởi nhiều học sinh

# Code LMS (Mua bán khóa học)

# Bảng User : id , username , phone , age 
# Bảng User_info : id , user_id (Uni) , sex , address , passport
# Bảng Project : id , project_name , user_id , technology , day , project_detail 
# Bảng Course : id , course_name , course_detail , money  , status 
# Bảng Enrollment : id , user_id , course_id

# Bảng User - User_info : 1 - 1 
# Bảng User - Project : 1 - N
# Bảng User - Enrollment : 1 - N
# Bảng Course - Enrollment : 1 - N
# Bảng User - Course : N - N

# Xây dựng Bộ API làm việc với Project 
# CRUD 

# Read : 
# API : Lấy tất cả dự án 
# API : Lấy dự án theo ID dự án
# API : Lấy dự án theo ID người dùng 

# Create : 
# API : Thêm dự án theo ID người dùng 
# API : Thêm dự án theo Role Admin 

# Update : 
# API : Cập Nhật dự án theo ID người dùng 
# API : Cập Nhật dự án theo ID dự án

# Delete : 
# API : Xóa dự án theo ID người dùng 
# API : Xóa tất cả dự án 


# Các bước xây dựng một API 
# Bước 1 : Tạo Schema
# Bước 2 : Tạo router : Bộ định tuyến , controller 
# Bước 3 : Tạo service : Xử lý logic ở tầng database 
# Bước 4 : Quay lại tầng router => Đẩy dữ liệu ra phía Client (Response)


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

# Xây dựng API dùng để quản Lý dự án cá nhân của User 

# CRUD 
# Read : 
# lấy toàn bộ dự án , phân trang 
# lấy dự án theo ID người dùng 

# Create : 
# Tạo dự án theo ID người dùng 
# Tạo dự án băng role admin 

# Update : (PUT và Patch)
# Cập nhật dự án theo ID người dùng 
# Cập Nhật dự án băng role admin 

# Delete : 
# Xóa dự án theo ID người dùng , và phải truyền thêm ID dự án
# Xóa toàn bộ dự án của người dùng muốn xóa 


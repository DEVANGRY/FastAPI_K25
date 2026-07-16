-- ============================================================
--  SAMPLE DATA cho database: crm_lms
--  Thứ tự INSERT phải đúng theo quan hệ FK:
--  1. user  →  2. user_info  →  3. course  →  4. project  →  5. enrollment
-- ============================================================

USE crm_lms;

-- ============================================================
-- 1. Bảng USER
-- ============================================================
INSERT INTO user (username, phone, age) VALUES
('Nguyen Van An',   '0901234561', 22),
('Tran Thi Bich',   '0901234562', 25),
('Le Hoang Nam',    '0901234563', 28),
('Pham Minh Tuan',  '0901234564', 30),
('Hoang Thi Lan',   '0901234565', 23);

-- ============================================================
-- 2. Bảng USER_INFO  (user_id: 1-1 với user)
--    sex      : 'male' | 'female'
--    address  : max 12 ký tự (theo model)
--    passport : max 12 ký tự
-- ============================================================
INSERT INTO user_info (user_id, sex, address, passport) VALUES
(1, 'male',   'Ha Noi',    'P001234561'),
(2, 'female', 'HCM',       'P001234562'),
(3, 'male',   'Da Nang',   'P001234563'),
(4, 'male',   'Can Tho',   'P001234564'),
(5, 'female', 'Hue',       'P001234565');

-- ============================================================
-- 3. Bảng COURSE
--    status default = 'OPEN'
-- ============================================================
INSERT INTO course (course_name, course_detail, money, status) VALUES
('Python Cơ Bản',      'Nhập môn',   1500000, 'OPEN'),
('FastAPI Backend',    'Web API',    2500000, 'OPEN'),
('React Frontend',     'UI Dev',     2000000, 'OPEN'),
('Machine Learning',   'AI & ML',    3500000, 'OPEN'),
('Docker & DevOps',    'Container',  2800000, 'CLOSED');

-- ============================================================
-- 4. Bảng PROJECT  (1 user có thể có nhiều project)
-- ============================================================
INSERT INTO project (project_name, technology, day, project_detail, user_id) VALUES
('Quản lý sinh viên',   'Python',    30, 'Ứng dụng quản lý sinh viên dùng FastAPI và MySQL',    1),
('E-commerce Web',      'React',     45, 'Website bán hàng online với giỏ hàng và thanh toán',  2),
('Chatbot hỗ trợ',      'Python',    20, 'Bot tự động trả lời câu hỏi khách hàng qua Telegram', 3),
('Dashboard phân tích', 'React',     60, 'Bảng điều khiển hiển thị biểu đồ dữ liệu kinh doanh',4),
('API quản lý kho',     'FastAPI',   35, 'RESTful API quản lý tồn kho và xuất nhập hàng hóa',  5),
('Blog cá nhân',        'Python',    15, 'Website blog với chức năng viết bài và bình luận',    1),
('App đặt lịch',        'React',     25, 'Ứng dụng đặt lịch hẹn cho phòng khám',               2);

-- ============================================================
-- 5. Bảng ENROLLMENT  (N-N giữa user và course)
-- ============================================================
INSERT INTO enrollment (user_id, course_id) VALUES
-- Nguyen Van An  học Python, FastAPI, Docker
(1, 1),
(1, 2),
(1, 5),
-- Tran Thi Bich học Python, React
(2, 1),
(2, 3),
-- Le Hoang Nam  học FastAPI, Machine Learning
(3, 2),
(3, 4),
-- Pham Minh Tuan học tất cả
(4, 1),
(4, 2),
(4, 3),
(4, 4),
(4, 5),
-- Hoang Thi Lan học React, Machine Learning
(5, 3),
(5, 4);
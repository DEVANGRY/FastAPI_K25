
-- 1. TẠO DATABASE VÀ SỬ DỤNG
CREATE DATABASE IF NOT EXISTS crm_foodball;
USE crm_foodball;

INSERT INTO role (role_name) 
VALUES 
    ('Admin'),
    ('Manager'),
    ('User');

INSERT INTO `user` (username, password, role_id) 
VALUES 
    ('admin_vip', 'hashed_password_1', 1),  
    ('manager_01', 'hashed_password_2', 2), 
    ('user_john', 'hashed_password_3', 3),  
    ('user_anna', 'hashed_password_4', 3),   
    ('user_peter', 'hashed_password_5', 3);  
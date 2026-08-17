CREATE DATABASE crm_lms_v2;
INSERT INTO `crm_lms_v2`.`role`(`role_name`,`det`)
VALUES
( "Admin" , "Role có mọi quyền"),
( "User" , "Role của người dùng");

INSERT INTO `crm_lms_v2`.`user`(`username`,`password`,`is_activate`,`role_id`)
VALUES
("tuanlq","askfjasfjhasf",true,1);

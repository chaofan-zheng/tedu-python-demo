--级联动作示例
alter table person add foreign key (dept_id) references dept(id)
on delete cascade on update cascade;

alter table person add foreign key (dept_id) references dept(id)
on delete set null on update set null;


--练习1： 根据所学关系模型完成用户朋友圈
--数据表的创建
用户表
create table user(
id int primary key auto_increment,
name varchar(30),
passwd char(64)
);

朋友圈
create table pyq(
id int primary key auto_increment,
image blob,
content text,
time datetime,
address varchar(256),
user_id int,
foreign key (user_id) references user(id)
);

点赞评论 (多对多关系)
create table user_pyq(
id int primary key auto_increment,
u_id int,
p_id int,
`like` bit default 0,
`comment` text default null,
foreign key (u_id) references user(id),
foreign key (p_id) references pyq(id)
);



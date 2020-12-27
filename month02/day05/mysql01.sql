--创建数据表
create table class (
id int primary key auto_increment,
name varchar(30) not null,
age tinyint unsigned,
sex enum('m','w','o'),
score float default 0
);

create table hobby (
id int primary key auto_increment,
name varchar(30) not null,
hobby set("sing","dance","draw") comment "选择兴趣爱好",
level char,
price decimal(7,2),
remark text
);


--插入hobby表数据
insert into hobby
(name,hobby,level,price,remark)
values
("Lily","sing,dance","A",43800.888,"练舞奇才"),
("Joy","draw","B",8800,"当代达芬奇"),
("Emma","sing","C",24600,"天籁之音");

insert into hobby
(name,hobby,level,price)
values
("Jame","draw,dance","B",18000),
("Tom","sing","C",20000);


--练习1：
--创建一个数据库： books
create database books charset=utf8;
use books;

--在该数据库中创建一个数据表  book
--字段: id 书名  作者  出版社  价格  备注
create table book (
id int primary key auto_increment,
bname varchar(50) not null,
author varchar(30) not null,
press varchar(50),
price float,
comment text
);


--在该表中插入若干数据记录 >= 8
--参考：
--作者 ： 老舍  沈从文  鲁迅  冰心
--出版社： 中国文学  人民教育  机械工业
--价格： 30 -- 120

insert into book (bname,author,press,price,comment)
values
("边城","沈从文","机械工业出版社",36,"小城故事多"),
("骆驼祥子","老舍","机械工业出版社",43,"你是祥子么？"),
("茶馆","老舍","中国文学出版社",55,"老北京"),
("呐喊","鲁迅","人民教育出版社",71,"最后的声音"),
("朝花夕拾","鲁迅","中国文学出版社",53,"好时光"),
("围城","钱钟书","中国文学出版社",44,"你心中的围城是什么");

insert into book (bname,author,press,price)
values
("林家铺子","茅盾","机械工业出版社",51),
("巨人传","忘了","人名教育出版社",47);






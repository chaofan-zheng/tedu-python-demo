--将book表拆分为三个表
--书籍   作家   出版社
--自行定义字段和表关系，画出E-R图
--完成表的创建
create table 作家(
id int primary key auto_increment,
name varchar(30),
sex char,
remark text
);

create table 出版社(
id int primary key auto_increment,
pname varchar(30),
address varchar(512),
tel char(16)
);

create table 图书(
id int primary key auto_increment,
bname varchar(30),
price float,
aid int,
pid int,
foreign key(aid) references 作家(id),
foreign key(pid) references 出版社(id)
);

create table author_press(
id int primary key auto_increment,
签约时间 datetime,
a_id int,
p_id int,
foreign key(a_id) references 作家(id),
foreign key(p_id) references 出版社(id)
);

综合查询
1. 查询每位老师教授的课程数量
select tname,count(cname) as 教课数量 from
teacher left join course
on teacher.tid = course.teacher_id
group by tname;

2. 查询学生的信息及学生所在班级信息
select sid,sname,gender,caption from
student left join class
on class.cid = student.class_id;

3. 查询各科成绩最高和最低的分数,
形式 : 课程ID  课程名称 最高分  最低分
select cid as 课程ID,cname as 课程名称,
max(number) as 最高分,min(number) as 最低分
from
course left join score
on course.cid = score.course_id
group by cid,cname;

4. 查询平均成绩大于85分的所有学生学号,姓名和平均成绩
select stu.sid,sname,avg(number) from
student as stu left join score
on stu.sid = score.student_id
group by stu.sid,sname
having avg(number) > 85;

5. 查询课程编号为2且课程成绩在80以上的学生学号和姓名
select stu.sid,stu.sname from
student as stu left join score
on stu.sid = score.student_id
where course_id=2 and number>80;

6. 查询各个课程及相应的选修人数
select cname,count(course_id) from
course left join score
on course.cid = score.course_id
group by cname;

7. 查询每位学生姓名 所在班级和平均成绩
select sname,caption,avg(number) from
student left join class
on class.cid = student.class_id
left join score
on student.sid = score.student_id
group by sname,caption;


函数和存储过程

--简单函数
注意： 返回值必须是一个值，函数名不能重复
create function st1() returns int
begin
    update cls set score=99 where id=1;
    delete from cls where sex is null;
    return (select score from cls where id=1);
end $$

--局部变量
create function st2() returns int
begin
    declare a int;
    declare b int;
    set a=(select score from cls order by score limit 1);
    select score from cls order by score desc limit 1 into b;
    return a+b;
end $$

--形参
create function st3(uid int)
returns varchar(30)
begin
    return (select name from cls where id=uid);
end $$

--练习1： 编写一个函数，传入两个学生的ID
--返回这两个学生的分数之差
create function score_diff(uid1 int,uid2 int)
returns int
begin
    declare val1 int;
    declare val2 int;
    set val1=(select score from cls where id=uid1);
    set val2=(select score from cls where id=uid2);
    return val1-val2;
end $$


--存储过程
create procedure st()
begin
    select name,age from cls;
    select name,score from cls order by score desc;
end $$
delimiter ;

create procedure p_inout(INOUT num int )
begin
    select num;
    set num=100;
    select num;
end $$

set @a=1;

练习2 ： 编写一个存储过程，传入一个而学生
姓名，打印出这个学生的信息，并且 在爱好表中
加入这个学生，喜欢画画
create procedure like_draw(in uname varchar(30))
begin
  select * from cls where name=uname;
  insert into hobby (name,hobby,price) values (uname,"draw",18000);
end $$










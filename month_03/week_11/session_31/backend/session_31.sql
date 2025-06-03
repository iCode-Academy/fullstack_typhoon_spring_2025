-- session 31

create table student(
	student_id serial primary key, 
	first_name varchar(255),
	last_name varchar(255),
	birth_date DATE
);

-- alter table
-- student number
-- major

alter table student 
add student_number varchar(25);

select * from student;

alter table student 
add major varchar(125);

-- drop 
alter table student
add not_required integer;

alter table student 
drop column not_required;

create table dummy_table (
	id serial primary key,
	dummy_name varchar(255)
);

drop table dummy_table;

-- rename
select * from student;

alter table student
rename column student_number to student_nr;

/*
 * Multi line 
 * comment
 * 
 */

-- truncate - delete data from database table

insert into student (first_name, last_name, birth_date, student_nr, major)
values ('khangaikhuu', 'uvgunkhuu', '1992-04-09', 'MR123456', 'Computer Science');

select * from student;

truncate table student;

drop table student;

-- Foreign Key constraint

create table courses (
	course_id serial primary key,
	course_name varchar(255),
	course_duration integer
);

create table course_type (
	course_type_id serial primary key,
	course_type_name varchar(255)
);

-- data insert into course
insert into courses (course_name, course_duration)
values 
('Fullstack Course', 6),
('Web Course', 3),
('Flutter Mobile App Course', 3),
('Ui Ux Course', 3);

select * from courses;

insert into course_type (course_type_name)
values
('Computer Science'),
('Design');

select * from course_type;


alter table courses 
add column course_type varchar(255);

update courses 
set course_type = 'Computer Science'
where course_id = 1;

update courses 
set course_type = 'Computer Science'
where course_id = 2;

update courses 
set course_type = 'Computer science'
where course_id = 3;

update courses 
set course_type = 'Design'
where course_id = 4;


-- drop column course_type
alter table courses
drop column course_type;


-- alter table type integer
alter table courses 
add column course_type integer;

select * from courses;

-- create foreign key constraint
alter table courses 
add foreign key(course_type)
references course_type(course_type_id);


update courses 
set course_type = 1
where course_id = 2;


update courses 
set course_type = 1
where course_id = 1;

update courses 
set course_type = 1
where course_id = 3;

update courses 
set course_type = 2
where course_id = 4;

-- this is not good
-- update courses 
-- set course_type = 3
--set course_type = 
-- where course_id = 2;


select * from course_type ct ;





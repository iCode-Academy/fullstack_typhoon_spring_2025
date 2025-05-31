-- CREATE table students
-- database create table query

create table students (
	first_name VARCHAR(255),
	last_name VARCHAR(255),
	birth_date DATE,
	email VARCHAR(255),
	course_name VARCHAR(255),
	grade INTEGER
);

-- insert single data
insert into STUDENTS (first_name, last_name, birth_date, email, course_name, grade)
values('Berkh-Ochir', 'Ochirbat', '2000-01-01', 'berkhee@gmail.com', 'fullstack course', 70);

-- insert multiple data
insert into STUDENTS (first_name, last_name, birth_date, email, course_name, grade)
values
('Oyunbold', 'Naranjargal', '2001-01-01', 'oyunbold@gmail.com', 'fullstack course', 90),
('Buyanaa', 'Boldbaatar', '2002-01-01', 'buyanaa@gmail.com', 'fullstack course', 80);

-- SELECT table students query
select * from students;

-- WHERE clause 
select * from students where first_name = 'Buyanaa';

-- first_name-ийг нь сонгох
select first_name from students where first_name = 'Buyandelger';

-- first_name, last_name нь сонгох
select first_name, last_name from students where first_name = 'Buyanaa';

-- UPDATE table students query
update students set first_name = 'Buyandelger' where first_name = 'Buyanaa';


-- insert new student
insert into students (first_name, last_name, birth_date , email, course_name, grade)
values 
('Balt', 'Batzaya', '1999-01-01', 'balt@gmail.com', 'fullstack course', 60);

-- DELETE table students query

delete from students where first_name = 'Balt';


--  ID 
create table courses (
	course_id INTEGER,
	course_name VARCHAR(255)
);

select * from courses;


-- add data

insert into courses (course_id, course_name)
values 
(1, 'fullstack course'),
(2, 'flutter mobile course'),
(3, 'web front end course'),
(4, 'ui ux course');


insert into courses (course_id, course_name)
values 
(5, 'Kids mobile course');

-- автоматаар утгаа нэмдэг төрөлтэй багана

create table teachers (
	teacher_id SERIAL,
	teacher_name VARCHAR(255),
	teacher_course VARCHAR(255)
);


insert into teachers (teacher_name, teacher_course)
values 
('Enkhjin', 'Kids Web App'),
('Khangaikhuu', 'Fullstack Web'),
('Khongorzul', 'Web Front End'),
('Dairiima', 'Mobile App');


select * from teachers;

insert into teachers (teacher_id, teacher_name, teacher_course)
values 
(1, 'Khangaikhuu', 'Flutter Mobile App ');

-- unique ID - primary key

create table classes (
	class_id SERIAL primary key,
	class_name VARCHAR(255),
	class_duration INT
);



insert into classes (class_name , class_duration)
values
('Fullstack Web Course', 6),
('Web Front End', 3),
('Flutter Mobile', 3),
('Ui/UX', 3);


select * from classes;

--insert into classes(class_id, class_name, class_duration )
--values 
--(4, 'Kids Mobile', 2); Энэ хэсэг болохгүй яагаад гэвэл 4 гэдэг id буюу тоо баганад байгаа.

insert into classes(class_id, class_name, class_duration )
values 
(5, 'Kids Mobile', 2);


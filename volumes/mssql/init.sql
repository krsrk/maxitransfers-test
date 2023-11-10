IF NOT EXISTS(SELECT * FROM sys.databases WHERE name = 'admin')
    BEGIN
        CREATE DATABASE admin;
    END;
GO

USE admin;
GO

DROP TABLE IF EXISTS dbo.employee;
GO

create table dbo.employee
(
    id              int identity
        primary key,
    name            varchar(250) not null,
    last_name       varchar(550) not null,
    birth_date      date         not null,
    employee_number varchar(max) not null,
    curp            varchar(max) not null,
    ssn             varchar(max) not null,
    phone_number    varchar(10)  not null,
    nationality     varchar(max)
)
go

DROP TABLE IF EXISTS dbo.beneficiary;
GO

create table dbo.beneficiary
(
    id                       int identity
        primary key,
    name                     varchar(250) not null,
    last_name                varchar(550) not null,
    birth_date               date         not null,
    curp                     varchar(max) not null,
    ssn                      varchar(max) not null,
    phone_number             varchar(10)  not null,
    nationality              varchar(max),
    participation_percentage int,
    employee_id              int          not null
        constraint fk_beneficiary_employee
            references employee
            on delete cascade
)
go

DROP PROCEDURE IF EXISTS dbo.sp_create_employee;
GO

CREATE PROCEDURE dbo.sp_create_employee
    @name VARCHAR(250),
    @last_name VARCHAR(550),
    @birth_date DATE,
    @employee_number VARCHAR(100),
    @curp VARCHAR(30),
    @ssn VARCHAR(30),
    @phone_number VARCHAR(20),
    @nationality VARCHAR(180)
AS
BEGIN
    INSERT INTO employee (name, last_name, birth_date, employee_number, curp, ssn, phone_number, nationality)
    values (@name, @last_name, @birth_date, @employee_number, @curp, @ssn, @phone_number, @nationality)
    RETURN 0
END;

go

DROP PROCEDURE IF EXISTS dbo.sp_update_employee;
GO


CREATE PROCEDURE dbo.sp_update_employee
    @employee_id int,
    @name varchar (250),
    @last_name varchar(550),
    @birth_date DATE,
    @employee_number varchar(100),
    @curp varchar(30),
    @ssn varchar(30),
    @phone_number varchar(20),
    @nationality varchar(180)
AS
BEGIN
    UPDATE employee SET name=@name, last_name=@last_name, birth_date=@birth_date, employee_number=@employee_number, curp=@curp, ssn=@ssn, phone_number=@phone_number, nationality=@nationality
    WHERE id = @employee_id
    RETURN 0
END;

go

DROP PROCEDURE IF EXISTS dbo.sp_delete_employee;
GO


CREATE PROCEDURE dbo.sp_delete_employee(@employee_id int) AS
BEGIN
    DELETE FROM employee
    WHERE id = @employee_id
    RETURN 0
END;

go

DROP PROCEDURE IF EXISTS dbo.sp_create_beneficiary;
GO


CREATE PROCEDURE dbo.sp_create_beneficiary
    @name varchar (250),
    @last_name varchar(550),
    @birth_date DATE,
    @curp varchar(30),
    @ssn varchar(30),
    @phone_number varchar(20),
    @nationality varchar(180),
    @participation_percentage int,
    @employee_id int
AS
BEGIN
    INSERT INTO beneficiary (name, last_name, birth_date, curp, ssn, phone_number, nationality, participation_percentage, employee_id) values (@name, @last_name, @birth_date, @curp, @ssn, @phone_number, @nationality, @participation_percentage, @employee_id)
    RETURN 0
END;

go

DROP PROCEDURE IF EXISTS dbo.sp_update_beneficiary;
GO


CREATE PROCEDURE dbo.sp_update_beneficiary
    @beneficiary_id int,
    @name varchar (250),
    @last_name varchar(550),
    @birth_date varchar(50),
    @curp varchar(30),
    @ssn varchar(30),
    @phone_number varchar(20),
    @nationality varchar(180),
    @participation_percentage int
AS
BEGIN
    UPDATE beneficiary SET name=@name, last_name=@last_name, birth_date=@birth_date, curp=@curp, ssn=@ssn, phone_number=@phone_number, nationality=@nationality, participation_percentage=@participation_percentage
    WHERE id = @beneficiary_id
    RETURN 0
END;
go

DROP PROCEDURE IF EXISTS dbo.sp_delete_beneficiary;
GO



CREATE PROCEDURE dbo.sp_delete_beneficiary(@beneficiary_id int) AS
BEGIN
    DELETE FROM beneficiary
    WHERE id = @beneficiary_id
    RETURN 0
END;

go

INSERT INTO dbo.employee (name, last_name, birth_date, employee_number, curp, ssn, phone_number, nationality) VALUES (N'Monkey', N'D. Luffy', N'1991-11-02', N'001', N'DLUM911102HASCPH14', N'51048001140', N'4491878584', N'Mexicana');
INSERT INTO dbo.employee (name, last_name, birth_date, employee_number, curp, ssn, phone_number, nationality) VALUES (N'Zoro', N'Roronoa', N'1991-11-10', N'002', N'RORZ911102HASCPH15', N'51048001141', N'4491878685', N'Mexicana');
INSERT INTO dbo.employee (name, last_name, birth_date, employee_number, curp, ssn, phone_number, nationality) VALUES (N'Usopp', N'SogeKing', N'1991-11-02', N'003', N'SOGU911102HASCPH16', N'51048001142', N'4491878786', N'Mexicana');

INSERT INTO dbo.beneficiary (name, last_name, birth_date, curp, ssn, phone_number, nationality, participation_percentage, employee_id) VALUES (N'Beneficiario 1', N'X', N'1991-12-01', N'DLUM911102HASCPH14', N'51048001140', N'4491878584', N'Mexicana', 10, 1);
INSERT INTO dbo.beneficiary (name, last_name, birth_date, curp, ssn, phone_number, nationality, participation_percentage, employee_id) VALUES (N'Beneficiario 2', N'X', N'1991-12-01', N'DLUM911102HASCPH14', N'51048001140', N'4491878584', N'Mexicana', 20, 1);
INSERT INTO dbo.beneficiary (name, last_name, birth_date, curp, ssn, phone_number, nationality, participation_percentage, employee_id) VALUES (N'Beneficiario 3', N'X', N'1991-12-01', N'DLUM911102HASCPH14', N'51048001140', N'4491878584', N'Mexicana', 10, 2);
INSERT INTO dbo.beneficiary (name, last_name, birth_date, curp, ssn, phone_number, nationality, participation_percentage, employee_id) VALUES (N'Beneficiario 4', N'X', N'1991-12-01', N'DLUM911102HASCPH14', N'51048001140', N'4491878584', N'Mexicana', 30, 2);
INSERT INTO dbo.beneficiary (name, last_name, birth_date, curp, ssn, phone_number, nationality, participation_percentage, employee_id) VALUES (N'Beneficiario 5', N'X', N'1991-12-01', N'DLUM911102HASCPH14', N'51048001140', N'4491878584', N'Mexicana', 10, 3);
INSERT INTO dbo.beneficiary (name, last_name, birth_date, curp, ssn, phone_number, nationality, participation_percentage, employee_id) VALUES (N'Beneficiario 6', N'X', N'1991-12-01', N'DLUM911102HASCPH14', N'51048001140', N'4491878584', N'Mexicana', 40, 3);

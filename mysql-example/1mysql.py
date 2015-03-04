#github
import pymysql as MySQLdb
#Подключение к СУБД
db = MySQLdb.connect( host = "127.0.0.1", user = "root", passwd = "rootpass", charset = 'utf8' )
cursor = db.cursor()
#Создание БД "Victor"
sql = "CREATE DATABASE IF NOT EXISTS Victor"
cursor.execute(sql)
db.commit()
#Подключение к созданой БД
db = MySQLdb.connect( host = "127.0.0.1", user = "root", passwd = "rootpass", db = "victor", charset = 'utf8' )
cursor = db.cursor()
#Создание таблицы Персонал : идентификатор - число длиною 5, ФИО - строка длиной не более 50, пол - перечисление, день рождения - дата, необязательный параметр, первичный ключ - идентификатор
sql = """CREATE TABLE personal (
id INT(5) AUTO_INCREMENT,
fio VARCHAR(50) CHARACTER SET utf8 COLLATE utf8_bin,
sex ENUM('male','female'),
b_day DATE NULL,
PRIMARY KEY (id));"""
cursor.execute(sql)
#Заполнение созданной таблицы
sql = """INSERT INTO personal (fio, sex, b_day) VALUES
('Иванов Иван Иванович', 'male', '1990-10-21'),
('Иванов Петр Сергеевич', 'male', '1987-08-12'),
('Смирнова Ирина Викторовна', 'female', '1988-05-14'),
('Плесовских Олег Дмитриевич', 'male', '1994-08-15'),
('Волынкина Мария Олеговна', 'female', '1990-11-12');"""
cursor.execute(sql)
#создание таблицы Фирмы : идентификатор - число длиною 5, название организации - строка длиною не более 40 символов, первичный ключ - идентификатор
sql = """CREATE TABLE firms (
id INT(5) AUTO_INCREMENT,
name VARCHAR(40),
PRIMARY KEY (id));"""
cursor.execute(sql)
#Заполнение
sql = """INSERT INTO firms (name) VALUES
('firmasoft'),
('microsoft'),
('goodfirm');"""
cursor.execute(sql)
# Создание таблицы большая таблиа, для связи таблиц персонала и фирм : идентификатор - число длиной 5, должность - строка длиною не более 30 символов и дефолтным значением "какая-то должность", идентификатор работника - число, вторичный ключ, вторичный ключ - идентификатор работника связанный с полем идентификатор из таблицы персонал
sql = """CREATE TABLE bigtable (
id INT (5) AUTO_INCREMENT,
post VARCHAR(30) DEFAULT('какая-то должность'),
id_firm INT(5),
id_personal INT(5),
PRIMARY KEY (id),
FOREIGN KEY (id_personal) REFERENCES personal(id)),
FOREIGN KEY (id_firm) REFERENCES firm (id));"""
cursor.execute(sql)
#Заполнение
sql = """INSERT INTO bigtable (post, id_firm, id_personal) VALUES
('', 1, 1),
('manager', 1, 2),
('director', 2, 3),
('security', 3, 4),
('admin', 2, 3);"""
db.commit()

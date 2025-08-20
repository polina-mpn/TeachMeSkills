-- 📘 TeachMeSkills: Домашнее задание по SQL
-- Тема: Создание таблиц, связи и JOIN
--
-- 📌 Примеры:
-- Создать таблицу:
-- CREATE TABLE example (
--     id INT PRIMARY KEY,
--     name VARCHAR(255)
-- );
--
-- Вставить данные:
-- INSERT INTO example (id, name) VALUES (1, 'Пример');
--
-- Пример INNER JOIN:
-- SELECT a.id, b.name FROM table_a a
-- INNER JOIN table_b b ON a.id = b.a_id;
--
-- Пример агрегатной функции:
-- SELECT author_id, SUM(quantity) FROM sales
-- JOIN books ON sales.book_id = books.id
-- GROUP BY author_id;
--
-- 💡 Вопросы для самоконтроля:
-- 1. Чем отличается INNER JOIN от LEFT JOIN?
-- INNER JOIN - возвращает только те строки, которые есть и в первой, и во второй таблице.
-- LEFT JOIN - возвращает все строки из левой таблицы, даже если для них нет соответствующих записей в правой таблице.
-- Тогда поля из правой таблицы будут заполнены значениями NULL.
-- 2. Почему внешний ключ важен для целостности данных?
-- Потому что он гарантирует, что данные, которые связаны между таблицами, всегда соответсвуют друг другу. Также помогает
-- избежать ошибок.
-- 3. Для чего нужен GROUP BY?
-- GROUP BY — группирует строки с одинаковыми значениями в указанных столбцах, чтобы к этим группам можно было применить
-- агрегатные функции. Нужен, чтобы получить обобщённую информацию по группам данных.

-- 📋 Задача 1: Создание и заполнение таблиц
-- TODO: Создайте таблицу authors с полями id, first_name, last_name
--       (используйте PRIMARY KEY для поля id)
CREATE TABLE authors (
    id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50)
);

-- TODO: Создайте таблицу books с полями id, title, author_id, publication_year
--       (PRIMARY KEY — id, FOREIGN KEY — author_id, ссылается на authors)
CREATE TABLE books (
    id INT PRIMARY KEY,
    title VARCHAR(150),
    author_id INT,
    publication_year INT,
    FOREIGN KEY (author_id) REFERENCES authors(id)
);

-- TODO: Создайте таблицу sales с полями id, book_id, quantity
--       (PRIMARY KEY — id, FOREIGN KEY — book_id, ссылается на books)
CREATE TABLE sales (
    id INT PRIMARY KEY,
    book_id INT,
    quantity INT,
    FOREIGN KEY (book_id) REFERENCES books(id)
);

-- TODO: Добавьте нескольких авторов в таблицу authors
--       (INSERT INTO authors ...)
INSERT INTO authors (id, first_name, last_name) VALUES
(1, 'William', 'Shakespeare'),
(2, 'Jane', 'Austen'),
(3, 'Charles', 'Dickens'),
(4, 'Agatha ', 'Christie');

-- TODO: Добавьте несколько книг в таблицу books, указывая авторов из authors
INSERT INTO books (id, title, author_id, publication_year) VALUES
(1, 'Hamlet', 1, 1599),
(2, 'Great Expectations', 3, 1860),
(3, 'Pride and Prejudice', 2, 1813);

-- TODO: Добавьте записи о продажах книг в таблицу sales
INSERT INTO sales (id, book_id, quantity) VALUES
(1, 3, 2700000),
(2, 1, 1850000),
(3, 2, 1700);

-- 📋 Задача 2: Использование JOIN
-- TODO: Используйте INNER JOIN, чтобы получить список всех книг и их авторов
-- 💡 Пример:
-- SELECT books.title, authors.first_name, authors.last_name
-- FROM books
-- INNER JOIN authors ON books.author_id = authors.id;
SELECT books.title, authors.first_name, authors.last_name
FROM books
INNER JOIN authors ON books.author_id = authors.id;

-- TODO: Используйте LEFT JOIN, чтобы получить список всех авторов и их книг
--       (включая авторов без книг)
-- 💡 Пример:
-- SELECT authors.first_name, authors.last_name, books.title
-- FROM authors
-- LEFT JOIN books ON books.author_id = authors.id;
SELECT authors.first_name, authors.last_name, books.title
FROM authors
LEFT JOIN books ON books.author_id = authors.id;


-- TODO: Используйте RIGHT JOIN, чтобы получить список всех книг и их авторов
--       (включая книги без автора)
-- 💡 Пример:
-- SELECT books.title, authors.first_name, authors.last_name
-- FROM books
-- RIGHT JOIN authors ON books.author_id = authors.id;
SELECT books.title, authors.first_name, authors.last_name
FROM authors
RIGHT JOIN books ON books.author_id = authors.id;

-- 📋 Задача 3: Множественные JOIN
-- TODO: Используйте INNER JOIN, чтобы связать authors, books и sales и получить
--       список всех книг, их авторов и продаж
-- 💡 Пример:
-- SELECT authors.first_name, authors.last_name, books.title, sales.quantity
-- FROM sales
-- INNER JOIN books ON sales.book_id = books.id
-- INNER JOIN authors ON books.author_id = authors.id;
SELECT authors.first_name, authors.last_name, books.title, sales.quantity
FROM sales
INNER JOIN books ON sales.book_id = books.id
INNER JOIN authors ON books.author_id = authors.id;

-- TODO: Используйте LEFT JOIN, чтобы связать authors, books и sales и получить
--       список всех авторов, их книг и продаж (включая авторов без книг и книги без продаж)
-- 💡 Пример:
-- SELECT authors.first_name, authors.last_name, books.title, sales.quantity
-- FROM authors
-- LEFT JOIN books ON books.author_id = authors.id
-- LEFT JOIN sales ON sales.book_id = books.id;
SELECT authors.first_name, authors.last_name, books.title, sales.quantity
FROM authors
LEFT JOIN books ON books.author_id = authors.id
LEFT JOIN sales ON sales.book_id = books.id;

-- 📋 Задача 4: Агрегация данных с использованием JOIN
-- TODO: Используйте INNER JOIN и агрегатные функции, чтобы определить общее
--       количество проданных книг каждого автора
-- 💡 Пример:
-- SELECT authors.first_name, authors.last_name, SUM(sales.quantity) AS total_sales
-- FROM sales
-- INNER JOIN books ON sales.book_id = books.id
-- INNER JOIN authors ON books.author_id = authors.id
-- GROUP BY authors.id;
SELECT authors.first_name, authors.last_name, SUM(sales.quantity) AS total_sales
FROM sales
INNER JOIN books ON sales.book_id = books.id
INNER JOIN authors ON books.author_id = authors.id
GROUP BY authors.first_name, authors.last_name;
-- TODO: Используйте LEFT JOIN и агрегатные функции, чтобы определить общее
--       количество проданных книг каждого автора, включая авторов без продаж
-- 💡 Пример:
-- SELECT authors.first_name, authors.last_name, COALESCE(SUM(sales.quantity),0) AS total_sales
-- FROM authors
-- LEFT JOIN books ON books.author_id = authors.id
-- LEFT JOIN sales ON sales.book_id = books.id
-- GROUP BY authors.id;
SELECT authors.first_name, authors.last_name, COALESCE(SUM(sales.quantity), 0) AS total_sales
FROM authors
LEFT JOIN books ON books.author_id = authors.id
LEFT JOIN sales ON sales.book_id = books.id
GROUP BY authors.first_name, authors.last_name;
-- 🚀 Удачи! Не бойтесь пробовать разные JOIN и GROUP BY, чтобы лучше понять, как они работают!
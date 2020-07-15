-- Получить список с информацией обо всех сотрудниках.
-- select * from Employees

-- Получить список всех сотрудников с именем 'David'
-- SELECT * FROM Employees
-- WHERE name = 'David'

-- Получить список всех сотрудников с job_id равным 'IT_PROG'
-- SELECT * FROM Employees
-- WHERE job_id = 'IT_PROG'

-- Получить список всех сотрудников из 50го отдела (department_id)
-- SELECT * FROM Employees
-- WHERE department_id = 50 AND salary>=4000

-- Получить список всех сотрудников из
-- 20го и из 30го отдела (department_id)
-- SELECT * FROM Employees
-- WHERE department_id IN (20,30)

-- Получить список всех сотрудников у которых последняя буква
-- в имени равна 'a'
-- SELECT * FROM Employees
-- WHERE name LIKE '%a'

-- Получить список всех сотрудников из 50го и из 80го отдела
-- (department_id) у которых есть бонус
-- (значение в колонке commission_pct не пустое)
-- SELECT * FROM Employees
-- WHERE department_id IN (50,80) AND commission_pct NOT NULL

-- Получить список всех сотрудников у которых в имени содержатся
-- минимум 2 буквы 'n'
-- SELECT * FROM Employees
-- WHERE name LIKE '%nn%'

-- Получить список всех сотрудников у которых длина
-- имени больше 4 букв.
-- SELECT * FROM Employees
-- WHERE length(name)>4

-- Получить список всех сотрудников у которых
-- зарплата находится в промежутке от 8000 до 9000 (включительно).
-- SELECT * FROM Employees
-- WHERE salary BETWEEN 8000 AND 9000

-- Получить список всех сотрудников у которых
-- в имени содержится символ '%'
-- SELECT * FROM Employees
-- WHERE name LIKE '%\%%' ESCAPE '\'
-- SELECT id FROM Employees
-- WHERE job_id='MANAGEMENT'

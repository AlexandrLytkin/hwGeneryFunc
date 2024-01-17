Цель задания:

Научиться создавать функции динамически в зависимости от заданных условий и параметров, используя различные подходы, такие как фабрики функций, лямбда-функции и вызываемые объекты.
Теоретический комментарий:

1. Динамическое определение функций (def):
В Python можно определять функции внутри других функций. Такие функции могут создаваться и возвращаться. Это основа для создания "фабрик функций" - функций, создающих функции.

2. Лямбда-функции:
Лямбда-функции в Python — это анонимные функции, определённые одной строкой. Они удобны для создания простых функций на лету, особенно когда функция нужна временно или для одноразового использования.

3. Вызываемые объекты (__call__):
В Python у класса может быть метод __call__, что позволяет его экземплярам вести себя как функции. Это дает возможность создавать объекты, которые могут быть вызваны как функции и хранить состояние между вызовами.
Задание:

Задача 1: Фабрика Функций
Написать функцию, которая возвращает различные математические функции (например, деление, умножение) в зависимости от переданных аргументов.

Задача 2: Лямбда-Функции
Использовать лямбда-функцию для реализации простой операции и написать такую же функцию с использованием def. Например, возведение числа в квадрат

Задача 3: Вызываемые Объекты
Создать класс с Rect c полями a, b которые задаются в __init__ и методом __call__, который возвращает площадь прямоугольника, то есть a*b.
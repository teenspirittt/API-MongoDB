db = db.getSiblingDB('mydatabase');

db.createCollection('tasks');

db.tasks.insertMany([
  {
    "_id": "1",
    "title": "Рекурсия",
    "description": "Задача проведения границы на карте («создание военных блоков»). Страны на карте заданы матрицей смежности. Если страны i,j имеют на карте общую границу, то элемент матрицы A[i,j] равен 1, иначе 0. Необходимо разбить страны на две группы так, чтобы количество пар смежных стран из противоположных групп было минимальным (генерация матрицы смежности в progrramms/randomatrix.cpp)",
  },
  {
    "_id": "2",
    "title": "Указатель на функцию",
    "description": "Преобразовать функцию сортировки с использованием массивов (b), списков (6.3), деревьев (8.4, 8.5) в итератор. Проверить его работу на двух структурах данных содержащих указатели на различные типы (например, целые и строки). Массив преобразовать в массив указателей.",
  },
  {
    "_id": "3",
    "title": "Алгоритм Дейкстры",
    "description": "Реализовать алгоритм Дейкстры для поиска кратчайшего пути в графе.",
  },
  {
    "_id": "4",
    "title": "Бинарное дерево поиска",
    "description": "Реализовать бинарное дерево поиска и операции вставки, удаления и поиска элемента.",
  }
]);

db.createCollection('status_log');

db.status_log.insertMany([
  {
    "student_task_id": "1",
    "from_status": "new",
    "to_status": "in_progress",
    "date": "2023-07-31",
  },
]);

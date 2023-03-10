# db_hack
db_hack представляет собой набор функций. Предназначенных для редактирования базы данных 
электронного школьного дневника в django shell. [Репозиторий со школьным дневником](https://github.com/devmanorg/e-diary/tree/master).

## Как установить

Python3 уже должен быть установлен на вашем компьютере.
Так же необходимо скачать и запустить проект школьного дневника. [См. README](https://github.com/devmanorg/e-diary/blob/master/README.md)


### Установка
Файл **db_hack.py** необходимо положить в корневую директорию проекта дневника к **manage.py**.

## Использование
Для начала нужно запустить django shell проекта дневника. 
```bash
(venv) sergeiperevera e-diary % python3 manage.py shell     
```
И импортировать файл с функциями.
```bash
import db_hack
```
### db_hack.py
Файл содержит 3 функции для редактирование БД дневника.
1. **fix_marks** - Исправляет все плохие оценки (2 и 3) указанного ученика на 5.
```bash
db_hack.fix_marks("Галкин Изяслав Филиппович")
```
2. **remove_chastisements** - Удаляет замечания учителя у указанного ученика.
```bash
db_hack.remove_chastisements("Галкин Изяслав Филиппович")
```
3. **create_commendation** - Добавляет похвалу от учителя по указанному предмету на дату последнего урока для указанного ученика.
```bash
db_hack.create_commendation("История","Галкин Изяслав Филиппович")
```

## Цель проекта

Проект написан в образовательных целях. В рамках прохождения курса на [dvmn.org](https://dvmn.org/).

# 📊 CSV Фильтрация и Агрегация

## Описание

Этот скрипт позволяет удобно обрабатывать CSV-файлы, поддерживая:

- 📌 Фильтрацию по одной колонке с операторами: `>`, `<`, `=`
- 📌 Агрегацию значений по колонке: `avg` (среднее), `min` (минимум), `max` (максимум)
- 📌 Комбинирование фильтрации и агрегации
- 📌 Форматированный вывод результатов в консоль с помощью `tabulate`

---

## Примеры запуска

📁 Пример CSV-файла (`products.csv`):

```csv
name,brand,price,rating
iphone 15 pro,apple,999,4.9
galaxy s23 ultra,samsung,1199,4.8
redmi note 12,xiaomi,199,4.6
poco x5 pro,xiaomi,299,4.4
```

### 🔸 Вывод всех данных

```bash
python main.py --file products.csv
```

### 🔸 Фильтрация

```bash
python main.py --file products.csv --where "rating>4.7"
```

### 🔸 Фильтрация по строке

```bash
python main.py --file products.csv --where "brand=apple"
```

### 🔸 Агрегация

```bash
python main.py --file products.csv --aggregate "rating=avg"
```

### 🔸 Комбинированный запрос

```bash
python main.py --file products.csv --where "brand=xiaomi" --aggregate "rating=min"
```

---

## Установка

Минимальные зависимости:

- Python 3.7+
- `tabulate` для форматированного вывода

Установка:

```bash
pip install -r requirements.txt
```


---

## Структура проекта

```
workmate/
├── main.py                # Основной скрипт
├── products.csv           # Пример входного CSV-файла
├── requirements.txt       # Основные зависимости
├── requirements-dev.txt   # Зависимости для разработки и тестирования
├── README.md              # Документация
└── tests/
    └── test_main.py       # Набор unit-тестов
```

---

## Тестирование

Тесты написаны с использованием `pytest`.

Запуск:

```bash
pytest --cov=main tests/
```

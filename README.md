# Workmate

📄 Утилита для обработки CSV-файлов с поддержкой фильтрации и агрегации.

## Возможности

- Фильтрация по колонке (`--where "rating>4.5"`)
- Агрегация (`--aggregate "price=avg"`)
- Поддержка операторов `>`, `<`, `=`
- Табличный вывод (через `tabulate`)
- Совместимо с Python 3.7+

## Пример запуска

```bash
python main.py --file products.csv --where "brand=apple" --aggregate "rating=avg"
```

## Установка

```bash
pip install -r requirements.txt
```

## Автор

GitHub: [OlegVladimirovichG](https://github.com/OlegVladimirovichG)

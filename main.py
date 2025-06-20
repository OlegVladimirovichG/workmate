import csv
import argparse
import operator
from tabulate import tabulate

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', required=True)
    parser.add_argument('--where', required=False)
    parser.add_argument('--aggregate', required=False)
    return parser.parse_args()

def read_csv(file_path):
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        data = [row for row in reader]
    return data

OPS = {
    '>': operator.gt,
    '<': operator.lt,
    '=': operator.eq,
}

def parse_condition(condition):
    for op in OPS.keys():
        if op in condition:
            field, value = condition.split(op, 1)
            return field.strip(), OPS[op], value.strip()
    raise ValueError("Invalid condition")

def apply_filter(data, condition):
    if not condition:
        return data

    field, op_func, value = parse_condition(condition)
    result = []
    for row in data:
        cell_value = row[field]
        try:
            cell_value = float(cell_value)
            value_cmp = float(value)
        except ValueError:
            value_cmp = value
        if op_func(cell_value, value_cmp):
            result.append(row)
    return result

def aggregate(data, operation):
    if not operation:
        return data

    field, func = operation.split('=')
    field = field.strip()
    func = func.strip()

    values = []
    for row in data:
        try:
            values.append(float(row[field]))
        except ValueError:
            continue

    if not values:
        return [{func: 'no valid values'}]

    if func == 'avg':
        result = sum(values) / len(values)
    elif func == 'min':
        result = min(values)
    elif func == 'max':
        result = max(values)
    else:
        raise ValueError("Unknown aggregation function")

    return [{func: round(result, 4)}]

def print_table(data):
    if not data:
        print("No data found")
        return

    if isinstance(data[0], dict):
        headers = data[0].keys()
    else:
        headers = []

    print(tabulate(data, headers="keys", tablefmt="grid"))

def main():
    args = parse_args()
    data = read_csv(args.file)
    filtered = apply_filter(data, args.where)
    result = aggregate(filtered, args.aggregate)
    print_table(result)

if __name__ == "__main__":
    main()

import csv
from parser import SQLError


def load_csv(filename):
    try:
        with open(filename, newline='', encoding="utf-8") as f:
            return list(csv.DictReader(f))
    except FileNotFoundError:
        raise SQLError(f"File '{filename}' not found.")


def evaluate_condition(row, clause):
    col = clause["column"]
    op = clause["operator"]
    val = clause["value"]

    if col not in row:
        raise SQLError(f"Column '{col}' does not exist.")

    cell = row[col]

    try:
        cell = float(cell)
        val = float(val)
    except ValueError:
        pass

    if op == "=": return cell == val
    if op == "!=": return cell != val
    if op == ">": return cell > val
    if op == "<": return cell < val
    if op == ">=": return cell >= val
    if op == "<=": return cell <= val


def execute_query(parsed, data):
    if parsed["where"]:
        data = [row for row in data if evaluate_condition(row, parsed["where"])]

    if parsed["aggregate"]:
        if parsed["aggregate"].lower() == "count(*)":
            return [{"COUNT": len(data)}]
        else:
            col = parsed["aggregate"][6:-1]
            count = sum(1 for r in data if r[col])
            return [{"COUNT": count}]

    if parsed["select_cols"] == ["*"]:
        return data

    result = []
    for row in data:
        result.append({c: row[c] for c in parsed["select_cols"]})
    return result

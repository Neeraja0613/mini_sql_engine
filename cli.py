from parser import parse_query, SQLError
from engine import load_csv, execute_query


def print_result(rows):
    if not rows:
        print("No results found.")
        return

    headers = rows[0].keys()
    print(" | ".join(headers))
    print("-" * 40)
    for row in rows:
        print(" | ".join(str(row[h]) for h in headers))


def main():
    filename = input("Enter CSV file name: ")
    data = load_csv(filename)

    print("Mini SQL Engine Started (type 'exit' to quit)")
    while True:
        try:
            query = input("sql> ")
            if query.lower() in ("exit", "quit"):
                break

            parsed = parse_query(query)
            result = execute_query(parsed, data)
            print_result(result)

        except SQLError as e:
            print("Error:", e)


if __name__ == "__main__":
    main()

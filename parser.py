class SQLError(Exception):
    pass


def parse_query(query):
    query = query.strip().rstrip(";")

    if not query.lower().startswith("select"):
        raise SQLError("Only SELECT queries are supported.")

    parts = query.split("where", 1)
    main_part = parts[0].strip()
    where_part = parts[1].strip() if len(parts) == 2 else None

    tokens = main_part.split()
    if "from" not in [t.lower() for t in tokens]:
        raise SQLError("Missing FROM clause.")

    from_index = [t.lower() for t in tokens].index("from")
    select_part = " ".join(tokens[1:from_index])
    table_name = tokens[from_index + 1]

    aggregate = None
    if select_part.lower().startswith("count"):
        aggregate = select_part
        select_cols = []
    elif select_part == "*":
        select_cols = ["*"]
    else:
        select_cols = [c.strip() for c in select_part.split(",")]

    where_clause = None
    if where_part:
        operators = ["<=", ">=", "!=", "=", "<", ">"]
        for op in operators:
            if op in where_part:
                col, val = where_part.split(op)
                where_clause = {
                    "column": col.strip(),
                    "operator": op,
                    "value": val.strip().strip("'")
                }
                break

    return {
        "table": table_name,
        "select_cols": select_cols,
        "where": where_clause,
        "aggregate": aggregate
    }
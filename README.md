\# Mini In-Memory SQL Query Engine



\## Project Overview

This project implements a simplified in-memory SQL query engine using Python.

It demonstrates how basic SQL queries are parsed and executed internally by a database.

The engine loads data from CSV files into memory and allows users to run simple SQL

queries through a command-line interface (CLI), supporting selection, filtering,

and basic aggregation.





\## Setup and Execution Instructions



\### Prerequisites

\- Python 3.8 or higher



\### Steps to Run the Application



1\. Clone the repository:

&nbsp;  ```bash

&nbsp;  git clone <repository-url>

&nbsp;  cd mini-sql-engine

&nbsp;  ```



2\. Run the CLI application:



&nbsp;  ```bash

&nbsp;  python cli.py

&nbsp;  ```



3\. When prompted, enter the CSV file name:



&nbsp;  ```

&nbsp;  data.csv

&nbsp;  ```



4\. Enter SQL queries at the prompt:



&nbsp;  ```

&nbsp;  sql>

&nbsp;  ```



5\. To exit the application, type:



&nbsp;  ```

&nbsp;  exit

&nbsp;  ```





\## Supported SQL Grammar



This engine supports a limited subset of SQL as described below.



\### SELECT Clause



Select all columns:



```sql

SELECT \* FROM data;

```



Select specific columns:



```sql

SELECT name, age FROM data;

```





\### WHERE Clause (Single Condition)



Filtering rows using one condition.



Numeric comparison:



```sql

SELECT \* FROM data WHERE age > 30;

```



String comparison:



```sql

SELECT name FROM data WHERE country = 'India';

```



Supported operators:



```

= , != , > , < , >= , <=

```





\### Aggregation (COUNT)



Count total number of rows:



```sql

SELECT COUNT(\*) FROM data;

```



Count non-null values in a column:



```sql

SELECT COUNT(age) FROM data WHERE country = 'USA';

```



\## Limitations



\* Only SELECT queries are supported

\* Only one WHERE condition is allowed

\* Only one table (CSV file) can be queried at a time

\* No JOIN, GROUP BY, ORDER BY, or subqueries


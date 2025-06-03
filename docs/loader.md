# Data Loading

This section explains how the framework handles loading data from databases and prepares it for use in model training, evaluation, and experimentation.

The data loading pipeline is designed to be **modular**, **extensible**, and **easy to use**. It is composed of three main components:

- **Connector** — manages database connections
- **DataSource** — handles querying and parsing data
- **DataLoader** — provides convenient, high-level data access methods

---

## Connector

The `Connector` is responsible for establishing and managing the connection to your PostgreSQL database. It supports two main modes:

- **Local connection**: connects directly using credentials stored in an environment configuration file (`.env`).
- **Remote SSH tunneling**: securely connects to a remote database via SSH.

This design makes it easy to switch between local development and remote production environments without changing your code.

---

## DataSource

`DataSource` acts as the middleman between your database and the application logic. It uses SQLAlchemy to:

- Execute raw or parameterized SQL queries.
- Parse results into Pandas `DataFrame` objects.
- Automatically apply sport-specific parsing logic based on the `SportType` enumeration.

This means that regardless of the sport or data source, `DataSource` ensures your data is returned in a consistent, ready-to-use format.

---

## DataLoader

The `DataLoader` sits at the top layer and offers simple class methods that make data retrieval straightforward:

- Methods like `load()`, `load_distinct()`, and `preview()` let you query and retrieve data with minimal code.
- The `load_and_wrap()` method wraps the loaded data into specialized domain-specific objects (`DataWrapper` subclasses), making it ready for model consumption.

Using `DataLoader`, you don't need to worry about database connections, SQL syntax, or parsing details — it’s all handled behind the scenes.

---

## Typical Data Loading Flow

Here's what happens when you load data through the framework:

1. Your code calls a method on `DataLoader` to request data.
2. `DataLoader` creates a `DataSource` instance.
3. `DataSource` initializes a `Connector` and opens a database connection.
4. A SQL query is executed to fetch the data.
5. The raw data is parsed and converted to a Pandas DataFrame with sport-specific processing.
6. Optionally, the data is wrapped in a `DataWrapper` for downstream use.

---




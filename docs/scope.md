## Iterative Training with Scope

To support flexible and systematic model training, the framework introduces the concept of a **Scope** — a generalized abstraction for iterating over segments of a dataset. This makes it easy to implement strategies like rolling windows, expanding horizons, or category-based splits for training and evaluation.

### Scope: The Core Iterator

At its core, the `Scope` class defines a consistent interface for stepping through data partitions. It exposes key methods such as:

- `shift()`: Advance the scope to the next data segment.
- `inside()`: Check whether iteration can continue.
- `reset_state()`: Return the scope to its initial state.
- `current_state()`: Return the current position or window definition.

Several concrete implementations of `Scope` are available:

#### WindowScope

A base class for time-based iteration. It operates on a numeric or temporal column and is controlled by three parameters:
- `start`: Where to begin.
- `size`: Length of the window.
- `stride`: Step size between iterations.

Derived classes include:

- `ScopeRoller`: Uses a fixed-size window and moves it forward by `stride` on each iteration. This is similar to a rolling window approach.
- `ScopeExpander`: Starts with a fixed point and increases the window size with each iteration. Useful for walk-forward validation.

#### EnumScope

Used for iterating over categorical values (e.g., leagues or countries). It loops through unique entries in a specified column, enabling segmented evaluation for each category.

---

## ScopeSelector: Bridging Scope and Data

While `Scope` defines *how* iteration happens, it doesn’t know anything about the dataset itself. That’s where `ScopeSelector` comes in.

A `ScopeSelector` pairs a `Scope` with a `DataWrapper` and provides the `transform()` method, which applies the current scope state to the dataset. This enables dynamic slicing of data during iterative training or evaluation.

Different selectors specialize in different types of filtering:
- `WindowSelector`: Filters rows within a numeric or temporal range.
- `EnumSelector`: Filters by specific category values.

This design separates *when* the data changes (`Scope`) from *how* it’s extracted (`ScopeSelector`), improving modularity and making it easier to extend or compose new strategies.

---

## DataSelector: Orchestrating Iteration

The `DataSelector` class coordinates multiple `ScopeSelector` instances—both for training and testing—and ensures smooth iteration over all valid combinations of data splits.

It supports:
- Recursive iteration with backtracking to explore complex scope setups.
- Mixed scope types (e.g., rolling training window with category-based testing).
- Validation of each scope configuration via `holds()` before proceeding.

During each step, `DataSelector`:

1. Calls `transform()` on all selectors to extract the current data subset.
2. Validates the configuration.
3. Advances or backtracks based on the iteration logic.

This design supports reproducible and structured experiments across multiple training and testing regimes, including nested, time-based, and categorical splits.

# Simulation Framework

To evaluate the effectiveness of betting strategies based on model predictions and associated odds, the framework introduces a modular and extensible simulation infrastructure centered around the `Simulation` base class.

## Abstract Simulation Interface

The `Simulation` class serves as an abstract base class that defines the contract for all betting simulations. It operates over a `DataWrapper`, which provides access to model predictions, betting odds, and match outcomes in a unified structure.

### Key Methods

- **Initialization**  
  Accepts a `DataWrapper` instance and stores the underlying DataFrame for simulation use.

- **`simulate()`** *(abstract)*  
  Must be implemented by subclasses. Defines the specific betting logic and how returns are calculated.

- **`evaluate()`**  
  A shared utility method that summarizes simulation performance using the following metrics:
  - **Total Return** – Cumulative return from all simulated bets.
  - **Mean Return** – Average return per bet.
  - **Standard Deviation** – Measures the volatility of returns.
  - **Sharpe Ratio** – Risk-adjusted return, computed as:  
    ```
    Sharpe Ratio = Mean Return / Standard Deviation
    ```

This abstraction ensures consistent evaluation while allowing custom betting logic to be defined independently for each strategy.

---

This design enables empirical evaluation and benchmarking of various betting strategies, all backed by model-driven predictions and structured performance metrics.

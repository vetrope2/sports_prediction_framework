# DataWrapper Module

The **DataWrapper** module provides a unified and extensible interface for handling sports data within the framework. It abstracts the complexity of working with heterogeneous datasets by standardizing access to core elements such as features, labels, and predictions—essential components in machine learning workflows.

## Core Components

The module revolves around two primary classes:

### DataHandler

- Acts as the foundational data container.
- Stores raw sports data in a `pandas.DataFrame`.
- Manages explicit collections of feature columns, label columns, and prediction columns.
- Supports operations like merging new features or labels, extracting specific data subsets, and creating copies for safe data manipulation.

### DataWrapper

- A higher-level interface built on top of `DataHandler`.
- Provides convenient methods to access the dataframe, features, labels, and predictions.
- Supports adding or updating columns seamlessly.
- Designed to be extended for sport-specific adaptations by subclassing.

## Specialized Wrappers

To handle the diverse structures of sports data, the framework includes specialized `DataWrapper` subclasses tailored to different domains:

- **MatchWrapper**  
  Focuses on match-based sports data. It manages columns related to competing teams (`Home`, `Away`, `HID`, `AID`), scores (`HS`, `AS`), and outcomes (`WDL`). This wrapper offers helper methods to retrieve and update teams involved in the dataset, encapsulating match-specific logic for easier downstream processing.

- **RaceWrapper**  
  Designed for individual competitor sports such as racing. It standardizes access to ranking and performance-related data, facilitating feature extraction and modeling for race results.

- **LeagueWrapper**  
  Handles aggregated competition data such as league standings or seasonal summaries. This wrapper is useful for datasets that represent competition contexts broader than individual events.

### Combining Wrappers

Some sports combine multiple data perspectives and therefore require multiple inheritance from these wrappers. For example, the `FootballWrapper` inherits from both `MatchWrapper` and `LeagueWrapper` to provide comprehensive support for both match-level and league-level data semantics.

---

This modular design ensures that data handling remains consistent across different sports, while still being flexible enough to accommodate the unique aspects of each sport’s data structure.

---

# Parser Component

The **Parser** module is responsible for converting raw data from external or internal databases into a standardized internal format that the framework can use for modeling and analysis. This step is crucial when working with heterogeneous data sources, each with its own naming conventions, formats, and quirks.

Parsing is automatically triggered during data loading when data is wrapped into a `DataWrapper`, ensuring all data entering the pipeline follows a consistent schema.

## Parser Architecture

All parser implementations inherit from a common base class, `AbstractParser`, which defines the standard interface and expected behavior.

### Current Implementations

  - Filtering out rows with invalid or placeholder results.
  - Extracting home and away team goals from raw result strings.
  - Normalizing season representations (e.g., `"2020/2021"`) into a consistent numeric format.
  - Mapping categorical match outcomes (`"W"`, `"D"`, `"L"`) to numeric labels (`1`, `0`, `2`) suitable for classification.
  - Renaming inconsistent column names to standardized schema (e.g., `"HT"` → `"Home"`).
  - Ensuring proper data types for key columns to maintain downstream compatibility.



## Data Source Specific Parsing

The parser implementations include custom methods for different data sources, since each source may have unique formats or conventions. This modular design allows easy extension to new data sources without affecting existing parsers.

## Summary

The Parser component abstracts the complexity of raw data heterogeneity, providing a clean and reliable interface to the rest of the framework. By standardizing input data, it enables consistent and accurate downstream processing and model training.

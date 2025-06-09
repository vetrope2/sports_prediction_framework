# Self-Contained Demonstration

We provide a self-contained demonstration that does **not** require any database access. This makes it easy to explore and test the framework without setting up a database connection.

The demonstration runs in **Google Colab** and uses the `data.parquet` file located in the `examples` directory of the repository.



You can open and run the notebooks directly via the following links:

- [Flat Model](https://colab.research.google.com/drive/1cvTSVJl9IKZ5zetAArQoUHMiGpkao_N1?usp=sharing)

- [Other Flat](https://colab.research.google.com/drive/1s_RPveoUixcFV2rnhW3lM3VRf8ynknlg?usp=sharing)

- [Model Evaluation](https://colab.research.google.com/drive/1h-C7imynYpMc1OvjwBnfxgcU2mvczJsb?usp=sharing)

- [Optimization](https://colab.research.google.com/drive/1PDxtwabuDKNq8BPbRyAJmk8nsWcuTvUy?usp=sharing)

- [Simulation example](https://colab.research.google.com/drive/18KNe19nwtR_dQaZLlF6deUjtP77b12B9?usp=sharing)

Feel free to explore these notebooks to get a hands-on understanding of the framework using real data samples.


### Example of `data.parquet` Content 

| Date       | Home          | Away           | HS | AS | WDL | odds_1 | odds_X | odds_2 |
|------------|---------------|----------------|----|----|-----|--------|--------|--------|
| 2004-01-21 | Bayern Munich | Hamburger SV   | 3  | 0  | 1   | 1.39   | 4.00   | 6.50   |
| 2004-01-22 | Wolfsburg     | Dortmund       | 1  | 2  | 2   | 1.83   | 3.25   | 3.75   |
| 2004-01-22 | Nurnberg      | Kaiserslautern | 1  | 3  | 2   | 2.10   | 3.25   | 3.00   |
| 2004-01-22 | Nurnberg      | Kaiserslautern | 1  | 3  | 2   | 2.00   | —      | 3.25   |
| 2004-01-22 | Mainz         | Stuttgart      | 2  | 3  | 2   | 2.79   | 3.25   | 2.20   |

> **Note:** This is a small excerpt of the `data.parquet` file. The actual dataset contains many more rows and columns with additional information.

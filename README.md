# Traslatio
Data pipeline for learning data engineering concepts


[![Data Pipeline workflow][workflow-image]](https://example.com)


<!-- MARKDOWN LINKS & IMAGES -->
[workflow-image]: traslatio_3.drawio-min.png


## Project Organization

```
    ├── LICENSE
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    └── src                <- Source code for use in this project.
        ├── __init__.py    <- Makes src a Python module
        │
        ├── data           <- Scripts to download or generate data
        │   └── download_dabase.sh
        │   └── make_csv.sql
        │   └── make_dataset.sh
```

## How to run locally

1. Install requirements

`pip install -r requirements.txt`

2. Extract data:
    - Choice 1: Scrape data.
        - Use this Scrapy project https://github.com/lmontanares/Translatio and then generate the SQLite database file `biobio.db`
    - Choice 2: Download database file `biobio.db` from Google Drive.
        - Give executable permissions to the bash file if needed. Like this:
        ```bash
        chmod +x src/data/download_database.sh
        ```
        - Run the script from the root directory:

        ```bash
        source src/data/download_database.sh
        ```

3. Now create the CSV file.
    - From the root directory run `source src/data/make_dataset.sh`

4. Open the jupyter notebook `notebooks/1.0-initial-data-cleaning.ipynb` to generate `data/interim/clean_data_01.csv`

<p><small>Inspired by <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>

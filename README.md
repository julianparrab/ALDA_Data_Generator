# ALDA_Data_Generator

## Project Structure

This project simulates and generates synthetic datasets for urban tree inventories in Bogotá, Colombia. Below is the structure of the main directories and files:

ALDA_Data_Generator/ │ ├── data/ # Reference and input data (CSV, GeoJSON) │ ├── info_especies.csv # Botanical species reference │ └── localidades_bogota.geojson # Bogotá localities polygons │ ├── src/ # Source code │ ├── data_reference.py # Reference data loader and constants │ ├── data_generator.py # Main data generation logic │ └── generate_coord.py # Functions for generating random coordinates │ ├── notebooks/ # Jupyter notebooks for analysis (optional) │ ├── tests/ # Unit tests (optional) │ ├── requirements.txt # Python dependencies ├── README.md # Project documentation └── mk.md # Project structure (this file)

## Main Files

- **data_reference.py**  
  Loads reference data (species, treatments, localities, etc.) and provides constants for the generator.

- **data_generator.py**  
  Contains the main classes and logic for generating synthetic tree data, including random attribute assignment and dataset creation.

- **generate_coord.py**  
  Generates random geographic coordinates within the boundaries of Bogotá’s localities using GeoJSON data.

## Data Directory

- **info_especies.csv**  
  Contains botanical species information and typical measurements.

- **localidades_bogota.geojson**  
  Geospatial data for Bogotá’s localities, used for spatial simulation.

## How to Use

1. Install dependencies from `requirements.txt`.
2. Place the required data files in the `data/` directory.
3. Run the generator scripts in `src/` to create synthetic datasets.

---

*This file describes the structure and main components of the ALDA_Data_Generator project.*
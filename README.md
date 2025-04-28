# DataSpaces

## Personal Fitness Data Space 

🚴‍♂️ This project builds a personal Data Space to manage, process, and analyze fitness activities, applying Data Mesh and Data Product principles. 

## Project Goals 

- Build a fully cloud-based fitness data management system. 

- Ingest and parse .fit and .tcx files from Strava or other sources. 

- Structure data into Bronze, Silver, and Gold layers. 

- Orchestrate pipelines using Prefect. 

- Visualize key training metrics (speed, power, cadence, heart rate). 

## Architecture 

- **Storage:** GitHub repo for code; cloud DB for structured data (Supabase/Railway). 

- **Compute:** GitHub Codespaces (Python runtime). 

- **Orchestration:** Prefect Cloud (Free tier). 

- **Dashboard:** (Future) Streamlit App or similar. 

## How to Run 

1. Clone this repository inside GitHub Codespaces. 
2. Install dependencies:
   ```bash
   pip install -r requirements.txt 
   ```
3. Upload .fit and .tcx files into data/raw/.
4. Run ETL scripts in /etl/ to generate Bronze datasets.
5. (Optional) Register and schedule Prefect Flows. 

## Folder Structure 

```bash
DataSpaces/ 
├── configs/ 
│   └── config.yaml 
├── data/ 
│   ├── raw/ 
│   ├── bronze/ 
│   ├── silver/ 
│   └── gold/ 
├── db/ 
│   └── schema.sql 
├── docs/ 
│   ├── architecture.md 
│   ├── data_products.md 
│   └── data_contracts.md 
├── etl/ 
│   ├── bronze_layer_parser.py 
│   ├── silver_layer_transformer.py 
│   └── gold_layer_analytics.py 
├── dashboard/ 
│   └── (future Streamlit app) 
├── README.md 
└── requirements.txt
```

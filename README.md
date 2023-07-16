# IPL winning chance predictor

## Overview of Amazon sales data analysis: -  
**When it is IPL we all want to know how much chance left in favour our favourite team. so i made this web application to do so**  

## Data location: -   
- data:
  - Processed data: [Here](ipl_data\data.csv)
  - EDA teams notebook: [Here](ipl_data\EDA_players.ipynb)
  - Model training notebook: [Here](ipl_data\model_training.ipynb)
  - EDA players notebook: [Here](ipl_data\EDA_players.ipynb)
  - Ball by ball raw data: [Here](ipl_data\IPL_Ball_by_Ball_2008_2022.csv)
  - IPL matches raw data: [Here](ipl_data\IPL_Matches_2008_2022.csv)


## Setup: -
  - Run for create virtual environment
    - > conda create -p venv python=3.10 -y
  - Run before start application: -
    - > pip install -r requirements.txt
  - Run the app
    - > streamlit run app.py
  - Run for create docker image: -
    - > docker build -t ranjitkundu/amazon_sales:v1 .
  - Show docker images: -
    - > docker images
  - Run the docker image in container: - 
    - > docker run -p 8501:8501 ranjitkundu/amazon_sales:v1
  - Initiate GitHub: -
    - > git init
  - Add all files in GitHub: -
    - > git add .
  - Commit code in GitHub: -
    - > git commit -m "message"
  - Push code in GitHub: -
    - > git push -u origin main


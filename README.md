# Customer Risk Prediction

This analysis uses sample data from a payment platform that allows users to pay 
merchants over 4 periods following the purchase. Using payment transaction-level 
data, we have predicted the likelihood of a default in repayment.

The focus of this analysis is to use Python to gain a basic understanding of the
data and build features for the predictive model. We did not build a predictive
model per se.

### Setup

Run the following commands to create a [Jupyter Data Science](https://hub.docker.com/r/jupyter/datascience-notebook/) Docker image. 
```
docker run -p 8888:8888 -e JUPYTER_ENABLE_LAB=yes jupyter/datascience-notebook
```

Open the URL this command prints into your web browser. Open the Jupyter command 
line in Jupyter and run the following commands.
```
git clone https://github.com/gordonsilvera/algom-trading.git
pip install -U -r /home/jovyan/quadpay_analysis/requirements.txt
```

### Contents

+ __notebooks/01_feature_engineering.ipynb__. Generate features from the input data `orders.csv`.

+ __notebooks/02_data_viz_analysis.ipynb__. Visualize features to gain an understanding of their influence on repayment rates.

+ __src/functions.py__. Aggregation functions used in 01_feature_engineering. 

+ __src/viz.py__. Functions to visualize datasets in a standardized way. 

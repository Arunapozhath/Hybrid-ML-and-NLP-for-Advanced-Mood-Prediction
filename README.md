
# Hybrid-ML-and-NLP-for-Advanced-Mood-Prediction

## *Project Overview*
This is a comprehensive mental health mood prediction system designed to monitor an individual’s mood and mental well-being using a combination of machine learning (ML), deep learning (DL), and NLP techniques. The project integrates various models, including a Linear Regressor, LSTM, and BERT, to analyze sentiment scores and time series data, providing actionable insights through an interactive GUI built with Streamlit.

## *Dataset*
The project utilizes a custom dataset containing 20 features related to mental health. Key features include:
- Mood Score
- Activity Level
- Sleep Hours
- Stress Level
- Heart Rate
- Sentiment Score (from BERT model)

## *Database Setup*
1. Created a MySQL database to store the raw and processed data.
2. Accessed and deployed the database using Python for data ingestion and preprocessing.
3. Performed data cleaning and transformation for model readiness.

## *Model Development*
### *Sentiment Analysis using BERT*
- Built a BERT model to analyze sentiment scores from text input data.
- Tokenization was performed to preprocess the text data before feeding it into the BERT model.
- Integrated the sentiment scores into the main dataset for further analysis.

### *Linear Regressor Model*
- Developed a Linear Regressor model to predict mood scores based on the features in the dataset.

### *LSTM for Sentiment and Time Series Analysis*
- Built an LSTM model that integrates sentiment scores and time series data to predict mood scores.

### *Hybrid Model*
- Developed a hybrid model combining the LSTM and Linear Regressor models to enhance mood prediction accuracy.

## *Explainability*
To enhance model interpretability, the project uses:
- *SHAP (SHapley Additive exPlanations)*
- *LIME (Local Interpretable Model-agnostic Explanations)*
- *XAI (Explainable AI) Techniques*

These methods help explain feature importance and individual predictions, providing transparency in decision-making.

## *Deployment*
1. *GUI Development with Streamlit:*
   - Created an interactive user interface using Streamlit for the Linear Regressor model.
   - Allows users to input data and view real-time predictions and visualizations.

## *Visualization*
- Data was exported from the MySQL database as a CSV file and visualized in Tableau for insights and patterns.
- Used *Matplotlib* to create additional visualizations for the project, including charts and graphs to represent trends, feature relationships, and model performance.

## *Technologies Used*
- *Programming Languages:* Python
- *Database:* MySQL
- *Machine Learning Libraries:* Scikit-learn, TensorFlow, Keras
- *NLP:* BERT (Bidirectional Encoder Representations from Transformers)
- *Explainability:* SHAP, LIME, XAI
- *Data Visualization:* Tableau, Matplotlib
- *Deployment:* Streamlit

## *How to Run*
1. Clone the repository:
  
   ```bash
   git clone https://github.com/Arunapozhath/Hybrid-ML-and-NLP-for-Advanced-Mood-Prediction.git
   ```

2. Install necessary dependencies:
    
   ```bash
   pip install -r requirements.txt
   ```

3. Run Streamlit:

   ```bash
   streamlit run <filename.py>
   ```

---

### Tableau Dashboard Link:
You can view the Tableau dashboard using the following link:  
[Tableau Dashboard](https://public.tableau.com/views/Dashboard_17316914384510/Dashboard1?:language=en-US&publish=yes&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)

### Embedded Tableau Dashboard Code:
For embedding the Tableau dashboard directly, use this HTML code:


<div class='tableauPlaceholder' id='viz1731691495159' style='position: relative'>
    <noscript>
        <a href='#'>
            <img alt='Dashboard 1' src='https://public.tableau.com/static/images/Da/Dashboard_17316914384510/Dashboard1/1_rss.png' style='border: none'/>
        </a>
    </noscript>
    <object class='tableauViz' style='display:none;'>
        <param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' />
        <param name='embed_code_version' value='3' />
        <param name='site_root' value='' />
        <param name='name' value='Dashboard_17316914384510/Dashboard1' />
        <param name='tabs' value='no' />
        <param name='toolbar' value='yes' />
        <param name='static_image' value='https://public.tableau.com/static/images/Da/Dashboard_17316914384510/Dashboard1/1.png' />
        <param name='animate_transition' value='yes' />
        <param name='display_static_image' value='yes' />
        <param name='display_spinner' value='yes' />
        <param name='display_overlay' value='yes' />
        <param name='display_count' value='yes' />
        <param name='language' value='en-US' />
        <param name='filter' value='publish=yes' />
    </object>
</div>
<script type='text/javascript'>
    var divElement = document.getElementById('viz1731691495159');
    var vizElement = divElement.getElementsByTagName('object')[0];
    if ( divElement.offsetWidth > 800 ) {
        vizElement.style.width='100%';
        vizElement.style.height=(divElement.offsetWidth*0.75)+'px';
    } else if ( divElement.offsetWidth > 500 ) {
        vizElement.style.width='100%';
        vizElement.style.height=(divElement.offsetWidth*0.75)+'px';
    } else {
        vizElement.style.width='100%';
        vizElement.style.height='1627px';
    }
    var scriptElement = document.createElement('script');
    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';
    vizElement.parentNode.insertBefore(scriptElement, vizElement);
</script>



\# CyberMirror – Machine Learning Module



\## 1. Overview



The ML module of CyberMirror is designed to process vehicle network traffic, extract relevant features, and identify unusual traffic patterns using machine learning.



The current implementation includes data preprocessing, feature scaling, Isolation Forest anomaly detection, model evaluation, and model persistence.



\## 2. Technology Stack



\- Python 3.12

\- Pandas

\- NumPy

\- Scikit-learn

\- Matplotlib

\- Seaborn

\- Joblib



\## 3. Project Structure



```text

ml/

├── datasets/

│   ├── raw/

│   │   ├── sample\_can\_traffic.csv

│   │   └── synthetic\_can\_training.csv

│   └── processed/

├── evaluation/

│   ├── metrics.py

│   └── evaluate\_model.py

├── models/

│   ├── anomaly\_detector.py

│   ├── compare\_contamination.py

│   ├── train\_anomaly\_model.py

│   └── trained/

│       ├── isolation\_forest.joblib

│       └── feature\_scaler.joblib

├── preprocessing/

│   ├── data\_loader.py

│   ├── data\_cleaner.py

│   ├── feature\_extraction.py

│   ├── feature\_selection.py

│   ├── feature\_scaling.py

│   └── preprocess\_pipeline.py

└── README.md

```



\## 4. Data Preprocessing



The preprocessing workflow consists of:



1\. Loading and validating CSV traffic data.

2\. Cleaning duplicate and missing records.

3\. Extracting numerical traffic features.

4\. Selecting the required feature columns.

5\. Scaling features using StandardScaler.



\### Selected Features



\- message\_frequency

\- inter\_arrival\_time

\- payload\_length



The dataset also contains timestamp, CAN ID, and ECU ID information.



\## 5. Anomaly Detection



CyberMirror currently uses the Isolation Forest algorithm from Scikit-learn.



The model identifies unusual traffic patterns based on the selected numerical features.



\### Model Configuration



\- Algorithm: Isolation Forest

\- Number of estimators: 100

\- Contamination: 0.15

\- Random state: 42



The contamination value was selected provisionally after comparing 0.10, 0.15, 0.20, and 0.25 on the synthetic test dataset.



\## 6. Model Evaluation



The initial model was evaluated using a synthetic dataset containing 40 records:



\- 30 normal-looking traffic records

\- 10 deliberately abnormal-looking traffic records



Initial evaluation results at contamination 0.25:



| Metric | Result |

|---|---:|

| Accuracy | 75% |

| Normal precision | 81% |

| Normal recall | 87% |

| Abnormal precision | 50% |

| Abnormal recall | 40% |

| Abnormal F1-score | 44% |



The contamination comparison produced the highest F1-score at 0.15:



| Contamination | Precision | Recall | F1-score |

|---|---:|---:|---:|

| 0.10 | 0.50 | 0.20 | 0.29 |

| 0.15 | 0.67 | 0.40 | 0.50 |

| 0.20 | 0.50 | 0.40 | 0.44 |

| 0.25 | 0.50 | 0.40 | 0.44 |



These results are preliminary. The same synthetic records were used for training and evaluation, so they do not represent independent validation or real-world vehicle detection performance.



\## 7. Model Persistence



The trained model and fitted scaler are saved using Joblib.



\- `isolation\_forest.joblib`

\- `feature\_scaler.joblib`



The preprocessing pipeline supports both fitting a new scaler during training and reusing a saved scaler during inference.



\## 8. Current Status



Implemented:

\- CSV data loading and validation

\- Data cleaning

\- Feature extraction and selection

\- Feature scaling

\- Scaler persistence

\- Isolation Forest training

\- Anomaly prediction and scoring

\- Model persistence

\- Initial synthetic-data evaluation

\- Contamination comparison



Pending:

\- Integration with real CAN traffic from the simulation module

\- Independent model validation

\- Further model tuning using representative vehicle traffic

\- Integration with the backend alert and risk analysis workflow




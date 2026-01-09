# AI & Machine Learning Midterm Exam – Cybersecurity
**Student:** Roman Tsertsvadze  
**Repository:** aimlmid2026_r_tsertsvadze25  

### TASK 1 Finding the correlation
### Pearson Correlation Result
Finding the correlation "max.ge/aiml_midterm/84687_html"
blue dots : blue dots cordination : 
X = [-9.20, -6.60, -4.10, -1.5, 0.90, 3.50, 6.00, 8.60]
Y = [-7.40, -4.80, -2.50, -0.10, 1.80, 4.00, 6.20, 8.20]

Using the Pearson correlation coefficient formula, the computed value is:

r = 0.9994

<img width="858" height="639" alt="image" src="https://github.com/user-attachments/assets/bebb807c-da39-4083-a6bb-937a6070730e" />


This value is very close to +1, indicating an extremely strong positive
linear relationship between the variables X and Y. This result is also
confirmed visually by the scatter plot, where the blue data points form
an almost straight increasing line.
The Pearson correlation coefficient was calculated using the standard
formula involving covariance of X and Y divided by the product of their
standard deviations.



### TASK 2 Spam email detection
## Task 2.1 – Dataset Upload

The dataset used for spam email detection was provided at:
max.ge/aiml_midterm/r_tsertsvadze25_84687_csv

The file has been uploaded to this repository:
data/r_tsertsvadze25_84687.csv

The dataset contains 2500 email records with the following features:
- words
- links
- capital_words
- spam_word_count

The target class is `is_spam`, where 1 represents spam and 0 represents legitimate email.
## Task 2.2 – Model Training

### Data Loading and Processing
The dataset is loaded using pandas. Feature columns (`words`, `links`,
`capital_words`, `spam_word_count`) are separated from the class label
`is_spam`.

The data is split into 70% training and 30% testing using
`train_test_split`.

### Model
A Logistic Regression model was used for email classification. Logistic
Regression is a common algorithm for binary classification problems
such as spam detection.

### Model Coefficients
After training, the model outputs coefficients for each feature, which
represent how strongly each feature influences the prediction of spam.

## Task 2.3 – Model Validation

The trained model was evaluated on the test dataset that was not used
during training.

- Accuracy measures the proportion of correctly classified emails.
- The Confusion Matrix shows correct and incorrect predictions for both
  spam and legitimate emails.

  ## Task 2.4 – Custom Email Classification

The application can classify new emails by extracting the same features
used in the dataset and passing them to the trained Logistic Regression
model.


## Task 2.5 – Spam Email Example

"WIN BIG NOW! Limited time offer!!! Click the link to claim your free
reward immediately."

This email was designed to be classified as spam due to the use of
promotional language, urgency, excessive capital letters, and spam-
related keywords.

## Task 2.6 – Legitimate Email Example

"Hello, please find attached the project report for review. Let me know
if you have any feedback."

This email represents normal professional communication without spam-
related characteristics.


The class distribution chart shows the balance between spam and
legitimate emails in the dataset.

The feature importance plot shows which features contribute most to
spam detection according to the Logistic Regression model.

Task 7

Two visualizations please check python code. 
Visualization 1 – Class distribution
Visualization 2 – Feature importance


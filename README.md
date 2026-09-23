# 🌱 Dry Bean Classification Using Machine Learning

## 📌 Project Overview

This project is a **Machine Learning-based Dry Bean Classification System** developed using Python and Streamlit.

The application predicts the **variety of a dry bean** based on its morphological and geometric measurements. The user enters 16 feature values into the Streamlit web application, and the trained Machine Learning model predicts the corresponding dry bean variety.

The application also displays the **prediction probabilities** for the different bean varieties and provides a probability distribution chart.

---

## 🎯 Objectives

The main objectives of this project are:

* To classify dry bean varieties using Machine Learning.
* To use morphological and geometric characteristics of beans for classification.
* To develop an interactive web application using Streamlit.
* To load a previously trained Machine Learning model using Joblib.
* To display the predicted bean variety.
* To display prediction probabilities for each class.
* To provide a simple and user-friendly interface for prediction.

---

## 🫘 Bean Varieties

The model can classify the following dry bean varieties:

* Seker
* Barbunya
* Bombay
* Cali
* Dermason
* Horoz
* Sira

---

## 📊 Input Features

The application uses the following **16 features**:

| No. | Feature         |
| --: | --------------- |
|   1 | Area            |
|   2 | Perimeter       |
|   3 | MajorAxisLength |
|   4 | MinorAxisLength |
|   5 | AspectRation    |
|   6 | Eccentricity    |
|   7 | ConvexArea      |
|   8 | EquivDiameter   |
|   9 | Extent          |
|  10 | Solidity        |
|  11 | roundness       |
|  12 | Compactness     |
|  13 | ShapeFactor1    |
|  14 | ShapeFactor2    |
|  15 | ShapeFactor3    |
|  16 | ShapeFactor4    |

The feature names are kept consistent with the trained model because the prediction code passes these columns directly to the model.

---

## 🛠️ Technologies Used

* **Python**
* **Pandas**
* **Scikit-learn**
* **Joblib**
* **Streamlit**
* **Jupyter Notebook**
* **Machine Learning**

---

## 📂 Project Structure

```text
dry-bean-classification/
│
├── app.py
├── drybean.ipynb
├── requirements.txt
│
├── data set/
│   └── DryBeanDataset/
│       └── best_dry_bean_model.pkl
│
└── README.md
```

### File Description

**app.py**

Contains the Streamlit web application and prediction interface.

**drybean.ipynb**

Jupyter Notebook containing the Machine Learning development/training work.

**best_dry_bean_model.pkl**

Saved trained Machine Learning model used by the Streamlit application.

**requirements.txt**

Contains the Python libraries required to run the application.

**README.md**

Project documentation.

---

## ⚙️ How the Application Works

The application follows these steps:

```text
User enters bean measurements
             ↓
       Input DataFrame
             ↓
      Trained ML Model
             ↓
       Model Prediction
             ↓
   Predicted Bean Variety
             ↓
 Prediction Probabilities
             ↓
     Probability Chart
```

The application loads the trained model using Joblib before performing predictions.

---

## 🖥️ Streamlit Application

The application provides an interface where users can enter all 16 bean measurements.

After entering the values, the user clicks:

```text
🔮 Predict Bean Variety
```

The application then displays:

* Predicted dry bean variety
* Prediction probabilities
* Probability distribution chart
* Prediction summary

These prediction and probability components are implemented in the Streamlit application.

---

## 🚀 Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/dry-bean-classification.git
```

### Step 2: Open the Project Folder

```bash
cd dry-bean-classification
```

### Step 3: Create a Conda Environment

```bash
conda create -n drybean python=3.10 -y
```

Activate it:

```bash
conda activate drybean
```

### Step 4: Install Required Libraries

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

Run the following command:

```bash
streamlit run app.py
```

The Streamlit application will open in your browser.

---

## 🔮 Making a Prediction

1. Open the Streamlit application.
2. Enter the 16 bean measurements.
3. Review the input values.
4. Click **Predict Bean Variety**.
5. The predicted bean variety will be displayed.
6. View the prediction probabilities.
7. View the probability distribution chart.

---

## 📈 Prediction Output

The application provides a result similar to:

```text
Predicted Dry Bean Variety: Seker
```

It also displays the probability associated with each bean variety when the trained model supports probability prediction.

---

## 🧠 Machine Learning Task

This project performs:

**Multi-Class Classification**

The goal is to predict one class from multiple possible dry bean varieties.

```text
Input:
16 bean measurements

Output:
One dry bean variety
```

---

## 🌐 Deployment

The Streamlit application can be deployed using **Streamlit Community Cloud**.

General deployment process:

1. Upload the project to GitHub.
2. Open Streamlit Community Cloud.
3. Connect your GitHub repository.
4. Select the repository.
5. Select `app.py` as the main file.
6. Deploy the application.

---

## 🔒 Model File

The trained model is stored

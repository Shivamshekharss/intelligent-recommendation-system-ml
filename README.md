# 🎬 Intelligent Agent-Based Hybrid Recommendation System (ML)

An advanced Agent-Based Hybrid Movie Recommendation System built using Machine Learning.  
This project uses the MovieLens 100K dataset and combines collaborative filtering, hybrid modeling, genre-aware personalization, and explainable AI agents.

---

## 🚀 Key Features

### 🎯 Recommendation Models
- User-Based Collaborative Filtering (UBCF)
- Item-Based Collaborative Filtering (IBCF)
- Hybrid Recommendation System (CF + Popularity)

---

### 🤖 Agent-Based Architecture (Core Innovation)
- Decision Agent
  - Dynamically selects best model based on user behavior

- Cold Start Agent
  - Handles new users with no ratings
  - Uses popularity + genre-based recommendation

---

### 🎭 Genre-Aware Personalization
- User selects preferred genre
- System filters recommendations based on genre
- Improves personalization and relevance

---

### 🧠 Explainable Recommendations
Each recommendation includes:
- CF-based reasoning
- Genre-based reasoning
- Hybrid score contribution

---

### 📊 Evaluation Metrics
- Precision@K
- Recall@K
- F1-Score

---

### 🌐 Web Application
- Built using Streamlit
- Interactive UI for recommendations
- Supports user-based + genre-based modes

---

## 📁 Project Structure

FinalYearProject/
│
├── data/
│   └── ml-100k/
│
├── recommendation/
│   ├── main.py
│   ├── app.py
│   ├── evaluation.py
│
│   ├── models/
│   │   ├── user_based.py
│   │   ├── item_based.py
│   │   └── hybrid.py
│
│   ├── agents/
│   │   ├── decision_agent.py
│   │   └── cold_start_agent.py
│
│   ├── explainability/
│   │   └── explanation_engine.py
│
│   ├── preprocessing/
│   │   └── genre_processing.py
│
├── notebooks/
│   └── evaluation.ipynb
│
└── requirements.txt

---

## ⚙️ Installation

### 1. Clone Repository
```bash
git clone https://github.com/Shivamshekharss/intelligent-recommendation-system-ml.git
cd intelligent-recommendation-system-ml
## ⚙️ Installation

### 2. Create Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

---

## ▶️ Run Project

### Run System
```bash
cd recommendation
python main.py
```

### Run Streamlit App
```bash
streamlit run app.py
```

Open:
```
http://localhost:8501
```

---

## 📊 Results

| Model        | Precision@5 | Recall@5 |
|--------------|-------------|----------|
| User-Based   | 0.342       | 0.116    |
| Item-Based   | 0.356       | 0.121    |
| Hybrid       | Better balance |
| Agent-Based  | Best performance |

---

## 🧠 Workflow

- User inputs data  
- Decision Agent selects model  
- CF / Item CF / Hybrid runs  
- Genre filter applied  
- Explainability generated  
- Final recommendations shown  

---

## 🎯 Contributions

- Agent-Based Recommendation System  
- Hybrid CF with adaptive selection  
- Genre-aware personalization  
- Explainable AI module  
- Full evaluation framework  

---

## 🛠️ Tech Stack

- Python  
- Pandas  
- NumPy  
- Scikit-learn  
- Streamlit  

---

## 👨‍💻 Author

Shivam Shekhar  
Final Year Project – Machine Learning

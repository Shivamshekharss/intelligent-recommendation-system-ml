# 🎬 Intelligent Recommendation System (ML)

An intelligent movie recommendation system built using Machine Learning and an agent-based architecture.  
This project uses the MovieLens 100K dataset to recommend movies based on user behavior, item similarity, and hybrid techniques.

---

## 🚀 Features

- 🎯 User-Based Collaborative Filtering
- 🎯 Item-Based Collaborative Filtering
- 🔀 Hybrid Recommendation System
- 🤖 Agent-Based Decision System
  - Decision Agent (selects best model)
  - Cold Start Agent (handles new users)
- 🎭 Genre-Based Recommendations
- 📊 Evaluation Metrics
  - Precision@K
  - Recall@K
- 🌐 Streamlit Web App UI

---

## 📁 Project Structure
FinalYearProject/
│
├── data/
│ └── ml-100k/
│
├── recommendation/
│ ├── main.py
│ ├── app.py
│ ├── evaluation.py
│ │
│ ├── models/
│ │ ├── user_based.py
│ │ ├── item_based.py
│ │ └── hybrid.py
│ │
│ ├── agents/
│ │ ├── decision_agent.py
│ │ └── cold_start_agent.py
│
├── notebooks/
│ └── evaluation.ipynb
│
└── requirements.txt


---

## ⚙️ Installation

### 1️⃣ Clone the Repository
git clone https://github.com/Shivamshekharss/intelligent-recommendation-system-ml.git
cd intelligent-recommendation-system-ml

---

### 2️⃣ Create Virtual Environment
python -m venv venv
venv\Scripts\activate


---

### 3️⃣ Install Dependencies
pip install -r requirements.txt


---

## ▶️ Run the Project

### 🔹 Run Main System
cd recommendation
python main.py


---

### 🔹 Run Streamlit App
cd recommendation
streamlit run app.py


Then open:
http://localhost:8501


---

## 📊 Evaluation Results

| Model        | Precision@5 | Recall@5 |
|-------------|------------|----------|
| User-Based  | 0.342      | 0.116    |
| Item-Based  | 0.356      | 0.121    |

📌 Conclusion:  
Item-Based Collaborative Filtering performs better than User-Based on this dataset.

---

## 🧠 How It Works

1. Create user-item matrix  
2. Compute similarity (user & item)  
3. Agent selects best model  
4. Hybrid combines CF + popularity  
5. Generate recommendations  

---

## 🎯 Future Improvements

- Movie posters integration  
- Model comparison dashboard  
- Search-based recommendation  
- Cloud deployment  
- Deep learning-based models  

---

## 🛠️ Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Jupyter Notebook

---

## 👨‍💻 Author

Shivam Shekhar  
Final Year Project – Machine Learning

---

## ⭐ Support

If you like this project:

- Star ⭐ the repo  
- Fork 🍴 it  
- Share 📢  

---

## 📜 License

This project is for academic purposes only.

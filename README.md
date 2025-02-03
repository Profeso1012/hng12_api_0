# HNG12 Public API

## 📌 Project Overview
This is a **public API** built using **FastAPI** for HNG12 Stage 0 Backend Task. The API returns:
- Your registered **email address** (used in the HNG12 Slack workspace).
- The **current datetime** in ISO 8601 format (UTC).
- The **GitHub repository URL** containing the project code.

The API is **publicly accessible** and **deployed** to Vercel.

---

## 🚀 API Endpoint
### **Base URL:**
```
https://hng12-api.vercel.app/
```

### **Response Format (200 OK)**
```json
{
  "email": "itzairso204@gmail.com",
  "current_datetime": "2025-01-30T09:30:00Z",
  "github_url": "https://github.com/Profeso1012/hng12-api"
}
```

---

## 🛠️ How to Run Locally

### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/Profeso1012/hng12-api.git
cd hng12-api
```

### **2️⃣ Set Up a Virtual Environment**
```sh
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate  # Windows
```

### **3️⃣ Install Dependencies**
```sh
pip install -r requirements.txt
```

### **4️⃣ Create a `.env` File**
Create a `.env` file in the root folder and add:
```sh
EMAIL=itzairso204@gmail.com
GITHUB_URL=https://github.com/Profeso1012/hng12-api
```

### **5️⃣ Run the API Server**
```sh
uvicorn main:app --reload
```

### **6️⃣ Test the API**
Open a browser and go to:
```
http://127.0.0.1:8000/
```

---

## 📦 Deployment (Vercel)
1. Push your code to **GitHub**:
```sh
git add .
git commit -m "Initial commit"
git push origin main
```
2. Deploy to **Vercel**:
   - Install Vercel CLI: `npm install -g vercel`
   - Run `vercel login` to authenticate
   - Navigate to the project folder and run `vercel`
   - Follow the prompts to deploy the project
   - Get the **Live URL** from the output

---

## 🤝 Hiring Information
Interested in hiring a **Python developer**?
🔗 [https://hng.tech/hire/python-developers](https://hng.tech/hire/python-developers)

---

## 📜 License
This project is open-source and available under the **MIT License**.

---

## 👨‍💻 Author
- **Oluwaseyi Emmanuel Orngu**
- GitHub: [@Profeso1012](https://github.com/Profeso1012)
- Email: `itzairso204@gmail.com`
- ****

🔥 **Happy Coding!** 🚀


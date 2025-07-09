# 📚 Library Management System (KivyMD)

> A KivyMD-based modern UI library app to help readers find, borrow, and explore books. Powered by OTP login and machine learning recommendations.

## 🚀 Features
- 🔐 OTP Login (WhatsApp via pywhatkit)
- 📘 Check Book Availability, ISBN, and Shelf Location
- 🔁 Borrow / Return / Renew Books and Pay Late Fines
- 🧠 Book Recommendations using Scikit-learn + NLP
- 💡 Personalized Book Recommendations
- 📊 Track User Reading History
- 🎨 KivyMD UI with custom fonts & images
- 📦 Secure user profile handling

## 🛠️ Technologies Used
- Python
- Kivy
- KivyMD
- WhatsApp OTP (via `pywhatkit`)
- CSV for book/user data
- Custom `.kv` layout files

## 📁 Project Structure

📂Library-Management-System/

├── LMS.py

├── kv/

├── assets/

├── fonts/

├── data/Books.csv

├── requirements.txt

├── README.md

└── .gitignore

## 📸 App Screenshots

All screenshots are organized by flow. Below are visual previews of each feature in the app.

---

### 🔐 1. Sign In / Sign Up Flow
- ![Step 1.0](Screenshots/1.SignIn_Up_SS/Step_1.0.png)
- ![Step 2.0 (Login)](Screenshots/1.SignIn_Up_SS/Step_2.0(LOGIN).png)
- ![Step 2.0 (SignUp)](Screenshots/1.SignIn_Up_SS/Step_2.0(SignUp).png)

---

### 🏠 2. Home, Profile & Navigation
- ![Edit Profile](Screenshots/2.HOME_&Nav_Profile_SS/Edit_Profile_page.png)
- ![HOME Page](Screenshots/2.HOME_&Nav_Profile_SS/HOME.png)
- ![Navigation 1](Screenshots/2.HOME_&Nav_Profile_SS/Navigation_bar(1).png)
- ![Navigation 2](Screenshots/2.HOME_&Nav_Profile_SS/Navigation_bar(2).png)

---

### 📍 3. Book Location
- ![Book Location](Screenshots/3.Book_Location_SS/HomePage.png)

---

### 🔍 4. Search Feature
- ![Search Step 1](Screenshots/4.Search_Book_SS/Step_1.0.png)
- ![Search Step 1.1](Screenshots/4.Search_Book_SS/Step_1.1.png)
- ![Search Step 2.0](Screenshots/4.Search_Book_SS/Step_2.0.png)
- ![Search Step 2.1](Screenshots/4.Search_Book_SS/Step_2.1.png)

---

### 🤖 5. Book Recommendation
- ![Recommendation 1](Screenshots/5.Book_Recommendation_SS/Step_1.0.png)
- ![Recommendation 1.1](Screenshots/5.Book_Recommendation_SS/Step_1.1.png)
- ![Recommendation 2.0](Screenshots/5.Book_Recommendation_SS/Step_2.0.png)

---

### 📚 6. Borrow Book Flow
- ![Step 1.0](Screenshots/6.borrow_BOOK_SS/Step_1.0.png)
- ![Step 1.1](Screenshots/6.borrow_BOOK_SS/Step_1.1.png)
- ![Step 2.0](Screenshots/6.borrow_BOOK_SS/Step_2.0.png)
- ![Step 2.1](Screenshots/6.borrow_BOOK_SS/Step_2.1.png)
- ![Step 3.0](Screenshots/6.borrow_BOOK_SS/Step_3.0.png)
- ![Step 4.0](Screenshots/6.borrow_BOOK_SS/Step_4.0.png)
- ![Step 5.0](Screenshots/6.borrow_BOOK_SS/Step_5.0(Additional).png)
- ![Step 6.0](Screenshots/6.borrow_BOOK_SS/Step_6.0(Additional).png)

---

### ✅ 7. Return Books
- ![Return Step 1.0](Screenshots/7.Return_Book_SS/Step_1.0.png)
- ![Return Step 1.1](Screenshots/7.Return_Book_SS/Step_1.1.png)
- ![Return Step 2.0](Screenshots/7.Return_Book_SS/Step_2.0.png)

---

### ♻️ 8. Renew Books
- ![Renew Step 1.0](Screenshots/8.Renew_Book_SS/Step_1.0.png)
- ![Renew Step 1.1](Screenshots/8.Renew_Book_SS/Step_1.1.png)
- ![Renew Step 2.0](Screenshots/8.Renew_Book_SS/Step_2.0.png)

---

### 📈 9. Reading History
- ![History Step 1.0](Screenshots/9.Reading_History_SS/Step_1.0.png)
- ![History Step 1.1](Screenshots/9.Reading_History_SS/Step_1.1.png)
- ![History Step 2.0](Screenshots/9.Reading_History_SS/Step_2.0.png)

## ▶️ How to Run
```bash
pip install -r requirements.txt
python LMS.py

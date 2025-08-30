# 🚀 Selenium Form Auto‑Fill Demo

Automates filling and submitting a sample sign‑up form using **Selenium** and **Google Chrome**.

> Target page: [Secure Retreat Demo Form](https://secure-retreat-92358.herokuapp.com/)

---

## 📌 Features

* Opens Chrome browser automatically
* Fills out **First Name**, **Last Name**, and **Email** fields
* Submits the form programmatically
* Keeps browser open after script ends (thanks to `detach` option)

---

## 📂 Project Structure

```
selenium-form-fill/
├── main.py              # Python script to run the automation
├── requirements.txt     # Dependencies
└── .gitignore           # Ignore unnecessary files in Git
```

---

## ⚙️ Requirements

* Python **3.8+**
* Google Chrome (latest version)
* Selenium **4.6+** (includes Selenium Manager to auto‑manage ChromeDriver)

Install dependencies:

```bash
pip install -r requirements.txt
```

`requirements.txt`:

```
selenium>=4.12
```

---

## ▶️ How to Run

1. **Clone this repo**

```bash
git clone https://github.com/<your-username>/selenium-form-fill.git
cd selenium-form-fill
```

2. **(Optional) Create a virtual environment**

```bash
# Windows (PowerShell)
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# macOS/Linux
python3 -m venv .venv
source .venv/bin/activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Run the script**

```bash
python main.py
```

---

## 📝 Example Code (`main.py`)

```python
from selenium import webdriver
from selenium.webdriver.common.by import By

# Chrome options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Open browser
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://secure-retreat-92358.herokuapp.com/")

# Fill form
first_name = driver.find_element(By.NAME, "fName")
last_name = driver.find_element(By.NAME, "lName")
email_address = driver.find_element(By.NAME, "email")

first_name.send_keys("Sayan")
last_name.send_keys("Sanki")
email_address.send_keys("sayan@gmail.com")

# Submit
submit = driver.find_element(By.CSS_SELECTOR, "form button")
submit.click()
```

---

## ⚡ Enhancements

* Run in **headless mode** (no window):

  ```python
  chrome_options.add_argument("--headless=new")
  ```

* Use **WebDriverWait** to avoid timing issues:

  ```python
  from selenium.webdriver.support.ui import WebDriverWait
  from selenium.webdriver.support import expected_conditions as EC

  wait = WebDriverWait(driver, 10)
  first_name = wait.until(EC.presence_of_element_located((By.NAME, "fName")))
  ```

---

## 📂 .gitignore

```
# Python
__pycache__/
*.pyc
.venv/
venv/

# Editors / OS
.vscode/
.idea/
.DS_Store
```

---

## ❗ Troubleshooting

* **`NoSuchElementException`** → Add `WebDriverWait`.
* **Driver mismatch** → Use Selenium **4.6+** (auto‑driver management).
* **Browser not opening** → Ensure Chrome is installed and updated.

---

## 📜 License

This project is open‑sourced under the **MIT License**.

---

## 🙌 Acknowledgements

* Practice form hosted at [Heroku](https://secure-retreat-92358.herokuapp.com/) (for demo purposes only).

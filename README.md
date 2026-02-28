# Placement Portal Application (PPA)

A comprehensive web application for managing campus placements, built with **Flask (Backend)** and **Vue.js (Frontend)**. It supports Admin, Company, and Student roles with background job processing using **Celery & Redis**.

---

## 🛠️ Prerequisites

Before running the project, ensure you have the following installed:
1.  **Python 3.10+**
2.  **Node.js & npm** (LTS version recommended)
3.  **Redis** (Required for background tasks)

---

## 🚀 Step 1: Install & Start Redis

Redis is the message broker for background jobs (like sending emails and exporting CSVs).

1.  **Download Redis for Windows:**
    * Download the `.msi` installer from here: [Redis-x64-3.0.504.msi](https://github.com/microsoftarchive/redis/releases) (or any modern Windows port).
2.  **Install:** Run the installer and keep all defaults.
3.  **Verify it is running:**
    * Open PowerShell and type: `redis-cli ping`
    * If it replies `PONG`, Redis is ready.
    * *Note:* If the command isn't found, you may need to add the Redis installation folder to your System PATH or run the server manually.

---

## ⚙️ Step 2: Backend Setup (Flask)

1.  Open a terminal in the `backend` folder.
2.  Create and activate a virtual environment:
    ```powershell
    python -m venv venv
    .\venv\Scripts\activate
    ```
3.  Install dependencies:
    ```powershell
    pip install -r requirements.txt
    ```
4.  **Terminal 1: Start the API Server:**
    ```powershell
    python app.py
    ```
    *The server will run at `http://127.0.0.1:5000`.*

---

## 👷 Step 3: Background Workers (Celery)

You need **two separate terminals** for Celery to handle async tasks and scheduled reports.

1.  **Terminal 2: Start the Worker (Processes tasks):**
    * Navigate to `backend` folder and activate venv (`.\venv\Scripts\activate`).
    * Run:
        ```powershell
        celery -A celery_worker.celery_app worker --pool=solo --loglevel=info
        ```

2.  **Terminal 3: Start the Scheduler (Triggers monthly reports):**
    * Navigate to `backend` folder and activate venv.
    * Run:
        ```powershell
        celery -A celery_worker.celery_app beat --loglevel=info
        ```

---

## 💻 Step 4: Frontend Setup (Vue.js)

1.  Open **Terminal 4** and navigate to the `ppa_frontend` folder.
2.  Install dependencies (first time only):
    ```powershell
    npm install
    ```
3.  Start the development server:
    ```powershell
    npm run dev
    ```
    *The app will run at `http://localhost:5173`.*

---

## 🧪 End-to-End Testing Workflow

Follow this sequence to test all features:

### 1. Admin Login & Setup
* **Login:** Username `admin` / Password `change-me`.
* **Check:** View the Dashboard stats.
* **Reports:** Go to "Reports" tab. You can click **"Generate Report Now"** to test the Monthly HTML report generation. A "View" button will appear once generated.

### 2. Company Registration & Approval
* **Register:** Logout and Register a new user as **Company** (e.g., `google`, password `123`).
* **Block Check:** Try to login immediately. It will work, but if you try to "Create Drive", it will say "Company not approved".
* **Approve:** Login as **Admin**. You will see `google` in "Pending Companies". Click **Approve**.

### 3. Creating & Approving a Job Drive
* **Create:** Login as `google`. Click **Create New Drive**.
    * Job Title: "SDE 1", CGPA: 7.0.
* **Check:** The drive status will be "Pending".
* **Approve:** Login as **Admin**. Go to Dashboard. You will see "SDE 1" in "Pending Placement Drives". Click **Approve**.

### 4. Student Application (Eligibility Check)
* **Register:** Register a **Student** (e.g., `student1`).
* **Profile:** Go to Profile. **Upload a Resume (PDF)**.
* **Test Eligibility:** Set your CGPA to `6.0` (below the required 7.0). Go to Dashboard. The "SDE 1" drive should **NOT** appear.
* **Apply:** Set CGPA to `8.0`. The drive appears. Click **Apply**.

### 5. Selection & Offer Letter
* **Select:** Login as `google`. Go to Dashboard -> **Applicants**.
* **View Resume:** Click the "View Resume" button to download the PDF.
* **Shortlist:** Click "Shortlist", then "Select".
* **Offer Letter:** Once selected, click the yellow **"Offer Letter"** button to download the generated text file.

### 6. Export Data (Async Job)
* **Export:** Login as `student1`. Go to **My Applications**.
* **Trigger:** Click **"Export to CSV"**.
* **Result:** Wait 5-10 seconds. A download link for the CSV file will appear automatically (handled by Celery worker).

---

## 📂 Folder Structure
* `backend/`: Flask API, Database models, Celery tasks.
* `backend/uploads/`: Stores Resumes, Generated Reports, and CSV exports.
* `ppa_frontend/`: Vue.js source code.
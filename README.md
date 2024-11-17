
# Local Arbitrage Notification System

This project is a web-based arbitrage tool that integrates a **Node.js server** with a **Python script** to monitor market conditions and send notifications when specific criteria are met. The project also includes a basic frontend for user input.

---

## Features
1. **Market Monitoring**: Uses Selenium with undetected ChromeDriver to monitor market availability on a specified website.
2. **Notification System**: Sends email alerts when the desired market conditions are met.
3. **Web Interface**: A simple frontend to input email and website URLs.
4. **Backend Integration**: Node.js server interacts with the Python script to handle user requests.

---

## Project Structure

```
local-arbitrage/
├── WebScraper.py                 # Python script for market monitoring and email notifications
├── server.js                 # Node.js server for handling requests
├── public/
│   ├── stakeCalculator.html # Frontend for further stake calculations
│   ├── notificationsForm.html # Frontend for notifications setup
│   ├── index.html              # Frontend home page with stake calculator
├── package.json             # Node.js dependencies and metadata
└── README.md                # Documentation
```

---

## Prerequisites

### Python
- Python 3.8 or higher
- Pip package manager
- Google Chrome browser installed

### Node.js
- Node.js 14 or higher
- npm (Node Package Manager)

---

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/Yuzgin/local-arbitrage.git
cd local-arbitrage
```

### 2. Install Dependencies

#### Python
```bash
pip install -r requirements.txt
```

#### Node.js
```bash
npm install
```

---

## Usage

### Start the Node.js Server
```bash
node index.js
```
The server will run at `http://localhost:3000`.

### Access the Frontend
- Open a browser and navigate to `http://localhost:3000/stakeCalculator.html` or `http://localhost:3000/notificationsForm.html`.

### Run the Python Script
The Python script is triggered automatically by the Node.js backend when a user submits a form on the frontend. However, you can also run it manually:
```bash
python WebScraper.py <url> <smtp_server> <smtp_port> <sender_email> <sender_password> <recipient_email>
```

Example:
```bash
python WebScraper.py "http://example.com" "smtp.gmail.com" 587 "your-email@gmail.com" "your-password" "recipient@gmail.com"
```

---

## Environment Variables
To avoid hardcoding sensitive credentials, you can use environment variables or a `.env` file for:
- `SMTP_SERVER`
- `SMTP_PORT`
- `SENDER_EMAIL`
- `SENDER_PASSWORD`

For example, create a `.env` file:
```env
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
SENDER_EMAIL=your-email@gmail.com
SENDER_PASSWORD=your-password
```

Then modify the Python script to load these variables using `dotenv`.

---

## Frontend Functionality

1. **HomePage Calculator (`index.html`)**:
   - Calculate minimum odds required for arbitrage profit.
   - Results are displayed dynamically based on input.

2. **Notifications Setup (`notificationsForm.html`)**:
   - Users can enter an email and URL to be monitored.
   - Sends a POST request to the backend, which triggers the Python script.

3. **Stake Calculator ('stakeCalculator')**:
   - Calculates stake needed for £5 profit given the two arbitrage odds.
   - Displayed dynamically.

---

## Technologies Used

### Backend
- **Node.js** with Express: To handle HTTP requests.
- **Python** with Selenium: For browser automation and market monitoring.

### Frontend
- HTML, CSS, and JavaScript: For user interface.

---

## Limitations
1. **Email Credentials**: The current implementation requires plaintext credentials. Consider using environment variables or OAuth2 for secure email integration.
2. **Error Handling**: The project currently lacks robust error handling in both the backend and frontend.

---

## Future Improvements
- **Testing**: Add unit and integration tests for both Python and Node.js components.
- **Database Integration**: Save user inputs and results for persistence.
- **Enhanced UI**: Improve the frontend design and usability.

---

## Acknowledgements
- Selenium and undetected ChromeDriver for browser automation.
- Express for simplifying backend development.

---

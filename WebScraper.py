import sys
import undetected_chromedriver as uc
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import random
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(subject, body, to_email, smtp_server, smtp_port, sender_email, sender_password):
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = to_email
    message['Subject'] = subject
    message.attach(MIMEText(body, 'plain'))

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.send_message(message)

def check_shots_market(driver, url):

    # Navigate to the page
    driver.get(url)

    try:
        # Wait for the specific element to load
        shots_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//span[@class="tab__title" and contains(text(), "Shots")]'))
        )
        print("Shots market is available!")
        return True
    except:
        print("Shots market is not available yet.")
        return False

def main(url, smtp_server, smtp_port, sender_email, sender_password, *recipient_emails):
    # Create a new instance of the Chrome driver
    chrome_options = uc.ChromeOptions()
    driver = uc.Chrome(options=chrome_options)

    while True:
        if check_shots_market(driver, url):

            subject = 'Shots Market Available!'
            body = 'The shots market is now available. Check it out!'
            for recipient_email in recipient_emails:
                send_email(subject, body, recipient_email, smtp_server, smtp_port, sender_email, sender_password)

            break  # Exit the loop if the shots market is available

        wait_time = random.randint(120, 600)  # Wait for a random time from 4 -> 15 minutes
        time.sleep(wait_time)
        driver.refresh()  # Refresh the page

    driver.quit()

if __name__ == "__main__":
    # Extract command line arguments (URL, SMTP server info, recipient emails)
    url = sys.argv[1]
    smtp_server = sys.argv[2]
    smtp_port = int(sys.argv[3])  # Convert port to an integer
    sender_email = sys.argv[4]
    sender_password = sys.argv[5]
    recipient_email = sys.argv[6]

    main(url, smtp_server, smtp_port, sender_email, sender_password, recipient_email)
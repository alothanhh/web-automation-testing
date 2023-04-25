# Test script for the calendar import functionality

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from webdriver_manager.chrome import ChromeDriverManager

import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "..", "..", "utils"))
from rich_unittest import RichTestRunner


# Set up the driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(10)

# Open the page
LOGIN_URL = "https://sandbox.moodledemo.net/login/index.php"
FEATURE_URL = "https://sandbox.moodledemo.net/calendar/import.php"
USERNAME = "admin"
PASSWORD = "sandbox"

driver.get(LOGIN_URL)

# Log in
username = driver.find_element(By.ID, "username")
username.send_keys(USERNAME)

password = driver.find_element(By.ID, "password")
password.send_keys(PASSWORD)

login = driver.find_element(By.ID, "loginbtn")
login.click()


class TestCalendarImport(unittest.TestCase):

	def test_calendar_import(self):
		# Go to the calendar import page
		driver.get(FEATURE_URL)
		# Check that the page is correct
		self.assertTrue("Import calendar" in driver.page_source)

	def test_calendar_import_ical(self):
		# Go to the calendar import page
		driver.get(FEATURE_URL)
		# Check that the page is correct
		self.assertTrue("Import caledar" in driver.page_source)
		


		

if __name__ == "__main__":
	suite = unittest.TestLoader().loadTestsFromTestCase(TestCalendarImport)
	RichTestRunner().run(suite)
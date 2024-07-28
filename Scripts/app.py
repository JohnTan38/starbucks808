import os
from flask import (Flask, redirect, render_template, request,
                   send_from_directory, url_for)

from selenium import webdriver #login
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import Keys
from selenium.webdriver.support.ui import Select
#import pyautogui
import time

app = Flask(__name__)

@app.route('/')
def index():
   print('Request for index page received')
   return render_template('index.html')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/hello', methods=['POST'])
def hello():
    email = request.form.get('email')
    password = request.form.get('password')

    if email and password:
        print('Request for hello page received with email=%s' % email)
        print('Request for hello page received with password=%s' % password)
       
        driver = webdriver.Chrome()
        driver.get("https://az3.ondemand.esker.com/ondemand/webaccess/asf/home.aspx")
        driver.maximize_window()
        time.sleep(2)

        driver.find_element(By.XPATH, '//*[@id="ctl03_tbUser"]').send_keys(email)
        driver.find_element(By.XPATH, '//*[@id="ctl03_tbPassword"]').send_keys(password)
        driver.find_element(By.XPATH, '//*[@id="ctl03_btnSubmitLogin"]').click()
        time.sleep(2)
        return render_template('hello.html', email = email, password = password)
    else:
        print('Request for hello page received with no email or password -- redirecting')
        return redirect(url_for('index'))

if __name__ == '__main__':
   app.run(debug=True)

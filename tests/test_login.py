import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def setup_driver():
    driver = webdriver.Chrome()  
    driver.implicitly_wait(10)   
    return driver

def test_login_success():
    driver = setup_driver()
    try:
        driver.get("http://demo.testarena.pl/zaloguj/")
        
        driver.find_element(By.ID, "email").send_keys("administrator@testarena.pl")
        driver.find_element(By.ID, "password").send_keys("sumXQQ72$L")
        driver.find_element(By.ID, "login").click()
        
        WebDriverWait(driver, 10).until(EC.title_contains("Kokpit - TestArena Demo"))

        assert "Kokpit" in driver.title
    finally:
        driver.quit()

def test_login_failure():
    driver = setup_driver()
    try:
        driver.get("http://demo.testarena.pl/zaloguj/")
        
        driver.find_element(By.ID, "email").send_keys("administrator@testarena.pl")
        driver.find_element(By.ID, "password").send_keys("wrong_password")
        driver.find_element(By.ID, "login").click()
        
        error_message = driver.find_element(By.CLASS_NAME, "login_form_error").text
        assert "Adres e-mail i/lub hasło są niepoprawne." in error_message
    finally:
        driver.quit()





def test_add_new_task():
    driver = setup_driver()
    try:
        driver.get("http://demo.testarena.pl/zaloguj/")
        driver.find_element(By.ID, "email").send_keys("administrator@testarena.pl")
        driver.find_element(By.ID, "password").send_keys("sumXQQ72$L")
        driver.find_element(By.ID, "login").click()

        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "footer")))

        driver.get("http://demo.testarena.pl/DSP2/project_view")

        driver.find_element(By.XPATH, "//a[text()='Zadania']").click()

        WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a.button_link[href='http://demo.testarena.pl/DSP2/task_add']"))).click()

        WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, "title"))).send_keys("test2108111")
        driver.find_element(By.ID, "description").send_keys("zadanietest2108111")       

        environments_input = driver.find_element(By.ID, "environments")
        environments_input.clear()
        environments_input.send_keys("fsd")
        
        try:
            suggestion = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, ".autocomplete-suggestion"))
            )
            suggestion.click()
        except:
            print("Brak widocznych sugestii autouzupełniania lub problem z selektorem.")

        versions_input = driver.find_element(By.ID, "versions")
        versions_input.clear()
        versions_input.send_keys("1111")
        
        try:
            suggestion = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, ".autocomplete-suggestion"))
            )
            suggestion.click()
        except:
            print("Brak widocznych sugestii autouzupełniania dla wersji lub problem z selektorem.")

        due_date_element = driver.find_element(By.ID, "dueDate")
        due_date_element.clear() 
        due_date_element.send_keys("2024-02-09 23:59")

        assign_to_me_link = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.ID, "j_assignToMe"))
        )
        assign_to_me_link.click()

        save_button = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.ID, "save"))
        )
        save_button.click()

    finally:
        driver.quit()


import time
from selenium.webdriver.support.select import Select
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import  WebElement

def locator(driver:Chrome,by:By,identifier:str) -> WebElement:
    element = WebDriverWait(driver,15).until(EC.presence_of_element_located((by,identifier)))
    return element

def alert(driver: Chrome) -> [str]:
    # Driver config
    driver.get('http://the-internet.herokuapp.com/javascript_alerts')
    driver.maximize_window()

    # Define variables
    excepted_result = ['You successfully clicked an alert', 'You clicked: Ok',
                       'You entered: C++ is very powerful language.']

    scripts = ("jsAlert()", "jsConfirm()", "jsPrompt()")
    result = driver.find_element(By.ID, 'result')
    result_list = list()

    # Click and handle alerts
    for script in scripts:
        driver.execute_script(script)
        alert_var = driver.switch_to.alert
        if 'prompt' in alert_var.text:
            alert_var.send_keys("C++ is very powerful language.")
        alert_var.accept()
        result_list.append(result.text)
        time.sleep(2)
    # Return
    return result_list,excepted_result


def iframe(driver: Chrome) -> [str]:
    driver.get('http://automationpractice.com/index.php')
    driver.set_window_size(800, 800)
    wait = WebDriverWait(driver, 30)
    container = locator(driver,By.CLASS_NAME, 'product-container')
    container.find_element(By.CLASS_NAME, 'icon-eye-open').click()
    wait.until(EC.frame_to_be_available_and_switch_to_it((By.CLASS_NAME, 'fancybox-iframe')))
    time.sleep(5)
    add_to_card_btn = driver.find_element(By.ID, 'add_to_cart')
    add_to_card_btn.click()
    locator(driver,By.CSS_SELECTOR, '#layer_cart > div.clearfix > div.layer_cart_cart.col-xs-12.col-md-6 > div.button-container > a').click()
    locator(driver,By.CLASS_NAME,'cart_navigation').find_element(By.CLASS_NAME,'button').click()
    locator(driver,By.ID,'email').send_keys("exm1@walla.com")
    locator(driver,By.ID,'passwd').send_keys('12345')
    locator(driver,By.ID,'SubmitLogin').click()
    locator(driver,By.NAME,'processAddress').click()
    locator(driver,By.ID,'cgv').click()
    locator(driver,By.NAME,'processCarrier').click()
    locator(driver,By.ID,'HOOK_PAYMENT').find_element(By.CLASS_NAME,'bankwire').click()
    finish_btn = locator(driver,By.ID,'cart_navigation')
    finish_btn.find_element(By.CLASS_NAME,'button').click()
    excepted_result = ("Your order on My Store is complete","Order confirmation - My Store")
    actual_result = []
    text_label = locator(driver,By.XPATH,'//*[@id="center_column"]/div/p/strong')
    actual_result.append(text_label.text)
    actual_result.append(driver.title)

    return actual_result,excepted_result

def drag_drop(driver: Chrome) -> [str]:
    # Driver config
    driver.get('https://demo.guru99.com/test/drag_drop.html')
    driver.maximize_window()

    # Define variables
    block_button = locator(driver,By.CLASS_NAME, 'block13 ')
    table = locator(driver,By.ID, 'shoppingCart1')
    button_bank = locator(driver,By.ID, 'credit2')
    button_5000 = block_button.find_element(By.CLASS_NAME, 'button ')
    button_sales = locator(driver,By.ID, 'credit1')
    drop_off_2 = table.find_element(By.CLASS_NAME, 'ui-widget-content')
    drop_off_1 = locator(driver,By.ID, 'shoppingCart4')
    drop_off_3 = locator(driver,By.ID, 'shoppingCart3').find_element(By.ID, 'loan')
    drop_off_4 = locator(driver,By.ID, 'amt8')
    result_label = locator(driver,By.CLASS_NAME, 'table4_result')
    result_btn = result_label.find_element(By.CLASS_NAME, 'button')

    # Perform actions
    action = ActionChains(driver)
    action.drag_and_drop(button_5000, drop_off_1).perform()
    action.drag_and_drop(button_bank, drop_off_2).perform()
    action.drag_and_drop(button_5000, drop_off_4).perform()
    action.drag_and_drop(button_sales, drop_off_3).perform()
    result_btn.click()

    # Return validate
    validate_assert = (drop_off_1.text[7::], drop_off_2.text, drop_off_4.text, drop_off_3.text, result_btn.text)
    excepted_result = ("5000", "BANK", "5000", "SALES", "Perfect!")
    return validate_assert, excepted_result


def selection_register(driver: Chrome) -> [str]:
    # Driver config
    driver.get('https://demo.guru99.com/test/newtours/register.php')
    driver.maximize_window()
    # Define variables
    data = (('firstName',"dor"),('lastName',"cohen"),('phone',"0529990099"),('userName',"dorcohen111@walla.co.il")
            ,('address1',"grove street 11"),('city',"los santos"),('state',"san andreas"),('postalCode',"12210"),
            ('email',"dor1122"),('password',"12345"),('confirmPassword',"12345"))
    excepted_result =('Dear dor cohen','Thank you for registering','Your user name is dor1122.')


    # Perform actions
    selection_box = driver.find_element(By.NAME, 'country')
    select = Select(selection_box)
    select.select_by_value("ISRAEL")
    for field in data:
        confirm_pass = locator(driver,By.NAME, field[0])
        confirm_pass.send_keys(field[1])
    confirm_pass.send_keys(Keys.ENTER)
    time.sleep(1)
    # Return validate
    actual_result = locator(driver,By.XPATH,'/html/body/div[2]/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[3]/td').text
    return actual_result,excepted_result


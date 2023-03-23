import requests, time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from termcolor import cprint
import traceback

def clickOnXpath(driver, wait_time, str_path):
    WebDriverWait(driver, wait_time).until(EC.element_to_be_clickable((By.XPATH, str_path))).click()

def clickOnClassName(driver, wait_time, str_path):
    WebDriverWait(driver, wait_time).until(EC.element_to_be_clickable((By.CLASS_NAME, str_path))).click()

def clickOnID(driver, wait_time, str_path):
    WebDriverWait(driver, wait_time).until(EC.element_to_be_clickable((By.ID, str_path))).click()

def inputTextXpath(driver, wait_time, send_data, str_path):
    WebDriverWait(driver, wait_time).until(EC.element_to_be_clickable((By.XPATH, str_path))).send_keys(send_data)

def inputTextName(driver, wait_time, send_data, str_path):
    WebDriverWait(driver, wait_time).until(EC.element_to_be_clickable((By.NAME, str_path))).send_keys(send_data)

def inputTextClassName(driver, wait_time, send_data, str_path):
    WebDriverWait(driver, wait_time).until(EC.element_to_be_clickable((By.CLASS_NAME, str_path))).send_keys(send_data)

def inputTextByID(driver, wait_time, send_data, str_path):
    WebDriverWait(driver, wait_time).until(EC.element_to_be_clickable((By.ID, str_path))).send_keys(send_data)

def waitElementXpath(driver, wait_time, str_path):
    WebDriverWait(driver, wait_time).until(EC.presence_of_element_located((By.XPATH, str_path)))

def waitElementID(driver, wait_time, str_path):
    WebDriverWait(driver, wait_time).until(EC.presence_of_element_located((By.ID, str_path)))


def line_control(file_txt):
    # Удаление пустых строк
    with open(file_txt) as f1:
        lines = f1.readlines()
        non_empty_lines = (line for line in lines if not line.isspace())
        with open(file_txt, "w") as n_f1:
            n_f1.writelines(non_empty_lines)


def add_network(driver, networks, name_network):

    try:
        xpatch = '/html/body/div[1]/div/div[3]/div/div[2]/div[2]/div/div[2]/div/div[2]/div'

        driver.get('chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html#settings/networks/add-network')

        # name
        inputTextXpath(driver, 5, networks[name_network]['net_name'], f'{xpatch}[1]/label/input')

        # new_rpc
        inputTextXpath(driver, 5, networks[name_network]['rpc'], f'{xpatch}[2]/label/input')

        # chain
        inputTextXpath(driver, 5, networks[name_network]['chain_id'], f'{xpatch}[3]/label/input')

        # currency_symbol
        inputTextXpath(driver, 5, networks[name_network]['symbol'], f'{xpatch}[4]/label/input')

        # explorer_url
        inputTextXpath(driver, 5, networks[name_network]['explorer'], f'{xpatch}[5]/label/input')

        # save
        while True:
            try:
                time.sleep(.35)
                clickOnXpath(driver, 3, '/html/body/div[1]/div/div[3]/div/div[2]/div[2]/div/div[2]/div/div[3]/button[2]')
                break
            except:
                driver.find_element(By.XPATH, f'{xpatch}[5]/label/input').clear()
                time.sleep(.2)
                inputTextXpath(driver, 5, networks[name_network]['explorer'], f'{xpatch}[5]/label/input')
                time.sleep(.2)

        # ponyatno btn
        time.sleep(.2)
        clickOnXpath(driver, 5, '/html/body/div[2]/div/div/section/div[3]/button')
        time.sleep(.2)
    except:
        cprint(f'network < {name_network} > network not added', 'white')


def main(zero, ads_id, seed, password, networks):

    try:
        open_url = "http://local.adspower.net:50325/api/v1/browser/start?user_id=" + ads_id
        close_url = "http://local.adspower.net:50325/api/v1/browser/stop?user_id=" + ads_id

        try:
            # Отправка запроса на открытие профиля
            resp = requests.get(open_url).json()
        except requests.exceptions.ConnectionError:
            cprint(f'adspover is not running', 'white')
            exit(0)

        try:
            chrome_driver = resp["data"]["webdriver"]
            chrome_options = Options()
            chrome_options.add_experimental_option("debuggerAddress", resp["data"]["ws"]["selenium"])
            driver = webdriver.Chrome(service=Service(chrome_driver), options=chrome_options)
        except KeyError:
            cprint(f'{ads_id} = open error', 'red')
            driver.quit()
            requests.get(close_url)
            return
        url = 'chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html'
        driver.get(url)

        # ##################################Login MetaMask version 10.22.1##############################################
        driver.switch_to.window(driver.window_handles[0])
        clickOnXpath(driver, 12, '/html/body/div[1]/div/div[2]/div/div/div/button')
        clickOnXpath(driver, 5, '/html/body/div[1]/div/div[2]/div/div/div/div[5]/div[1]/footer/button[2]')
        clickOnXpath(driver, 5, '/html/body/div[1]/div/div[2]/div/div/div[2]/div/div[2]/div[1]/button')

        # Determining the length of a phrase
        split_seed = seed.split(' ')
        seed_length = len(split_seed)
        dropdown_select_path = '/html/body/div[1]/div/div[2]/div/div/div[2]/form/div[1]/div[2]/select'
        if seed_length == 15:
            clickOnXpath(driver, 5, dropdown_select_path)
            clickOnXpath(driver, 5, '/html/body/div[1]/div/div[2]/div/div/div[2]/form/div[1]/div[2]/select/option[2]')
        elif seed_length == 18:
            clickOnXpath(driver, 5, dropdown_select_path)
            clickOnXpath(driver, 5, '/html/body/div[1]/div/div[2]/div/div/div[2]/form/div[1]/div[2]/select/option[3]')
        elif seed_length == 21:
            clickOnXpath(driver, 5, dropdown_select_path)
            clickOnXpath(driver, 5, '/html/body/div[1]/div/div[2]/div/div/div[2]/form/div[1]/div[2]/select/option[4]')
        elif seed_length == 24:
            clickOnXpath(driver, 5, dropdown_select_path)
            clickOnXpath(driver, 5, '/html/body/div[1]/div/div[2]/div/div/div[2]/form/div[1]/div[2]/select/option[5]')

        # Filling in text phrase fields
        waitElementID(driver, 8, 'import-srp__srp-word-0')
        for i in range(seed_length):
            driver.find_element(By.ID, f'import-srp__srp-word-{i}').send_keys(split_seed[i])

        inputTextXpath(driver, 5, password, '/html/body/div[1]/div/div[2]/div/div/div[2]/form/div[2]/div[1]/div/input')
        inputTextXpath(driver, 5, password, '/html/body/div[1]/div/div[2]/div/div/div[2]/form/div[2]/div[2]/div/input')
        clickOnXpath(driver, 5, '/html/body/div[1]/div/div[2]/div/div/div[2]/form/div[3]/input')
        clickOnXpath(driver, 5, '/html/body/div[1]/div/div[2]/div/div/div[2]/form/button')
        clickOnXpath(driver, 7, '/html/body/div[1]/div/div[2]/div/div/button')
        # ##############################################################################################################

        # =================================== if you don't need to add a networks, comment everything below ============
        # wait_elem
        waitElementXpath(driver, 7, '//*[@class="currency-display-component__suffix"]')

        add_network(driver, networks, 'BSC')
        add_network(driver, networks, 'Polygon')
        add_network(driver, networks, 'Optimism')
        add_network(driver, networks, 'Arbitrum')
        # ==============================================================================================================

        driver.quit()
        requests.get(close_url)

        cprint(f'{zero + 1}. {ads_id} = done', 'green')

    except Exception as ex:
        # traceback.print_exc()
        cprint(f'{zero + 1}. {ads_id} = already done', 'yellow')
        driver.quit()
        requests.get(close_url)


if __name__ == '__main__':

    networks = {
        'Optimism': {
            'net_name': 'Optimism',
            'rpc': 'https://mainnet.optimism.io',
            'chain_id': 10,
            'symbol': 'ETH',
            'explorer': 'https://optimistic.etherscan.io/',
        },

        'Arbitrum': {
            'net_name': 'Arbitrum One',
            'rpc': 'https://arb1.arbitrum.io/rpc',
            'chain_id': 42161,
            'symbol': 'ETH',
            'explorer': 'https://arbiscan.io/',
        },

        'BSC': {
            'net_name': 'Smart Chain',
            'rpc': 'https://bsc-dataseed.binance.org/',
            'chain_id': 56,
            'symbol': 'BNB',
            'explorer': 'https://bscscan.com',
        },

        'Polygon': {
            'net_name': 'Polygon',
            'rpc': 'https://polygon-rpc.com',
            'chain_id': 137,
            'symbol': 'MATIC',
            'explorer': 'https://polygonscan.com/',
        },
    }

    line_control("id_users.txt")
    line_control("seeds.txt")

    with open("id_users.txt", "r") as f:
        id_users = [row.strip() for row in f]

    with open("seeds.txt", "r") as f:
        seeds = [row.strip() for row in f]

    zero = -1
    password = 'password123'  # password for metamask

    for ads_id in id_users:
        zero = zero + 1
        seed = seeds[zero]

        main(zero, ads_id, seed, password, networks)

# ======================================================================================================================
# Reworked by Desti
# ======================================================================================================================

import requests, time, sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import TimeoutException
from termcolor import cprint
import pyperclip
import platform
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


# Onboard Page
XPATH_ONBOARDING_IMPORT_WALLET = '//*[@data-testid="onboarding-import-wallet"]'
XPATH_ONBOARDING_NO_METRIC = '//*[@data-testid="metametrics-no-thanks"]'
XPATH_CONFIRM_MNEMONIC = '//*[@data-testid="import-srp-confirm"]'
XPATH_INPUT_PASS = '//*[@data-testid="create-password-new"]'
XPATH_INPUT_PASS_CNFRM = '//*[@data-testid="create-password-confirm"]'
XPATH_INPUT_TERMS = '//*[@data-testid="create-password-terms"]'
XPATH_CREATE_NEW_WALLET = '//*[@data-testid="create-password-import"]'
XPATH_ONBOARDING_DONE = '//*[@data-testid="onboarding-complete-done"]'
XPATH_PIN_EXT_NEXT = '//*[@data-testid="pin-extension-next"]'
XPATH_PIN_EXT_DONE = '//*[@data-testid="pin-extension-done"]'
XPATH_ETH_DISPLAYED = '//*[@data-testid="eth-overview__primary-currency"]'

# Forgot Pass Page
XPATH_FORGOT_PASS = '//*[@class="button btn-link unlock-page__link"]'
XPATH_SUBMIT_BTN = '//*[@class="button btn--rounded btn-primary create-new-vault__submit-button"]'
XPATH_PONYATNO_BTN = '//*[@class="button btn--rounded btn-primary"]'

# Unlock
XPATH_INPUT_UNLOCK_PASS = '//*[@data-testid="unlock-password"]'
XPATH_UNLOCK = '//*[@data-testid="unlock-submit"]'

XPATH_INPUTS_MNEMONIC = '//*[@class="MuiInputBase-input MuiInput-input"]'
XPATH_POPOVER_CLOSE = '//*[@data-testid="popover-close"]'


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

    'Zksync Era': {
        'net_name': 'zkSync Era Mainnet',
        'rpc': 'https://mainnet.era.zksync.io',
        'chain_id': 324,
        'symbol': 'ETH',
        'explorer': 'https://explorer.zksync.io/',
    },

    'Arbitrum Nova': {
        'net_name': 'Arbitrum Nova',
        'rpc': 'https://nova.arbitrum.io/rpc',
        'chain_id': 42170,
        'symbol': 'ETH',
        'explorer': 'https://nova-explorer.arbitrum.io',
    },

    'Avalanche': {
        'net_name': 'Avalanche Network C-Chain',
        'rpc': 'https://api.avax.network/ext/bc/C/rpc',
        # 'rpc': 'https://avalanche-mainnet.infura.io',
        'chain_id': 43114,
        'symbol': 'AVAX',
        'explorer': 'https://snowtrace.io/',
    },

    'Gnosis Chain': {
        'net_name': 'Gnosis Chain',
        'rpc': 'https://rpc.gnosischain.com',
        'chain_id': 100,
        'symbol': 'xDai',
        'explorer': 'https://blockscout.com/xdai/mainnet/',
    },

    'Fantom': {
        'net_name': 'Fantom',
        'rpc': 'https://rpc.ftm.tools/',
        'chain_id': 250,
        'symbol': 'FTM',
        'explorer': 'https://ftmscan.com/',
    },

    'Aurora': {
        'net_name': 'Aurora Mainnet',
        'rpc': 'https://mainnet.aurora.dev',
        # 'rpc': 'https://aurora-mainnet.infura.io',
        'chain_id': 1313161554,
        'symbol': 'ETH',
        'explorer': 'https://explorer.aurora.dev/',
    }
}


def line_control(file_txt):
    # Удаление пустых строк
    with open(file_txt) as f1:
        lines = f1.readlines()
        non_empty_lines = (line for line in lines if not line.isspace())
        with open(file_txt, "w") as n_f1:
            n_f1.writelines(non_empty_lines)


def add_network(driver, name_network):

    try:
        xpatch = '/html/body/div[1]/div/div[3]/div/div[2]/div[2]/div/div[2]/div/div[2]/div'

        driver.get('chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html#settings/networks/add-network')
        inputTextXpath(driver, 5, networks[name_network]['net_name'], f'{xpatch}[1]/label/input')  # name
        inputTextXpath(driver, 5, networks[name_network]['rpc'], f'{xpatch}[2]/label/input')       # new_rpc
        inputTextXpath(driver, 5, networks[name_network]['chain_id'], f'{xpatch}[3]/label/input')  # chain
        inputTextXpath(driver, 5, networks[name_network]['symbol'], f'{xpatch}[4]/label/input')    # currency_symbol
        inputTextXpath(driver, 5, networks[name_network]['explorer'], f'{xpatch}[5]/label/input')  # explorer_url
        # save
        q = 0
        while True:
            try:
                time.sleep(.5)
                clickOnXpath(driver, 3, XPATH_PONYATNO_BTN)  # Save button
                break
            except:
                time.sleep(.5)
                driver.find_element(By.XPATH, f'{xpatch}[5]/label/input').clear()
                time.sleep(.5)
                inputTextXpath(driver, 5, networks[name_network]['explorer'], f'{xpatch}[5]/label/input')
                time.sleep(.5)
                q += 1
                if q >= 6:
                    raise
        try:
            time.sleep(.8)
            waitElementXpath(driver, 3, XPATH_POPOVER_CLOSE)  # krestik btn
            time.sleep(.8)
            clickOnXpath(driver, 3, XPATH_POPOVER_CLOSE)    # krestik btn click
            time.sleep(.5)
        except Exception:
            pass
    except Exception:
        cprint(f'network < {name_network} > network not added', 'white')


def fill_seed(driver, seed):
    # Filling in text phrase fields
    waitElementID(driver, 8, 'import-srp__srp-word-0')
    driver.find_element(By.XPATH, XPATH_INPUTS_MNEMONIC).click()

    # Определение ОС пользователя
    if platform.system() == 'Darwin':
        # Mac operating system
        pyperclip.copy(seed)
        ActionChains(driver).key_down(u'\ue03d').send_keys('v').key_up(u'\ue03d').perform()
    else:
        # Other operating systems
        pyperclip.copy(seed)
        ActionChains(driver).key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()


def onboard_page(driver, seed, password):
    # ##################################Login MetaMask version 10.26.2##################################################
    clickOnXpath(driver, 12, XPATH_ONBOARDING_IMPORT_WALLET)        # Import exist wallet
    clickOnXpath(driver, 5, XPATH_ONBOARDING_NO_METRIC)             # No metric button
    fill_seed(driver, seed)                                         # Input seed phrase
    clickOnXpath(driver, 5, XPATH_CONFIRM_MNEMONIC)                 # Confirm a seed phrase
    inputTextXpath(driver, 5, password, XPATH_INPUT_PASS)
    inputTextXpath(driver, 5, password, XPATH_INPUT_PASS_CNFRM)
    clickOnXpath(driver, 5, XPATH_INPUT_TERMS)                      # Terms checkbox
    clickOnXpath(driver, 5, XPATH_CREATE_NEW_WALLET)                # Import wallet btn

    svg_spinner = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "lds-spinner")))
    WebDriverWait(driver, 30).until(
        EC.invisibility_of_element_located(svg_spinner))            # Waiting for svg_spinner to disappear

    clickOnXpath(driver, 30, XPATH_ONBOARDING_DONE)                 # Got it button
    clickOnXpath(driver, 30, XPATH_PIN_EXT_NEXT)                    # Next button
    clickOnXpath(driver, 7, XPATH_PIN_EXT_DONE)                     # Done button

    # =================================== if you don't need to add a networks, comment everything below ================
    waitElementXpath(driver, 7, XPATH_ETH_DISPLAYED)                # wait_elem ETH display

    add_network(driver, 'BSC')
    add_network(driver, 'Polygon')
    add_network(driver, 'Optimism')
    add_network(driver, 'Arbitrum')
    add_network(driver, 'Zksync Era')
    add_network(driver, 'Arbitrum Nova')
    add_network(driver, 'Avalanche')
    add_network(driver, 'Gnosis Chain')
    add_network(driver, 'Fantom')
    add_network(driver, 'Aurora')
    # ==================================================================================================================
    # ##################################################################################################################


def forgot_password_page(driver, seed, password):
    # ##################################Forgot Pass MetaMask version 10.26.2############################################
    clickOnXpath(driver, 7, XPATH_FORGOT_PASS)              # Forgot Pass Btn
    fill_seed(driver, seed)                                 # Fills in the seed phrase and password fields
    inputTextByID(driver, 5, password, 'password')
    inputTextByID(driver, 5, password, 'confirm-password')
    clickOnXpath(driver, 7, XPATH_SUBMIT_BTN)               # Recover button
    try:
        clickOnXpath(driver, 2.5, XPATH_PONYATNO_BTN)       # Got it button
        time.sleep(.5)
    except Exception:
        pass

    # ##################################################################################################################


def mode_selector(driver):
    try:
        waitElementXpath(driver, 3, XPATH_ONBOARDING_IMPORT_WALLET)
        return True
    except Exception:
        return False


def main(zero, ads_id, seed, password, unlock_mode):
    try:
        args1 = ["--disable-popup-blocking", "--window-position=700,0"]
        args1 = str(args1).replace("'", '"')

        open_url = f"http://local.adspower.net:50325/api/v1/browser/start?user_id=" + ads_id + f"&launch_args={str(args1)}"
        close_url = "http://local.adspower.net:50325/api/v1/browser/stop?user_id=" + ads_id

        try:
            # Отправка запроса на открытие профиля
            resp = requests.get(open_url).json()
            time.sleep(.5)
        except requests.exceptions.ConnectionError:
            cprint(f'Adspower is not running.', 'red')
            sys.exit(0)
        except requests.exceptions.JSONDecodeError:
            cprint(f'Проверьте ваше подключение. Отключите VPN/Proxy используемые напрямую.', 'red')
            sys.exit(0)

        while True:
            try:
                chrome_driver = resp["data"]["webdriver"]
                chrome_options = Options()
                chrome_options.add_experimental_option("debuggerAddress", resp["data"]["ws"]["selenium"])
                driver = webdriver.Chrome(service=Service(chrome_driver), options=chrome_options)
                break
            except KeyError:
                # Перезапуск профиля для попытки устраниения ошибки открытия
                try:
                    requests.get(open_url).json()
                    time.sleep(3)
                    requests.get(close_url).json()
                except Exception:
                    cprint(f'{ads_id} - profile opening error', 'red')
                    break
            except Exception:
                cprint(f'{ads_id} - profile opening error', 'red')
                driver.quit()
                requests.get(close_url)
                break

        url = 'chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html'

        time.sleep(2)
        driver.switch_to.new_window()
        time.sleep(.3)
        driver.get(url)
        time.sleep(.3)
        driver.refresh()
        time.sleep(.9)

        # ==============================================================================================================
        # Выбор режима
        mode_bool = mode_selector(driver)
        if mode_bool is True:
            onboard_page(driver, seed, password)
        elif mode_bool is False:
            if unlock_mode == 0:
                forgot_password_page(driver, seed, password)
            elif unlock_mode == 1:
                inputTextXpath(driver, 5, password, XPATH_INPUT_UNLOCK_PASS)
                clickOnXpath(driver, 5, XPATH_UNLOCK)
        # ==============================================================================================================

        if unlock_mode == 0:
            driver.quit()
            requests.get(close_url)

        cprint(f'{zero + 1}. {ads_id} - done', 'green')

    except TimeoutException as ex1:
        # traceback.print_exc()
        time.sleep(.3)
        cprint(f'Profile < {ads_id} >  has TimeOut Error. Please contact the developer.', 'red')
        driver.quit()
        requests.get(close_url)

    except WebDriverException as ex:
        if 'LavaMoat' in str(ex):
            cprint(f'Profile < {ads_id} >  has LavaMoat Error. Please use fix scripts.', 'red')
        else:
            traceback.print_exc()
            time.sleep(.3)
            cprint(f'WebDriverException Error. Please contact the developer.', 'red')
        driver.quit()
        requests.get(close_url)

    except Exception as ex:
        traceback.print_exc()
        time.sleep(.3)
        cprint(f'{zero + 1}. {ads_id} = already done', 'yellow')
        driver.quit()
        requests.get(close_url)


if __name__ == '__main__':

    line_control("id_users.txt")
    line_control("seeds.txt")

    with open("id_users.txt", "r") as f:
        id_users = [row.strip() for row in f]

    with open("seeds.txt", "r") as f:
        seeds = [row.strip() for row in f]

    # ===========================================Settings===============================================================
    # Change the metamask password here
    password = 'password123'

    # 0 - The unlock mode is disabled. If you need to replace some metamask wallets in your profiles.
    # 1 - Enters the metamask wallet, using the password from the password variable.
    # The variable in unlock mode - 1 is designed to prepare profiles for operation, in this value the profiles
    # will NOT be closed automatically!
    unlock_mode = 0
    # ==================================================================================================================

    for i, ads_id in enumerate(id_users):
        try:
            if unlock_mode == 1:
                seeds.append('blank')
            main(i, ads_id, seeds[i], password, unlock_mode)
        except IndexError as ex:
            cprint(f'\nCheck the correspondence of the number of seed phrases with '
                   f'the number of profiles in the files id_users.txt and seeds.txt', 'red')
            sys.exit(0)
        except Exception as ex:
            cprint(str(ex), 'red')


# ======================================================================================================================
# Reworked by Desti
# ======================================================================================================================

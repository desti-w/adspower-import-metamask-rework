import time
from termcolor import cprint
import traceback


def runtime_lavamoat_editor(path):
    with open(path, 'r', encoding="utf-8") as read:
        lines = read.readlines()

    # Изменяет переменную scuttleGlobalThis на значение false
    with open(path, 'w', encoding="utf-8") as read:
        for line in lines:
            if line.startswith('    } = {"scuttleGlobalThis":true,"scuttleGlobalThisExceptions":["toString","getComputedStyle","addEventListener","removeEventListener","ShadowRoot","HTMLElement","Element","pageXOffset","pageYOffset","visualViewport","Reflect","Set","Object","navigator","harden","console","location","/cdc_[a-zA-Z0-9]+_[a-zA-Z]+/iu","performance","parseFloat","innerWidth","innerHeight","Symbol","Math","DOMRect","Number","Array","crypto","Function","Uint8Array","String","Promise","__SENTRY__","appState","extra","stateHooks","sentryHooks","sentry"]}'):
                line = '    } = {"scuttleGlobalThis":false,"scuttleGlobalThisExceptions":["toString","getComputedStyle","addEventListener","removeEventListener","ShadowRoot","HTMLElement","Element","pageXOffset","pageYOffset","visualViewport","Reflect","Set","Object","navigator","harden","console","location","/cdc_[a-zA-Z0-9]+_[a-zA-Z]+/iu","performance","parseFloat","innerWidth","innerHeight","Symbol","Math","DOMRect","Number","Array","crypto","Function","Uint8Array","String","Promise","__SENTRY__","appState","extra","stateHooks","sentryHooks","sentry"]}'
            read.write(line)


if __name__ == '__main__':

    # Change this path according to the instructions====================================================================
    """
    For Windows add path from setting without slash at the end. The path should be something like this:
    path_from_ads_settings = r"C:\.ADSPOWER_GLOBAL" 
    Depending on the location of the folder on your disk.

    For macOS add path from setting without slash at the end. The path should be something like this:
    path_from_ads_settings = r"/Users/YOUR_NICKNAME/Library/Application Support/adspower_global/cwd_global/source" 
    Depending on the location of the folder on your disk and your nickname.
    """

    path_from_ads_settings = r"C:\.ADSPOWER_GLOBAL"  # Add path WITHOUT SLASH AT THE END (ДОБАВИТЬ БЕЗ СЛЭША НА КОНЦЕ)
    # ==================================================================================================================

    try:
        path_to_js = fr'{path_from_ads_settings}/extension/19657/3f78540a9170bc1d87c525f061d1dd0f/10.26.2_0/runtime-lavamoat.js'
        runtime_lavamoat_editor(path_to_js)
        cprint(f'Фикс применен/fix applied', 'green')

    except FileNotFoundError:
        cprint(f'Файл не найден. Проверьте путь/наличие файла или обратитесь к разработчику.', 'red')

    except Exception as ex:
        traceback.print_exc()
        time.sleep(.3)
        cprint(f'Unexpected error. Обратитесь к разработчику.', 'red')

# ======================================================================================================================
# Created by Desti
# ======================================================================================================================

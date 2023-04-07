import time
from termcolor import cprint
import platform
import traceback


def line_control(file_txt):
    # Удаление пустых строк
    with open(file_txt) as f1:
        lines = f1.readlines()
        non_empty_lines = (line for line in lines if not line.isspace())
        with open(file_txt, "w") as n_f1:
            n_f1.writelines(non_empty_lines)


def get_profile_cache_path(ads_id, user_ID, path_from_ads_settings):

    user_ID = '_' + user_ID.split('_')[1]
    path = fr'{path_from_ads_settings}/cache/{ads_id}{user_ID}/extensionCenter/3f78540a9170bc1d87c525f061d1dd0f/10.26.2_0/runtime-lavamoat.js'
    return path


def runtime_lavamoat_cache_editor(path):

    with open(path, 'r') as read:
        lines = read.readlines()

    key_edt = False
    # Изменяет переменную scuttleGlobalThis на значение false
    with open(path, 'w') as read:
        for line in lines:
            if line.startswith('    } = {"scuttleGlobalThis":true,"scuttleGlobalThisExceptions":["toString","getComputedStyle","addEventListener","removeEventListener","ShadowRoot","HTMLElement","Element","pageXOffset","pageYOffset","visualViewport","Reflect","Set","Object","navigator","harden","console","location","/cdc_[a-zA-Z0-9]+_[a-zA-Z]+/iu","performance","parseFloat","innerWidth","innerHeight","Symbol","Math","DOMRect","Number","Array","crypto","Function","Uint8Array","String","Promise","__SENTRY__","appState","extra","stateHooks","sentryHooks","sentry"]}'):
                line = '    } = {"scuttleGlobalThis":false,"scuttleGlobalThisExceptions":["toString","getComputedStyle","addEventListener","removeEventListener","ShadowRoot","HTMLElement","Element","pageXOffset","pageYOffset","visualViewport","Reflect","Set","Object","navigator","harden","console","location","/cdc_[a-zA-Z0-9]+_[a-zA-Z]+/iu","performance","parseFloat","innerWidth","innerHeight","Symbol","Math","DOMRect","Number","Array","crypto","Function","Uint8Array","String","Promise","__SENTRY__","appState","extra","stateHooks","sentryHooks","sentry"]}'
                key_edt = True
            read.write(line)

    return key_edt


if __name__ == '__main__':

    # Change this path according to the instructions====================================================================
    user_ID = 'user_he3t5p'

    '''
    For Windows add path from setting without slash at the end. The path should be something like this:
    path_from_ads_settings = r"C:\.ADSPOWER_GLOBAL" 
    Depending on the location of the folder on your disk.
    
    For macOS add path from setting without slash at the end. The path should be something like this:
    path_from_ads_settings = r"/Users/YOUR_NICKNAME/Library/Application Support/adspower_global/cwd_global/source" 
    Depending on the location of the folder on your disk and your nickname.
    '''

    path_from_ads_settings = r"C:\.ADSPOWER_GLOBAL"  # Add path WITHOUT SLASH AT THE END (ДОБАВИТЬ БЕЗ СЛЭША НА КОНЦЕ)
    # ==================================================================================================================

    line_control("id_users.txt")
    with open("id_users.txt", "r") as f:
        id_users = [row.strip() for row in f]

    i = 0
    for ads_id in id_users:
        i += 1

        try:
            path = get_profile_cache_path(ads_id, user_ID, path_from_ads_settings)
            key_edt = runtime_lavamoat_cache_editor(path)
            if key_edt is True:
                cprint(f'{i}. < {ads_id} >  fixed', 'green')
            elif key_edt is False:
                cprint(f'{i}. < {ads_id} >  already fixed', 'White')

        except FileNotFoundError:
            # traceback.print_exc()
            # time.sleep(.3)
            cprint(f'{i}. < {ads_id} >  Не найден файл runtime-lavamoat.js', 'red')

        except Exception as ex:
            traceback.print_exc()
            time.sleep(.3)
            cprint(f'Unexpected error. Обратитесь к разработчику.', 'red')

# ======================================================================================================================
# Created by Desti
# ======================================================================================================================

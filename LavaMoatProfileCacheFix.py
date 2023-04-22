import time, os, sys
from termcolor import cprint
import glob
import traceback
import os
import string
import platform
import getpass


def line_control(file_txt):
    # Удаление пустых строк
    with open(file_txt) as f1:
        lines = f1.readlines()
        non_empty_lines = (line for line in lines if not line.isspace())
        with open(file_txt, "w") as n_f1:
            n_f1.writelines(non_empty_lines)


def path_to_ads_folder():
    # Определение ОС пользователя
    if platform.system() == 'Darwin':
        # Mac operating system
        folder_name = "adspower_global/cwd_global/source"
        username = getpass.getuser()
        path = os.path.join("/Users/", username + "/Library/Application Support/", folder_name)
        if os.path.exists(path):
            return path

    else:
        # Other operating systems (Windows)
        drives = [drive for drive in string.ascii_uppercase if os.path.exists(drive + ":")]
        folder_name = ".ADSPOWER_GLOBAL"
        for drive in drives:
            path = drive + ":" + "\\" + folder_name
            if os.path.exists(os.path.join(path)):
                return path


def cache_folder_exist():
    path_to_cache = path_from_ads_settings + r"/cache"
    if os.path.exists(path_to_cache):
        return
    else:
        return 0


def get_profile_cache_path(ads_id, path_from_ads_settings):
    folder_path = glob.glob(fr"{path_from_ads_settings}/cache/{ads_id}*")

    if folder_path:
        path_to_profile = folder_path[0].replace("\\", "/")
        path = fr'{path_to_profile}/extensionCenter/3f78540a9170bc1d87c525f061d1dd0f/10.26.2_0/runtime-lavamoat.js'
    else:
        return 0
    return path


def runtime_lavamoat_cache_editor(path):

    with open(path, 'r', encoding="utf-8") as read:
        lines = read.readlines()

    key_edt = False
    # Изменяет переменную scuttleGlobalThis на значение false
    with open(path, 'w', encoding="utf-8") as read:
        for line in lines:
            if line.startswith('    } = {"scuttleGlobalThis":true,"scuttleGlobalThisExceptions":["toString","getComputedStyle","addEventListener","removeEventListener","ShadowRoot","HTMLElement","Element","pageXOffset","pageYOffset","visualViewport","Reflect","Set","Object","navigator","harden","console","location","/cdc_[a-zA-Z0-9]+_[a-zA-Z]+/iu","performance","parseFloat","innerWidth","innerHeight","Symbol","Math","DOMRect","Number","Array","crypto","Function","Uint8Array","String","Promise","__SENTRY__","appState","extra","stateHooks","sentryHooks","sentry"]}'):
                line = '    } = {"scuttleGlobalThis":false,"scuttleGlobalThisExceptions":["toString","getComputedStyle","addEventListener","removeEventListener","ShadowRoot","HTMLElement","Element","pageXOffset","pageYOffset","visualViewport","Reflect","Set","Object","navigator","harden","console","location","/cdc_[a-zA-Z0-9]+_[a-zA-Z]+/iu","performance","parseFloat","innerWidth","innerHeight","Symbol","Math","DOMRect","Number","Array","crypto","Function","Uint8Array","String","Promise","__SENTRY__","appState","extra","stateHooks","sentryHooks","sentry"]}'
                key_edt = True
            read.write(line)

    return key_edt


if __name__ == '__main__':

    path_from_ads_settings = path_to_ads_folder()
    if path_from_ads_settings is None:
        cprint(f'Adspower не установлен/Не найден путь. Обратитесь к разрабочику', 'red')
        sys.exit(0)
    if cache_folder_exist() == 0:
        cprint(f'Папка /Cache/ не была обнаружена. Обратитесь к разрабочику', 'red')
        sys.exit(0)

    line_control("id_users.txt")
    with open("id_users.txt", "r") as f:
        id_users = [row.strip() for row in f]

    i = 0
    for ads_id in id_users:
        i += 1

        try:
            path = get_profile_cache_path(ads_id, path_from_ads_settings)
            if path == 0:
                cprint(f'{i}. < {ads_id} >  cache not found or wrong id', 'yellow')
                continue
            key_edt = runtime_lavamoat_cache_editor(path)
            if key_edt is True:
                cprint(f'{i}. < {ads_id} >  fixed', 'green')
            elif key_edt is False:
                cprint(f'{i}. < {ads_id} >  already fixed', 'green')

        except FileNotFoundError:
            # traceback.print_exc()
            # time.sleep(.3)
            cprint(f'{i}. < {ads_id} >  runtime-lavamoat.js not found', 'red')

        except Exception as ex:
            traceback.print_exc()
            time.sleep(.3)
            cprint(f'{i}. < {ads_id} >  Unexpected error. Обратитесь к разработчику.', 'red')

# ======================================================================================================================
# Created by Desti
# ======================================================================================================================

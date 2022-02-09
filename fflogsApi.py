import requests
import json


def retrieve(name, server, fight, partition):
    # {73: 9, 74: 10, 75: 11, 76: p1, 77: p2}

    url = "https://www.fflogs.com/api/v2/client"

    payload = '{"query":"query{characterData{character' + f'(name: \\\"{name}\\\", serverSlug: \\\"{server}\\\", serverRegion: \\\"NA\\\") ' + '{encounterRankings' + f'(difficulty:101, encounterID:{fight}, partition:{partition})' + '}}}"}'
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiI5NDA3NTgwZC1jNTNlLTRjZWQtOTRmMi03ZWRhNmQ4ZGM5Y2QiLCJqdGkiOiI5MWM2YmYzNDY4ZGFlZTQ5NDYwZGI5NzczYzY0NTVmNGU0OWEzNjhiY2Q3ZWVjZTUxMWNmMjgxZmVkNGQ0YWM1Y2MxOTAzMjEzYWViOTE1YSIsImlhdCI6MTYyNzU5MjkwMywibmJmIjoxNjI3NTkyOTAzLCJleHAiOjE2Mzc5NjA5MDMsInN1YiI6IjMxNDMwNSIsInNjb3BlcyI6WyJ2aWV3LXVzZXItcHJvZmlsZSIsInZpZXctcHJpdmF0ZS1yZXBvcnRzIl19.TWJ6nPvW_fQ-ivwEJ5gX0I7mDitlvV691OiWjT276NGblUoN013Fe-lGjCEQDnGJq26HKwmqnYyIUuSXKBgVorcsdlQLjXx_SZzouLAW-rucaMli3Mv0yUnD3ui4jQ_LZxSobihm51CnRw0Ha4BhQElLzAFrjiQo7YPv1UQF5skKeyJUz5WRmpYJBPb8IO-Ud2k1ZeBQwbF-QI_nN8hFMHj-KmCxc38ipj4A89aJLC6nD_Lq8vpALaN-54Tqtr3SGrHs2Zx2vIjsHyD89Daso1BlMjFSdoylX7ZoXpIqq4sR8ZuZHXZjEYiMh5h1xLlg1LTYUm8fBgy_WyI3jzQ9aGFyMuBdyanpofMV-jSFDuljpFhDFD0whznWYlU_TWBjAtTscASfzpV6Nt27Mqtzjt7NZTp11YEN7Y5jc1PnIc81LGDRw8LzH6WzN_6MVyCSix5dr4LNSf8b4NRXBI2C_OIZh1gWnuv5J21wUwEqo7Kr2aYH_UMvxq1M0J5tuahoTZPHw8umB9A3CvIJ1vFE6F4kOgiaabVGlEuDRDTpjZGhQQzQjtfrSRFaOa37vP9C_mtxB8fuWUfQc5NECmWse-KDOsVrTqqlgO9OLmkYcRpBviI-JguO-evVxzEz7PRb0w6CB4bqtM5MEV2trAZOUwlYRHcUg55Ejq4Sj_ksfR4"
    }

    try:
        response = requests.request("POST", url, data=payload, headers=headers)
        d = response.json()  # convert to json, export?
        print(d)
        print(d['data']['characterData']['character']['encounterRankings']['ranks'][0]['bestSpec'])
    except TypeError:
        print('Invalid name or world')


def validate(name, server):
    url = "https://www.fflogs.com/api/v2/client"

    payload = '{"query":"query{characterData{character' + f'(name: \\\"{name}\\\", serverSlug: \\\"{server}\\\", serverRegion: \\\"NA\\\") ' + '{lodestoneID}}}"}'
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiI5NDA3NTgwZC1jNTNlLTRjZWQtOTRmMi03ZWRhNmQ4ZGM5Y2QiLCJqdGkiOiI5MWM2YmYzNDY4ZGFlZTQ5NDYwZGI5NzczYzY0NTVmNGU0OWEzNjhiY2Q3ZWVjZTUxMWNmMjgxZmVkNGQ0YWM1Y2MxOTAzMjEzYWViOTE1YSIsImlhdCI6MTYyNzU5MjkwMywibmJmIjoxNjI3NTkyOTAzLCJleHAiOjE2Mzc5NjA5MDMsInN1YiI6IjMxNDMwNSIsInNjb3BlcyI6WyJ2aWV3LXVzZXItcHJvZmlsZSIsInZpZXctcHJpdmF0ZS1yZXBvcnRzIl19.TWJ6nPvW_fQ-ivwEJ5gX0I7mDitlvV691OiWjT276NGblUoN013Fe-lGjCEQDnGJq26HKwmqnYyIUuSXKBgVorcsdlQLjXx_SZzouLAW-rucaMli3Mv0yUnD3ui4jQ_LZxSobihm51CnRw0Ha4BhQElLzAFrjiQo7YPv1UQF5skKeyJUz5WRmpYJBPb8IO-Ud2k1ZeBQwbF-QI_nN8hFMHj-KmCxc38ipj4A89aJLC6nD_Lq8vpALaN-54Tqtr3SGrHs2Zx2vIjsHyD89Daso1BlMjFSdoylX7ZoXpIqq4sR8ZuZHXZjEYiMh5h1xLlg1LTYUm8fBgy_WyI3jzQ9aGFyMuBdyanpofMV-jSFDuljpFhDFD0whznWYlU_TWBjAtTscASfzpV6Nt27Mqtzjt7NZTp11YEN7Y5jc1PnIc81LGDRw8LzH6WzN_6MVyCSix5dr4LNSf8b4NRXBI2C_OIZh1gWnuv5J21wUwEqo7Kr2aYH_UMvxq1M0J5tuahoTZPHw8umB9A3CvIJ1vFE6F4kOgiaabVGlEuDRDTpjZGhQQzQjtfrSRFaOa37vP9C_mtxB8fuWUfQc5NECmWse-KDOsVrTqqlgO9OLmkYcRpBviI-JguO-evVxzEz7PRb0w6CB4bqtM5MEV2trAZOUwlYRHcUg55Ejq4Sj_ksfR4"
    }

    try:
        response = requests.request("POST", url, data=payload, headers=headers)
        d = response.json()  # convert to json, export?
        if type(d['data']['characterData']['character']['lodestoneID']) == int:
            return True
    except TypeError:
        return False


def eligible(server, fight, partition, number):
    # {73: 9, 74: 10, 75: 11, 76: p1, 77: p2}
    url = "https://www.fflogs.com/api/v2/user"

    payload = "{\"query\":\"{worldData{encounter " + f'(id:{fight})' + "{characterRankings " + f'(page: {number}, difficulty: 101, serverSlug: \\\"{server}\\\", serverRegion: \\\"NA\\\", partition:{partition})' + "}}}\"}"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiI5NDA3NTgwZC1jNTNlLTRjZWQtOTRmMi03ZWRhNmQ4ZGM5Y2QiLCJqdGkiOiI1NzA0MmJjMTY3ZTQ1MGRmNDdlODk1NzZjNzUxNzc0NThkMzRkN2Q0YmYxODgzYzdkZTIwZmYwYWMwODFkZmIxYjI2OTlkNGRkMGM1ZWQ3NCIsImlhdCI6MTYyNzU5NDMyNSwibmJmIjoxNjI3NTk0MzI1LCJleHAiOjE2Mzc5NjIzMjUsInN1YiI6IjMxNDMwNSIsInNjb3BlcyI6WyJ2aWV3LXVzZXItcHJvZmlsZSIsInZpZXctcHJpdmF0ZS1yZXBvcnRzIl19.QRhT2ZZbqe_J4bZ_pJhXid_zx6AiYf3xfsK4mEtdlJvB4Tvw0S-u9VMEUzbA0aY5WbsbFpPX3c3IHAX2vjZ3lmOM-ByFzC-tqIM4FSm3g3LzXxHHDBBgkSqtvaZotA4tjg6Z7ogOaFLlHLuBc_W_NJt9yGBQkQe--5nmEJ5u6ZWVitFITJ9Z6pEOyRfxeKTmDzUMhBSai-KpXqBVgDvESLcSvNqEef50Ir3v0y1q62wwITp3v-iXlbVH8K0ieTOyM6XzB7Vm07QMQuBW3K2Rr3fC2B3ypTl4qY6WMZgHKOtFk81K7TLPY_kgiRRSuDn8qOSzFkrZSY2JhnzIyGkv8eVruzCZpBnYmWpo51u2v6ibvnoyCzS4ScgXd_LjbB4QKwxgk2TNIxTPbWoPH71ZBSj7CCCHbo6hJr0xVhzC3SMy_QWzs9EB6-IEAP7lbs5TSFNvw5lTZ9JGp5zPu4cMMrwimYfn2wC8cKMtnHluMyDhZdLhEA_4WOY0SEV46TukKMYWbsWZxgjcRFB4SccmrWZoskMk0GpfNtHlgFTs78fzcLeNfzsEh_-GIUKUTc_2lNGLL51bziEHS6sAKLTpBQ_VhjLE45mfDZpnN8w5pjthW7q8Yx_bqFdXv-lR0U_KF5_SZ8qcsyf6SUKT-3VdHkLR-D5KJOJTcZq_DMSjoaw"
    }

    response = requests.request("POST", url, data=payload, headers=headers)
    d = response.json()
    # print(d['data']['worldData']['encounter']['characterRankings']['rankings'][1]['name'])
    # print(d['data']['worldData']['encounter']['characterRankings']['count'])
    return d

#
# retrieve('Lazarus Mercer', 'Malboro', 73, 13)
# validate('Lazarus Mercer', 'Malboro')
# eligible('Mateus', 77, 7, 1)


def role(name, server, fight):
    url = "https://www.fflogs.com/api/v2/client"

    payload = '{"query":"query{characterData{character' + f'(name: \\\"{name}\\\", serverSlug: \\\"{server}\\\", serverRegion: \\\"NA\\\") ' + '{encounterRankings' + f'(difficulty:101, encounterID:{fight}, partition:13)' + '}}}"}'
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiI5NDA3NTgwZC1jNTNlLTRjZWQtOTRmMi03ZWRhNmQ4ZGM5Y2QiLCJqdGkiOiI5MWM2YmYzNDY4ZGFlZTQ5NDYwZGI5NzczYzY0NTVmNGU0OWEzNjhiY2Q3ZWVjZTUxMWNmMjgxZmVkNGQ0YWM1Y2MxOTAzMjEzYWViOTE1YSIsImlhdCI6MTYyNzU5MjkwMywibmJmIjoxNjI3NTkyOTAzLCJleHAiOjE2Mzc5NjA5MDMsInN1YiI6IjMxNDMwNSIsInNjb3BlcyI6WyJ2aWV3LXVzZXItcHJvZmlsZSIsInZpZXctcHJpdmF0ZS1yZXBvcnRzIl19.TWJ6nPvW_fQ-ivwEJ5gX0I7mDitlvV691OiWjT276NGblUoN013Fe-lGjCEQDnGJq26HKwmqnYyIUuSXKBgVorcsdlQLjXx_SZzouLAW-rucaMli3Mv0yUnD3ui4jQ_LZxSobihm51CnRw0Ha4BhQElLzAFrjiQo7YPv1UQF5skKeyJUz5WRmpYJBPb8IO-Ud2k1ZeBQwbF-QI_nN8hFMHj-KmCxc38ipj4A89aJLC6nD_Lq8vpALaN-54Tqtr3SGrHs2Zx2vIjsHyD89Daso1BlMjFSdoylX7ZoXpIqq4sR8ZuZHXZjEYiMh5h1xLlg1LTYUm8fBgy_WyI3jzQ9aGFyMuBdyanpofMV-jSFDuljpFhDFD0whznWYlU_TWBjAtTscASfzpV6Nt27Mqtzjt7NZTp11YEN7Y5jc1PnIc81LGDRw8LzH6WzN_6MVyCSix5dr4LNSf8b4NRXBI2C_OIZh1gWnuv5J21wUwEqo7Kr2aYH_UMvxq1M0J5tuahoTZPHw8umB9A3CvIJ1vFE6F4kOgiaabVGlEuDRDTpjZGhQQzQjtfrSRFaOa37vP9C_mtxB8fuWUfQc5NECmWse-KDOsVrTqqlgO9OLmkYcRpBviI-JguO-evVxzEz7PRb0w6CB4bqtM5MEV2trAZOUwlYRHcUg55Ejq4Sj_ksfR4"
    }

    response = requests.request("POST", url, data=payload, headers=headers)
    d = response.json()  # convert to json, export?
    # job = d['data']['characterData']['character']['encounterRankings']['ranks'][0]['bestSpec']
    # print(d)
    # print(job)
    return d

#
# role("j'talhdi wijixa", 'balmung', 74)

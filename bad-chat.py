import json
import sys
import random
import requests
import time
def main():
    test_id = open("chat_id.txt", "r")
    old_chat_id = test_id.read()
    if __name__ == '__main__':
        if old_chat_id==chat_id:
            print('yeni id bekleniyor, son chat id: '+old_chat_id)
        elif old_chat_id!=chat_id:
            url = "https://hooks.slack.com/services/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"
            message = ("CHAT ID: "+chat_id)
            title = (f"CANLI DESTEK: "+agent_name)
            slack_data = {
                "username": "Bad Chat Bot",
                "icon_emoji": ":red_circle:",
                "attachments": [
                    {
                        "color": "#9733EE",
                        "fields": [
                            {
                                "title": title,
                                "value": message,
                                "short": "false",
                            }
                        ]
                    }
                ]
            }
            byte_length = str(sys.getsizeof(slack_data))
            headers = {'Content-Type': "application/json", 'Content-Length': byte_length}
            response = requests.post(url, data=json.dumps(slack_data), headers=headers)
            if response.status_code != 200:
                raise Exception(response.status_code, response.text)


while True:
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:91.0) Gecko/20100101 Firefox/91.0',
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Referer': 'https://my.livechatinc.com/',
        'Authorization': 'Bearer dal:QzpMk9XLb926vT8H18NubQNJim4',
        'Content-Type': 'application/json',
        'Origin': 'https://my.livechatinc.com',
        'Proxy-Authorization': 'Basic U1F5Y3pnQ1hoS2oyVEozRXRNUktXWkR4OmRuR1JwV25Ed2VxZDljOEpHYzZOQjNCcQ==',
        'Connection': 'keep-alive',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        'TE': 'trailers',
    }

    params = (
        ('timezone', 'Europe/Istanbul'),
    )

    data = '{"filters":{"properties":{"rating":{"score":{"values":[0]}}}},"sort_order":"desc","limit":25}'

    response = requests.post('https://api.livechatinc.com/v3.4/agent/action/list_archives', headers=headers, params=params, data=data)

    veriler = response.content
    veri_x = json.loads(veriler)
    chat_id=veri_x['chats'][0]['thread']['id']
    get_agent_name = veri_x['chats'][0]['thread']['user_ids'][0]

    if get_agent_name ==  'cemates12345@hotmail.com':
        agent_name="Cem"

    elif get_agent_name ==  'aalp7216@gmail.com':
        agent_name="Alp"

    elif get_agent_name ==  'yigit.yigitx01@gmail.comm':
        agent_name="Yiğit"

    elif get_agent_name ==  'sonmezalp01@hotmail.com':
        agent_name="Hızır"

    elif get_agent_name ==  'cengizgn8@outlook.com':
        agent_name="Cengiz"

    elif get_agent_name ==  'tolgataha1234@gmail.com':
        agent_name="Bartu"
    chat_txt = open("chat_id.txt", "w")
    chat_txt.write(chat_id)
    time.sleep(5)

    main()

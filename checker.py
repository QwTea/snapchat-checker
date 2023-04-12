import yaml
import argparse
from MainWork import CheckEmail

with open("translations.yaml", encoding="utf-8") as f:
    translations = yaml.safe_load(f)



parser = argparse.ArgumentParser(description="SnapChat checker")
parser.add_argument("--language", type=str, help="Язык, на котором будет работать программа, например ru    |     The language in which the program will work, for example en", default="en")
parser.add_argument("--type_proxy", type=str, help="Тип прокси сервера, например http    |     The type of proxy server, for example http", default=None)
parser.add_argument("--proxy", type=str, help="Прокси сервер, например admin:12345@127.0.0.1:8080    |     Proxy server, for example admin:12345@127.0.0.1:8080", default=None)
parser.add_argument("--email", type=str, help="Email для проверки    |     Email to check")
args = parser.parse_args()
language = args.language
type_proxy = args.type_proxy
proxy = args.proxy
email = args.email

choose_language = translations[language]

checker_email = CheckEmail(choose_language, proxy, type_proxy)

information_about_email = checker_email.get_information(email)

if information_about_email == 'snapchat':
    print(f"{choose_language['mail_found_in']} {information_about_email}")
elif information_about_email == 'bitmoji':
    print(f"{choose_language['mail_found_in']} {information_about_email}")
elif information_about_email is None:
    print(choose_language['mail_not_found'])
else:
    print(choose_language['limits_exceeded'])
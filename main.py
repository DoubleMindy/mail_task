import smtplib
import argparse
import os

parser = argparse.ArgumentParser(description = 'Отправка электронной почты')
parser.add_argument('-n', '--name', help = 'Имя друга')
parser.add_argument('-to', '--mailto', help = 'Почта друга')
args = parser.parse_args()

friend_name = args.name
my_name = 'Илья'
website = 'dvmn.org'
mail_text = '''Привет, %friend_name%! %my_name% приглашает тебя на сайт %website%!

%website% — это новая версия онлайн-курса по программированию. 
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя. 

Как будет проходить ваше обучение на %website%? 

→ Попрактикуешься на реальных кейсах. 
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей. 
Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.
→ Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят. 

Регистрируйся → %website%  
На модули, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл.'''

mail_text = mail_text.replace('%website%', website).replace('%friend_name%', friend_name).replace('%my_name%', my_name)

from_who = 'tim-star@ya.ru'
to_who = args.mailto

msg = '''From: mymail@gmail.com
To: friend@gmail.com
Subject: Важно!
Content-Type: text/plain; charset="UTF-8";

{}'''.format(mail_text).encode("UTF-8")

server = smtplib.SMTP_SSL('smtp.yandex.ru:465')
login = os.getenv("LOGIN")
password = os.getenv("PASSWORD")
server.login(login, password)
server.sendmail(from_who, to_who, msg)
server.quit()

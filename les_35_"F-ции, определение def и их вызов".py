# def send_mail():
#     text = "Hello world!"
#     print(text)
#
#
# send_mail()
# send_mail()

#-------------------
def get_mail(from_name, old):
    text = f"""Уважаемый, Сергей!
    Я так и не понял, что такое фукция.
    Объясните лучше!
    Ваш, {from_name}! И не судите строго мне {old} лет!
"""
    print(text)
    

get_mail("Вася", 7)
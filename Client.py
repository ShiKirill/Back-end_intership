import telebot
import time
from opcua import Client

if __name__ == "__main__":
    client = Client("opc.tcp://127.0.0.1:587")


bot = telebot.TeleBot('1480869311:AAFqzhAMhFL071vTN2-U1dkoJ4K8CgPuCQU')


@bot.message_handler(commands=['start'])
def start_message(message):
    client.connect()
    try:
        while True:
            time.sleep(3)
            values = []
            bot.send_message(message.chat.id, "###")
            for i in range(10):
                values.append(client.get_node("ns=2;i=" + str(i + 2)).get_value())
                if values[i] <= -3 or values[i] >= 7:
                    bot.send_message(message.chat.id, 'Значение переменной №' + str(i+1) + " : " + str(values[i]) + ' лежит за пределами.')
    finally:
        client.disconnect()


bot.polling()
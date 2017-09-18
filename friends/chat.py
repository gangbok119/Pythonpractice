
def send_massage():
    name = input('친구명: ')
    message = input('메세지: ')
    print('%s에게 "%s" 메세지를 전송했습니다. ' % (name, message) )

if __name__ == '__main__':
    send_massage()

num = 0

def rec():
    global num
    if num > 100:
        return
    print(num)
    num += 1
    rec()

rec()

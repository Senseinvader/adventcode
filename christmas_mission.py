def get_sum_of_captcha():
    list_captcha = process_captcha()
    sum_of_captcha = 0

    for i in range(len(list_captcha)-1):
        if list_captcha[i] == list_captcha[i+1]:
            sum_of_captcha += list_captcha[i+1]

    #  here we are checking the last and the first numbers separately from the rest of massive
    if list_captcha[-1] == list_captcha[0]:
        sum_of_captcha += list_captcha[0]

    print(sum_of_captcha)


def get_halfway_sum_captcha():
    list_captcha = process_captcha()
    sum_of_captcha = 0

    divider = int(len(list_captcha)/2)
    for i in range(len(list_captcha) - divider):
        if list_captcha[i] == list_captcha[i+divider]:
            sum_of_captcha += (2 * list_captcha[i])
    print(sum_of_captcha)


def process_captcha():
    number = int(input('Enter number for captcha:\n'))
    list_captcha = []
    list_captcha = [int(x) for x in str(number)]
    return list_captcha


def main():
    #get_sum_of_captcha()
    get_halfway_sum_captcha()


if __name__ == '__main__':
    main()

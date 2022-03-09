# 0. 종료 1.계좌 개설 2. 계좌 목록 3. 입금 4. 출금 5 계좌 해지 6. 계좌 조회
from random import random

from review.domain import myRandom


class Account:
    def __init__(self, account_number, money):
        self.NAME = '유재혁'
        self.BANKNAME = '비트 은행'
        self.account_number = self.create_account_number()
        self.money = myRandom(100, 999)

    def to_string(self):
        return f'은행 : {self.BANKNAME},' \
               f'통장주 : {self.NAME},' \
               f'계좌 번호: {self.account_number},' \
               f'금액:{self.money} 만원'

    def create_account_number(self):
        return ''.join(['-' if i == 3 or i == 6 else str(myRandom(0, 9)) for i in range(13)])

    @staticmethod
    def deposit(ls, account_number,add):
        for i, j in enumerate(ls):
            if j.account_number == account_number :
                ls[i].money += int(add)
                return ls[i].to_String

    @staticmethod
    def withdraw(ls, account_number,draw):
        for i, j in enumerate(ls):
            if j.account_number == account_number :
                ls[i].money -= int(draw)
                return ls[i].to_String

    @staticmethod
    def del_account(ls, account_number):
        for i, j in enumerate(ls):
            if j.account_number == account_number:
                del ls[i]

    @staticmethod
    def find_account(ls, account_number):
        return ''.join([j.to_string() if j.account_number == account_number else '찾는 계좌가 없습니다.' for (i,j) in enumerate(ls)])

if __name__ == '__main__':
    ls = []
    while 1:
        menu = input('0. 종료 1. 계좌 개설 2 계좌 목록 3. 입금 4. 출금 5. 계좌 해지 6. 계좌 조회')
        if menu == '0': break
        if menu == '1':
            acc = Account(None, None)
            print(f'{acc.to_string()} .. 개설')
            ls.append(acc)
        if menu == '2':
            li = '\n'.join([i.to_string() for i in ls])
            print(li)
        if menu == '3':
            print(Account.deposit(ls,input('입금할 계좌번호'), input('입금액')))
        if menu == '4':
            print(Account.withdraw(ls,input('출금할 계좌번호'),input('출금액')))
        if menu == '5':
            print(Account.del_account(ls, input('삭제할 계좌번호')))
        if menu == '6':
            print((Account.find_account(ls,input('조회할 계좌번호'))))



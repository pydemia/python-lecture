# -*- coding: utf-8 -*-


class Hangman:

    def __init__(self, word, chance=5):

        assert isinstance(word, str)
        assert isinstance(chance, int)

        self.answer = word.lower()
        self.remains = chance
        self.history = []
        self._marker = ['_ '] * len(self.answer)
        self._status = True

        self._mrkstr = ''.join(self._marker)
        self.messege = self._mrkstr + '(Chance: {})'.format(self.remains)

        print(self.messege)

    def guess(self, character):

        assert isinstance(character, str)
        assert len(character) == 1
        
        character = character.lower()

        if character in self.history:

            print('Already spoken!')

        else:

            self.remains -= 1
            self.history.append(character)

            if character in self.answer:

                print('Correct!')
                idx = [i for i, x in enumerate(self.answer) if x == character]
                for i in idx:
                    self._marker[i] = self.answer[i] + ' '
                    self._mrkstr = ''.join(self._marker)
                    self.messege = (self._mrkstr +
                                    '(Chance: {})'.format(self.remains))
                print(self.messege)

            else:
                print('Wrong!')
                self.messege = (self._mrkstr +
                                '(Chance: {})'.format(self.remains))
                print(self.messege)

            if '_ ' not in list(self._marker):

                self._status = False
                print('\nYou win!')
                print('Answer: ' + self.answer)

            elif self.remains == 0:

                self._status = False
                print('\nYou lose!')
                print('Answer: ' + self.answer)

#%%  Start

print("Hangman 게임을 시작합니다.")
givenWord = str(input("영어 단어를 입력하세요 :"))
chanceNum = int(input("게임 횟수를 입력하세요 (default: 5): "))

gameBoard = Hangman(givenWord, chanceNum)

while gameBoard._status:
    guessWord = str(input("영어 알파벳을 입력하세요."))
    gameBoard.guess(guessWord)

input("게임이 끝났습니다. Enter 키를 누르면 프로그램이 종료됩니다.")

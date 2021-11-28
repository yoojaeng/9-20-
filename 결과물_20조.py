#눈 print 함수
def e(eyes):
    if eyes==1:
        i1='﻿● '
        i2='﻿ ●'
    if eyes==2:
        i1='> '
        i2=' <'
    if eyes==3:
        i1='= '
        i2=' ='
    if eyes==4:
        i1='＠'
        i2='＠'
    print('       *****       ')
    print('   ***       ***   ')
    print('  *             *  ')
    print(' *    %s   %s    * '%(i1, i2))

#코 print 함수
def n(nose):
    if nose==1:
        i=' '
    if nose==2:
        i='.'
    if nose==3:
        i='<'
    if nose==4:
        i='C'
    print(' *       %s       * '%(i))

#입 print 함수
def l(lips):
    if lips==1:
        i1=')'
        i2='-'
        i3='('
    if lips==2:
        i1=' '
        i2='U'
        i3=' '
    if lips==3:
        i1='_'
        i2='_'
        i3='_'
    if lips==4:
        i1=' '
        i2='◇'
        i3=' '
    print('  *     %s%s%s     *  '%(i1, i2, i3))
    print('   ***       ***   ')
    print('       *****       ')
    result()

    
#입력 함수
print('함께 이모지를 만들어볼까요!')

def emoji():
    eyes=int(input('1~4 중에서 눈모양 번호를 골라주세요 :'))
    nose=int(input('1~4 중에서 코모양 번호를 골라주세요 :'))
    lips=int(input('1~4 중에서 입모양 번호를 골라주세요 :'))
    
    if not 5>eyes>0 :
        print('입력하신 숫자', eyes, '는 눈 선택지에 없습니다.')
    if not 5>nose>0 :
        print('입력하신 숫자', nose, '는 코 선택지에 없습니다.')
    if not 5>lips>0 :
        print('입력하신 숫자', lips, '는 입 선택지에 없습니다.')
    if eyes>4 or eyes<1 or nose>4 or nose<1 or lips>4 or lips<1 :
        print()
        print('프로그램을 재실행합니다.')
        print('번호를 다시 입력해 주세요.')
        print()
        emoji()

    else :
        e(eyes)
        n(nose)
        l(lips)



#이모지를 성공적으로 출력한 후
def result():
    reply=input('이모지가 마음에 드나요?(yes/no) :')
    if reply=='yes':
        print('감사합니다! 다음에도 또 이용해 주세요!')
    elif reply=='no':
        replay()
    else :
        print('yes/no 로 대답해주세요.')
        result()

def replay():
    reply=input('프로그램을 다시 실행할까요?(yes/no) :')
    if reply=='yes' :
        print()
        emoji()
    elif reply=='no' :
        print('이용해 주셔서 감사합니다.')
    else :
        print('yes/no 로 대답해주세요.')
        replay()

emoji()

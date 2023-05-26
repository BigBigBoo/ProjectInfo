﻿
# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define e = Character('Мзю', color="#14d114")
define r = Character ('Зю', color="#eeff00")
define l = Character ('...', color= "#1400ca")
define k = Character ('Преподаватель', color="#a30000")
define u = Character ('Водитель', color="#a30a24")

# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

# Игра начинается здесь:
label start:

    scene loka
    
    play music "audio/everlasting_summer_34 - Reflection On Water.mp3" volume 0.1 fadeout 1

    l "Приветствую вас в моем проекте 'Бесконечная Юрюзань' и в этой истории я хочу вам поведать, про мою первую и последнюю поездку в это 'прекрасное' место..."

    l "Итак, начнём!"

    l "Меня зовут Мзю, мне 16"

    l "и как-то раз мой друг Зю предложил поехать вместе с ним в Юрюзань..."

    scene classic

    show zy

    r "Иу, Мзю, поехали со мной на выходные в Юрюзань"

    menu:
        "Ну давай,я всё равно свободен!":
          jump s2

        "Зю, извини конечно, но у меня последняя пересдача по математике":
          jump s1

    stop music

    label s1:

      play music "audio/i want to play.mp3" volume 0.1 fadeout 1
      
      r "Ну и ладно!"

      l "Зю обиделся на вас"

      l "Суббота, 8:00"

      e "Ты как, сел? "

      r "Да, отпишу как приеду.. "

      play music "audio/two glasses.mp3" volume 0.1 fadeout 1

      l "Вы открыли тестовый вариант экзамена"

      scene exam

      label q1:
          python:
           a = renpy.input("сколько будет 2+2?")
          if a == "4":
            e "Правильно"
      
          else:
            e "Неправильно"
            jump q1

      label q2:
        python:  
          b = renpy.input("сколько будет 7*9?")
        if b == "63":
          e "Правильно"
        else:
          e "Неправильно"
          jump q2

      label q3:
        python:
          c = renpy.input("сколько будет 941*743?")
        if c == "699163":
          e "Правильно"
        else:
          e "Неправильно"
          jump q3

      l "Верно! 3/3"

      e "Ха-ха, да я гений!"

      e "Ну всё, пойду отдыхать..."

      l "Понедельник, 8:00"
 
      play music "audio/just think.mp3" volume 0.1 fadeout 1

      scene classic

      e "У меня всё получится..."

      l "Учительница положила вам вариант на стол"

      l "Вы заметили подпись в углу листа"

      l "'От твоего лучшего друга'"

      e "'Ты выбрал неправильный вариант...'"

      e "Подождите, но мы ещё не проходили этих заданий!"

      show uchilka

      k "Как это не проходили?"

      k "У всех одинаковый вариант"

      l "На лице учителя появилась злая ухмылка"

      k "Начинаем писать! У вас есть 2 часа"

      l "По истечению двух часов вы не смогли сделать ни единого задания" 

      l "Плохая концовка"
        
      return

    label s2:

      play music "audio/i want to play.mp3" volume 0.1 fadeout 1

      r "Отлично!"

      r "Тогда жду тебя завтра в 8:00 на автобусной станции"

      e "А в этой твоей Юрюзани не опасно??"

      r "Да поверь, все будет хорошо"

      scene images

      l "Суббота, 8:00"

      l "Автобусная станция"
    
      scene busstop

      e "Сколько нам ехать?"

      show zy

      r "Примерно 4 часа, успеем и поспать, и поесть.. Хаха"

      e "Дааа, долгая предстоит поездка"

      scene images

      l "Зю и Мзю сели в атобус"

      scene bussin

      show zy
      r "Дорога долгая,может поедим?"

      scene loka

      l "Зю достал бутерброды"
   
      show byter:
        xalign 0.0
        yalign 0.6
    
      l "Кока-колу"
    
      show voda:
    
        xalign 1.0
        yalign 0.6

      l"Ребята съели бутерброд и выпили колу"

      scene bussin
 
      show zy

      r "Ну,как там говорится... После смачного обеда, по закону Архимеда, чтобы плохо не было,нужно поспать!"

      e "Дааа... Рифмовать у тебя конечно не получается, но ты дело говоришь!"

      scene images

      l "Ребята достали наушники"

      menu:

          "Послушать музыку Зю":
              jump choice1_yes

          "Включить свою музыку":
              jump choice1_no

      label choice1_yes:

          $ menu_flag = True

          play music "audio/zymzy.mp3" volume 0.2

          l "..."

          stop music
        
          e "Как он это слушает..."

          jump choice1_done

      label choice1_no:

          $ menu_flag = False

          play music "audio/komarovo.mp3" volume 0.1
                 
          e "..."

          jump choice1_done

      label choice1_done:

      stop music

      scene images
       
      play music "audio/just think.mp3" volume 0.1 fadeout 1

      l "Прошло 4 часа"

      u "Просыпайтесь!"

      scene bussin

      show vodila

      e "Ой, извините пожалуйста"

      u "Ну наконец-то! У меня уже рейс на 5 минут из-за вас задерживается!"

      u "Выходите быстрее"

      l "Зю и Мзю вышли из автобуса и осмотрелись"
 
      scene avtou

      e "Что за?..."
    
      e "Почему потемнело???"
      
      e "мы же должны были приехать к 12 часам!"

      show zy

      r "Слушай,тут есть одно интересное место,я думаю тебе понравится"

      e "Почему он меня просто проигнорировал?..."
  
      l "Зю привёл Мзю к заброшенному дому" 

      play music "audio/You lost me.mp3" volume 0.1 fadeout 1

      scene house
  
      e "Смотри! Там какие-то девочки!!"

      r "Давай скорее за ними, вдруг познакомишься с кем-то!" 

      e "Ой,да ну тебя! Пошли уже"

      l "Зю и Мзю вошли в дом и окликнули девочек"

      scene room

      e "Странно,они же вот только что зашли сюда"
  
      e "Мрачная тут обстановка какая-то, если это розыгрыш,то лучше заканчивай сейчас!"

      r "Хотел бы и я,чтобы это был мой розыгрыш.."

      r "Мзю,смотри! Тут какая-то тетрадка лежит"
   
      scene images

      l "Мзю пришёл в соседнюю комнату"

      scene room2

      l "Мзю обратил внимание на стол, на котором лежала его тетрадь по математике"

      e "Что за..."

      scene classic

      show uchilka

      k "Мзю, что с тобой?"

      e "А?"

      l "Вы очнулись с зачёткой в руках"

      e "Я же только что был в Юрюзани..."

      k "Мзю, у тебя солнечный удар?"
      
      k "Сейчас конец июня,ты сдал математику"

      e "Извините, в мысли ушёл..."

      l "Хорошая концовка"

      scene images

      l "Вот и конец моей истории. Поставьте зачёт:)"
      return
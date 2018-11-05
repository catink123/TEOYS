﻿label mainscript:
  stop music fadeout 2.0
  #scene bg koshka
  scene black
  with dissolve_scene_full
  play music t10
  "Вокруг так темно, лишь маленький холодок проходит по коже. Всё кажется таким реальным."
  #$ renpy.movie_cutscene("images/bg/ZzxX.webm")
  show videotest
  "Юри... Я так с ней хорошо дружил." 
  "Почему она уехала в другой город?" 
  "Мы играли вместе, помогали друг другу." 
  "Это был мой самый лучший друг детства." 
  "Было бы хорошо если бы она~"
  play music t10
  scene bg bedroom
  mc "Что это был за сон?.."
  "Приоткрыв глаза я услышал как мама звала меня завтракать. Я быстренько одел только что выутюженную школьную форму. Я вышел из своей комнаты и пошел на кухню."
  scene bg kitchen
  with dissolve_scene_full
  mum "Доброе утро, [player]. Ты же помнишь, что сегодня твой первый день  в старшей школе?"
  mc "Конечно мам."
  "Я взял палочки для еды и принялся за завтрак."
  mum "Вот. Держи, твоё бенто."
  mc "Спасибо."
  mum "Не говори с полным ртом."
  stop music fadeout 1.0
  scene black
  with dissolve_scene_full
  "{i}Прошло около 6 минут{/i}"
  mc "Всё, я пошёл."
  mum "Удачи тебе."
  play sound closet_open
  scene bg residential_day
  with dissolve_scene_full
  play music t3
  play sound closet_close
  "Закрыв дверь, я вышел на улицу и меня встретил яркий солнечный свет."
  "Я шёл по улице, по которой всегда ходят в среднюю школу. Очень много людей шли по одной дороге со мной."
  "{w=2}{nw}"
  #"{i}Тут должно быть ожидание, но я его не сделал.{/i}"
  scene bg corridor
  with dissolve_scene_full
  "{w=2}{nw}"
  "Я подошёл к стенду со списками."
  mc "Класс 1-Е. Хорошо."
  "Несколько минут я пытался найти свой класс. Но решил всё же у кого-нибудь спросить."
  mc "Эмм.. Простите, что отвлекаю, но не могли бы вы мне помочь?"
  show monika 1b at t11 zorder 2
  unknown "Конечно. Вы потерялись?"
  show monika 1a at t11 zorder 2
  mc "Да."
  show monika 1j at t11 zorder 2
  "От смущения я опустил голову, а девушка рассмеялась."
  show monika 2k at t11 zorder 2
  unknown "Вам в какой класс?"
  show monika 2a at t11 zorder 2
  mc "1-Е."
  show monika 1d at t11 zorder 2
  unknown "Ух ты! Оказывается мы с вами в одном классе."
  show monika 1c at t11 zorder 2
  mc "Правда?"
  "С удивлением на лице, спросил я."
  show monika 1d at t11 zorder 2
  unknown "Да."
  "Какое-то время над нами нависла неловкая пауза."
  show monika 1g at t11 zorder 2
  unknown "Эмм... Скоро начнутся уроки, поэтому нам следует поторопиться."
  show monika 1f at t11 zorder 2
  mc "Да, конечно."
  show monika 2b at t11 zorder 2
  unknown "Слушай, давай общаться на 'ты'. Мы же одноклассники как никак."
  show monika 2a at t11 zorder 2
  mc "Хорошо."
  show monika 4i at t11 zorder 2
  unknown "А как тебя зовут?"
  show monika 5a at t11 zorder 2
  "Девушка с интересом посмотрела на меня."
  mc "Меня зовут [player]."
  m 1k "[player], красивое имя. А меня зовут Моника."
  mc "Приятно познакомится."
  m "Взаимно."
  hide monika
  "По дороге в класс мы с Моникой говорили на довольно разные темы."
  stop music fadeout 1.0
  scene bg class
  with dissolve_scene
  play music t8
  play sound bell
  "Как только мы зашли в класс, прозвенел звонок."
  "Я сел поближе к окну. Моника села напротив  меня. После звонка сразу вошел учитель."
  tchr "Меня зовут Оигава Кенске. С сегодняшнего дня, я ваш классный руководитель, надеюсь мы с вами подружимся."
  "С улыбкой на лице, учитель достал журнал и начал называть имена учеников. Как только очередь дошла до меня, послышался стук в дверь."
  tchr "Войдите."
  show yuri 4a at t11 zorder 2 
  unknown "Простите за опоздание."
  "Девушка с длинными фиолетовыми волосами чуть ли не крикнула."
  show yuri 4b at t11 zorder 2
  tchr "Ты у нас Юри, так? Ничего страшного, ты можешь сесть рядом с [player]."
  show yuri 1q at t11 zorder 2
  y 1b "Да, хорошо."
  show yuri 1a at t11 zorder 2
  "Девушка медленно подошла к парте, достала вещи и присела. Учитель продолжил называть имена."
  tchr "Так, на ком мы закончили?..[player]?"
  mc "Да, я здесь."
  show yuri 3p at t11 zorder 2
  "Может мне и показалось, но когда назвали мое имя девушка сидевшая рядом со мной вздрогнула. Но я не обратил на это внимания."
  show yuri 3o at t11 zorder 2
  "Так прошли первые три уроков."
  hide yuri
  scene bg stolovaya
  with dissolve_scene_full
  "Настало время обеда. Все собрались по кучкам и начали заниматься своими делами."
  "Мы с Моникой решили пообедать вместе. Только Юри сидевшая рядом со мной, была одна."
  "Она достала из своего рюкзака книгу и начала читать."
  scene art_yuribook
  with dissolve_scene
  "Её глаза как будто опустели во время чтения книги."
  "Она так сильно была увлечена, что не слышала голоса в столовой."
  scene bg stolovaya
  with dissolve_scene
  "Мы с Моникой разговаривали на разные темы."
  "Первый день в школе прошел довольно хорошо."
  "Новые знакомства, новые возможности, а теперь надо было идти домой."
  scene bg schoolcorridor2
  with wipeleft_scene
  show monika 1a at t11 zorder 2
  "Как только я переодел обувь, ко мне подошла Моника и предложила идти домой вместе."
  "Но тут я вспомнил, что забыл сумку в классе."
  mc "Сейчас, пожоджи минутку. Я забыл свой портфель в классе."
  "Моника с улыбкой на лице просто покачала головой. Было видно, что у неё хорошее настроение."
  "Я быстренько побежал в класс."
  hide monika
  stop music fadeout 1.0
  scene bg class2
  with wipeleft_scene
  play music yuri_remember
  show yuri 2u at t11 zorder 2
  "Как только я зашёл, я увидел Юри смотрящую в окно."
  show yuri 2s at t11 zorder 2
  mc "А почему ты не идёшь домой?"
  y 2t "Просто хотела побыть одна."
  show yuri 2s at t11 zorder 2
  mc "Прости, что всё испортил."
  "Я печально опустил голову, а Юри подошла ко мне."
  y 1f "Слушай [player], ты меня не помнишь?"
  show yuri 1e at t11 zorder 2
  mc "Что?"
  "С недоумением на лице, спросил я."
  y 1b "Помнишь девочку которая жила по соседству с тобой?"
  y "Но потом из-за проблемы родителей ей пришлось уехать."
  mc "Юри? Это же ты, Юри?"
  y 4a "Все таки помнишь. Я рада."
  show yuri 4c at t11 zorder 2
  "На лице Юри были видны слёзы, она вздрагивала, пытаясь вытереть слёзы."
  "Я подошел к ней и крепко обнял."
  show yuri 4b at t11 zorder 2
  "Юри немного успокоилась."
  y 4a "Слушай [player]…"
  mc "Что такое?"
  "Голос Юри дрожал."
  y 2o "Сможем ли мы опять стать друзьями…?.."
  show yuri 2e at t11 zorder 2
  "Я засмеялся, а Юри с недоумением на меня смотрела."
  mc "Конечно."
  show yuri 1c at t11 zorder 2
  "Я погладил Юри по голове, на что та, только улыбнулась."
  y 1b "Ладно, тебе пора идти."
  show yuri 1a at t11 zorder 2
  mc "А ведь, точно."
  "Я быстро взял сумку и подбежал к двери."
  mc "До завтра, Юри."
  y 1d "До завтра, [player]."
  "Юри с улыбкой на лице помахала мне вслед, я ответил тем же. Я быстро побежал к выходу, меня ждала Моника."
  play sound door_close
  stop music fadeout 1.0
  hide yuri
  scene bg schoolcorridor2
  play music t3
  with wipeleft_scene
  show monika 1i at t11 zorder 2
  m "Долго же ты."
  show monika 1h at t11 zorder 2
  "Она смотрела на меня с угрюмым выражением лица."
  mc "Прости."
  m 1i "Ладно пошли."
  scene bg park
  with wipeleft_scene
  "Итак мы с Моникой пошли домой."
  scene black 
  with dissolve_scene
  "{i}Через 20 минут{/i}"
  scene bg kitchen
  with dissolve_scene
  mc "Я дома."
  mc "Слушай мам, я тебе сейчас такое расскажу."
  "Я рассказал матери, что подружился с Моникой и встретил Юри."
  "Она была за меня рада."
  "Я поужинал, сделал уроки и лёг спать."
  "Так закончился мой первый день в старшей школе."
  stop music fadeout 1.0
  scene black
  with dissolve_scene_full
  play music dream
  "Что происходит..? Где я..?"
  "Я не мог ничего заметить из-за темноты вокруг меня."
  "Я чувствовал холод и чьё-то дыхание."
  "Оно было таким тяжелым и громким."
  "Потом всё затихло. Где-то вдалеке я слышал чей-то голос."
  "Он был нежным и тихим, таким тихим, что я ничего не услышал."
  stop music
  scene bedroom
  with dissolve_scene
  play music t9
  mc "Уже утро?"
  "Я посмотрел на будильник."
  mc "Черт, я опаздываю!"
  "Я быстро оделся, взял свое бенто и даже не спросил маму почему она меня не разбудила."
  scene bg kitchen
  with wipeleft_scene
  show yuri 1c at t11 zorder 2
  "Как только я открыл дверь, я увидел Юри, она улыбалась."
  y 1d "Привет [player]."
  show yuri 1a  at t11 zorder 2
  mc "Привет."
  y 1b "Ну что, пойдем?"
  show yuri 1a at t11 zorder 2
  mc "Ага."
  stop music fadeout 1.0
  scene bg residential_day
  with dissolve_scene
  show yuri 1c at t11 zorder 2
  play music t8
  "Юри с улыбкой на лице, шла возле меня." 
  "По дороге в школу мы говорили о жизни."
  scene bg schoolcorridor1
  with wipeleft_scene
  show yuri 1a at t21 zorder 2
  show monika 1a at t22 zorder 2
  "Как только мы пришли в школу нас встретила Моника."
  "Я решил её познакомить с Юри."
  mc "Моника, знакомься это Юри. Юри, это Моника."
  show yuri 1b at f21 zorder 2
  y "Приятно познакомиться Моника."
  show yuri 1a at t21 zorder 2
  show monika 1b at f22 zorder 2
  m "Взаимно."
  m "Скоро начнутся уроки, поэтому нам надо идти."
  stop music fadeout 1.0
  show monika 1a at t22
  scene bg class 
  with wipeleft_scene
  play music t9
  "Мы втроем пошли в класс, каждый сел за свою парту и прозвенел звонок."
  hide monika
  hide yuri
  "Целый урок я только и делал, что смотрел в окно."
  "Я был счастлив, что снова встретил Юри, что познакомился с Моникой."
  tchr "Эй, [player]!"
  tchr "Повтори, что я только что сказал."
  mc "Эмм.. Вы сказали..."
  tchr "Ладно, хоть это и второй день. Я тебе прощаю."
  "Учитель нахмурил брови, а я опять сел за парту. Было немного стыдно."
  "Я ждал пока прозвенит звонок."
  play sound bell
  stop music fadeout 1.0
  play music t5
  "Через 15 минут он прозвенел."
  mc "Фух, наконец-то.."
  "И вдруг к нам в класс зашел директор."
  drk "Я рад вас всех видеть."
  drk "Я пришел для того, чтобы сделать небольшое объявление. Завтра первые классы поедут в поездку к замку в Осаке. Вместо уроков."
  drk "Всё, хорошего вам дня."
  "Директор хороший человек."
  "Осака, значит. Когда-то я хотел туда съездить."
  "Юри и Моника разговаривали о чем-то своем. Весь класс зашумел."
  show yuri 1b at f22 zorder 2
  show monika 1a at t21 zorder 2
  y "Осака довольно красивое место."
  show yuri 1a at t22 zorder 2
  show monika 1b at f21 zorder 2
  m "Ты там была Юри?"
  show yuri 1b at f22 zorder 2
  show monika 1a at t21 zorder 2
  y "[player] говорил тебе, что я уехала из Токио, когда мы были маленькими?"
  show yuri 1a at t22 zorder 2
  show monika 1b at f21 zorder 2
  m "Да, помню."
  show yuri 1b at f22 zorder 2
  show monika 1a at t21 zorder 2
  y "[player] а ты, что думаешь? Хочешь поехать?"
  show yuri 1a at t22 zorder 2
  mc "Очень."
  show yuri 1c at t22 zorder 2
  show monika 1j at t21 zorder 2
  "Моника и Юри посмотрели на меня и улыбнулись."
  hide yuri
  hide monika
  show natsuki 4e at t11 zorder 2
  unknown "Да кому это надо?"
  show natsuki 4g at t11 zorder 2
  "Вдруг в классе раздался голос."
  "Это была девочка с розовыми волосами. Её звали Нацуки."
  n 4e "Что? Ты хочешь поехать туда? Ты совсем дура, что ли???"
  show natsuki 4g at t11 zorder 2
  "Нацуки разговаривала с Ханакой-сан."
  "На её лице было видно, что она напугана."
  "Я не мог смотреть на это и уже хотел сказать, но заступилась Моника."
  show monika 1d at f21 zorder 2
  show natsuki 4g at t22 zorder 2
  m "Ты же Нацуки, верно?"
  show monika 1c at t21 zorder 2
  show natsuki 4p at f22 zorder 2
  stop music
  play music t7
  n "Да, и что с того?"
  show natsuki 4o at t22 zorder 2
  "Лицо Нацуки скривилось от злости."
  show monika 1g at f21 zorder 2
  m "Пожалуйста перестань."
  m "Если ты не хочешь ехать, не обязательно лезть к другим людям. Ты же просто можешь не пойти завтра в школу, не так ли?"
  show monika 1f at t21 zorder 2
  show natsuki scream at f22 zorder 2
  n "Да..это так..но-"
  show monika 1d at t21 zorder 2
  "Глаза Моники опустели, Нацуки хотела что-то сказать, но по её выражению лица был виден испуг."
  show natsuki 4t at f22 zorder 2
  n "Ладно, пока неудачники!"
  hide natsuki
  play sound door_close
  "С криком Нацуки хлопнула дверью."
  show monika 1b at f22 zorder 2
  show yuri 2e at t21 zorder 2
  stop music fadeout 2.0
  play music t10
  m "Фух, как дитя малое."
  show monika 1j at t22 zorder 2
  show yuri 2f at f21 zorder 2
  y "Моника, ты была неотразимала!"
  show yuri 2e at t21 zorder 2
  show monika 1k at f22 zorder 2
  m "Хах, спасибо."
  hide monika
  hide yuri
  "Подходил вечер."
  "Юри ушла домой одна, так как она очень хотела собраться для завтрашнего дня."
  "Монику, после случая с Нацуки, я больше не видел."
  "Я сидел за своей партой. В классе был только я один."
  stop music fadeout 3.5
  play sound gasp
  "Вдруг я услышал что-то в коридоре."
  mc "Надо посмотреть что там."
  scene bg schoolcorridor2
  with wipeleft_scene
  "Я вышел из класса и никого не увидел."
  mc "Я точно что-то слышал."
  play music mend
  scene bg class 
  with wipeleft_scene
  "Я пошёл к своей парте, на ней лежал листок."
  mc "Что он тут делает? Сюда же никто не заходил. Может это из-за того, что я открыл окно."
  "Я решил прочитать, что было написано на листке."
  call showpoem (poem1, track=audio.poem, where=truecenter) from _call_showpoem_6
  play music t10 fadein 2.5
  mc "Довольно странно."
  "Я положил листок себе в карман и пошел к выходу."
  scene black
  with dissolve_scene_full
  m "Где же я могла оставить свой учебник?"
  "Слышится шорох."
  m "Кто там?"
  scene bg schoolcorridor2
  with dissolve_scene
  show monika 1c at t11 zorder 2
  "Моника подходит к стенке, там сидела Нацуки."
  m 1d "Ты что тут делаешь?"
  show monika 1c at t21 zorder 2
  show natsuki scream at f22 zorder 2
  stop music fadeout 2.0
  play music t6
  n "Мать вашу!!!!"
  n 1h "А, это ты. Что хотела?"
  show monika 1d at f21 zorder 2
  show natsuki 1i at t22 zorder 2
  m "Я просто искала свой учебник."
  show monika 1c at t21 zorder 2
  show natsuki 1h at f22 zorder 2
  n "А разве он не в классе?"
  show natsuki 1i at t22 zorder 2
  show monika 1b at f21 zorder 2
  m "А ведь, точно."
  show monika 1a at t21 zorder 2
  "Нацуки посмотрела на Монику, Моника ответила тем же."
  show monika 1b at f21 zorder 2
  m "Что-то не так?"
  show monika 1a at t21 zorder 2
  show natsuki 1q at f22 zorder 2
  n "Ты чего за учебником не идёшь?"
  show monika 1k at f21 zorder 2
  show natsuki 1i at t22 zorder 2
  m "Я думаю, что кто-то не хочет чтобы я уходила."
  show monika 1j at t21 zorder 2
  show natsuki 1o at f22 zorder 2
  "Нацуки подавилась кофе."
  show natsuki 1p at f22 zorder 2
  n "Ещё чего?!"
  show natsuki 1n at t22 zorder 2
  show monika 1l at f21 zorder 2
  m "Я конечно не против остаться, но раз ты настаиваешь."
  show natsuki 1m at f22 zorder 2
  show monika 1m at t21 zorder 2
  n "Ладно, садись."
  show monika 5a at f21 zorder 2
  show natsuki 1n at t22 zorder 2
  m "Ага~"
  hide monika
  hide natsuki
  stop music fadeout 5.0
  "Нацуки разговаривала с Моникой почти до самого вечера."
  scene black 
  with dissolve_scene
  "{w=2}{nw}Я вернулся домой и сразу улегся на кровать, и через минуты три я заснул."
  scene bg bedroom
  with dissolve_scene
  play music t6
  mum "[player], просыпайся."
  mc "Я встаю уже."
  mum "Ну ты соня, ей богу."
  mc "Я виноват что постоянно спать хочу?"
  mum "Ты же помнишь, что у тебя сегодня важный день?"
  mc "Да, конечно помню. Думаешь я такое забуду?"
  mum "Ну кто тебя знает."
  mum "Пошли завтракать."
  mc "Хорошо."
  scene bg kitchen
  with wipeleft_scene
  "Вдруг послышался звонок в дверь."
  mum "Пойду открою, а ты садись ешь."
  mc "Не указывай мне как ребёнку."
  mum "Ну а кто ты для меня? Кто как не ребенок!"
  "С усмешкой сказала мама."
  mc "Между прочем, я уже взрослый человек и должен сам за собой ухаживать, даже если ты моя мама."
  mum "Какой серьёзный."
  "Пробормотав она подошла к двери."
  mum "Это ты Юри. Привет."
  y "О, здравствуйте, можно к вам зайти?"
  "На лице Юри был виден красный румянец."
  mum "Конечно, не стесняйся."
  y "Хорошо, только не смотрите на меня так все."
  mum "Уфуфу."
  "С усмешкой мама проводит Юри к столу."
  show yuri 2e at t11 zorder 2
  mc "Привет Юри. Я смотрю приходить ко мне домой, вошло у тебя в привычку?"
  y 2f "Я просто.."
  show yuri 2e at t11 zorder 2
  mum "Ладно, не буду вам мешать. Мне ещё на работу собраться надо."
  "Мама собралась и выходя из дома сказала чтобы я не опоздал в школу заговариваясь."
  mum "Пока ребятишки."
  y 2f "Дос-видания."
  show yuri 2e at t11 zorder 2
  mc "Пока мам."
  play sound closet_close
  stop music fadeout 1.0
  scene bg residential_day
  with dissolve_scene
  play music t10
  show yuri 1a at t11 zorder 2
  "Мы с Юри собрав вещи пошли в школу. По дороге нас встретила Моника."
  show monika 1l at f22 zorder 2
  show yuri 1a at t21 zorder 2
  m "Привет, ребята!"
  "Вся впопыхах крикнула Моника, видимо она пыталась нас догнать."
  show monika 1l at t22 zorder 2
  mc "Привет Моника. Ты за нами бежала?"
  show monika 1b at f22 zorder 2
  m "Это уже не важно."
  show monika 1a at t22 zorder 2
  "Мне казалось, что она может упасть в любую минуту. Я её придерживал за руку весь путь чтобы если ей станет плохо, то она бы не упала и не рассшиблась."
  scene bg park
  with wipeleft_scene
  "Мы уже подходили к школе. Люди только начали собираться."
  stop music fadeout 1.0
  scene bg schoolcorridor2
  with wipeleft_scene
  play music t8
  "Я решил сходить в класс за книгой, которую я хотел подарить свой маме."
  "Но вчера я так устал, что совсем забыл про неё."
  mc "Я пойду схожу в класс. А вы тут подождите."
  show yuri 1d at f21 zorder 2
  y "Хорошо."
  show yuri 1c at t21 zorder 2
  show monika 1b at f22 zorder 2
  m "Ага."
  show monika 1a at t21 zorder 2
  hide monika
  hide yuri
  stop music fadeout 2.0
  "В это время школа была практически пуста."
  "По дороге в класс я никого не встретил."
  scene bg class
  with wipeleft_scene
  play music t10
  mc "Так прохладно."
  "Видимо класс кто-то проветривал и доносился запах свежести." 
  "Было так приятно. Маленький холодок прошел по моей коже и мне сразу стало хорошо."
  mc "Хм, что это?"
  "Я увидел, что на моей парте лежит листок, точно такой же что был и вчера."
  call showpoem (poem2, track=audio.poem, where=truecenter) from _call_showpoem_7
  play music t10 fadein 2.5
  "Я опять подумал, что это просто чья-то шутка, и не стал заморачиваться на счет этого. Я достал книгу и пошел к выходу."
  scene bg street
  with dissolve_scene_full
  show yuri 1ba at t31 zorder 2
  show monika 1ba at t32 zorder 2
  show natsuki 1ba at t33 zorder 2
  "Юри и Моника сидели и наслаждались хорошей погодой, с ними сидела Нацуки."
  mc "Я вернулся."
  show yuri 1bb at f31 zorder 2
  y "С возвращением."
  show yuri 1ba at t31 zorder 2
  show monika 1bb at f32 zorder 2
  m "Ага."
  show monika 1ba at t32 zorder 2
  show natsuki 1bb at f33 zorder 2
  n "Скоро все соберутся и мы поедем."
  show natsuki 1ba at t33 zorder 2
  mc "Хорошо."
  hide yuri
  hide monika
  hide natsuki
  "Я не спрашивал почему Нацуки так дружелюбно вела себя. Я наслаждался голубым небом."
  scene bg bus
  with wipeleft_scene
  "Где-то через минут 10, мы поехали." 
  "Я сел рядом с Юри. Моника села с Нацуки. Мы разговаривали обо всем чем можно."
  scene bg bus_evening
  "Прошло около пол дня и мы приехали. Уже наступил вечер." 
  scene bg hotel
  with dissolve_scene
  "Наш класс остановился в отеле Ивашиба."
  "После ночи в отеле, экскурсовод позвал нас к выходу."
  show yuri 2bb at t11 zorder 2
  y "Наконец-то мы дождались все этого момента."
  show yuri 2ba at t21 zorder 2
  show monika 2bb at f22 zorder 2
  m "Ага, я с тобой согласна."
  show yuri 2ba at t31 zorder 2
  show monika 2ba at t32 zorder 2
  show natsuki 1bd at f33 zorder 2
  n "Идём уже скорее!"
  hide yuri
  hide monika
  hide natsuki
  stop music fadeout 1.0
  scene bg castle_outside
  with wipeleft_scene
  play music t6
  "Итак мы вышли из отеля и пошли к замку."
  show yuri 2bf at t31 zorder 2
  show monika 1bd at t32 zorder 2
  show natsuki 1bk at t33 zorder 2
  "Как только мы увидели замок все девушки ахнули."
  show yuri 2bf at f31 zorder 2
  y "Он такой старый."
  show yuri 2be at t31 zorder 2
  show monika 1bd at f32 zorder 2
  m "И замшелый."
  show monika 1bc at t32 zorder 2
  show natsuki 1bl at f33 zorder 2
  n "И такой разваленный!"
  show natsuki 1bj at t33 zorder 2
  show monika 1bg at f32 zorder 2
  m "Ну не такой он уж и разваленный, Нацуки. Он потерпел атаки и его долго восстанавливали рабочие. Так что ты должна ценить то, что он сейчас стоит на этой земле."
  show monika 1bf at t32 zorder 2
  mc "Ну что ж, зайдём уже?"
  show yuri 1bh at f31 zorder 2
  y "И правда, пошли. Мне уже интересно что внутри."
  show yuri 1bi at t31 zorder 2
  show monika 1bk at f32 zorder 2
  m "[player], Юри, надо же ведь насладиться каждой частью этого замка, потому что такое даётся бесплатно один раз в жизни и возможно ты больше не захочешь сюда приехать."
  show monika 1bj at t32 zorder 2
  show natsuki 1bh at f33 zorder 2
  n "Ну ладно пошли. Этой частью я уже насладилась."
  show natsuki 1bg at t33 zorder 2
  guide "Зайдём внутрь. Вы ещё не увидели самой красоты."
  scene bg castle1
  with wipeleft_scene
  "Итак мы зашли внутрь."
  "Внутри всё выглядело так, будто бы этот замок нарисован или как картинка в книге по истории."
  show yuri 2bf at f31 zorder 2
  y "Вот это я называю живопись."
  show yuri 2be at t31 zorder 2
  show monika 1bb at f32 zorder 2
  m "Ага."
  show monika 1ba at t32 zorder 2
  show natsuki 2bb at f33 zorder 2
  n "Что тут живописного?"
  show natsuki 2ba at t33 zorder 2
  show yuri 1be at t31 zorder 2
  show monika 1bc at t32 zorder 2
  "Юри и Моника так посмотрели на Нацуки с удивлением."
  show natsuki 2bb at f33 zorder 2
  n "Это просто комната сделанная из разломанных камней, а также всё в леанах и мхе и много пыли."
  show natsuki 2ba at t33 zorder 2
  "Нацуки опять завелась..."
  show monika 1bd at f32 zorder 2
  m "Ну Нацуки, видимо ты не понимаешь живописи."
  show monika 1bc at t32 zorder 2
  show natsuki 2bb at f33 zorder 2
  n "А это разве назовёшь живописью?"
  show natsuki 2ba at t33 zorder 2
  show yuri 1bf at f31 zorder 2
  y "Существуют разные типы живописи и это один из них."
  show yuri 1be at t31 zorder 2
  show natsuki 2bc at f33 zorder 2
  n "Я всё равно не понимаю живописи."
  show natsuki 2ba at t33 zorder 2
  show monika 1bb at f32 zorder 2
  m "Ну, ничего. Ты ещё научишься понимать всё это со временем."
  show monika 1ba at t32 zorder 2
  show yuri 1bb at f31 zorder 2
  y "Может, если появится свободное время, то мы обязательно съездим ещё куда-нибудь все вместе. Правда ГГ, Моника?"
  show yuri 1ba at t31 zorder 2
  show monika 1bb at f32 zorder 2
  m "Да."
  show monika 1ba at t32 zorder 2
  mc "Ага. Возможно даже на летних каникулах."
  show natsuki 1bc at f33 zorder 2
  n "А куда мы тогда пое~{nw}"
  show yuri 1be at t31 zorder 2
  show monika 1bc at t32 zorder 2
  show natsuki 1bg at t33 zorder 2
  stop music
  play music t9
  guide "Ну что же вы стоите? Время уже вышло, пора на автобус."
  "Мы опять заговорились и не заметили как все уже ушли на автобус."
  scene bg bus_outside
  with wipeleft_scene
  "Сбегав за вещами в отель, мы вернулись к автобусу."
  show yuri 1ba at t31 zorder 2
  show monika 1bb at f32 zorder 2
  show natsuki 1bi at t33 zorder 2
  m "Успели слава богу."
  show monika 1ba at t32 zorder 2
  show yuri 1bb at f31 zorder 2
  y "Без нас никуда не уедут."
  show yuri 1ba at t31 zorder 2
  show natsuki 1bh at f33 zorder 2
  n "Надеюсь больше такой поездки не будет."
  show natsuki 1bi at t33 zorder 2
  "Она это еле-еле промямлила, но все её хорошо услышали."
  show yuri 1bb at f31 zorder 2
  y "Твоё мнение изменится в ближайшем будущем."
  hide yuri
  hide monika
  hide natsuki
  scene bg bus
  with wipeleft_scene
  "Мы сели на автобус."
  "Приехали мы быстро, время пролетело незаметно."
  "По дороге Нацуки крепко спала, а Моника и Юри приглядывали за ней чтобы она не ударилась при тряске."
  stop music fadeout 1.0
  scene black
  with dissolve_scene_full
  "{w=1}{nw} Наступило утро. Всё было как обычно, я поел, собрался и пошел в школу."
  scene bg kitchen
  with wipeleft_scene
  "Телевизор" "Сегодня утром было обнаружено тело ученицы старшей школы Сейва. Были обнаружены ножевые ранения." 
  "Телевизор" "На распознавание личности можете позвонить по номеру на экране. Будем благодарны любой помощи по поиску преступника."
  mc "Что?"
  play music monika_ct
  "На экране была отчетливо видна девушка, похожая на Монику."
  scene black
  with dissolve_scene
  "Мир будто провалился подомной." 
  "Как такое могло произойти?" 
  "Кто убийца? Зачем?" 
  show screen tear(20, 0.1, 0.1, 0, 40)
  pause 0.25
  hide screen tear
  scene bg glitch
  "Как это связано с Моникой?"
  show screen tear(20, 0.1, 0.1, 0, 40)
  pause 0.25
  hide screen tear
  scene bg trainstop
  "Голоса людей продолжали обсуждать этот инцидент. Где-то вдалеке были слышны крики и звуки полицейской сигнализации." 
  "Репортеры набрасывались на полицейских с вопросами. И все это сопровождалось под звуки только что уехавшего поезда."
  show screen tear(20, 0.1, 0.1, 0, 40)
  pause 0.25
  hide screen tear
  scene bg glitch
  show monika 1d at t11 zorder 1
  "Скажи мне...Что ты хочешь изменить?"
  hide monika
  scene black
  stop music fadeout 1.0
  scene bedroom
  with dissolve_scene_full
  play music monika_ct2
  mc "Уже утро?"
  "Меня разбудил громкий звонок будильника." 
  scene bg kitchen
  with wipeleft_scene
  "Я пошел на кухню, на столе лежала записка."
  "'Еда и обед в холодильнике, сегодня у меня смена, так что домой приду поздно. Не перенапрягайся, хорошо? Мама'"
  mc "Хорошо."
  "Я поел, собрался и пошел в школу." 
  play sound door_close
  scene bg park2
  with wipeleft_scene
  "День сегодня был довольно темный из-за облаков на небе. Будто что-то потухло в этом мире. Но что?"
  scene bg schoolcorridor1
  with wipeleft_scene
  mc "Наконец-то я пришел.. Погода такая отвратительная."
  scene bg class
  with wipeleft_scene
  "Я сел за парту и начал доставать учебники. Ко мне подошла Ханако-сан."
  h "Слушай [player], мне надо занести очень много учебников в класс искусства, не мог бы ты мне помочь?"
  mc "Хорошо."
  h "Огромное спасибо."
  scene bg schoolcorridor2
  with wipeleft_scene
  "Мы с Ханокой-сан взяли учебники и пошли в класс. По её лицу было видно, что ей было неловко. "
  mc "А где находится класс искусства?"
  h "Мы почти пришли."
  scene bg drawing_class
  with wipeleft_scene
  "Мы зашли в какой-то класс. Он словно был заброшен, все было в пыли. Дышать в классе было просто невозможно, я решил открыть окно."
  mc "Куда ложить книги?"
  h "Вот сюда."
  "Ханако показала на парту которая стояла посередине класса."
  h "Ой прости [player], я забыла взять список. Сейчас приду."
  mc "Ага."
  "Сейчас я мог полностью наедине остаться со своими мыслями." 
  "Дул прохладный ветерок, и я даже не заметил как изменилась пасмурная погода на такую красочную."
  "Смотря в окно, я видел людей идущих домой на обед, старшеклассников бегущих на стадионе, девушку сидящую на скамейке."
  "Не знаю почему, но я все это время не отводил от неё глаз. Длинные фиолетовые волосы, высокая, она читала книгу."
  "Я и не заметил как Ханако стояла рядом возле меня. Я резко отскочил."
  h "Прости, я тебя напугала?"
  mc "Немного. Давай забудем, что только что было?"
  h "Хорошо."
  "После минуты молчания, мы с Ханакой-сан пошли в класс."
  "Итак прошел день. Ничего интересного не произошло."
  scene bg street
  with wipeleft_scene
  "Я переобулся и пошел домой. Небо было очень красивое." 
  "Дети бегали по улицам, машины ездили. Всё одно и тоже, ничего не изменилось."
  "Вдруг у меня зазвонил телефон."
  unknown "Алло..?.[player]..?"
  mc "Алло? Кто это?"
  unknown "Мне нужна твоя помощь.."
  mc "Алло? О чём вы говорите? Я не понимаю."
  "Связь была очень плохая, я не мог разобрать, что мне пытались сказать."
  unknown "ха..."
  mc "Что?"
  "Связь окончательно оборвалась."
  mc "Что это значит?"
  stop music fadeout 1.0
  scene black
  with dissolve_scene_full
  "Я быстрым шагом пошел домой. Мама ещё не пришла, я направился в свою комнату. Быстро переоделся и лёг спать, чтобы побыстрей забыть этот кошмар."
  show screen tear(20, 0.1, 0.1, 0, 40)
  pause 0.25
  hide screen tear
  $ style.say_dialogue = style.bold
  "Вытащи меня из этого ада."
  "Я не могу освободить себя от этой боли."
  "Мне кажется, что я так далеко."
  "Словно мне уже не будет дано ещё одного шанса."
  "Всё, что происходит перед глазами, застилает мгла."
  "Скоро всё обрушится, конец совсем уже близко."
  "Я чувствую острую реальность всё больше с каждым днём."
  show screen tear(20, 0.1, 0.1, 0, 40)
  pause 0.25
  hide screen tear
  $ style.say_dialogue = style.normal
  play music t9
  scene bg clouds
  with dissolve_scene
  mc "Сегодня такая хорошая погода."
  "Я стоял на балконе и смотрел за красивым утренним пейзажем. Вдруг я заметил Юри."
  mc "Доброе утро Юри."
  "Она немного испугалась."
  y "Д-Доброе утро. Могу я зайти?" 
  mc "Конечно заходи."
  scene bg kitchen
  with wipeleft_scene
  "Я пошёл встречать Юри. Она выглядела счастливой."
  show yuri 1a at t11 zorder 1
  mc "Юри, всё хорошо?"
  y 1b "Угу. Я просто прикупила чая, который так давно хотела."
  show yuri 1c at t11 zorder 1
  "Она была очень рада этому. Я просто умилялся с этого счастливого личика." 
  mc "Ладно, пошли."
  y 1b "Пошли."
  hide yuri
  play sound door_close
  scene bg residential_day
  with wipeleft_scene
  "Я закрыл дверь и мы пошли в школу. По дороге мы встретили Нацуки." 
  show yuri 1b at f21 zorder 1
  show natsuki 1a at t22 zorder 1
  y "Привет Нацуки."
  show yuri 1a at t21 zorder 1
  show natsuki 1h at f22 zorder 1
  n "Чего вам надо?"
  show natsuki 1i at t22 zorder 1
  mc "Ты наверное не выспалась..."
  show natsuki 1h at f22 zorder 1
  n "Возможно."
  show natsuki 1i at t22 zorder 1
  "Нацуки выглядела уставшей и мы с Юри просто шли рядом." 
  hide yuri
  hide natsuki
  scene bg park
  with wipeleft_scene
  "{i}Прошло 10 минут{/i}"
  "Сегодня Моника нас не встретила, я очень волновался. На душе было неспокойно."
  show yuri 1e at t21 zorder 1
  show natsuki 1a at t22 zorder 1
  n "Ааах..."
  "Нацуки начала зевать, Юри просто стояла рядом со мной." 
  mc "Слушайте, вы не знаете где Моника?"
  show natsuki 1c at f22 zorder 1
  n "Не-а."
  show natsuki 1a at t22 zorder 1
  show yuri 1f at f21 zorder 1
  y "Я тоже. Может у учителя спросить?"
  show yuri 1h at t21 zorder 1
  mc "Точно, тогда после урока я спрошу."
  hide yuri
  hide natsuki
  scene bg class
  with wipeleft_scene
  play sound bell
  "Мы пошли в класс и прозвенел звонок. Пришел учитель и начал объяснять нам тему урока."
  stop music fadeout 5.0
  scene black
  with dissolve_scene
  mc "Наконец-то урок закончился."
  "Я встал со стула и подошел к учителю."
  mc "Учитель, можно у вас кое-что спросить?"
  tchr "Конечно, [player]."
  mc "Вы не знаете где Моника?"
  tchr "А разве она вам не говорила? Моника уехала на 3 дня в Осаку. Не волнуйся, с ней всё хорошо."
  mc "Вот как. Большое спасибо вам."
  tchr "Всегда пожалуйста."
  scene bg class
  with dissolve_scene
  "Я пошел обратно к своей парте и с облегчением вздохнул."
  mc "Хорошо что с Моникой ничего не случилось."
  scene black
  with dissolve_scene_full
  "Мои глаза начали закрываться и я не заметил как заснул."
  "Дождь. Всё было так же как и тогда. То же место, та же погода, та же дата."
  "Я всё же надеюсь, что мне хватит 3 дней, чтобы найти тебя."
  show screen tear(20, 0.1, 0.1, 0, 40)
  pause 0.25
  hide screen tear
  scene glitch
  $ style.say_dialogue = style.bold
  "Люби меня или оставь," 
  "прими меня или отвергни."
  show screen tear(20, 0.1, 0.1, 0, 40)
  pause 0.25
  hide screen tear
  $ style.say_dialogue = style.normal
  scene black
  "Это место где произошла катастрофа 2 летней давности."
  "Мы с Саёри были знакомы с самых ранних лет. Всё было хорошо, мы всегда были вместе. Радовались, веселились, помогали друг другу. Но однажды..." 
  "Саёри была влюблена в Кагую, самого красивого парня и хулигана школы. Было много слухов о том, что он просто использует девушек в своих целях." 
  "Кагуя заметил как Саёри смотрит на него и решил предложить ей встречаться. Её счастью не было границ." 
  "Я пыталась хоть как-то её отговорить не встречаться с ним, но это была её первая любовь, а она обычно слепа."
  "Саёри считала, что Кагуя - это смысл её никчемной жизни."
  "Они встречались где-то месяц, Саёри вся расцвела, а Кагуя казалось бы менялся с лучшую сторону."
  "Но счастье Саёри длилось не так долго." 
  "Однажды она застукала Кагую который целовался с учительницей, все чувства мигом пропали, сердце начало бешенно колотиться от душераздирающей боли."
  "Из глаз Саёри потекли слезы и она убежала. Всю ночь она не могла заснуть, на следующий день Кагуя вел себя как обычно, но при этом позвал куда-то Саёри после школы." 
  "Оказалось он сделал это ради того, чтобы избить Саёри и рассстаться с ней." 
  "Она вернулась домой поздно, все волновались за неё, а она лишь пошла и закрылась в своей комнате." 
  "Оттуда были слышны всхлипы, я знала что ей надо было побыть одной." 
  "На следующий день родители сказали, что мне нужно уехать в другой город на неделю к своей бабушке. Я не хотела оставлять Саёри, но пришлось." 
  "Я даже не думала что произойдет то, чего Саёри так сильно боялась." 
  "Она впала в депрессию и начала резать себе вены, её родители пытались помочь, но все тщетно. В школе её начали обсуждать и гнобить." 
  "Прошла неделя. Я стою около клумбы с розами и жду Саёри. Она сказала, что придёт встретить меня. Проходит 15 минут, 30 минут, но её все нет." 
  "Я поворачиваюсь, слышу крики и звук тормозов." 
  "На земле лежало окровавленное тело Саёри, её сбила машина. Кровь была повсюду, люди сразу же начали звонить в скорую." 
  "Через 10 минут Саёри забрали. Водитель сказал, что она сама бросилась под машину и он ничего не успел сделать." 
  "Я каждый день приходила к ней в палату, но шанс что она выживет очень мал. Можно сказать, что она впала в кому."
  show screen tear(20, 0.1, 0.1, 0, 40)
  pause 0.25
  hide screen tear
  scene glitch
  "Это была моя вина."
  "Я не помогала Саёри." 
  "Теперь этот грех лежит на моих плечах..." 
  "От него не избавиться, как бы я не хотела.."
  show screen tear(20, 0.1, 0.1, 0, 40)
  pause 0.25
  hide screen tear
  scene black
  "Я решила, что будет лучше если мы никогда не встретимся, поэтому уехала в Токио. Даже сейчас я не знаю очнулась она или нет." 
  #scene tbc
  #with dissolve_scene_full
  #"Продолжение следует..."
  #scene black 
  #with dissolve_scene_full
  return
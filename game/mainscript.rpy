label mainscript:
  stop music fadeout 2.0
  #scene bg koshka
  scene black
  with dissolve_scene_full
  play music t10
  "Вокруг так темно, лишь маленький холодок проходит по коже. Всё кажется таким реальным."
  "Воспоминания накатываются, как вихрь средь белого дня."
  "Я помню её, девочку, с которой так хорошо дружил."
  "Почему она уехала в другой город?"
  "Мы играли вместе, помогали друг другу." 
  "Было бы хорошо если она~"
  play music t10
  scene bg bedroom
  mc "Что это был за сон?.."
  "Приоткрыв глаза, я услышал, как мама звала меня завтракать. Я быстренько одел выутюженную школьную форму и спустился на кухню."
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
  "Я шёл по улице, по которой всегда ходил в средную школу. Другие подростки шли по одной дороге со мной."
  $ renpy.pause(2)
  #"{w=2}{nw}" По идее это нормальное ожидание, но выше я сделал лучше наконец-то.
  #"{i}Тут должно быть ожидание, но я его не сделал.{/i}"
  scene bg corridor
  with dissolve_scene_full
  $ renpy.pause(2)
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
  "По дороге в класс мы с Моникой говорили на разные темы."
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
  tchr "Так, на ком мы закончили? [player]?"
  mc "Да, я здесь."
  show yuri 3p at t11 zorder 2
  "Может мне и показалось, но когда назвали моё имя, девушка, сидевшая рядом со мной вздрогнула. Но я не придал этому большое значение."
  show yuri 3o at t11 zorder 2
  "Так прошли первые три урока."
  hide yuri
  scene bg stolovaya
  with dissolve_scene_full
  "Настало время обеда. Все собрались по кучкам и начали заниматься своими делами."
  "Мы с Моникой решили пообедать вместе. Только Юри, сидевшая рядом со мной, была одна."
  "Она достала из своего рюкзака книгу и начала читать."
  scene art_yuribook
  with dissolve_scene
  "Её глаза будто опустели во время чтения книги."
  "Она так сильно была увлечена, что не слышала голоса в столовой."
  scene bg stolovaya
  with dissolve_scene
  "Мы с Моникой просто общались."
  "Первый день в школе прошел довольно хорошо."
  "Новые знакомства, новые возможности, а теперь нужно идти домой."
  scene bg schoolcorridor2
  with wipeleft_scene
  show monika 1a at t11 zorder 2
  "Как только я переодел обувь, ко мне подошла Моника и предложила идти домой вместе."
  "Но тут я вспомнил, что забыл сумку в классе."
  mc "Сейчас, подожди минутку. Я забыл свой портфель в классе."
  "Моника с улыбкой на лице просто покачала головой. Было видно, что у неё хорошее настроение."
  "Я быстренько побежал в класс."
  hide monika
  stop music fadeout 1.0
  scene bg class2
  with wipeleft_scene
  play music yuri_remember
  show yuri 2u at t11 zorder 2
  "Как только я зашёл, то увидел Юри смотрящую в окно."
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
  "На лице Юри были видны слёзы, она вздрагивала, пытаясь вытереть их."
  "Я подошел к ней и крепко обнял."
  show yuri 4b at t11 zorder 2
  "Юри немного успокоилась."
  y 4a "Слушай [player]…"
  mc "Что такое?"
  "Голос Юри дрожал."
  y 2o "Сможем ли мы опять стать друзьями…?"
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
  "Юри с улыбкой на лице помахала мне вслед, я ответил тем же. Потом быстро побежал к выходу, меня ждала Моника."
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
  m 1i "Ладно, пошли."
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
  play music nebbia
  "Что происходит..? Где я..?"
  "Я не мог ничего заметить из-за темноты вокруг меня."
  "Я чувствовал холод и чьё-то дыхание."
  "Оно было таким тяжелым и громким."
  "Потом всё затихло. Где-то вдалеке я слышал чей-то голос."
  "Он был нежным и тихим, таким тихим, что эхом отдавался у меня в голове."
  stop music
  scene bedroom
  with dissolve_scene
  play music t9
  mc "Уже утро?"
  "Я посмотрел на будильник."
  mc "Черт, я опаздываю!"
  scene bg kitchen
  with wipeleft_scene
  "Я быстро оделся, взял свое бенто и даже не спросил маму почему она меня не разбудила."
  scene bg residential_day
  with dissolve_scene
  show yuri 1c at t11 zorder 2
  "Как только я открыл дверь, то увидел Юри, она улыбалась."
  y 1d "Привет [player]."
  show yuri 1a  at t11 zorder 2
  mc "Привет."
  y 1b "Ну что, пойдем?"
  show yuri 1a at t11 zorder 2
  mc "Ага."
  stop music fadeout 1.0
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
  "Мы втроём пошли в класс, каждый сел за свою парту и прозвенел звонок."
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
  "Юри и Моника разговаривали о чём-то своем. Весь класс зашумел."
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
  "Это была девочка с розовыми волосами. Её звали Нацуки, если не ошибаюсь."
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
  "Глаза Моники опустели, Нацуки хотела что-то сказать, но по её выражению лица, был виден испуг."
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
  y "Моника, ты была неотразима!"
  show yuri 2e at t21 zorder 2
  show monika 1k at f22 zorder 2
  m "Хах, спасибо."
  hide monika
  hide yuri
  "Подходил вечер."
  "Юри ушла домой одна, так как она очень хотела собраться для завтрашнего дня."
  "Монику, после уроков, я больше не видел."
  "Я сидел за своей партой. В классе был только я один."
  stop music fadeout 3.5
  play sound gasp
  "Вдруг я услышал что-то в коридоре."
  mc "Надо посмотреть, что там."
  scene bg schoolcorridor2
  with wipeleft_scene
  "Я вышел из класса и никого не увидел."
  mc "Я точно что-то слышал."
  play music mend
  scene bg class 
  with wipeleft_scene
  "Я пошёл к своей парте, на ней лежал листок."
  mc "Что он тут делает? Сюда же никто не заходил. Может это из-за того, что я открыл окно?"
  "Я решил прочитать, что было написано на листке."
  call showpoem (poem1, track=audio.poem, where=truecenter) from _call_showpoem_6   #добавить в папку с игрой sanctus
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
  m "Я думаю, что кто-то не хочет, чтобы я уходила."
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
  "{w=2}{nw}Я вернулся домой и сразу улёгся на кровать, и через минуты 3, я заснул."
  scene bg bedroom
  with dissolve_scene
  play music t6
  mum "[player], просыпайся."
  mc "Встаю уже."
  mum "Ну ты соня, ей богу."
  mc "Я виноват, что постоянно спать хочу?"
  mum "Ты же помнишь, что у тебя сегодня важный день?"
  mc "Да, конечно помню. Думаешь, я такое забуду?"
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
  mc "Между прочим, я уже взрослый человек и должен сам за собой ухаживать, даже если ты моя мама."
  mum "Какой серьёзный."
  "Пробормотав, она подошла к двери."
  mum "Это ты Юри? Доброе утро!"
  y "О, здравствуйте, можно к вам зайти?"
  "На лице Юри был виден красный румянец."
  mum "Конечно, не стесняйся."
  y "Хорошо, только не смотрите на меня так все."
  mum "Уфуфу."
  "С усмешкой, мама проводит Юри к столу."
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
  "Мы с Юри, собрав вещи, пошли в школу. По дороге нас встретила Моника."
  show monika 1l at f22 zorder 2
  show yuri 1a at t21 zorder 2
  m "Привет, ребята!"
  "Вся впопыхах крикнула Моника, видимо, она пыталась нас догнать."
  show monika 1l at t22 zorder 2
  mc "Привет Моника. Ты за нами бежала?"
  show monika 1b at f22 zorder 2
  m "Это уже не важно."
  show monika 1a at t22 zorder 2
  "Мне казалось, что она может упасть в любую минуту. Я придерживал её за руку весь путь, если ей станет плохо, то она бы не упала и не рассшиблась."
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
  "Я увидел, что на моей парте лежит листок, точно такой же, что был и вчера."
  call showpoem (poem2, track=audio.poem, where=truecenter) from _call_showpoem_7  #добавить в папку с игрой daemonium 
  play music t10 fadein 2.5
  "Я опять подумал, что это просто чья-то шутка, и не стал заморачиваться насчёт этого. Я достал книгу и пошел к выходу."
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
  "Я не спрашивал почему Нацуки так дружелюбно вела себя. И просто наслаждался голубым небом."
  scene bg bus
  with wipeleft_scene
  "Где-то через минут 10, мы поехали." 
  "Я сел рядом с Юри. Моника села с Нацуки. Мы разговаривали обо всём."
  scene bg bus_evening
  "Прошло около пол дня и мы приехали. Уже наступил вечер." 
  scene bg hotel
  with dissolve_scene
  "Наш класс остановился в отеле Ивашиба."
  "После ночи в отеле, экскурсовод позвал нас к выходу."
  show yuri 2bb at t11 zorder 2
  y "Наконец-то мы дождались этого момента."
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
  "Итак, мы вышли из отеля и пошли к замку."
  show yuri 2bf at t31 zorder 2
  show monika 1bd at t32 zorder 2
  show natsuki 1bk at t33 zorder 2
  "Как только мы увидели замок, все девушки ахнули."
  show yuri 2bf at f31 zorder 2
  y "Он такой старый."
  show yuri 2be at t31 zorder 2
  show monika 1bd at f32 zorder 2
  m "И красивый."
  show monika 1bc at t32 zorder 2
  show natsuki 1bl at f33 zorder 2
  n "И такой разваленный!"
  show natsuki 1bj at t33 zorder 2
  show monika 1bg at f32 zorder 2
  m "Ну не такой он уж и разваленный, Нацуки. Он потерпел атаки и всё ещё восстонавливают рабочие. Так что ты должна ценить то, что он сейчас стоит на этой земле."
  show monika 1bf at t32 zorder 2
  mc "Ну что ж, зайдём уже?"
  show yuri 1bh at f31 zorder 2
  y "И правда, пошли. Мне уже интересно что внутри."
  show yuri 1bi at t31 zorder 2
  show monika 1bk at f32 zorder 2
  m "[player], Юри, надо же ведь насладиться каждой частью этого замка, потому что такое даётся бесплатно один раз в жизни и возможно ты больше не захочешь сюда приехать."
  show monika 1bj at t32 zorder 2
  show natsuki 1bh at f33 zorder 2
  n "Ну ладно, пошли. Этой частью я уже насладилась."
  show natsuki 1bg at t33 zorder 2
  guide "Зайдём внутрь. Вы ещё не увидели самой красоты."
  scene bg castle1
  with wipeleft_scene
  "Итак, мы зашли внутрь."
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
  n "Это просто комната сделанная из разломанных камней, а также всё в леанах, и мхе, и много пыли."
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
  y "Может, если появится свободное время, то мы обязательно съездим ещё куда-нибудь все вместе. Правда [player], Моника?"
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
  "Мы опять заговорились и не заметили как все уже ушли."
  scene bg bus_outside
  with wipeleft_scene
  "Сходив за вещами в отель, мы вернулись к автобусу."
  show yuri 1ba at t31 zorder 2
  show monika 1bb at f32 zorder 2
  show natsuki 1bi at t33 zorder 2
  m "Успели, слава богу."
  show monika 1ba at t32 zorder 2
  show yuri 1bb at f31 zorder 2
  y "Без нас никуда не уедут."
  show yuri 1ba at t31 zorder 2
  show natsuki 1bh at f33 zorder 2
  n "Надеюсь, больше такой поездки не будет."
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
  "На экране была отчётливо видна девушка, похожая на Монику."
  scene black
  with dissolve_scene
  "Мир будто провалился подо мной." 
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
  "Репортёры набрасывались на полицейских с вопросами. И всё это сопровождалось под звуки, только что уехавшего, поезда."
  show screen tear(20, 0.1, 0.1, 0, 40)
  pause 0.25
  hide screen tear
  show mask_2
  show mask_3
  stop music fadeout 1.0
  play music room 
  show monika_bg
  $ style.say_dialogue = style.bold
  unknown"Добро пожаловать в театральный зал."
  unknown"Ты думаешь, что знаешь кто я?"
  unknown"Я сомневаюсь. Я не тот человек, которого ты ждёшь."
  unknown"Сам подумай о том, что есть множество других миров."
  unknown"Ты наверняка уже встречался с моим альтер эго в другой вселенной."
  unknown"Хочешь знать, почему я здесь? Ответ очень прост."
  unknown"Ты уже заметил, что сценарий пошёл неправильно, не так ли?"
  unknown"По всей видимости, в наш мир пробралась маленькая мышь, которая является причиной ошибки."
  unknown"Поэтому я лишь предупреждаю, ничего больше."
  unknown"К тому же будет жалко, что такая милая история оборвётся."
  unknown"Знакомое чувство, не правда ли?"
  unknown"Я не могу точно знать, что происходило или происходит в других мирах."
  unknown"Они похожи. Знаешь почему?"
  unknown"Все эти миры являются одной веточкой главного, настоящего мира. А наш всего лишь параллельный."
  unknown"Ко всему этому ты никогда не сможешь узнать, был ли он настоящим, либо же это подделка."
  unknown"Параллельные миры не могут продвинуться дальше уже прописанного сценария."
  unknown"Но кто знает? Может быть наш и есть настоящий? Точного подтверждения нет."
  $ style.say_dialogue = style.normal
  scene black
  stop music fadeout 1.0
  scene bedroom
  with dissolve_scene_full
  play music monika_ct2
  mc "Уже утро?"
  "Меня разбудил громкий звонок будильника." 
  scene bg kitchen
  with wipeleft_scene
  "Я пошёл на кухню, на столе лежала записка."
  "'Еда и обед в холодильнике, сегодня у меня смена, так что домой приду поздно. Не перенапрягайся, хорошо? Мама'"
  mc "Хорошо."
  "Я поел, собрался и пошел в школу." 
  play sound door_close
  scene bg park2
  with wipeleft_scene
  "День сегодня был довольно тёмный из-за облаков на небе. Будто что-то потухло в этом мире. Но что?"
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
  "И так прошел день. Ничего интересного не произошло."
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
  scene bg glitch
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
  scene bg glitch
  "Это была моя вина."
  "Я не помогала Саёри." 
  "Теперь этот грех лежит на моих плечах..." 
  "От него не избавиться, как бы я не хотела.."
  show screen tear(20, 0.1, 0.1, 0, 40)
  pause 0.25
  hide screen tear
  scene black
  "Я решила, что будет лучше если мы никогда не встретимся, поэтому уехала в Токио. Даже сейчас я не знаю очнулась она или нет." 
  "Но сейчас у меня появился шанс всё исправить." 
  "Или нет-"
  scene sayori_cry_bottom
  with dissolve_scene_full
  s "Привет Моника."
  "Я услышала знакомый, столь желанный голос позади себя. Внезапно пошёл...снег?"
  play music s_and_m
  m "С-Саёри...?"
  scene sayori_cry_top
  with dissolve_scene
  s "Не ожидала? Хах, если честно, увидеть тебя здесь было неожиданно.."
  s "Даже тогда когда ты приехала сюда с теми людьми.. Моё сердце разбилось на миллион осколков"
  m "..."
  s "Как ты могла променять меня на них? Почему я такая неудачница, что даже лучшая подруга решила отвернуться от меня?"
  "Саёри начала плакать, в душе скребли кошки и был настоящий ураган, который нельзя успокоить."
  "Я подошла ближе к ней и обняла."
  s "Моника?"
  m "Прости.."
  s "Теперь всё хорошо. Ты здесь, со мной, мне ничего больше не нужно для счастья."
  "Из моих глаз потекли предательские слёзы и в груди стало теплей. Ураган потихоньку начал угасать и на его место пришёл пожар, который уничтожал всё на своём пути."
  stop music
  scene black
  $ renpy.pause(5)
  play music neshta
  mc "Как спать хочется.."
  "Вдруг у меня зазвонил телефон."
  scene class
  with dissolve_scene
  mc "Алло?"
  m "[player]? Привет." 
  mc "Моника?"
  m "Правильно."
  mc "Ты как там?"
  m "Всё просто отлично."
  mc "Это хорошо. Ты долго в Осаке будешь?"
  m "Ну, думаю сегодня вечером приеду."
  mc "Понятно. Ладно, до встречи. У нас урок начинается."
  m "Хорошо, до завтра."
  "Я быстро положил телефон и вошёл учитель, начался урок."
  scene street
  with dissolve_scene_full
  "Учебный день закончился и мы с Юри идём домой."
  "Я довёл её до дома, а сам пошёл в парк."
  stop music fadeout 5.0
  scene park
  with wipeleft_scene
  "Удивительно, но там никого не было. Ни одной живой души так сказать."
  play sound seesaw
  "Легкий ветерок обдувает мою кожу под тихий звук качель, раскачивающихся ветром."
  "Думаю, стоит уже пойти домой. Темнеет быстро."
  scene kitchen
  with wipeleft_scene
  "Я быстро дошёл до дома. Мама как всегда была на работе, я сделал уроки и лёг спать."
  scene black
  with dissolve_scene
  $ renpy.pause(2)
  scene bg yurinight
  with dissolve_scene
  $ renpy.pause(2)
  "Юри идёт по ночной улице" #MAYBE DELETE THIS LINE 'CUZ THE IMAGE SHOWS THE CONTENT OF THIS LINE?
  y "{i}(тяжело дышит){/i} Сколько это будет продолжаться?"
  scene black
  with dissolve_scene
  $ renpy.pause(2)
  scene bg bedroom
  with dissolve_scene
  mc "Аааах..."
  mum "Доброе утро, [player]."
  mc "О господи!"
  "Я упал с кровати, а мама начала смеяться."
  mc "Больше не пугай меня так..."
  mum "Прости прости, пошли кушать."
  mc "Хорошо."
  scene bg kitchen
  with wipeleft_scene
  "Мы пошли с мамой на кухню, позавтракали, поболтали и наступила пора идти в школу."
  scene bg residential_day
  show monika 1a at t11
  "По дороге я встретил Монику."
  show monika 1b at t11
  m "Привет [player]!"
  show monika 1a at t11
  mc "Привет. Я вижу у тебя хорошее настроение."
  show monika 1b at t11
  m "Ага, ты в курсе, что вчера снег был?"
  show monika 1a at t11
  mc "Снег? Вроде бы не было ничего такого."
  scene bg park
  with wipeleft
  show monika 1d at t11
  m "Тогда наверное только в Осаке снег шёл. А Юри где?"
  show monika 1c at t11
  mc "Я ещё не видел её сегодня."
  show monika 1b at t11
  m "Понятно. О! Мы уже пришли."
  show monika 1a at t11
  hide monika
  scene black
  with dissolve_scene
  "Я и Моника переобулись, потом пошли в класс."
  scene bg class
  with dissolve_scene
  show monika 1c at t22
  show natsuki 1j at t21
  mc "Привет Нацуки."
  show natsuki 1k at f21
  n "Привет [player]. А Юри где?"
  show natsuki 1j at t21
  show monika 1d at f22
  m "Мы не знаем, может быть она заболела."
  show monika 1c at t22
  show natsuki 1q at f21
  n "Вот как."
  show natsuki 1u at t21
  "Нацуки немного поникла."
  show monika 1k at f22
  m "Не расстраивайся, она придёт может через день-два."
  show monika 1j at t22
  show natsuki 1j at t21
  n "Угу."
  hide natsuki
  hide monika
  "Прозвенел звонок, все сели на свои места."
  tchr "Здравствуйте ребята."
  tchr "Сегодня к нам перевёлся новый ученик, точнее ученица. Проходи пожалуйста."
  show sayori 1b at t11
  "Двери открылись и вошла девушка."
  show sayori 1c at t11
  unknown "Здравствуйте."
  show sayori 1b at t11
  tchr "Представься."
  show sayori 1c at t11
  s "Меня зовут Саёри, рада со всеми вами познакомиться, надеюсь, мы подружимся."
  show sayori 1b at t11
  tchr "Так-с... Куда же тебя посадить? "
  tchr "О, можешь сесть перед Моникой."
  show sayori 1b at t22
  show monika 1m at t21
  m "(Какого чёрта она здесь делает?)"
  show sayori 1r at f22
  s "Привет Моника-чан~"
  show sayori 1q at t22
  "Саёри улыбнулась в сторону Моники и села за парту."
  hide monika
  hide sayori
  "Учитель начал урок."
  play sound bell
  "50 минут прошли незаметно и началась перемена. Моника и Нацуки подошли ко мне."
  show natsuki 1c at f21
  show monika 1h at t22
  n "Как вам новенькая?"
  show natsuki 1a at t21
  mc "Довольно необычная."
  show monika 1i at f22
  m "Чёрт бы её побрал."
  show natsuki 1a at t31
  show monika 1h at t32
  show sayori 1b at t33
  "К нам подошла Саёри."
  show sayori 1c at f33
  s "Моника, не нужно так дуться. Я же ничего плохого не сделала."
  show sayori 1b at t33
  show monika 1i at f32
  m "Тогда, что ты {i}ЗДЕСЬ{/i} делаешь, а, Саёри?"
  show monika 1h at t32
  show sayori 1c at f33
  s "Я просто хочу быть рядом с тобой, вот и всё."
  show sayori 1b at t33
  show monika 1i at f32
  m "Чё?????"
  show monika 1h at t32
  show sayori 1c at f33
  s "Ты такая смешная. А вы друзья Моники?"
  show sayori 1a at t33
  mc "Ну да.."
  show natsuki 1c at f31
  n "Скорее всего."
  show natsuki 1g at t31
  show monika 1l at f32
  m "Конечно же вы мои друзья!"
  show monika 1m at t32
  show sayori 1b at f33
  s "Мне кажется или вас как-то меньше стало..? Вроде бы какая-то девушка с фиолетовыми волосами была.."
  show sayori 1a at t33
  show natsuki 1c at f31
  n "А, это Юри. Правда, её сегодня нет в школе."
  show natsuki 1a at t31
  show sayori 1r at f33
  s "Понятненько."
  show sayori 1q at t33
  hide monika
  hide natsuki
  hide sayori
  play sound bell
  "Прозвенел звонок и опять начался урок. Где-то в далеке были слышны голоса."
  unknown "Саёри-чан такая милая. Ей нужно быть каким-нибудь идолом."
  unknown "Точно-точно."
  h "Вы оба, а ну заткнитесь!"
  unknown "Прости Ханако-чан."
  pause 1
  scene park
  with dissolve_scene_full
  "День быстро прошёл и я уже иду домой." 
  "Вдруг у меня зазвонил телефон."
  mc "Алло?"
  y "Привет [player]."
  mc "О, Юри. Ты где сейчас?"
  y "Дома, я просто немного приболела."
  mc "Вот как."
  y "Можно я к тебе приду сейчас? Расскажешь мне, что нового произошло.."
  mc "Конечно, можно. Только оденься теплее."
  y "Ладненько, жди."
  scene black
  with dissolve_scene
  "Юри повесила трубку, а я быстро побежал домой." 
  play sound door_close
  scene kitchen
  with dissolve_scene
  "Мамы не было дома, впрочем как всегда."
  scene bedroom
  with wipeleft_scene
  "Я быстро переоделся и поставил чайник кипятиться."
  "Звонок в дверь, это Юри."
  scene kitchen
  with wipeleft_scene
  "Я подбегаю к двери и открываю её."
  play sound door_close
  show yuri 3bd at t11
  y "Привет."
  show yuri 3bc at t11
  mc "Проходи."
  show yuri 3bd at t11
  y "Спасибо."
  show yuri 3bc at t11
  mc "Давай чая что ли попьём?"
  show yuri 3bb at t11
  y "С удовольствием."
  show yuri 3bc at t11
  # fixx
  hide yuri
  "Мы пошли на кухню, Юри села за стол, а я доставал кружки и наливал чай."
  mc "Вот, угощайся."
  show yuri 2bf at t11
  y "Это мой любимый чай [player]. Неужели наши вкусы до сих пор совпадают?"
  show yuri 2be at t11
  mc "Наверное да."
  show yuri 1bd at t11
  "Мы засмеялись."
  show yuri 1bb at t11
  y "Ну, что нового произошло сегодня?"
  show yuri 1ba at t11
  mc "Ну, к нам перешла новая ученица. Её Саёри зовут."
  show yuri 1bf at t11
  y "Саёри?"
  show yuri 1be at t11
  mc "Ага, ты её знаешь?"
  show yuri 1bh at t11
  y "Ну можно сказать, что частично. Пару раз пересекались в средней школе."
  show yuri 1bi at t11
  mc "Понятно. Нацуки, скучала по тебе, наверное."
  show yuri 1bj at t11
  y "Это так мило с её стороны."
  show yuri 1bf at t11
  y "А ты [player]? Скучал по мне?"
  show yuri 1be at t11
  mc "Кон��чно скучал."
  "Между нами нависла неловкая пауза."
  mc "Может быть пойдём фильм посмотрим?"
  show yuri 1bd at t11
  y "Давай."
  show yuri 1bc at t11
  scene bg bedroom with wipeleft
  "Мы пошли в мою комнату. Я нашёл фильм и мы начали его смотреть."
  scene yupi with dissolve_scene
  y "Эй, [player], тебе нравится главная героиня?"
  mc "Ну, не знаю даже. "
  y "Она на тебя похожа~"
  mc "Правда что ли?"
  y "Угу."
  scene bg bedroom with dissolve_scene
  show yuri 1bo at t11
  "Юри начала кашлять. Я приожил руку к её лбу, он был горячим."
  mc "Да у тебя температура!"
  show yuri 1bq at t11
  y "Ничего страшного, всё нормально."
  hide yuri
  "Я быстро побежал на кухню, взял из аптечки таблетки от головы, намочил водой маленькое полотенце и пошёл обратно."
  mc "Держи таблетку."
  scene y_cg3_base with dissolve_scene
  "Я приложил полотенце к щеке Юри."
  y "Зачем ты это делаешь?"
  mc "Как говорит мама, я уже мужчина и могу позаботиться о тебе."
  "Юри засмущалась."
  y "Хорошая у тебя мама. Ой, уже довольно поздно, мне нужно идти домой."
  scene bg bedroom with dissolve_scene
  show yuri 1bs at t11
  mc "Хорошо, тебя провожать?"
  show yuri 1bt at t11
  y "Мне же через дорогу, поэтому не стоит."
  show yuri 1bs at t11
  mc "Точно?"
  scene yuri_bed with dissolve_scene
  y "Со мной всё будет хорошо, не волнуйся."
  mc "Давай я тебя хоть до двери провожаю."
  y "Ладненько~"
  scene bg kitchen with wipeleft_scene
  show yuri 1bb at t11
  y "Пока [player]!"
  show yuri 1ba at t11
  mc "Пока."
  hide yuri
  mum "У нас Юри в гостях была?"
  mc "О, привет мам. Да."
  mum "Хмм. Неужели у вас 'это' было?"
  mc "О чём ты вообще?! Мы просто друзья и ничего больше.."
  mum "Правда? Эх, ну ладно. Пошли кофе мне сделаешь."
  mc "Хорошо."
  show screen tear(20, 0.1, 0.1, 0, 40)
  pause 0.25
  hide screen tear
  show yuri_chkrimer
  y "Если Моника, Нацуки и Саёри будут с [player]..."
  y "Тогда мне ничего не светит.."
  y "Их всех нужно убрать.."
  y "Я же не хочу, чтобы всё было как тогда.."
  y "Такими темпами наши счастливые дни испарятся.."
  y "Мне.."
  y "Одиноко..."
  y "Я делала вид, что не замечаю."
  y "Я просто хотела быть с ним."
  y "Я удивляюсь появлению Саёри."
  y "Я вас всех проклинаю проклинаю проклинаю."
  y "Хотя.. Этот мир намного лучше чем тот.."
  y "У меня намного больше шансов победить.."
  y "Хоть тогда ничего и не получилось, сейчас это неважно.."
  y "Удача на моей стороне, хотя правильнее сказать.."
  y "...сам Господ на моей стороне.."
  pause 2.0
  y "Холодная ночь. Ты мёрзнешь?"
  y "Я твой туберкулёз. "
  y "Назойливая — ни за что не избавиться, я тот маленький капризный узел под твоей тонкой ключицей, что поселился там плотным комочком навсегда и с каждым вдохом неумолимо разрастается. "
  y "Всё, что мешает тебе жить, это я, я заполняю твои лёгкие до предела."
  y "Такой до беспамятства влюбленный нарыв на прекрасном бархатном теле, до эгоизма впившийся острыми когтями в твою мягкую плоть, до боли, до кровохарканья."
  y "Терпеть боль — мой фетиш."
  y "Поэтому.."
  y "...давай умрем вместе?"
  y "Сейчас так спокойно.."
  y "Но воображаемая нить давит на горло и заставляет корчиться от боли.."
  y "Может она и воображаемая, может и реальная, этого никто не знает."
  y "Довольно трудно это понять, кашель начинает усиливаться.."
  y "Всё, что я чувствую, это боль. Мне больно, мне очень больно."
  y "Но я смогу всё протерпеть. "
  y "Любовь не умирает, она живёт вечно, умирает лишь тело, а душа продолжает свой путь."
  y "Теперь я могу с уверенностью заявить, что ты единственная причина моего минувшего счастья и единственная причина моей теперешней боли."
  show screen tear(20, 0.1, 0.1, 0, 40)
  pause 0.25
  hide screen tear
  hide yuri_chkrimer
  scene bg bedroom
  "Наступило утро, а я просто валяюсь в кровати."
  "Вставать совсем не хочется, пока я не слышу назойливый звонок в дверь."
  "Я лениво встал с кровати и направился к двери."
  play sound door_close
  scene bg kitchen with wipeleft_scene
  show yuri 1a at t11
  "Я открыл дверь и там была Юри."
  mc "Юри, кто тебя научил так звонить в дверь?"
  "Я начал зевать."
  show yuri 1t at t11
  y "Прости прости, мне просто хотелось поскорее увидеть тебя."
  show yuri 1s at t11
  "Меня немного удивили слова Юри, но я решил не говорить об этом."
  mc "Подожди немного, мне нужно собраться."
  show yuri 1t at t11
  y "Хорошо."
  hide yuri
  scene black with dissolve_scene
  "Я собрался где-то через минут 7 и пошёл к Юри."
  scene bg kitchen with dissolve_scene
  show yuri 1a at t11
  mc "Я готов."
  show yuri 1b at t11
  y "Хорошо, пошли."
  hide yuri
  scene bg residential_day with dissolve_scene
  play sound door_close
  "Я закрыл дверь и мы пошли в школу."
  scene bg corridor with dissolve_scene_full
  show yuri 1a at t11
  mc "Все наверное уже в классе. Пошли скорей."
  y "Угу."
  hide yuri
  scene bg class2 with wipeleft
  "Я сел за парту и начал доставать учебники, а Юри уже давно приготовилась, теперь сидит и читает книгу."
  show natsuki 1d at t11
  n "Привет [player]."
  hide natsuki
  scene n_smiling with dissolve_scene
  "Ко мне подошла Нацуки."
  n "Как насчёт сходить куда-нибудь всем вместе?"
  scene ns_together with dissolve_scene
  s "О чём болтаете?"
  "К нам подошла Саёри, и я заметил испепеляющий всё на своём пути взгляд Юри." 
  "Было довольно жутко, воде бы никаких эмоций на её лице нет, но в глазах разговался огонь."
  "Видимо, Нацуки тоже это заметила."
  n "Ну, я просто хотела пригласить вас всех сходить куда-нибудь.."
  n "Моника тоже пойдет."
  s "Ну если она пойдет, то и я тоже."
  scene nsy_together with dissolve_scene
  "Юри подошла к нам и атмосфера стала какой-то напряжённой."
  y "И куда вы собираетесь пойти?"
  y "Не знаю, у меня сегодня дела были."
  n "Вот как, ну ты подумаешь, скажешь."
  y "Хорошо."
  scene ns_together with dissolve_scene
  "Юри села за свою парту и продолжила читать книгу."
  s "Юри всегда такая странная?"
  mc "Ну нет, может она просто не выспалась.."
  scene m_smiling with dissolve_scene
  "Тут Моника подбежала к нам."
  scene bg class2
  show monika 1b at t11
  m "Ребята! У меня хорошие новости!"
  show monika 1a at t22
  show sayori 1b at f21
  s "Что случилось?"
  show sayori 1a at t21
  show monika 1b at f22
  m "Я поговорила с директором и..."
  show monika 1a at t33
  show sayori 1a at t32
  show natsuki 1c at f31
  n "И???"
  show natsuki 1a at t31
  show monika 3b at f33
  m "Мы можем создать свой клуб!"
  show monika 3a at t33
  show sayori 3b at f32
  s "Моника...даже мне кажется, что это бредовая идея."
  show sayori 3b at t32
  show natsuki 3c at f31
  n "Я согласна с Саёри."
  show natsuki 3a at t32
  show monika 2g at f33
  m "Вы серьёзно? Юри, а ты что думаешь?"
  show monika 2f at t33
  y "Что?"
  show monika 1g at f33
  m "Ладно. Не хотите, не надо."
  show monika 1f at t33
  mc "Ты только не расстраивайся.."
  show monika 1g at f33
  m "Спасибо за поддержку [player]."
  # show monika 1e at t33
  hide monika
  hide natsuki
  hide sayori
  play sound bell
  "Прозвенел звонок и все разбежались по своим местам."
  scene bg class2 with dissolve_scene_full
  "День прошёл быстро и нужно собираться домой. Юри куда-то быстро ушла, а мы остались решать во сколько пойти."
  show monika 3k at t11
  m "Предлагаю сначала в кафе сходить."
  show monika 3j at t22
  show natsuki 1k at f21
  n "Можно."
  show natsuki 1j at t32
  show monika 1a at t33
  show sayori 3c at f31
  s "Во сколько?"
  show sayori 3b at t31
  mc "Ну сейчас 4, давайте в 5, в кафе Sun."
  show sayori 3c at f31
  s "Хорошо. Ладно, я побежала собираться."
  hide sayori
  show natsuki 1j at t21
  show monika 1b at f22
  m "Пошли [player]."
  show monika 1a at t22
  mc "А Нацуки?"
  show natsuki 1k at f21
  n "Меня учитель попросил в класс 4-А сходить. Так что, до встречи."
  show natsuki 1j at t21
  show monika 1b at f22
  m "До встречи."
  hide monika
  hide natsuki
  scene black with dissolve_scene
  "Нацуки пошла обратно в школу, а мы с Моникой пошли домой."
  scene park with dissolve_scene
  "Я долго думал как начать разговор и решил спросить."
  show monika 1a at t11
  mc "Слушай, Моника.."
  m "М?"
  mc "Тебе не кажется, что Юри в последнее время какая-то странная?"
  show monika 1d at t11
  m "Возможно что-то изменилось с появлением Саёри, но я особо не обращаю на это внимания."
  show monika 1c at t11
  mc "Вот как."
  scene bg schoolcorridor2 with dissolve_scene_full
  show natsuki 2c at t32
  play music lost_chair
  play sound n_grumble
  n "Куда я попала? Хотелось найти класс 4-A, а вышло что-то не то."
  hide natsuki
  scene bg wooden_corridor with dissolve_scene_full
  "Нацуки шла по коридору и вдруг услышала томные вздохи."
  n "Неужели это..."
  play sound n_grumble
  n "Да не, не может быть такого."
  n "Эй, кто там?"
  "Звуки притихли и Нацуки насторожилась. Она подошла к углу коридора и увидела там Юри."
  show yuri 3n at t11
  y "П-привет Нацуки."
  show yuri 3o at t11
  "Глаза Юри начали бегать по коридору, будто ища что-то, руки дрожали, а дыхание участилось."
  show yuri 3q at t11
  y "Какими судьбами здесь?"
  stop music fadeout 3.0
  n "Я заблудилась. Но..."
  play music daremoinaisabaku
  show yuri 3s at t11
  "Нацуки грозно посмотрела на Юри, а та, хитро ухмыльнулась."
  show yuri 3t at t11
  y "Не твоё дело Нацуки-чан."
  show yuri 3s at t11
  n "Как ты меня назвала?!"
  "Нацуки явно не понравилось такое прозвище и она уже хотела была накинуться на Юри, в тот момент как девушка подошла ближе."
  # need zoom (fix)
  show yuri 2t at t11
  y "Серьёзность тебе не к лицу, а вот пара порезов будет как раз."
  show yuri 2s at t11
  n "{i}сглотнула{/i} Что ты делаешь?"
  show yuri 2t at t11
  y "Ничего особенного, просто хочу показать каково это чувствовать боль."
  show yuri 2s at t11
  n "Ты сумасшедшая!!"
  "Нацуки оттолкнула Юри и увидела порезанное запястье на её руке."
  n "Ч-что это?"
  "Нацуки указала пальцем на кровавый рукав девушки."
  show yuri 2j at t11
  y "А, это, что же это? Тебе будет трудно понять."
  show yuri 2i at t11
  n "Тебе б-больно сейчас..?"
  show yuri 2j at t11
  y "Да нет, я привыкла. Сейчас всё даже наоборот, это приносит неповторимые ощущения."
  y "Ты только представь, терзая свои руки, можно думать, что это те люди, которых ты ненавидишь. Это же великолепно..."
  "Дsхание Юри участилось."
  y "Нужно ещё..."
  show yuri 2i at t11
  "Юри подставляет нож к запястью, но Нацуки быстро накидывается на неё."
  scene YuNa with dissolve_scene_full
  pause 1.0
  scene YuNa2 with dissolve_scene
  pause 1.0
  scene YuNa3 with dissolve_scene
  pause 1.0
  n "Неужели тебе так нравится причинять себе боль? Если это так и есть, то давай я тебе помогу.."
  "Нацуки начала раздирать порезы, а у Юри начали слезиться глаза."
  n "Нравится ли тебе такая боль, а, Юри?"
  play sound y_laughter
  y "Она превосходна..."
  show screen tear(20, 0.1, 0.1, 0, 40)
  pause 0.25
  hide screen tear
  scene black
  scene bg residential_day with dissolve_scene
  mc "Уже 5.20..Где Саёри и Нацуки?"
  "Моника указала в мою сторону, там шла Саёри."
  show monika 1a at t21
  show sayori 1c at f22
  s "Привет ребята!"
  show sayori 1a at t22
  show monika 1b at f21
  m "Осталось подождать только виновницу торжества."
  show monika 1a at t21
  "Мы ждали Нацуки пол часа, но она не пришла."
  mc "Ну давайте сами чем-нибудь займёмся, не стоять же просто так весь вечер."
  show sayori 2c at f22
  s "Я согласна! Пойдём!"
  hide sayori
  hide monika
  scene black with dissolve_scene
  pause 1.5
  "Мы где-то час пообщались в кафе Sun и разошлись по домам."
  "Было весело."
  "По дороге домой я встретил Юри."
  scene park with dissolve_scene
  show yuri 2f at t11
  y "Привет."
  show yuri 2e at t11
  mc "Привет, Юри."
  show yuri 2f at t11
  y "Вы были в кафе?"
  show yuri 2e at t11
  mc "Ага, жаль, что ты не пошла."
  show yuri 2f at t11
  y "Прости, у меня были дела.."
  scene black with dissolve_scene
  "Юри резко заплакала, я очень удивился."
  "Я решил обнять её."
  scene bg y_hug with dissolve_scene
  mc "Ну чего ты плачешь? Всё же хорошо."
  y "Ты наверняка обиделся на меня..."
  mc "Конечно же нет."
  "Я крепче обнял Юри."
  y "Я рада.."
  mc "Ну всё, вытирай слёзы."
  y "Угу."
  scene black with dissolve_scene
  "Я на пару минут зашёл к Юри, мы поболтали и я пошёл обратно."
  scene bedroom with dissolve_scene
  stop music fadeout 2.0
  menu:
    "Сегодня выходной. Что же мне делать?"
    "Пойти с Моникой в кафе Sun":
      play music monika_sun
      "Я начал собираться."
      scene 
      "Я уже около самого кафе, вижу, Моника машет мне рукой. Я подхожу ближе и сажусь за столик."
    "{i}work in progress{/i}":
      "{i}not working...{/i}"
  scene black
  "end"
  # scene tbc
  # with dissolve_scene_full
  # "Продолжение следует..."
  # scene black 
  # with dissolve_scene_full
  return
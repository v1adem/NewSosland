#Characters:
define du = Character("Думас", color="#c4c4c4")
define d = Character("Думас-Зоркий Глаз", color="#75b4eb")
define b = Character("Бармен", color="#7fc42f")
define y = Character("Управляющая Магазином", color="#fff86b")
define sh = Character("Шиза", color="#b32e2e")

label start:

    scene bg blackground
    "Пролог"
    "Наша история начинается здесь...
    В небольшой пещере, посреди пустыни"
    "Кто-то проснувшись, посмотрел в сторону выхода"
    scene bg cave
    "Этого парня зовут Думас-Зоркий Глаз.
    До недавна он жил в городе шахтеров где-то посреди Техаса.{w=1.0}
    Его жизнь была скучна и легка,
    но вот он лежит {b}пьяный{/b} в темной сырой пещере"
    d "Блять!{w=1.0}
    Срань!{w=1.0}
    Как же болит! Моя бедная голова!"
    "{color=#b32e2e}Голос в голове{/color}" "Похоже кто-то вчера очень перепил..."
    d "Че это?! Кто это говорит?!"
    "{color=#b32e2e}Голос в голове{/color}" "{cps=25}...{/cps}"
    d "Фу-ух, похоже показалось...{w=1.0}
    Слава Богу, я уж думал что с ума сошел"
    sh "Ну знаешь,
    особенно, после {b}того{/b} что ты там натворил..."
    d "Да подумаешь!{w=1.0} Ну взял я \"немного\" денег"
    d "Жить же как-то надо..."
    d "Ничего же никому плохого не сделал..."
    "Думас еще немного побубнел..."
    "И отправился в городок на горизонте"
    "Похоже он совсем забыл о том что минуту назад услышал голоса в своей голове"
    du "В {b}этот{/b} раз я просто хочу осесть где-нибудь здесь,{w=1.0} и не искать себе приключений на задницу.."
    du "Я достаточно натерпелся"
    scene bg title01
    "Думас подъехал ко вьезду в город"
    "New Sosland..."
    du "Вот так название, конечно..."
    sh "Согласен."
    du "{cps=25}...{/cps}"
    du "Мне нужно найти местную таверну...{w=1.0} Жрать хочу"
    du "Денег нет даже на кружку пива!{w=1.0} На чертову кружку пива!"
    d "{cps=5}Я!!! ХОЧУ!!! ВЫПИТЬ!!!{/cps}"
    scene bg tavern_outside_day
    "Думас остановился перед Таверной"
    "И зашел внутрь"
    scene bg tavern01 #todo
    "Вокруг сидели одни пьяницы и больно похожие на бандитов люди"
    "Думас подошел к барной стойке"
    scene bg tavern02 #todo
    d "Привет!{w=1.0} Я с дороги, не найдется ли у тебя чего выпить?"
    b "Пожалуй найдется, но остался только Ром"#это ложь
    du "Ну, я бы хотел пивка...{w=1.0} Но главное это ведь нажраться?"
    d "Ла-адно, наливай!"
    b "С тебя 1.5$"#цены высокие только в таверне
    d "Дорого! Столько у меня нет..."
    b "Тогда, здесь тебе искать нечего"
    b "Город в руках у бандитской шайки...{w=1.0} Они диктуют цены, я ничего не могу с этим поделать"#На самом деле это просто предлог чтобы побольше зарабоать, а бандиты в принципе порядочные
    d "Интересный у Вас городок..."
    d "А, что еще за бандиты?{w=1.0} Город, ведь, выглядит даже неплохо..."
    b "В том то и дело что {b}просто{/b} неплохо. Не так давно здесь был процветающий оазис... {w=1.0}Я все еще советую тебе убираться отсюда пока не поздно!"
    d "Вот уж нет!{w=1.0} Я такой путь проделал, и не для того чтобы так просто уйти!"
    d "ДА Я ЧУТЬ НЕ СДОХ ПОКА ДОБИРАЛСЯ СЮДА!"
    b "Ну... Мне так-то всеравно, тебе решать,{w=1.0} если тебе так нужны деньги, то я готов дать тебе работу,{w=1.0} но много я тебе платить не собираюсь"#он всеравно заплатит, потому что Думас его повеселил
    d "Я готов на все , {w=1.0}кроме гей-оргии"
    b "Ну{cps=30}...{/cps} Покрайней мере не сегодня"
    b "Мне нужно чтобы ты пошел в магазин, {w=1.0}он на соседней улице,{w=1.0} и взял все по вот этому списку..."
    "-----------NEW ITEM-----------""{color=#fbff00}Список бармена{/color}"
    d "А деньги?"
    b "А деньги тебе не понадобятся..."
    d "Ладно.."
    b "Ступай-ступай...{w=1.0} Буду ждать тебя к вечеру"
    scene bg tavern_outside_day
    du "\"Деньги тебе не понадобятся\" {w=1.0}Это ведь не значит, что мне нужно это \"что-то\"{w=1.0} украсть?..."
    du "МММММММ..."
    scene bg blackground
    du "Не хотелось бы начинать знакомство с городом вот так...{w=1.0} Опять..."
    du "Шош, думаю мне просто надо сказать что я от этого-самого бармена...{w=1.0} Как его кстати там?... {w=1.0}Скрытный ублюдок..."#У гг своеобразный говор, который подчеркивает то что он из глубинки
    du "Между прочим я профессиональный авантюрист,{w=1.0} я Вам не посыльный!"#Он мечтает стать авантюристом, тоесть быть в почете у женщин, ловить бандитов, искать сокровища и т.д.
    "Дилинь!" ##todo Добавить звук
    show manager fun
    y "Приветствую, Вас, в моем магазине!{w=1.0} Вам что-то нужно?"
    menu: #Разветвление не фундаментальное, меняет только то что нам ответит Управляющая, пока-что ##todo
        "Как ответить?"

        "Ответить нормально":
            d "Драсте, я Думас-Зоркий глаз!{w=1.0} Мне нужно все по вот этому списку"
        "Флиртовать":
            d "Драсте, я Думас-Зоркий глаз!{w=1.0} И поэтому я отлично вижу что у Вас как минимум 4 размер.."
            show manager angry
            y "Хам!"
            "Управляющая дала пощечину Думасу"
            d "Мне это...{w=1.0} Мне надо все по вот этому вот списку"
            show manager fun
    y "Ах во-о-от оно что..."
    y "Полагаю ТЫ из Салуна.."
    d "Ну,{w=1.0} вообще да"
    y "Ох...{w=1.0} Мне нужно время что-бы все подготовить..."
    y "Не хотите ли принять ванную?"
    y "Я вижу Вы с дороги и, наверняка очень устали...{w=1.0} Прошу, проходите сюда, все бесплатно!"
    d "{color=#fbff00}БЕСПЛАТНО?{/color}"
    sh "А этот придурок думает только о деньгах..."
    menu: #Разветвление важное. Игнорирование шизы приведет к плохой концовке и дню сурка ##todo
        "Шиза?"

        "НУ И ЧТО?!":
            d "Деньги ведь это главное!{w=1.0} Без денег ты никто!"
        "Игнорировать":
            sh "Хм.."
    d "Да, конечно!{w=1.0} Что надо делать?"
    y "О-ох,{w=1.0} хи-хи.."
    y "Вам вот сюда,{w=1.0} раздевайтесь и проходите!"
    d "Купаца!"
    y "...придурок..."
    hide manager fun
    "Думас зашел в комнату, на которую указла управляющая"
    "Разделся и обернулся полотенцем.."
    d "А где ванная..?"
    show manager angry
    "В комнату зашла управляющая с револьвером в руке"
    y "СЛЫШ ТЫ УБЛЮДОК!"
    d "А..?"
    y "ТЫ ЧЕ ГРАБАНУТЬ МЕНЯ ВЗДУМАЛ?!"
    y "ПИЗДА ТЕБЕ, РЫЖИЙ!!"
    d "..блять.."
    "Думас решил не выяснять что случилось, жить хотелось сильнее"
    "Он увидел окно, решил не медлить и выскочил в него прямо в полотенце!"
    hide manager angry
    "И Думас бежал..."
    "Бежал как в последний раз.."
    "Полотенце быстро спало с него"
    sh "АХАХАХ"
    sh "А ведь это ведь наш {b}профессиональный авантюрист!{/b}{w=1.0} Хорошо бегаешь!"
    d "ЗАТКНИ-И-ИСЬ СУКА!!"
    "Пули свестели, но благо не попадли в цель.."
    "Стемнело..."
    "Наконец, Думас был загнан в угол.."
    show manager angry
    "Похоже у управляющей закончились патроны"
    d "Мне{w=1.0} пиздец.."
    y "КТО ТЫ ТАКОЙ И ЧТО ТЫ ЗАБЫЛ У МЕНЯ В МАГАЗИЕ!!?"
    d "Ну..{w=1.0} Я..{w=1.0} Я только что в город приехал..."
    d "Я пришел в таверну, но..{w=1.0} но у меня совсем небыло денег, и бармен...{w=1.0} Бармен дал мне поручение, он сказал что заплатит если я принесу все что в том списке!"
    show manager fun
    y "А?{w=1.0} Так ты не грабить меня пришел?"
    d "ДА ЗАЧЕМ МНЕ ТЕБЯ ГРАБИТЬ?!"
    show manager sad
    y "Ой..{w=1.0} Прости..."
    y "Ну я просто немного нервничаю когда мне дают списки, в которых первым пунктом {color=#ff0000}\"ЕЕ ДУША\"{/color}"
    d "ЧЕРТОВ БАРМЕН!{w=1.0} НАДО БЫЛО ПОСМОТРЕТЬ ЧТО ТАМ!"
    show manager fun
    y "А ты, кончено, забавный...{w=1.0} Меня кстати Таня зовут"
    y "И это, ну ты прости за это..{w=1.0} Я так поняла что ты совсем только-только приехал сюда..."
    show manager coquette
    y "Возьми вот немног о денег,{w=1.0} думаю тебе хватит на то чтобы выжить первое время,{w=1.0} такая себе моральная компенсация"
    "-----------NEW ITEM-----------""{color=#fbff00}5${/color}" ##Имеем возожность как нажраться в таверне, так и не делать этого
    d "Вау, а это не много?"
    show manager fun
    y "Уверена у тебя в карманах совсем пусто,{w=1.0} раз ты согласился на работу от этого хитрого старикашки"
    y "Кстати,{w=1.0} заходи ко мне если тебе нужны будут деньги,{w=1.0} работа то у меня всегда найдется"
    d "Мне теперь даже как-то неудобно..{w=1.0} Изза меня вы оставили свой магазин на целый день без присмотра.."
    y "О-о-о, об этом не волнуйся,{w=1.0} я перевернула табличку на Закрыто.{w=1.0} Поверь, никто не рискнет даже дернуть ручку двери. Ха-Ха"
    du "Да уж,{w=1.0} Бой-Баба..."
    sh "Ты ей это сейчас в лицо скажи!"
    du "Она ж меня просто убьет!!"
    sh "Да ладно тебе..{w=1.0} По-моему она милашка"
    d "Да-уж..."
    y "Ты что-то сказал?"
    d "Говорю, Вы очень щедры,{w=1.0} спасибо большое!"
    show manager coquette
    y "Что значит ВЫ?!{w=1.0} МЕЖДУ ПРОЧИМ Я МОЛОДА И ГОРЯЧА!"
    sh "Ну горяча так точно.."
    du "Заткнись!"
    y "Обращайся ко мне на ТЫ, дорогуша"
    d "Конечно..{w=1.0} Э-эм...{w=1.0} Таня, ты не знаешь где здесь можно переночевать?"
    y "Ну мой магазин в одном зздании с Отелем,{w=1.0} по правде говоря я не только заправляю Магазином, но и Отелем в том числе"
    y "Думаю если денег у тебя нет, можешь ночевать в стойле,{w=1.0} рядом с моей Искоркой"
    y "Но будь осторожен!{w=1.0} Она очень не любит когда кто-то шумит если она спит"
    d "Чтож, я тебя понял..."
    du "Я что, должен спать...{w=1.0} В стойле...{w=1.0} С лошадью..."
    du "С ЛОШАДЬЮ!?"
    y "Ну раз так, то куда ты идешь сейчас?"
    menu:
        "Пойду ка я бухать...":
            d "Ну.. Я пойду, пожалуй посижу сегодня в Таверне,{w=1.0} мне нужно избавиться от стресса.."
            jump tavern
        "Пойдем спать..":
            d "Я так устал бегать целый день"
            jump sleep_first_day
label tavern: #Выход на ветку
    show manager sad
    y "Ну и ладно...{w=1.0} А ведь мог и со мной пойти!"
    d "Ээ?.."
    show manager angry
    y "Грубиян!"
    hide manager angry
    du "А что я сделал то?"
    sh "Ну ты кончено тупой..."
    du "Вот кто настоящий грубиян!"
    scene bg tavern outside_night
    "И Думас отправился в Таверну"
    "На дворе уже ночь и Думас дико устал"
    "Он завалился внутрь, где его весело поприветствовали"
    "Толпа" "ХА-ХА, это же тот Авантюрирст, что так смело убегал от Танечки!!"
    "Думас аж скривился"
    du "Ебаные ублюдки!"
    "Но он пришел сюда выпить, так что..."
    d "Слыш ты!{w=1.0} Барменишка"
    b "Ооо,{w=1.0} так ты все-таки выжил"
    d "А были сомнения?"
    sh "Слушай, ну она ведь едва яйца тебе не отстрелила"
    d "ЗАТКНИСЬ НАХУЙ!"
    b "С тобой все в порядке?"
    d "СО МНОЙ ВСЕ ОТЛИЧНО!"
    b "Ну по тебе видно конечно..."
    sh "Истеричка.."
    du "Завались, или я тебя завалю."
    sh "Все-все, только не ори,{w=1.0} он видимо думает что ты совсем кукухой поехал"
    b "Помнится я говорил тебе что заплачу,{w=1.0} но только в том случае, если ты принесешь мне все что было в том списке.."
    d "Кстати о списке, че за подстава?!{w=1.0} Меня чуть не грохнули изза тебя!"
    b "Ну я же не запрещал тебе прочесть список заранее..{w=1.0} Так что технически...{w=1.0}"
    d "Слыш ты бля!{w=1.0} Тебе давно глаз на жопу натягивали?"
    b "Зато ты знатно повеселил меня,{w=1.0} я могу, например, сделать тебе скидку..{w=1.0} Скажем в 5%"
    d "Я смотрю ты вообще бессмертный"
    b "10%.."
    d "..."
    b "15..?"
    d "Кхм-кхм!"
    b "Ладно, так и быть...{w=1.0} 17% Ты меня так в убытки загонишь.."
    du "У тебя вискарь полтора бакса стоит,{w=1.0} мразь, тебе не стыдно?"
    sh "Ну тебя и развели, конечно!"
    d "Хрен с тобой, наливай,{w=1.0} и я хочу {cps=5}ПИВА{/cps} Пивка, пивулька, пивасика.{w=1.0} НАЛИВАЙ ДАВАЙ ЧЕ СТАЛ"
    b "Да-да..{w=1.0} секунду.."
    sh "Алкаш."
    "Думас мирно себе усвинячивался на те деньги что ему дала Таня,{w=1.0} орал песни под пианино,{w=1.0} в общем, {b}культурно{/b} отдыхал"
    "Спустя несколько часов,{w=1.0} наступила полночь,{w=1.0} но шум и гам в Таверне не утихал"
    "Похоже Думасу набили морду,{w=1.0} и он лежит на полу Таверны,{w=1.0} спит после тяжелого дня"
    "Вдруг, Таверну наполнила приятная музыка,{w=1.0} и красивый женский голос запел.."
    pause
    "Когда она закончила петь, Думас сумел открыть глаза"
    "Посреди Таверны стояла девушка, она была красивее остальных, девушка со светлыми волосами и в красивом, розово-голубом платье"
    "Снова заиграла музыка и она запела.."
    pause
    ""

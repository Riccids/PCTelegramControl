# PCTelegramControl
Телеграмм бот, созданный для управления функционалом компьютера удаленно.

# Глава 1. Создание телеграмм бота
Так как наш бот работает локально на вашем компрьютере, нам понадобится его для начала создать, делается это крайне просто.

Заходим в телеграмм и в поиске каналов вбиваем [@BotFather](https://t.me/BotFather).
Нам требуется вот такой вот канал с галочкой:
![image](https://github.com/Riccids/PCTelegramControl/assets/108303179/28654a3e-589c-4efa-8de4-fdb1e3ecd924)

Данный бот сам по себе представояет огромную мощность из команд, однако нам для создания понадобится всего парочка из них.

Первым делом прописываем команду /newbot, чтобы создать нового бота.
BotFather попросит нас написать какое-то название для бота, в моём случае это будет PCControl.
Далее мы получим сообщени следующего вида:
![image](https://github.com/Riccids/PCTelegramControl/assets/108303179/57c153bc-ab29-456b-824d-e8328a9da8cd)

Сделать нам нужно следующее:
Например, название нашего бота PCControl, теперь, мы отправляем тэг для него, как допустим, тэг человека, по которому вы ищите собеседника.
Выглядеть это может так: "PCControlbot", или так "PCControl_bot", вы вправе решать сами, какой тэг вы бы хотели выдать боту.
Как только вы получите сообщение с большим количеством текста, можем продолжать.

# Привязка API ключа к боту

Отлично, я вас поздравляю, теперь мы создали своего первого бота.
Теперь нам подобится привязать ключ к нашей программе, делается это следующим образом.
Заходим во вкладку "[Code](https://github.com/Riccids/PCTelegramControl)", и справа снизу ищем Releases, там мы скачиваем последнюю вышедшую версию программы.
Обычно к ней идёт Change log,там можно увидеть различную информацию о обновлении.

После скачивания программы мы её запускаем, она попросит нас ввести ранее созданный API ключ, копируем его и вставляем.
Не пугаемся, когда получаем вот такое вот сообщение, ничего не поломалось и всё хорошо :)
![image](https://github.com/Riccids/PCTelegramControl/assets/108303179/ea403c80-2961-465f-bf90-2bedd8f39a7f)

Теперь перезапускаем программу.
Если у вас открылась пустая командная строка, значит всё получилось!
КОНСОЛЬ ЗАКРЫВАТЬ НЕ НУЖНО, БОТ РАБОТАЕТ КАК КОНСОЛЬНОЕ ПРИЛОЖЕНИЕ!!!!!!!!!!!!!!!!!!!!!!!!

# Работа с самим ботом

Теперь возвращаемся в BotFather, открытый ранее.
В этом большом сообщении, самая первая ссылка на телеграмм, что нас встречает, это и есть наш бот, переходим по ней.

![image](https://github.com/Riccids/PCTelegramControl/assets/108303179/53fd4e21-a7d6-4f30-9bf2-22d7e9a759ac)

Далее остаётся лишь прописать команду /start и можно работать с ботом!

# Как добавить бота в автозагрузку

Вот небольшой гайд от самих Microsoft, как добавить .exe файл в автозагрузку вместе с компьютером:
![image](https://github.com/Riccids/PCTelegramControl/assets/108303179/84d3e3f9-39ac-4f90-bc8b-b9102183254f)

А так же вариант добавления .exe файла в планировщик задач:
https://ocomp.info/planirovshhik-zadaniy.html

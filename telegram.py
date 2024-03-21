این کد یک برنامه برای اتصال به تلگرام با استفاده از کتابخانهی Telethon ایجاد میکند و امکان ارسال پیامها به تعدادی مشخص از گفتگوها یا گروهها در زمانهای معین را فراهم میآورد. 

در اینجا توضیحات بخشهای مهم کد آورده شدهاند:

1. **وارد کردن کتابخانهها و ماژولها**: در این بخش، کتابخانهها و ماژولهای مورد نیاز وارد میشوند. اگر کتابخانهای وجود نداشته باشد، کد تلاش میکند آن را نصب کند.

2. **تنظیمات و نگاهداشت لاگ**: تنظیمات برای ثبت لاگها در یک فایل تعیین شده است.

3. **تعریف توابع کمکی**: توابعی برای خواندن و نوشتن اطلاعات از یک فایل JSON و یک تابع برای تغییر فونت متنها تعریف شدهاند.

4. **بررسی وجود فایل دادهها**: اگر فایل دادهها وجود نداشته باشد، یک فایل دادههای پیشفرض ساخته و اطلاعات اولیه در آن ذخیره میشوند.

5. **تعریف متغیرها**: شناسه و کلید API برای اتصال به تلگرام، نام سشن (جلسه) و شناسه توسعهدهنده تعریف شدهاند.

6. **تعریف تابع انتقال پیام**: این تابع برای ارسال پیام به گفتگوها یا گروهها تعریف شده و از تابع Telethon برای ارسال پیام استفاده میکند.

7. **تنظیم ارسال خودکار**: این قسمت با استفاده از کتابخانه aiocron زمانهایی را تعیین میکند که باید پیامها را به مقاصد مشخص فرستاده و تابع مربوطه را فراخوانی کند.

8. **تنظیم اشتراک**: این قسمت نیز با استفاده از کتابخانه aiocron زمانهایی را تعیین میکند که باید اشتراک کاربران را بررسی و اعلام کند.

9. **بروزرسانی دریافت پیام**: در اینجا یک واکشیکننده (event handler) برای دریافت پیامهای جدید تعریف شده است.

متن کد را به زبان فارسی مینویسم و توضیحات هر بخش را بررسی میکنم.

مطمئناً! دوباره کد را با توضیحات فارسی توضیح میدهم:

python
import os
import re
import json
import random
import aiocron
import asyncio
import logging
from telethon.sync import TelegramClient, events, functions, types
from telethon.errors.rpcerrorlist import FloodWaitError

# اگر کتابخانهها نصب نباشند، آنها را نصب میکنیم
try:
    import os
    import re
    import json
    import random
    import aiocron
    import asyncio
    import logging
    from telethon.sync import TelegramClient, events, functions, types
    from telethon.errors.rpcerrorlist import FloodWaitError
except ModuleNotFoundError:
    os.system('pip install --upgrade pip && pip install telethon && pip install asyncio && pip install aiocron && clear')
    os.sys.exit('بستههای مورد نیاز نصب شدند!')

# تنظیمات لاگها
logging.basicConfig(filename="log.txt", filemode="a+", format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# توابع کمکی
def get(file):
    with open(file, 'r') as r:
        return json.load(r)

def put(file, data):
    with open(file, 'w') as w:
        json.dump(data, w, indent=4)

def font(text):
    if isinstance(text, str):
        text = text.lower()
        return text.translate(text.maketrans('qwertyuiopasdfghjklzxcvbnm-0123456789',
                                             'ǫᴡᴇʀᴛʏᴜɪᴏᴘᴀsᴅғɢʜᴊᴋʟᴢxᴄᴠʙɴᴍ-𝟎𝟏𝟐𝟑𝟒𝟓𝟔𝟕𝟖𝟗'))
    else:
        return None

# اگر فایل دادهها وجود ندارد، یک فایل دادههای پیشفرض ایجاد میکنیم
if not os.path.exists('data.json'):
    data = {'bot': 'on', 'autojoin': 'off', 'contact': 'off', 'secretary': 'off', 'forward': 'on',
            'forwardauthor': 'off', 'forwardtime': 10, 'forwardid': 0, 'forwardchat': None, 'forwardtype': None,
            'forwardreply': None, 'subscription': 30, 'admins': [], 'groups': [], 'secretarytext': []}
    put('data.json', data)

api_id = 00000000  # شناسه API
api_hash = '000000'  # کلید API

bot = TelegramClient(input('نام جلسه را وارد کنید: '), api_id, api_hash)  # اتصال به تلگرام
dev = 000000  # شناسه توسعهدهنده

# تابع برای انتقال پیام
async def forward_message(to_peer, id, from_peer, reply_text, drop_author):
    message = await bot(
        functions.messages.ForwardMessagesRequest(
            from_peer=from_peer,
            id=[id],
            to_peer=to_peer,
            drop_author=drop_author
        )
    )
    if reply_text:
        await bot.send_message(to_peer, reply_text, reply_to=message.updates[0].id)

forwardtime = get('data.json')['forwardtime']  # زمان ارسال خودکار

# تنظیم زمانبندی ارسال خودکار
@aiocron.crontab(f'*/{forwardtime}    ')
async def clock():
    data = get('data.json')
    if data['bot'] == 'on' and data['subscription'] != 0:
        if data['forward'] == 'on':
            if data['forwardid'] and data['forwardchat'] and data['forwardtype']:
                i, limit_for_send = 0, 0
                async for dialog in bot.iter_dialogs():
                    if (data['forwardtype'] == 'privates' and isinstance(dialog.entity, types.User)) or \
                            (data['forwardtype'] == 'groups' and isinstance(dialog.entity, types.Chat)) or \
                            (data['forwardtype'] == 'super groups' and isinstance(dialog.entity, types.Channel) and
                             dialog.entity.megagroup):
                        try:
                            await forward_message(dialog.id, data['forwardid'], data['forwardchat'],
                                                  data['forwardreply'], data['forwardauthor'] == 'off')
                            i += 1
                            await asyncio.sleep(0.5)
                        except FloodWaitError as error:
                            limit_for_send = e.seconds
                            try:
                                await bot.send_message(dev, error)
                            except:
                                ...
                            print(error)
                            break
                        except Exception as e:
                            await bot.send_message(dev, font(e))
                print(f"محدودیت FloodWaitError بات: {limit_for_send} ثانیه")
                if limit_for_send:
                    await asyncio.sleep(limit_for_send)
                    await bot.send_message(dev, font(f"محدودیت FloodWaitError بات: {limit_for_send} ثانیه"))
                await asyncio.sleep(1)
                await bot.send_message(dev, font(f'ارسال شده به {i} از ' + data['forwardtype'] + ' !'))

# تنظیم اشتراک و زمانبندی آن
@aiocron.crontab(f'*/12 12   *')
async def subscription():
    data = get('data.json')
    if data['subscription'] > 0:
        data['subscription'] -= 1
        put('data.json', data)
    else:
        await bot.send_message(dev, font('اشتراک این تبچی به اتمام رسیده است!'))

# واکشی پیامهای جدید
@bot.on(events.NewMessage())
async def updateMessage(event):
    pass  # این قسمت خالی است و برای پیادهسازی پردازش پیامهای جدید باید پر شود

# شروع اتصال به تلگرام
bot.start()
bot.run

_until_disconnected()


در اینجا کدی است که اتصال به تلگرام را برقرار کرده و امکان ارسال پیامهای خودکار به گفتگوها یا گروهها را فراهم میآورد. این برنامه از کتابخانه Telethon برای ارتباط با تلگرام استفاده میکند و با استفاده از aiocron مدیریت و زمانبندی ارسال پیامها را انجام میدهد. همچنین از یک فایل JSON برای ذخیره تنظیمات و وضعیتهای مختلف استفاده میکند.
در این بخش از کد، اطلاعات مرتبط با گفتگوها و کاربران را جمعآوری و نمایش میدهد و همچنین امکان افزودن و حذف افراد مدیر (سودو) و تغییر اطلاعات پروفایل را فراهم میآورد. این بخش به صورت زیر توضیح داده میشود:

python
# در اینجا اطلاعات گفتگوها و کاربران جمعآوری میشود و نمایش داده میشود
if text == 'status':
    private_chats, bots, groups, broadcast_channels = 0, 0, 0, 0
    admin_in_groups, creator_in_groups = 0, 0
    admin_in_broadcast_channels, creator_in_channels = 0, 0
    unread_mentions, unread = 0, 0
    largest_group_member_count, largest_group_with_admin = 0, 0

    async for dialog in bot.iter_dialogs():
        entity = dialog.entity
        if isinstance(entity, types.Channel):
            broadcast_channels += 1
            if entity.creator:
                creator_in_channels += 1
        elif entity.megagroup:
            groups += 1
            if entity.creator or entity.admin_rights:
                admin_in_groups += 1
            if entity.creator:
                creator_in_groups += 1
        elif isinstance(entity, types.User):
            private_chats += 1
            if entity.bot:
                bots += 1
        elif isinstance(entity, types.Chat):
            groups += 1
            if entity.creator or entity.admin_rights:
                admin_in_groups += 1
            if entity.creator:
                creator_in_groups += 1

        unread_mentions += dialog.unread_mentions_count
        unread += dialog.unread_count

    # ساختن گزارش با اطلاعات جمعآوری شده
    report = f'وضعیت:'
    report += f'\nچتهای خصوصی: {private_chats}'
    report += f'\nرباتها: {bots}'
    report += f'\nگروهها: {groups}'
    report += f'\nکانالهای پخش: {broadcast_channels}'
    report += f'\nمدیر در گروهها: {admin_in_groups}'
    report += f'\nسازنده در گروهها: {creator_in_groups}'
    report += f'\nمدیر در کانالهای پخش: {admin_in_broadcast_channels}'
    report += f'\nسازنده در کانالها: {creator_in_channels}'
    report += f'\nمنشنهای خوانده نشده: {unread_mentions}'
    report += f'\nپیامهای خوانده نشده: {unread}'
    report += f'\nبزرگترین تعداد اعضا در گروه: {largest_group_member_count}'
    report += f'\nبزرگترین گروه با مدیر: {largest_group_with_admin}'

    # ارسال گزارش به گفتگوی فعلی
    await event.reply(font(report))
elif match := re.match(r'AddSudo (\d+)', text):
    # افزودن یک کاربر به لیست مدیران (سودو)
    id = int(match.group(1))
    data['admins'].append(id)
    put('data.json', data)
    await event.respond(font(f'{id} با موفقیت به لیست مدیران اضافه شد!'))
# (سایر قسمتهای کد نیز ادامه دارند)


در این بخش، با وارد کردن دستور `status`، اطلاعات مختلفی را از گفتگوها و کاربران (مثل تعداد گروهها، رباتها، کانالهای پخش و ...) جمعآوری میکند و به گونهای زیبا نمایش میدهد. همچنین، دستوراتی برای افزودن و حذف کاربران به عنوان مدیر (سودو) و تغییر اطلاعات پروفایل (مثل نام، نام خانوادگی و ...) نیز وجود دارند که با الگوهای خاص تشخصص دادهشدهاند.


در این بخش از کد، عملیاتهای مرتبط با مخاطبان و اطلاعات کاربری انجام میشود. این عملیات شامل حذف تماسها، اشتراکگذاری اطلاعات تماس، تنظیم زمانبندی برای ارسال خودکار و اقدامات مرتبط با پیامهای ورودی است. این بخش به صورت زیر توضیح داده میشود:

python
# (در این قسمت ادامه دیگر بخشهای کد آمده است)

elif text == 'CleanContactsList':
    # حذف تماسها
    try:
        contacts = await bot(functions.contacts.GetContactsRequest(hash=0))
        await bot(functions.contacts.DeleteContactsRequest(id=[contact.id for contact in contacts.users]))
        await event.reply(font('تمام مخاطبین شما حذف شدند!'))
    except Exception as e:
        await event.reply(font(e))

elif text == 'Share':
    # اشتراکگذاری اطلاعات تماس
    me = await bot.get_me()
    await bot.send_file(event.chat_id, types.InputMediaContact(phone_number=me.phone, first_name=me.first_name, last_name=me.last_name or str(), vcard=str()))

elif match := re.match(r'ForwardTime (\d+)', text):
    # تنظیم زمانبندی برای ارسال خودکار
    time = int(match.group(1))
    clock.spec = f'*/{time}    '
    clock.start()
    data['forwardtime'] = time
    put('data.json', data)
    await event.respond(font(f'زمان ارسال خودکار با موفقیت به {time} دقیقه تنظیم شد!'))

# (دیگر بخشهای کد نیز ادامه دارند)


در این بخش، عملیاتهایی برای مدیریت تماسها (مانند حذف تماسها)، اشتراکگذاری اطلاعات تماس، تنظیم زمانبندی برای ارسال خودکار و اقدامات مرتبط با پیامهای ورودی (مثل مشاهده اطلاعات یک پیام و ...) ارائه شدهاند. این دستورات با الگوهای خاص متناسب با هر عملیات تشخصص دادهشدهاند.


در این بخش از کد، اقدامات مرتبط با فوروارد پیامها به گروهها، کانالها و کاربران انجام میشود. عملیاتهایی گوناگون شامل ارسال پیامها به گروهها، کانالها و کاربران با استفاده از فوروارد، تنظیم زمانبندی برای ارسال خودکار و ذخیره تنظیمات مربوط به فوروارد در فایل `data.json` آورده شدهاند. این بخش به صورت زیر توضیح داده میشود:

python
# (در این قسمت ادامه دیگر بخشهای کد آمده است)

elif text == 'ForwardPrivates':
    # فوروارد پیامها به گفتگوهای خصوصی
    i, limit_for_send = 0, 0
    async for dialog in bot.iter_dialogs():
        if isinstance(dialog.entity, types.User):
            try:
                await forward_message(dialog.id, event.reply_to_msg_id, event.chat_id, data['forwardreply'], data['forwardauthor'] == 'off')
                i += 1
                await asyncio.sleep(0.5)
            except FloodWaitError as error:
                limit_for_send = e.seconds
                try: await bot.send_message(dev, error)
                except: ...
                print(error)
                break
            except Exception as e:
                await bot.send_message(dev, font(e))

    print(f"محدودیت زمانی FloodWaitError برای ربات: {limit_for_send} ثانیه")
    if limit_for_send:
        await asyncio.sleep(limit_for_send)
        await bot.send_message(dev, font(f"محدودیت زمانی FloodWaitError برای ربات: {limit_for_send} ثانیه"))
    await asyncio.sleep(1)
    await event.reply(font(f'به {i} گفتگوی خصوصی فوروارد شد!'))

elif text == 'ForwardGroups':
    # فوروارد پیامها به گروهها
    i = 0
    async for dialog in bot.iter_dialogs():
        if isinstance(dialog.entity, types.Chat):
            try:
                await forward_message(dialog.id, event.reply_to_msg_id, event.chat_id, data['forwardreply'], data['forwardauthor'] == 'off')
                i += 1
            except FloodWaitError as error:
                limit_for_send = e.seconds
                try: await bot.send_message(dev, error)
                except: ...
                print(error)
                break
            except Exception as e:
                await bot.send_message(dev, font(e))

    print(f"محدودیت زمانی FloodWaitError برای ربات: {limit_for_send} ثانیه")
    if limit_for_send:
        await asyncio.sleep(limit_for_send)
        await bot.send_message(dev, font(f"محدودیت زمانی FloodWaitError برای ربات: {limit_for_send} ثانیه"))
    await asyncio.sleep(1)
    await event.reply(font(f'به {i} گروه فوروارد شد!'))

# (دیگر بخشهای کد نیز ادامه دارند)


در این بخش، عملیاتهای مختلف برای فوروارد پیامها به گروهها، کانالها و کاربران خصوصی، گروهها و کانالهای پخش، و گروههای سوپر انجام میشود. همچنین، زمانبندی برای فوروارد خودکار نیز تنظیم میشود.


# ================================================================
try:
    import os
    import re
    import json
    import random
    import aiocron
    import asyncio
    import logging
    from telethon.sync import TelegramClient, events, functions, types
    from telethon.errors.rpcerrorlist import FloodWaitError
except ModuleNotFoundError:
    os.system('pip install --upgrade pip && pip install telethon && pip install asyncio && pip install aiocron && clear')
    os.sys.exit('installed the required packages !')

logging.basicConfig(filename="log.txt", filemode="a+",
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)


def get(file):
    with open(file, 'r') as r:
        return json.load(r)


def put(file, data):
    with open(file, 'w') as w:
        json.dump(data, w, indent=4)


def font(text):
    if isinstance(text, str):
        text = text.lower()
        return text.translate(text.maketrans('qwertyuiopasdfghjklzxcvbnm-0123456789', 'ǫᴡᴇʀᴛʏᴜɪᴏᴘᴀsᴅғɢʜᴊᴋʟᴢxᴄᴠʙɴᴍ-𝟎𝟏𝟐𝟑𝟒𝟓𝟔𝟕𝟖𝟗'))
    else:
        return None


if not os.path.exists('data.json'):
    data = {'bot': 'on', 'autojoin': 'off', 'contact': 'off', 'secretary': 'off', 'forward': 'on', 'forwardauthor': 'off', 'forwardtime': 10,
            'forwardid': 0, 'forwardchat': None, 'forwardtype': None, 'forwardreply': None, 'subscription': 30, 'admins': [], 'groups': [], 'secretarytext': []}
    put('data.json', data)

api_id = 00000000
api_hash = '000000'

bot = TelegramClient(input('enter the session name : '), api_id, api_hash)

dev = 000000


async def forward_message(to_peer, id, from_peer, reply_text, drop_author):
    message = await bot(
        functions.messages.ForwardMessagesRequest(
            from_peer=from_peer,
            id=[id],
            to_peer=to_peer,
            drop_author=drop_author
        )
    )
    if reply_text:
        await bot.send_message(to_peer, reply_text, reply_to=message.updates[0].id)

forwardtime = get('data.json')['forwardtime']


@aiocron.crontab(f'*/{forwardtime}    ')
async def clock():
    data = get('data.json')
    if data['bot'] == 'on' and data['subscription'] != 0:
        if data['forward'] == 'on':
            if data['forwardid'] and data['forwardchat'] and data['forwardtype']:
                i, limit_for_send = 0, 0
                async for dialog in bot.iter_dialogs():
                    if (data['forwardtype'] == 'privates' and isinstance(dialog.entity, types.User)) or (data['forwardtype'] == 'groups' and isinstance(dialog.entity, types.Chat)) or (data['forwardtype'] == 'super groups' and isinstance(dialog.entity, types.Channel) and dialog.entity.megagroup):
                        try:
                            await forward_message(dialog.id, data['forwardid'], data['forwardchat'], data['forwardreply'], data['forwardauthor'] == 'off')
                            i += 1
                            await asyncio.sleep(0.5)
                        except FloodWaitError as error:
                            limit_for_send = e.seconds
                            try: await bot.send_message(dev, error)
                            except: ...
                            print(error)
                            break
                        except Exception as e:
                            await bot.send_message(dev, font(e))

                print(f"bot limit FloodWaitError: {limit_for_send} s")
                if limit_for_send:

                    await asyncio.sleep(limit_for_send)
                    await bot.send_message(dev, font(f"bot limit FloodWaitError: {limit_for_send} s"))
                await asyncio.sleep(1)
                await bot.send_message(dev, font(f'Sent to {i} of ' + data['forwardtype'] + ' !'))


@aiocron.crontab(f'*/12 12   *')
async def subscription():
    data = get('data.json')
    if data['subscription'] > 0:
        data['subscription'] -= 1
        put('data.json', data)
    else:
        await bot.send_message(dev, font('The subscription to this tabchi has ended !'))


@bot.on(events.NewMessage())
async def updateMessage(event):
    data = get('data.json')
    text = event.raw_text
    chat_id = event.chat_id
    from_id = event.sender_id
    if from_id == dev or from_id in data['admins'] or chat_id in data['groups']:
        if from_id == dev:
            if match := re.match(r'AddSubscription (\d+)', text):
                time = int(match.group(1))
                data['subscription'] += time
                put('data.json', data)
                await event.reply(font('The subscription of the robot has been successfully increased !'))
            elif match := re.match(r'LowSubscription (\d+)', text):
                time = int(match.group(1))
                data['subscription'] -= time
                put('data.json', data)
                await event.reply(font('The subscription of the robot has been successfully reduced !'))
        if from_id != dev and data['subscription'] == 0:
            return await event.reply(font('Your subscription has ended !'))
        if match := re.match(r'(Bot|Secretary|Contact|AutoJoin|Forward|ForwardAuthor) ([Oo][Nn]|[Oo][Ff][Ff])', text):
            index = match.group(1).lower()
            status = match.group(2).lower()
            data[index] = status
            put('data.json', data)
            await event.reply(font(f'{index} now is {status} !'))
        elif data['bot'] == 'on':
            if text == 'Help':
                await event.reply(f'''
خاموش و روشن کردن ربات :
Bot on | off
خاموش و روشن کردن حالت منشی :
Secretary on | off
خاموش و روشن کردن حالت ذخیره خودکار مخاطب :
Contact on | off
خاموش و روشن کردن حالت عضو شدن خودکار لینک های خصوصی :
AutoJoin on | off
خاموش و روشن کردن فوروارد خودکار :
Forward on | off
فوروارد بدون نقل قول یا با نقل قول :
ForwardAuthor on | off
اطلاع از آنلاین بودن ربات :
Ping
گرفتن اطلاعات ربات :
Info
بدست آوردن اطلاعات یک فرد :
Id (REPLY)
اضافه کردن ادمین به ربات :
AddSudo (ID)

حذف ادمین از ربات :
DeleteSudo (ID)

گرفتن لیست ادمین ها :
SudoList
تغییر نام اکانت :
SetFirstName
تغییر نام خانوادگی اکانت :
SetLastName
تغییر بیوگرافی اکانت :
SetBiography
تغییر یوزرنیم اکانت :
SetUserName
تنظیم عکس برای عکس پروفایل اکانت :
SetPhoto (REPLY)
حذف تمام عکس های پروفایل ربات :
DeletePhoto
اضافه کردن متن منشی رندوم :
AddSecretary (TEXT)
حذف متن منشی :
DeleteSecretary (TEXT)
لیست متن های منشی رندوم :
SecretaryList
استارت کردن ربات :
Start (@username)
عضو شدن در یک گروه یا کانال :
Join (@username)
لفت دادن از یک گروه یا کانال :
Left (@username)
پاکسازی لیست مخاطبین :
CleanContactsList
اشتراک گزاری شماره اکانت :
Share
تنظیم زمان فوروارد خودکار :
ForwardTime (TIME)

اد کردن یه کاربر به همهی گروه ها :
AddAll (REPLY)
فوروارد برای همه :
ForwardAll (REPLY)
فوروارد برای پیوی ها :
ForwardPrivates (REPLY)
فوروارد برای گروه های عادی :
ForwardGroups (REPLY)
فوروارد برای سوپر گروه ها :
ForwardSuperGroups (REPLY)
تنظیم فوروارد خودکار :
SetForward privates | super groups | groups
تنظیم متن ریپلی کردن روی پیام فوروارد شده :
SetForwardReply (REPLY)
حذف متن ریپلی شده روی پیام فوروارد شده :
DeleteForwardReply
اضافه کردن یک گروه به عنوان گروه مدیریت اکانت :
AddGp (IN GROUP)
حذف کردن یک گروه از لیست گروه های مدیریت اکانت :
DeleteGp (IN GROUP)

اشتراک ربات : {data['subscription']}
''')
            elif text == 'Ping':
                await event.reply(font('I am Online !'))
            elif text == 'Info':
                private_chats = 0
                bots = 0
                groups = 0
                broadcast_channels = 0
                admin_in_groups = 0
                creator_in_groups = 0
                admin_in_broadcast_channels = 0
                creator_in_channels = 0
                unread_mentions = 0
                unread = 0
                largest_group_member_count = 0
                largest_group_with_admin = 0
                async for dialog in bot.iter_dialogs():
                    entity = dialog.entity
                    if isinstance(entity, types.Channel):
                        if entity.broadcast:
                            broadcast_channels += 1
                            if entity.creator or entity.admin_rights:
                                admin_in_broadcast_channels += 1
                            if entity.creator:
                                creator_in_channels += 1
                        elif entity.megagroup:
                            groups += 1
                            if entity.creator or entity.admin_rights:
                                admin_in_groups += 1
                            if entity.creator:
                                creator_in_groups += 1
                    elif isinstance(entity, types.User):
                        private_chats += 1
                        if entity.bot:
                            bots += 1
                    elif isinstance(entity, types.Chat):
                        groups += 1
                        if entity.creator or entity.admin_rights:
                            admin_in_groups += 1
                        if entity.creator:
                            creator_in_groups += 1
                    unread_mentions += dialog.unread_mentions_count
                    unread += dialog.unread_count
                list = f'status !'
                list += f'\nprivate chats : {private_chats}'
                list += f'\nbots : {bots}'
                list += f'\ngroups : {groups}'
                list += f'\nbroadcast channels : {broadcast_channels}'
                list += f'\nadmin in groups : {admin_in_groups}'
                list += f'\ncreator in groups : {creator_in_groups}'
                list += f'\nadmin in broadcast channels : {admin_in_broadcast_channels}'
                list += f'\ncreator in channels : {creator_in_channels}'
                list += f'\nunread mentions : {unread_mentions}'
                list += f'\nunread : {unread}'
                list += f'\nlargest group member count : {largest_group_member_count}'
                list += f'\nlargest group with admin : {largest_group_with_admin}'
                await event.reply(font(list))
            elif match := re.match(r'AddSudo (\d+)', text):
                id = int(match.group(1))
                data['admins'].append(id)

                put('data.json', data)
                await event.respond(font(f'{id} was successfully added to the list of admins !'))
            elif match := re.match(r'DeleteSudo (\d+)', text):
                id = int(match.group(1))
                data['admins'].remove(id)

                put('data.json', data)
                await event.respond(font(f'{id} was successfully removed from the list of admins !'))
            elif text == 'SudoList':
                list = font('Sudo List :')
                for id in data['admins']:
                    list += f'\n• [ᴜsᴇʀ](tg://user?id={id})'
                await event.respond(font(list))
            elif text == 'CleanSudoList':
                data['admins'] = []
                put('data.json', data)
            elif match := re.match(r'SetFirstName (.*)', text):
                try:
                    await bot(functions.account.UpdateProfileRequest(first_name=match.group(1)))
                    await event.reply(font('Your first name has been successfully changed !'))
                except Exception as e:
                    await event.reply(font(e))
            elif match := re.match(r'SetLastName (.*)', text):
                try:
                    await bot(functions.account.UpdateProfileRequest(last_name=match.group(1)))
                    await event.reply(font('Your last name has been successfully changed !'))
                except Exception as e:
                    await event.reply(font(e))
            elif match := re.match(r'SetBiography (.*)', text):
                try:
                    await bot(functions.account.UpdateProfileRequest(about=match.group(1)))
                    await event.reply(font('Your Biography has been successfully changed !'))
                except Exception as e:
                    await event.reply(font(e))
            elif match := re.match(r'SetUserName (.*)', text):
                try:
                    await bot(functions.account.UpdateUsernameRequest(username=match.group(1)))
                    await event.reply(font('Your username has been successfully changed !'))
                except Exception as e:
                    await event.reply(font(e))
            elif text == 'DeletePhoto':
                try:
                    photos = await bot.get_profile_photos('me')
                    for photo in photos:
                        await bot(functions.photos.DeletePhotosRequest(id=[types.InputPhoto(id=photo.id, access_hash=photo.access_hash, file_reference=photo.file_reference)]))
                    await event.reply(font('All your photos have been deleted !'))
                except Exception as e:
                    await event.reply(font(e))
            elif match := re.match(r'AddSecretary (.*)', text):
                if match.group(1) in data['secretarytext']:
                    await event.respond(font('This text is already saved !'))
                else:
                    data['secretarytext'].append(match.group(1))
                    put('data.json', data)
                    await event.respond(font('This text has been successfully added !'))
            elif match := re.match(r'DeleteSecretary (.*)', text):
                if match.group(1) in data['secretarytext']:
                    data['secretarytext'].remove(match.group(1))
                    put('data.json', data)
                    await event.respond(font('This text has been successfully removed !'))
                else:
                    await event.respond(font('This text does not exist !'))
            elif text == 'SecretaryList':
                list = font('Secretary List :')
                for text in data['secretarytext']:
                    list += f'\n• {text}'
                await event.respond(font(list))
            elif match := re.match(r'Start (.*)', text):
                try:
                    await bot.send_message(match.group(1), '/start')
                    await event.reply(font('The bot started successfully !'))
                except Exception as e:
                    await event.reply(font(e))
            elif match := re.match(r'Join (.*)', text):
                invitelink = match.group(1)
                explode = invitelink.split('/')
                if len(explode)
 > 1:
                    try:
                        await bot(functions.messages.ImportChatInviteRequest(explode[-1]))
                        await event.reply(font('I became a member !'))
                    except Exception as e:
                        await event.reply(font(e))
                else:
                    try:
                        await bot(functions.channels.JoinChannelRequest(invitelink))
                        await event.reply(font('I became a member !'))
                    except Exception as e:
                        await event.reply(font(e))
            elif match := re.match(r'Left (.*)', text):
                invitelink = match.group(1)
                explode = invitelink.split('/')
                if len(explode)
 > 1:
                    try:
                        group = await bot.get_entity(invitelink)
                        await bot(functions.messages.DeleteExportedChatInviteRequest(int('-100' + str(group.id))))
                        await event.reply(font('I became a member !'))
                    except Exception as e:
                        await event.reply(font(e))
                else:
                    try:
                        await bot(functions.channels.LeaveChannelRequest(invitelink))
                        await event.reply(font('I became a member !'))
                    except Exception as e:
                        await event.reply(font(e))
            elif text == 'CleanContactsList':
                try:
                    contacts = await bot(functions.contacts.GetContactsRequest(hash=0))
                    await bot(functions.contacts.DeleteContactsRequest(id=[contact.id for contact in contacts.users]))
                    await event.reply(font('All your contacts have been deleted !'))
                except Exception as e:
                    await event.reply(font(e))
            elif text == 'Share':
                me = await bot.get_me()
                await bot.send_file(event.chat_id, types.InputMediaContact(phone_number=me.phone, first_name=me.first_name, last_name=me.last_name or str(), vcard=str()))
            elif match := re.match(r'ForwardTime (\d+)', text):
                time = int(match.group(1))
                clock.spec = f'*/{time}    '
                clock.start()
                data['forwardtime'] = time
                put('data.json', data)
                await event.respond(font(f'The forwarding time was automatically set to {time} minute !'))
            elif text == 'DeleteForwardReply':
                data['forwardreply'] = None
                put('data.json', data)
                await event.reply(font(f'Replay on the forwarded message was successfully deleted !'))
            elif event.is_reply:
                if text == 'Id':
                    getMessage = await event.get_reply_message()
                    sender = getMessage.sender
                    id = sender.id
                    first_name = sender.first_name
                    last_name = sender.last_name
                    username = sender.username
                    phone = sender.phone
                    list = f'id : {id}'
                    list += f'\nfirst name : {first_name}'
                    list += f'\nlast name : {last_name}'
                    list += f'\nusername : {username}'
                    list += f'\nphone : {phone}'
                    await event.reply(font(list))
                elif text == 'SetPhoto':
                    try:
                        message = await event.get_reply_message()
                        media = await bot.download_media(message)
                        await bot(functions.photos.UploadProfilePhotoRequest(await bot.upload_file(media)))
                        os.remove(media)
                        await event.reply(font('Your photo has been successfully changed !'))
                    except Exception as e:
                        await event.reply(font(e))
                elif text == 'AddAll':
                    getMessage = await event.get_reply_message()
                    id = getMessage.sender.id
                    i = 0
                    async for dialog in bot.iter_dialogs():
                        if isinstance(dialog.entity, types.Chat):
                            try:
                                await bot(functions.channels.InviteToChannelRequest(dialog.id, [id]))
                                i += 1
                            except Exception as e:
                                await event.reply(font(e))
                    await event.reply(font(f'User {id} was successfully added to {i} groups !'))
                elif text == 'ForwardAll':
                    i, limit_for_send = 0, 0
                    async for dialog in bot.iter_dialogs():
                        if isinstance(dialog.entity, (types.Chat, types.User)) or (isinstance(dialog.entity, types.Channel) and dialog.entity.megagroup):
                            try:
                                await forward_message(dialog.id, event.reply_to_msg_id, event.chat_id, data['forwardreply'], data['forwardauthor'] == 'off')
                                i += 1
                                await asyncio.sleep(0.5)
                            except FloodWaitError as error:
                                limit_for_send = e.seconds
                                try: await bot.send_message(dev, error)
                                except: ...
                                print(error)
                                break
                            except Exception as e:
                                await bot.send_message(dev, font(e))

                    print(f"bot limit FloodWaitError: {limit_for_send} s")
                    if limit_for_send:

                        await asyncio.sleep(limit_for_send)
                        await bot.send_message(dev, font(f"bot limit FloodWaitError: {limit_for_send} s"))
                    await asyncio.sleep(1)

                    await event.reply(font(f'Sent to {i} of groups and super groups and privates !'))
                elif text == 'ForwardPrivates':
                    i, limit_for_send = 0, 0
                    async for dialog in bot.iter_dialogs():
                        if isinstance(dialog.entity, types.User):
                            try:
                                await forward_message(dialog.id, event.reply_to_msg_id, event.chat_id, data['forwardreply'], data['forwardauthor'] == 'off')
                                i += 1
                                await asyncio.sleep(0.5)
                            except FloodWaitError as error:
                                limit_for_send = e.seconds
                                try: await bot.send_message(dev, error)
                                except: ...
                                print(error)
                                break
                            except Exception as e:
                                await bot.send_message(dev, font(e))

                    print(f"bot limit FloodWaitError: {limit_for_send} s")
                    if limit_for_send:

                        await asyncio.sleep(limit_for_send)
                        await bot.send_message(dev, font(f"bot limit FloodWaitError: {limit_for_send} s"))
                    await asyncio.sleep(1)
                    await event.reply(font(f'Sent to {i} of privates !'))
                elif text == 'ForwardGroups':
                    i = 0
                    async for dialog in bot.iter_dialogs():
                        if isinstance(dialog.entity, types.Chat):
                            try:
                                await forward_message(dialog.id, event.reply_to_msg_id, event.chat_id, data['forwardreply'], data['forwardauthor'] == 'off')
                                i += 1
                            except FloodWaitError as error:
                                limit_for_send = e.seconds
                                try: await bot.send_message(dev, error)
                                except: ...
                                print(error)
                                break
                            except Exception as e:
                                await bot.send_message(dev, font(e))

                    print(f"bot limit FloodWaitError: {limit_for_send} s")
                    if limit_for_send:

                        await asyncio.sleep(limit_for_send)
                        await bot.send_message(dev, font(f"bot limit FloodWaitError: {limit_for_send} s"))
                    await asyncio.sleep(1)
                    await event.reply(font(f'Sent to {i} of groups !'))
                elif text == 'ForwardSuperGroups':
                    i = 0
                    async for dialog in bot.iter_dialogs():
                        if isinstance(dialog.entity, types.Channel) and dialog.entity.megagroup:
                            try:
                                await forward_message(dialog.id, event.reply_to_msg_id, event.chat_id, data['forwardreply'], data['forwardauthor'] == 'off')
                                i += 1
                                await asyncio.sleep(0.5)
                            except FloodWaitError as error:
                                limit_for_send = e.seconds
                                try: await bot.send_message(dev, error)
                                except: ...
                                print(error)
                                break
                            except Exception as e:
                                await bot.send_message(dev, font(e))

                    print(f"bot limit FloodWaitError: {limit_for_send} s")
                    if limit_for_send:

                        await asyncio.sleep(limit_for_send)
                        await bot.send_message(dev, font(f"bot limit FloodWaitError: {limit_for_send} s"))
                    await asyncio.sleep(1)
                    await event.reply(font(f'Sent to {i} of super groups !'))
                elif match := re.match(r'SetForward (privates|super groups|groups)', text):
                    data['forwardid'] = event.reply_to_msg_id
                    data['forwardchat'] = event.chat_id
                    data['forwardtype'] = match.group(1)
                    put('data.json', data)
                    await event.reply(font('Automatic forward
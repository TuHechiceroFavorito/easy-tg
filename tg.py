from telegram import InlineKeyboardButton, ReplyKeyboardMarkup
# import logging

# logging.basicConfig(
#     format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
# )

# logger = logging.getLogger(__name__)

def build_options_keyboard(buttons, back=True, state='Back', mode=True):
    keys = []
    index = 0
    for button in buttons:
        if len(button) < 30:
            if index%2 == 0:
                keys.append([button])
            else:
                keys[len(keys)-1].append(button)
            index += 1
        else:
            keys.append([button])
            index = 0
    if back:
        keys.append('Back')

    keyboard = ReplyKeyboardMarkup(keys, one_time_keyboard=mode)
    return keyboard

def build_options_inline(buttons, back=True, state='Back', marker='o'):
    keyboard = []
    index = 0
    for button in buttons:
        # logger.info(button + ' ' + str(len(button)))
        if len(button) < 30:
            if index%2 == 0:
                keyboard.append([InlineKeyboardButton(button, callback_data=marker + button)])
            else:
                keyboard[len(keyboard)-1].append(InlineKeyboardButton(button, callback_data=marker + button))
            index += 1
        else:
            keyboard.append([InlineKeyboardButton(button, callback_data=marker + button[:45])])
            index = 0
    if back:
        keyboard.append([InlineKeyboardButton('Back', callback_data=state)])
    return keyboard

def get_user(update):
    if update.callback_query:
        data = update.callback_query.message.chat
    else:
        data = update.message.chat 

    if data.username != None:
        user = data.username
    else:
        user = data.first_name
        if data.last_name != None:
            user += f' {data.last_name}'

    return user
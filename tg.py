from telegram import InlineKeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup


# Builds a keyboard from a list buttons.
# If back True, adds a back button.
# one determines if it is for one time
# It displays the buttons in two columns. It uses only one column if the text is too long
def buildKeyboard(buttons, back=False, one=True):
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
        keys.append(['Back'])

    keyboard = ReplyKeyboardMarkup(keys, one_time_keyboard=mode)
    return keyboard

# Builds an inline keyboard from a list buttons. The callback data will be the same as the buttons name. 
# If back True, adds a back button.
# state determines the value of the callback data of the back button. 
# Marker adds the specified string to the beggining of the callback data.
# It displays the buttons in two columns. It uses only one column if the text is too long.
# It also cuts the callback data to the first 45 characters, to avoid limit restrictions
def buildInline(buttons, back=False, state='Back', marker=''):
    keyboard = []
    index = 0
    for button in buttons:
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
    return InlineKeyboardMarkup(keyboard)

# Returns the username. In case it doesn't exist, it returns the first name with the last name (if any)
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
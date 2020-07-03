async def cmd_print(type, msg):
    if type == 'debug':
        print('[DEBUG] ' + msg)
    elif type == 'error':
        print('[ERROR] ' + msg)
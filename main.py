from mechanize import Browser, Cookie, CookieJar, _mechanize

class Cookie(Cookie):
    def __init__(self, nv: list):
        super().__init__(version=0, name=nv[0], value=nv[1], port=None, port_specified=False, domain='.facebook.com', domain_specified=True,
                         domain_initial_dot=True, path='/', path_specified=True, secure=True, expires=None, discard=False, comment=None, comment_url=None, rest={}, rfc2109=False)


def Send_Message(acc_id, message, cookie):
    br = Browser()
    br.set_handle_robots(False)
    jar = CookieJar()
    for cookie in cookie.replace(" ", "").split(';'):
        if not cookie == '':
            jar.set_cookie(Cookie(cookie.split('=')))
    br.set_cookiejar(jar)

    br.open(f'https://mbasic.facebook.com/messages/read/?fbid={acc_id}')
    br._factory.is_html = True

    if 'log in' in br.title().lower():
        raise Exception('Please Check Your Cookie. It might be expired or invalid.')

    client_name = br.title()
    print(f'Sending Message to {client_name}')
    try:
        br.select_form(predicate=lambda form: form.attrs.get("id") == "composer_form")
    except _mechanize.FormNotFoundError:
        raise Exception('Could not send message. Looks like you have been blocked.')

    print(f'Writing message to {client_name}')
    br.form['body'] = message
    br.submit()
    print(f'Successfully sent message to {client_name}')
    return True

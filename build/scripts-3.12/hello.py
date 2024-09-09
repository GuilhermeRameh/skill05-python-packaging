#!python
from dev_aberto import hello
from babel import format_datetime, format_name

import gettext
gettext.bindtextdomain('cli', 'locale')
gettext.textdomain('cli')
_ = gettext.gettext


if __name__ == '__main__':
    date, name = hello()
    print(_('Último commit feito em:'), format_datetime(date), _(' por'), format_name(name))

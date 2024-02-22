from datetime import datetime
from dtc import DTConvert


def show(obj: DTConvert):
    print('----- SHOW ITEM -----')
    print('init value: <{v}> {t}'.format(t=type(obj.value), v=obj.value))
    print('datetime: <{v}> {t}'.format(t=type(obj.datetime), v=obj.datetime))
    print('date: <{v}> {t}'.format(t=type(obj.date), v=obj.date))
    print('datetime string: <{v}> {t}'.format(t=type(obj.dtstring), v=obj.dtstring))
    print('date string: <{v}> {t}'.format(t=type(obj.dstring), v=obj.dstring))
    print()


show(DTConvert())
show(DTConvert('16/04/1986'))
show(DTConvert(datetime.now()))
show(DTConvert(datetime.now().date()))
show(DTConvert('хуй'))

show(DTConvert('26/01/1993  18:24:00 '))
show(DTConvert('26/01/1993  18.24.00 '))
show(DTConvert('26.01.1993  18:24:00 '))
show(DTConvert('26.01.1993  18.24.00 '))
show(DTConvert('26.01.1993  18,24,00 '))
# show(DTConvert('26-01-1993  18.24.00 '))
# show(DTConvert('26-01-1993  18:24:00 '))
show(DTConvert('01-26-1993  18:24:00 '))
show(DTConvert('1993-01-26  18:24:00 '))
show(DTConvert('1993-01-26  18.24.00 '))

show(DTConvert('26/01/1993'))
show(DTConvert('26.01.1993'))
# show(DTConvert('26-01-1993'))
show(DTConvert('01-26-1993'))
show(DTConvert('1993-01-26'))

# 1 февраля 1993
show(DTConvert('01/02/1993'))
show(DTConvert('01.02.1993'))
# show(DTConvert('01-02-1993'))
show(DTConvert('02-01-1993'))
show(DTConvert('1993-02-01'))

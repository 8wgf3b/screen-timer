import os


def csv_appender(*args, file='data/pc_stats.csv'):
    if os.path.exists(file):
        append_write = 'a'
    else:
        append_write = 'w'
    f = open(file,append_write)
    line = ','.join(args) + '\n'
    f.write(line)
    f.close()


if __name__ == '__main__':
    csv_appender('dummy.csv', '1', 'asdasasd')

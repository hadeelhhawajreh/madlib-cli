import re
import textwrap


def welcoming():
    return(textwrap.dedent('''
    **********************

    ** Welcome to Madli game **

    **********************
    '''))


def open_file(file_name):
    '''
    read the file 
    '''
    with open(file_name) as file:
        # print('Is the files closed ?', file.closed)
        content = file.read()
        file.close()
        return content


def editing(value):
    '''
    make all  {} in file  empty
    '''
    return re.sub('\{(.*?)\}', '{}', value)


def input_(value2):
    '''
    to fill all data inside {}
    '''
    values = re.findall("\{(.*?)\}", value2)
    answer = []
    for i in values:
        inp_value = input('Insert  '+i + ': ')
        answer.append(inp_value)
    return answer


def render(read, i):
    value_reading = read.format(*i)
    return value_reading


if __name__ == "__main__":
    print(welcoming())
    reading = open_file('assets/file.txt')
    edit = editing(reading)
    input = input_(reading)
    print(render(edit, input))

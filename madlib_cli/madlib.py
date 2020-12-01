import re
def open_file():
    with open('assets/file.txt', 'r+') as file:
        print('Is the files closed ?', file.closed)
        content = file.read()
        file.close()
        return content
# read the file as string

def editing(value):
    return re.sub('\{(.*?)\}', '{}', value)
# make {} empty

def input_(value2):
    r1 = re.findall("\{(.*?)\}",value2)
    print(len(r1))
    answer=[]
    for i in r1:
        inp_value=input('Insert '+i)
        answer.append(inp_value)
    return answer
# بعبي ال {}
def render(read,i):
    #i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10],i[11],i[12],i[13],i[14],i[15],i[16],i[17],i[18],i[19],i[20],i[21]
    value_reading=read.format(*i)
    return value_reading

if __name__ == "__main__":
    reading = open_file()
    edit=editing(reading)
    input=input_(reading)
    print(render(edit,input))
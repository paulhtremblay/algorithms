import random
import string

def _gen_random():
        return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(random.randint(30, 49)))

def make_sql_file(path, num_lines):
    with open(path, 'w') as write_obj:
        for i in range(num_lines):
            write_obj.write('{pk},{name1},{name2}\n'.format(
                pk = i, name1 = _gen_random(), 
                name2 = _gen_random()))

num_lines = 10000000
make_sql_file('/home/henry/test1.txt', num_lines)
make_sql_file('/home/henry/test2.txt', num_lines)
make_sql_file('/home/henry/test3.txt', num_lines)

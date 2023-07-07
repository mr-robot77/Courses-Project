def csv_reader(path):
    with open(path) as csv:
        for row in csv.readlines():
            yield row.rstrip().split(',')

def process(path):
    with open(path, 'r') as file:
        rows = []
        for row in file.readlines():
            values = row.rstrip().split(',')
            total = sum(map(int, values))
            new_row = ','.join(values + [str(total)])
            rows.append(new_row)
        
    with open('ans.csv', 'w') as output_file:
        output_file.write('\n'.join(rows))

#def process(path):
#    with open('ans.csv', 'w') as out:
#        for line in csv_reader(path):
#            ssum = sum(list(map(int, line.split(','))))
#            line = line + ',' + str(ssum)
#            out.write(line + '\n')  
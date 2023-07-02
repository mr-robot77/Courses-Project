def solve(path):
    with open(path, 'r') as file:
        lines = file.readlines()
        count = 0
        for line in lines:
                stripped_line = line.strip()
                if stripped_line and not stripped_line.startswith("#"):
                    count += 1
        return count
#print(solve('in.py'))
#print(solve('in1.py'))
#print(solve('in2.py'))
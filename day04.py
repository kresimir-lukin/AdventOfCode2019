import sys

def criteria_match(password, group_size_match_func):
    if len(password) != 6 or any(password[i] > password[i+1] for i in range(5)):
        return False
    groups = [password.count(ch) for ch in set(password)]
    return any(group_size_match_func(group) for group in groups)

assert len(sys.argv) == 2
pass_from, pass_to = map(int, open(sys.argv[1]).read().split('-'))

part1 = sum(criteria_match(str(pass_num), lambda x:x >= 2) for pass_num in range(pass_from, pass_to + 1))
part2 = sum(criteria_match(str(pass_num), lambda x:x == 2) for pass_num in range(pass_from, pass_to + 1))

print('Part 1: {0}, Part 2: {1}'.format(part1, part2))
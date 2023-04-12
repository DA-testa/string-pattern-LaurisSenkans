# python3

def read_input():
    input_type = input().strip()
    if input_type == 'I':
        pattern = input().strip()
        text = input().strip()
    elif input_type == 'F':
        with open('./tests/06', 'r') as f:
            pattern = f.readline().strip()
            text = f.readline().strip()
    return pattern, text



def print_occurrences(output):
    print(' '.join(map(str, output)))


def get_occurrences(pattern, text):

    occurrences = []
    p_len = len(pattern)
    t_len = len(text)
    p_hash = hash(pattern)
    t_hash = hash(text[:p_len])
    if t_hash == p_hash and text[:p_len] == pattern:
        occurrences.append(0)
    for i in range(1, t_len - p_len + 1):
        t_hash = hash(text[i:i+p_len])
        if t_hash == p_hash and text[i:i+p_len] == pattern:
            occurrences.append(i)
    return occurrences


if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
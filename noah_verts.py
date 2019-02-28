import sys

from read_input import read_input

def calc_score(prev_tag_set, nex_tag_set):
    return min(len(prev_tag_set & nex_tag_set),
               len(prev_tag_set - nex_tag_set),
               len(nex_tag_set - prev_tag_set))

def create_pairs(inp):
    outs = [] # (is_horizontal, pair_a, pair_b, tag_set, tmp_id)
    used = set()
    for i in inp:
        if i.i in used:
            continue
        if i.horizontal:
            used.add(i.i)
            outs.append((True, i, None, i.tag_set, len(outs)))
            continue
        for j in inp:
            if i.i == j.i:
                continue
            if j.horizontal or j.i in used:
                continue
            # todo: choose a better j
            used.add(i.i)
            used.add(j.i)
            outs.append((False, i, j, (i.tag_set | j.tag_set), len(outs)))
            break
    if len(outs) % 100 == 0:
        sys.stderr.write('Creating pairs {}\n'.format(len(outs)))
    return outs

def get_next(prev, slides, used_tmp_ids):
    BEST_SCORE_THRESH = 2
    best_score = -1
    best = None

    prev_horiz, prev_a, prev_b, prev_tag_set, prev_tmp_id = prev

    for other in slides:
        is_horiz, pair_a, pair_b, other_tag_set, other_tmp_id = other
        if other_tmp_id in used_tmp_ids:
            continue
        s = calc_score(prev_tag_set, other_tag_set)
        if s > best_score:
            best_score = s
            best = other
            if best_score > BEST_SCORE_THRESH:
                return best

    if best is None:
        for other in slides:
            is_horiz, pair_a, pair_b, other_tag_set, other_tmp_id = other
            if other_tmp_id not in used_tmp_ids:
                return other
    return best

def main():
    import random
    inp, tag2photo = read_input()
    random.shuffle(inp)

    slides = create_pairs(inp)

    sys.stderr.write('Chosen pairs\n')

    prev = slides[0]
    if prev is None:
        print('nope!')
        return

    outs = []
    used_ids = set()

    def ack(other):
        is_horiz, pair_a, pair_b, other_tag_set, other_tmp_id = other
        used_ids.add(other_tmp_id)
        if is_horiz:
            outs.append((pair_a.i, ))
        else:
            outs.append((pair_a.i, pair_b.i))
        
    ack(prev)
    while True:
        other = get_next(prev, slides, used_ids)
        if other is None:
            break
        ack(other)
        
        prev = other

        # debug
        if len(outs) % 100 == 0:
            sys.stderr.write('{}!\n'.format(len(outs)))
    print(len(outs))
    for s in outs:
        print(*s)

    


if __name__ == '__main__':
    main()

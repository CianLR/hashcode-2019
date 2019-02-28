import sys

from read_input import read_input

def calc_score(prev_tag_set, nex_tag_set):
    a = len(prev_tag_set & nex_tag_set)
    if a == 0:
        return 0
    b = len(prev_tag_set) - a
    c = len(nex_tag_set) - a
    return min(a, b, c)

def create_pairs(inp):
    outs = [] # (is_horizontal, pair_a, pair_b, tag_set, tmp_id)
    used = set()

    horiz = [p for p in inp if p.horizontal]

    for i in horiz:
        outs.append((True, i, None, i.tag_set, len(outs)))

    verts = [p for p in inp if p.vertical]
    verts = sorted(verts, key=lambda v: len(v.tag_set))
    for p in range(0, len(verts)//2):
        i = verts[p]
        j = verts[len(verts)-1-p]
        outs.append((False, i, j, (i.tag_set | j.tag_set), len(outs)))
    return outs

BEST_SCORE_THRESH = 2
def get_next(prev, slides, used_tmp_ids):
    global BEST_SCORE_THRESH
    calc_score_func = calc_score
    best_score = -1
    best = None

    prev_horiz, prev_a, prev_b, prev_tag_set, prev_tmp_id = prev

    for other in slides:
        is_horiz, pair_a, pair_b, other_tag_set, other_tmp_id = other
        if other_tmp_id in used_tmp_ids:
            continue
        s = calc_score_func(prev_tag_set, other_tag_set)
        if s > best_score:
            best_score = s
            best = other
            if best_score > BEST_SCORE_THRESH:
                return best

    if best_score < BEST_SCORE_THRESH:
        BEST_SCORE_THRESH = max(BEST_SCORE_THRESH-1, 0)
    # No best found, try to choose a random unused one.
    if best is None:
        # Couldn't find any at thresh
        for other in slides:
            is_horiz, pair_a, pair_b, other_tag_set, other_tmp_id = other
            if other_tmp_id not in used_tmp_ids:
                return other
    return best

def main():
    import random
    inp, tag2photo = read_input()
    random.shuffle(inp)

    sys.stderr.write('About to choose pairs.\n')

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
            sys.stderr.write('{} (thresh = {})!\n'.format(len(outs), BEST_SCORE_THRESH))
            # Clean out slides
            slides = [s for s in slides if s[4] not in used_ids]
            slides = sorted(slides, key=lambda s:-len(s[3]))
    print(len(outs))
    for s in outs:
        print(*s)

    


if __name__ == '__main__':
    main()

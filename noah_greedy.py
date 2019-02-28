import sys

from read_input import read_input

def s(prev, nex_tag_set):
    return min(len(prev.tag_set & nex_tag_set),
               len(prev.tag_set - nex_tag_set),
               len(nex_tag_set - prev.tag_set))

def get_next(inp, used_set, poss_set, prev, tag2photo):
    BEST_SCORE_THRESH = 100000
    best_score = -1
    best = None
    for t in prev.tags:
        for o in tag2photo[t]:
            if o.i in used_set:
                continue
            if o.vertical:
                for vert2 in poss_set:
                    if vert2.horizontal:
                        continue
                    tag_set = o.tag_set | vert2.tag_set
                    score = s(prev, tag_set)
                    if score > best_score:
                        best_score = score
                        best = (o, vert2)
                        if best >= BEST_SCORE_THRESH:
                            return best
                continue
            score = s(prev, o.tag_set)
            if score > best_score:
                best_score = score
                best = (o,)
                if best_score >= BEST_SCORE_THRESH:
                    return best
    return best

def choose_first(inp):
    for i in inp:
        if i.horizontal:
            return i
    return None

def main():
    import random
    inp, tag2photo = read_input()
    random.shuffle(inp)
    used_ids = set()

    poss_set = set(p for p in inp if p.horizontal)

    outs = []
    prev = choose_first(inp)
    if prev is None:
        print('nope!')
        return

    outs.append((prev.i,))
    used_ids.add(prev.i)
    poss_set.remove(prev)
    while True:
        nex = get_next(inp, used_ids, poss_set, prev, tag2photo)
        if nex is None:
            break
        if len(nex) == 1:
            nex = nex[0]
            outs.append((nex.i,))
            used_ids.add(nex.i)
            poss_set.remove(nex)
        else:
            outs.append(nex)
            for n in nex:
                used_ids.add(n.i)
                poss_set.remove(n)
            nex = Photo(-1, 'COMBO', nex[0].tags + nex[1].tags)
        prev = nex
        if len(outs) % 100 == 0:
            sys.stderr.write('{}!\n'.format(len(outs)))
    print(len(outs))
    for s in outs:
        print(*s)

    


if __name__ == '__main__':
    main()

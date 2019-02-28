import sys

from read_input import read_input

def s(prev, nex):
    return min(len(prev.tag_set & nex.tag_set),
               len(prev.tag_set - nex.tag_set),
               len(nex.tag_set - prev.tag_set))

def get_next(inp, used_set, poss_set, prev, tag2photo):
    best_score = -1
    best = None
    for t in prev.tags:
        for o in tag2photo[t]:
            if o.vertical:
                continue
            if o.i in used_set:
                continue
            score = s(prev, o)
            if score > best_score:
                best_score = score
                best = o
                if best_score >= 1:
                    return best
    return best

def choose_first(inp):
    for i in inp:
        if i.horizontal:
            return i
    return None

def main():
    inp, tag2photo = read_input()
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
        outs.append((nex.i,))
        used_ids.add(nex.i)
        poss_set.remove(nex)
        prev = nex
        if len(outs) % 100 == 0:
            sys.stderr.write('{}!\n'.format(len(outs)))
    print(len(outs))
    for s in outs:
        print(*s)

    


if __name__ == '__main__':
    main()

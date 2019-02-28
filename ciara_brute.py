from read_input import *
from collections import defaultdict
from random import shuffle

def gen_vert(vert):
    tags = sorted([(len(v.tag_set)," ".join(sorted(v.tag_set)), v) for v in vert], key=lambda a: a[:2])
    new_vert = []
    for i in range((len(tags) // 2) - 1):
        new_vert.append((tags[i][2], tags[-i - 1][2]))
    return new_vert

def main():
    photos, _ = read_input()
    slides = []
    vert, hor = [], []
    tag_to_index = defaultdict(list)
    tag_count = defaultdict(int)
    for p in photos:
        if p.vertical:
            vert.append(p)
        else:
            hor.append(p)
    vert = gen_vert(vert)
    phots = []
    for p in vert:
        phots.append((p[0].tag_set.union(p[1].tag_set), p[0].i, p[1].i))

    for p in hor:
        phots.append((p.tag_set, p.i))

    photo_used = [0] * len(phots)
    for i, p in enumerate(phots):
        for tag in p[0]:
            tag_count[tag] += 1
            tag_to_index[tag].append(i)
    freq = sorted(tag_count, reverse=True, key=lambda k: tag_count[k])
    
    for tag in freq:
        if tag_count[tag] < 2:
            break
        to_match = []
        for i in tag_to_index[tag]:
            if not photo_used[i]:
                to_match.append(i)
        for i in range(len(to_match) - 1):
            best_match = -1
            best_i = -1
            if not photo_used[to_match[i]]:
                for j in range(i + 1, len(to_match)):
                    if not photo_used[to_match[j]]:
                        intersect_len = len(phots[to_match[i]][0].intersection(phots[to_match[j]][0]))
                        score = min(intersect_len, len(phots[to_match[i]][0]) - intersect_len , len(phots[to_match[j]][0]) - intersect_len)
                        if score > best_match:
                            best_match = score
                            best_i = j
                if best_i != -1:
                    slides.append(phots[to_match[i]][1:])
                    slides.append(phots[to_match[best_i]][1:])
                    photo_used[to_match[i]] = 1
                    photo_used[to_match[best_i]] = 1
        #index_1, index_2 = False, False
        #for i in range(len(tag_to_index[tag])):
            '''if not index_1 and index_2:
                index_1 = index_2
                index_2 = False
            elif not index_1 and not index_2:
                index_1 = tag_to_index[tag][i]
            elif index_1 and not index_2:
                index_2 = tag_to_index[tag][i]

            if index_1 and index_2:
                if not photo_used[index_1] and not photo_used[index_2]:
                    slides.append(phots[index_1][1:])
                    slides.append(phots[index_2][1:])
                    photo_used[index_1] = 1
                    photo_used[index_2] = 1
                if photo_used[index_1]:
                    index_1 = False
                if photo_used[index_2]:
                    index_2 = False
            '''
    for i in range(len(photo_used)):
        if not photo_used[i]:
            slides.append(phots[i][1:])

    print(len(slides))
    for s in slides:
        print(*s)


if __name__ == '__main__':
    main()
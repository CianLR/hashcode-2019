from read_input import *
from collections import defaultdict

def main():
    photos, _ = read_input()
    verts = sum(p.vertical for p in photos)
    horz = sum(p.horizontal for p in photos)
    print("Number of photos", len(photos))
    print("{:.2f}% vertical, {:.2f} horizontal".format(
        verts*100/len(photos), horz*100/len(photos)))
    avg_tag_count = sum(len(p.tags) for p in photos) / len(photos)
    print("Average tag count: {:.2f}".format(avg_tag_count))
    all_tags = defaultdict(int)
    for p in photos:
        for t in p.tags:
            all_tags[t] += 1
    print("Unique tags", len(all_tags))
    freq = sorted(all_tags, reverse=True, key=lambda k: all_tags[k])
    print("Most common")
    for k in freq[:5]:
        print(k, all_tags[k])
    print("Least common")
    for k in freq[-5:]:
        print(k, all_tags[k])



if __name__ == '__main__':
    main()


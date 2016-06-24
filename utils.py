import sys

def progressbar(it, prefix = "", size = 60):
    count = len(it)
    def _show(_i):
        x = int(size*_i/count)
        print("%s[%s%s] %i/%i\r" % (prefix, "#"*x, "."*(size-x), _i, count) + "\n")
        sys.stdout.flush()

    _show(0)
    for i, item in enumerate(it):
        yield item
        _show(i+1)
    print()
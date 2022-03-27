def seq_notify(iterable, predicate, on_start=None, on_end=None):
    it = iter(iterable)
    for first in it:
        retval = predicate(first)
        if not isinstance(retval, bool):
            raise ValueError("Predicate must be a function which returns boolean value")
        if retval:
            break
    else:
        return
    last = first
    try:
        last = next(it)
    except StopIteration:
        if on_start is None and on_end is None:
           yield last
        else:
            if not on_start is None:
                on_start(last)
            if not on_end is None:
                on_end(last)
        return
    if predicate(last):
        if on_start is None:
            yield first
        else:
            on_start(first)
        for val in it:
            if predicate(val):
                yield last
                last = val
            else:
                if on_end is None:
                    yield last
                else:    
                    on_end(last)
                return
    else:
        if on_start is None and on_end is None:
           yield first
        else:
            if not on_start is None:
                on_start(first)
            if not on_end is None:
                on_end(first)
        return
    if on_end is None:
        yield last
    else:
        on_end(last)

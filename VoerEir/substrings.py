def lds(string: str) -> str:
    """ returns first longest distinct substring in input `string` """
    seens = {}
    start, end, curt_start = 0, 0, 0
    for curt_end, c in enumerate(string):
        try:
            last_seen = seens[c]
            if last_seen < curt_start:
                raise KeyError(f"'{c}' not found in '{string[curt_start: curt_end]}'")
            if end - start <  curt_end - curt_start:
                start, end = curt_start, curt_end
            curt_start = last_seen + 1
        except KeyError:
            pass
        seens[c] = curt_end
    else: 
        # case when the longest substring is suffix of the string, here curt_end
        # do not point to a repeating char hance included in the substring
        if string and end - start <  curt_end - curt_start + 1:
            start, end = curt_start, curt_end + 1
    return string[start: end]

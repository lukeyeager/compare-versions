from . import schemes

def is_valid(version):
    try:
        schemes.schemes['semver'](version)
    except schemes.InvalidVersionError:
        return False
    return True

def verify_list(versions, comparison):
    """
    Verify that a list of versions all match comparison
    Returns True if the versions are in order

    Arguments:
    versions -- a list of version strings
    comparison -- the comparison to evaluate on the list
    """
    if comparison not in ['eq','ne','gt','lt','ge','le']:
        raise ValueError('Invalid comparison "%s" - must be eq/ne/gt/lt/ge/le' % comparison)

    if len(versions) < 2:
        raise ValueError('You must provide at least two versions to compare')

    prev = schemes.schemes['semver'](versions[0])
    for curr in versions[1:]:
        curr = schemes.schemes['semver'](curr)
        if comparison == 'eq':
            res = prev == curr
        elif comparison == 'ne':
            res = prev != curr
        elif comparison == 'gt':
            res = prev > curr
        elif comparison == 'lt':
            res = prev < curr
        elif comparison == 'ge':
            res = prev >= curr
        elif comparison == 'le':
            res = prev <= curr
        if not res:
            print('ERROR: %s %s %s' % (prev, comparison_symbol(prev, curr), curr))
            return False
        prev = curr
    return True

def comparison_symbol(v1, v2):
    """
    Returns a character representation of the relationship between two objects
    """
    if v1 == v2:
        return '=='
    elif v1 > v2:
        return '>'
    elif v1 < v2:
        return '<'
    else:
        raise RuntimeError('Could not compare "%s" and "%s"' % (v1, v2))


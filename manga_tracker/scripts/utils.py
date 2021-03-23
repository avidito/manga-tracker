from terminaltables import AsciiTable

def cvt_group_to_table(group):
    """
    Convert group information from dict format to AsciiTable.
    """
    header = ['Title', 'Link']
    tbl_website = AsciiTable([['Website: ' + group[0]]])
    tbl_targets = AsciiTable([header] + group[1:])
    return tbl_website, tbl_targets

def cvt_target_to_table(target, new=False):
    """
    Convert target information from dict format to AsciiTable.

    Params:
        target      : dict. Target information that will be extracted.
        new         : boolean (default=False). Flag to set behaviour for new target (not from bounty list).

    Returns:
        preview_tbl : AsciiTable Object. Table format from target.
    """
    keys = ['website', 'newalias', 'newlink'] if (new) else ['website', 'alias', 'link']
    columns = ["Website", "Alias", "URL"]
    values = [target[key] for key in keys]
    preview = [[col, val] for col, val in zip(columns, values)]
    preview_tbl = AsciiTable([['Key', 'Value']] + preview)
    return preview_tbl

def cvt_header_to_table(header):
    """
    Convert header string to AsciiTable.

    Params:
        header      : str. String of header text.

    Returns:
        header_tbl : AsciiTable Object. Table format from header.
    """
    header_tbl = AsciiTable([[header]])
    return header_tbl

def cvt_idx_to_target(bounty_list, group_id, target_id):
    """
    Convert group id and target id into target dict.

    Params:
        bounty_list : dict. Full list of groups from bounty list.
        group_id    : int. Index of group to be converted.
        target_id   : int. Index of target in group to be converted.

    Returns:
        target      : dict. Target in dictionary format.
    """
    target = {
        'website': bounty_list[group_id]['website'],
        'alias': bounty_list[group_id]['targets'][target_id][0],
        'link': bounty_list[group_id]['targets'][target_id][1]
    }
    return target

def cvt_output_to_table(output):
    """
    Convert output list to AsciiTable.

    Params:
        output      : list. Output data in 2D list format.

    Returns:
        output_tbl  : AsciiTable Object. Table format from ouput data.
    """
    output_tbl = AsciiTable(output)
    return output_tbl

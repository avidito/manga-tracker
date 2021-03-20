from terminaltables import AsciiTable

def cvt_group_to_table(group):
    """
    Convert group information from dict format to AsciiTable.
    """
    header = ['Title', 'Link']
    tbl_website = AsciiTable([['Website: ' + group[0]]])
    tbl_targets = AsciiTable([header] + group[1:])
    return tbl_website, tbl_targets

def cvt_target_to_table(target):
    """
    Convert target information from dict format to AsciiTable.
    """
    keys = ['website', 'alias', 'link']
    columns = ["Website", "Alias", "URL"]
    values = [target[key] for key in keys]
    preview = [[col, val] for col, val in zip(columns, values)]
    preview_tbl = AsciiTable([['Key', 'Value']] + preview)
    return preview_tbl

def cvt_header_to_table(header):
    """
    Convert header string to AsciiTable.
    """
    return AsciiTable([[header]])

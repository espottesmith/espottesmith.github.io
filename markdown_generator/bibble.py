import re
import sys
from calendar import month_name

from pybtex.database.input import bibtex
import jinja2
import jinja2.sandbox

_months = {
    'jan': 1, 'feb': 2, 'mar': 3, 'apr': 4, 'may': 5, 'jun': 6,
    'jul': 7, 'aug': 8, 'sep': 9, 'oct': 10, 'nov': 11, 'dec': 12,
}


def _author_fmt(author):
    first = author.first_names[0] if len(author.first_names) else ""
    middle = " ".join(author.middle_names) if len(author.middle_names) else ""
    prelast = author.prelast_names[0] if len(author.prelast_names) else ""
    last = author.last_names[0] if len(author.last_names) else ""
    return ' '.join((first, middle, prelast, last))


def _andlist(ss, sep=', ', seplast=', and ', septwo=' and '):
    if len(ss) <= 1:
        andlist = ''.join(ss)
    elif len(ss) == 2:
        andlist = septwo.join(ss)
    else:
        andlist = sep.join(ss[:-1]) + seplast + ss[-1]

    return andlist.replace("Evan Walter Clark  Spotte-Smith", "<b>Evan Walter Clark  Spotte-Smith</b>")


def _author_list(authors):
    return _andlist([_author_fmt(a) for a in authors])


def _venue_type(entry):
    venuetype = ''
    if entry.type == 'inbook':
        venuetype = 'Chapter in '
    elif entry.type == 'techreport':
        venuetype = 'Technical Report '
    elif entry.type == 'phdthesis':
        venuetype = 'Ph.D. thesis, {}'.format(entry.fields['school'])
    elif entry.type == 'mastersthesis':
        venuetype = 'Master\'s thesis, {}'.format(entry.fields['school'])
    return venuetype


def _venue(entry):
    f = entry.fields
    if entry.type == 'article':
        venue = f['journal']
        try:
            if 'issue' in f:
                f['number'] = f['issue']
            if 'volume' in f and f.get('number'):
                venue += ' {0}({1})'.format(f['volume'], f['number'])
            elif 'volume' in f: # volume but no truthy (e.g. not "") number
                venue += ' {0}'.format(f['volume'])
            # TODO future feature DW 2015/02/06
            # if 'doi' in f:
            #     import re
            #     # stip e.g. "http://dx/doi.org/" prefix
            #     f['doi'] = re.sub(r'^https?://.+?/', '', f['doi'])
            #     venue += 'DOI: <a href="http://dx.doi.org/{0}">{0}</a>'.format(f['doi'])
        except KeyError:
            pass
    elif entry.type == 'inproceedings':
        venue = f['booktitle']
        try:
            if f['series']:
                venue += ' ({})'.format(f['series'])
        except KeyError:
            pass
    elif entry.type == 'inbook':
        venue = f['title']
    elif entry.type == 'techreport':
        venue = '{0}, {1}'.format(f['number'], f['institution'])
    elif entry.type == 'phdthesis' or entry.type == 'mastersthesis':
        venue = ''
    elif entry.type == "unpublished":
        venue = f['journal']
    else:
        venue = 'Unknown venue (type={})'.format(entry.type)
    return venue


def _title(entry):
    if entry.type == 'inbook':
        title = entry.fields['chapter']
    else:
        title = entry.fields['title']

    # remove curlies from titles -- useful in TeX, not here
    mapping = dict.fromkeys(map(ord, '{}'))
    title = title.translate(mapping)
    return title


def _main_url(entry):
    urlfields = ('url', 'ee')
    for f in urlfields:
        if f in entry.fields:
            return entry.fields[f]
    return None


def _extra_urls(entry):
    """Returns a dict of URL types to URLs, e.g.
       { 'nytimes': 'http://nytimes.com/story/about/research.html',
          ... }
    """
    urls = {}
    for k, v in entry.fields.items():
        k = k.lower()
        if not k.endswith('_url'):
            continue
        k = k[:-4]
        urltype = k.replace('_', ' ')
        urls[urltype] = v
    return urls


def _month_match (mon):
    if re.match('^[0-9]+$', mon):
        return int(mon)
    return _months[mon.lower()[:3]]


def _month_name (monthnum):
    try:
        return month_name[int(monthnum)]
    except:
        return ''


def _sortkey(entry):
    e = entry.fields
    year =  '{:04d}'.format(int(e['year']))
    return year


def main(bibfile, template):
    pathname = bibfile.split("/")[-1].split(".")[0]

    prefix =  """---
layout: archive
title: "{}"
permalink: /{}/
author_profile: true
---

""".format(pathname.capitalize(),
              pathname.lower())

    # Load the template.
    tenv = jinja2.sandbox.SandboxedEnvironment(extensions=['jinja2.ext.do'])
    tenv.filters['author_fmt'] = _author_fmt
    tenv.filters['author_list'] = _author_list
    tenv.filters['title'] = _title
    tenv.filters['venue_type'] = _venue_type
    tenv.filters['venue'] = _venue
    tenv.filters['main_url'] = _main_url
    tenv.filters['extra_urls'] = _extra_urls
    tenv.filters['monthname'] = _month_name
    with open(template) as f:
        tmpl = tenv.from_string(f.read())

    # Parse the BibTeX file.
    with open(bibfile) as f:
        db = bibtex.Parser().parse_stream(f)

    # Include the bibliography key in each entry.
    for k, v in db.entries.items():
        v.fields['key'] = k

    # Render the template.
    bib_sorted = sorted(db.entries.values(), key=_sortkey, reverse=True)
    out = tmpl.render(entries=bib_sorted)

    outstring = prefix + str(out)
    print(outstring.replace("./img", "/images"))


if __name__ == '__main__':
    main(*sys.argv[1:])

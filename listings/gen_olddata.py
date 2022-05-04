#!/usr/bin/env python3
"""Pull old posts / comments from mysql."""

import collections
import datetime
import html
import os

import pypandoc
import sqlalchemy as sa

TARGET = os.path.join(
    os.path.dirname(__file__),
    '..',
    'posts',
)
os.makedirs(TARGET, exist_ok=True)

ENGINE = sa.create_engine('mysql+mysqlconnector://root@localhost/oldblog')
META = sa.MetaData(ENGINE)
POSTS = sa.Table('gw_posts', META, autoload=True)
COMMENTS = sa.Table('gw_comments', META, autoload=True)
TERMS = sa.Table('gw_terms', META, autoload=True)
TERM_TAXO = sa.Table('gw_term_taxonomy', META, autoload=True)
TERM_RELS = sa.Table('gw_term_relationships', META, autoload=True)

COMMENT_BLACKLIST = {
    887,
    20,
    21,
    844,
    61,
    62,
    439,
    951,
    952,
    978,
    979,
    993,
}

def text_fix(text):
    for search, replace in [
        ('\r', ''),
        ('Ã¼', 'ü'),
        ('Ã®', 'î'),
        ('â€™', '’'),
        ('â€œ', '“'),
        ('â€¦', '…'),
        ('â€', '”'),
        ('Ã¥', 'å'),
        ('Ã†', 'Æ'),
        ('Ã¦', 'æ'),
        ('Ã¸', 'ø'),
        ('Ã˜', 'Ø'),
    ]:
        text = text.replace(search, replace)
    return text

def clean_content(content):
    content = text_fix(content)
    if '<p>' not in content:
        content = '<p>' + content.replace('\n\n', '</p><p>') + '</p>'
    content = pypandoc.convert_text(content, 'rst', format='html')
    while '\n\n\n' in content:
        content = content.replace('\n\n\n', '\n\n')
    content = content.strip()
    return content

for post in ENGINE.execute(sa.select([POSTS])):
    if post['post_status'] != 'publish':
        print('!skipping unpublished:', post['post_name'])
        continue
    print('processing:', post['post_date_gmt'].year, post['post_name'])
    slug = post['post_name']
    date = post['post_date_gmt'].replace(tzinfo=datetime.timezone.utc)
    updated = post['post_modified_gmt'].replace(tzinfo=datetime.timezone.utc)
    title = html.unescape(post['post_title'])
    content = clean_content(post['post_content'])

    tag_query = sa.select([
        TERMS.c.name
    ]).select_from(
        TERMS.join(
            TERM_TAXO, TERMS.c.term_id == TERM_TAXO.c.term_id
        ).join(
            TERM_RELS, TERM_TAXO.c.term_taxonomy_id == TERM_RELS.c.term_taxonomy_id
        )
    ).where(TERM_RELS.c.object_id == post['ID'])
    tag_list = [html.unescape(r['name']) for r in ENGINE.execute(tag_query)]

    post_meta = collections.OrderedDict()
    post_meta['slug'] = slug
    post_meta['date'] = str(date)
    if updated != date:
        post_meta['updated'] = str(updated)
    post_meta['tags'] = ', '.join(t.strip() for t in tag_list)

    folder = os.path.join(TARGET, f'{date.year:04d}', f'{date.month:02d}')
    os.makedirs(folder, exist_ok=True)
    path = os.path.join(folder, f'{slug}.rst')
    with open(path, 'wt') as outfile:
        outfile.write(title + '\n')
        outfile.write('=' * len(title) + '\n\n')
        for key, value in post_meta.items():
            outfile.write(f':{key}: {value}\n')
        outfile.write('\n')
        outfile.write(content + '\n')

    comment_query = sa.select([
        COMMENTS
    ]).where(COMMENTS.c.comment_post_ID == post['ID'])
    for comment in ENGINE.execute(comment_query):
        if comment['comment_approved'] != '1' or comment['comment_ID'] in COMMENT_BLACKLIST:
            print(
                ' -! skipping unapproved:',
                comment['comment_ID'],
                comment['comment_author'])
            continue
        print(' - processing comment', comment['comment_ID'])
        cid = comment['comment_ID']
        cauthor = text_fix(comment['comment_author'])
        cauthor_email = comment['comment_author_email']
        cauthor_url = comment['comment_author_url']
        cdate = comment['comment_date_gmt']
        cparent = comment['comment_parent']
        ccontent = clean_content(comment['comment_content'])

        comment_meta = collections.OrderedDict()
        comment_meta['id'] = str(cid)
        if cparent != 0:
            comment_meta['parent_id'] = str(cparent)
        comment_meta['author'] = cauthor
        if cauthor_email:
            comment_meta['author_email'] = cauthor_email
        if cauthor_url:
            comment_meta['author_url'] = cauthor_url
        comment_meta['date_utc'] = cdate
        comment_meta['compiler'] = 'rest'

        cpath = os.path.join(folder, f'{slug}.{cid}.wpcomment')
        with open(cpath, 'wt') as coutfile:
            for key, value in comment_meta.items():
                coutfile.write(f'.. {key}: {value}\n')
            coutfile.write('\n')
            coutfile.write(ccontent + '\n')

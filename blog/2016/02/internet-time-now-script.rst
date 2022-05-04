Internet Time Now script
========================

:slug: internet-time-now-script
:date: 2016-02-05 19:40:05+00:00
:tags: time, code snippets
:category: rumblings

On account of being mentioned by `Reply All <https://gimletmedia.com/show/reply-all/>`__,
I've been listening to back episodes of
`[TLDR] <http://www.onthemedia.org/tags/tldr_podcast/>`__. Listening to
`#15 - Internet Time <http://www.onthemedia.org/story/15-internet-time/>`__ caught
my attention and made me aware of
`Swatch Internet Time <https://en.wikipedia.org/wiki/Swatch_Internet_Time>`_.
It's kind of impractical but also kind of fun, especially as I've been a little
annoyed at recording times across timezones for something meant to persist,
like this blog.


For fun, I whipped up a quick python implementation:

.. code-block:: python

    import datetime
    import decimal

    def decimal_time(ts):
        mus_ts = (ts.hour * 3600 + ts.minute * 60 + ts.second) * 1000000 + ts.microsecond
        mus_day = 24 * 3600 * 1000000
        dec_time = decimal.Decimal(mus_ts) / decimal.Decimal(mus_day)
        return dec_time * 1000

    def internet_time_now(precision=0):
        precision = int(max(0, min(25, precision)))
        precision = 0 if precision < 1 else int(precision)
        format_len = 3 if precision < 1 else 4 + precision
        format_str = '@{{:0{l:d}.0{p:d}f}}'.format(l=format_len, p=precision)
        it_utc_p1 = datetime.datetime.utcnow() + datetime.timedelta(hours=1)
        return format_str.format(decimal_time(it_utc_p1))


Or, if you don't care about precision:

.. code-block:: python

    import datetime

    def decimal_time(ts):
        s_ts = ts.hour * 3600 + ts.minute * 60 + ts.second
        s_day = 24 * 3600
        return int(1000 * s_ts / s_day)

    def internet_time_now():
        it_utc_p1 = datetime.datetime.utcnow() + datetime.timedelta(hours=1)
        return '@{:03d}'.format(decimal_time(it_utc_p1))

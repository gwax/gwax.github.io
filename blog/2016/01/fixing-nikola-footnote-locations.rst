Fixing Nikola Footnote Locations
================================

:slug: fixing-nikola-footnote-locations
:date: 2016-01-23 23:44:17+00:00
:updated: 2018-04-16T06:06:57.494348+00:00
:tags: nikola, meta, code snippets
:category: meta

Personally, I prefer to intersperse my footnote declarations with the text
that is being footnoted when writing my. For example:[#]_

.. [#] This is just an example.

.. code-block:: ReST

    I might want to write something[#]_ where there's a footnote there.

    .. [#] I put the footnote definition here.

    And then I continue on with the rest of my writing.

Wherever they are declared, I prefer to have all of my footnotes appear at the
end of my posts. By default, `Nikola <https://getnikola.com>`_  puts the
footnotes in wherever they are declared. A simple snippet of javascript can be
used to fix the locations of footnotes:

.. code-block:: javascript

    $(document).ready(function() {
        $('.footnote').each(function(i, el) {
            $(el).appendTo(
                $(el).closest('.entry-content,.entry-summary'));
        });
    });

Simply wrap in a <script> tag and include in the BODY_END section of conf.py
or add it to your theme.

An Arbitrary map from SQL with Go
=================================

:slug: an-arbitrary-map-from-sql-with-go
:date: 2019-10-21 04:13:56+00:00
:tags: code snippets, golang
:category: progging

I've been writing a lot of Go_ lately and finding it a pleasant balance of
simplicity, power, functionality, and ecosystem support. In a lot of cases, I
am finding the guarantees afforded by type safety to be really nice but,
occasionally, the strict requirements can make some easy things much harder
than I want them to be.

.. _Go: https://golang.org/

Recently, I found myself wanting to test the behavior of some code the hit a
SQL database. Specifically, I wanted to check the results of a handful of
queries with varied columns and column types. With Python_, I'd approach this
with SQLAlchemy_, and turn the result into a :code:`list` of :code:`dict`\ s.

.. _Python: https://www.python.org/
.. _SQLAlchemy: https://www.sqlalchemy.org/

.. code-block:: python

    def rows_to_dicts(rows):
        """Covert a SQLAlchemy RowProxy into a list of dicts."""
        return [dict(r) for r in rows]

From here, it's pretty straightforward to assert the result matches
expectations. If you're using pytest_, you'll also get really clear details on
where the results aren't what you expect. If you don't have the expected
columns or column types spot on, you're assertion will be off but you won't
hit any underlying errors at this point of your testing.

.. _pytest: https://docs.pytest.org/en/latest/

Go_, on the other hand doesn't have quite as easy an option. The crux of the
problem is that the only way to get a result row out of a sql query is via
`(*Rows) Scan <https://golang.org/pkg/database/sql/#Rows.Scan>`_, which
demands you know something about the structure of the result before you
query. Luckily :code:`Scan` is happy to read anything into a :code:`*string`
as long as you're asking for the right number of values so we can write an
equivalent function to the python list comprehension.

.. code-block:: go

    import (
        "database/sql"
    )

    func RowsToMaps(rows *sql.Rows) ([]map[string]string, error) {
        columns, err := rows.Columns()
        if err != nil {
            return nil, err
        }
        columnCount := len(columns)

        cursor := make([]interface{}, columnCount)
        for i := 0; i < columnCount; i++ {
            var columnValue string
            cursor[i] = &columnValue
        }

        var resultMaps []map[string]string
        for rows.Next() {
            err := rows.Scan(cursor...)
            if err != nil {
                return resultMaps, err
            }
            rowMap := make(map[string]string, columnCount)
            for i, columnPtr := range cursor {
                key := columns[i]
                var columnStr string
                if columnStrPtr := columnPtr.(*string); columnStrPtr != nil {
                    columnStr = *columnStrPtr
                }
                rowMap[key] = columnStr
            }
            resultMaps = append(resultMaps, rowMap)
        }
        if err := rows.Err(); err != nil {
            return resultMaps, err
        }
        return resultMaps, nil
    }

This, much like the Python_ above, gives us a list of maps of column name
to column value, with the minor caveats that all values are strings and
:code:`NULL` values become empty strings. I found it a useful chunk of code,
so I thought I'd throw it up.

Sure, it's more verbose but sometimes that's the price we pay for dealing
with dynamic results in a staticly typed language. There are other prices
paid in the other direction.

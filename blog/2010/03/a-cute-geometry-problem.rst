A cute geometry problem
=======================

:slug: a-cute-geometry-problem
:date: 2010-03-11 19:57:13+00:00
:updated: 2010-05-06 23:26:10+00:00
:tags: musings, science & technology
:category: rumblings
:has_math: yes

I came across a cute geometry problem recently and I would like to pass it
along.

Problem
-------

Problem Statement
~~~~~~~~~~~~~~~~~

.. container:: row

    .. container:: four columns

        .. raw:: html

            <svg version="1.1" xmlns="http://www.w3.org/2000/svg"
                 class="u-max-full-width"
                 viewBox="0 0 1 1">
                <g stroke="black" stroke-width="0.005">
                    <rect x="0" y="0" width="1" height="1" fill="white"></rect>

                    <path fill="red" d="
                        M 0.5 0.1339745962155614
                        A 1 1, 0, 0, 1, 0.8660254037844386 0.5
                        A 1 1, 0, 0, 1, 0.5 0.8660254037844386
                        A 1 1, 0, 0, 1, 0.1339745962155614 0.5
                        A 1 1, 0, 0, 1, 0.5 0.1339745962155614
                        Z"></path>

                    <path fill="none" d="M 0 0 A 1 1, 0, 0, 0, 1 1 L 1 0 Z"></path>
                    <path fill="none" d="M 0 1 A 1 1, 0, 0, 0, 1 0 L 0 0 Z"></path>
                    <path fill="none" d="M 1 1 A 1 1, 0, 0, 0, 0 0 L 0 1 Z"></path>
                    <path fill="none" d="M 1 0 A 1 1, 0, 0, 0, 0 1 L 1 1 Z"></path>
                </g>
            </svg>

    .. container:: eight columns

        If the sides of the square are of unit length and all curves are
        circular arcs, what is the area of the highlighted region?

        Although substantially easier with the use of calculus or trigonometry,
        this problem can be solved entirely with basic geometry (no weird laws
        you might have forgotten since high school are necessary).

        I have derived a geometric solution, which follows, but I highly
        recommend trying to do it yourself first.

.. TEASER_END

Step 1
~~~~~~

.. container:: row

    .. container:: four columns

        .. raw:: html

            <svg version="1.1" xmlns="http://www.w3.org/2000/svg"
                 class="u-max-full-width"
                 viewBox="0 0 1 1">
                <g stroke="black" stroke-width="0.005">
                    <rect x="0" y="0" width="1" height="1" fill="white"></rect>

                    <path fill="red" d="M 0 1 A 1 1, 0, 0, 1, 1 0 L 0 0 Z"></path>

                    <path fill="none" d="M 0 0 A 1 1, 0, 0, 0, 1 1 L 1 0 Z"></path>
                    <path fill="none" d="M 0 1 A 1 1, 0, 0, 0, 1 0 L 0 0 Z"></path>
                    <path fill="none" d="M 1 1 A 1 1, 0, 0, 0, 0 0 L 0 1 Z"></path>
                    <path fill="none" d="M 1 0 A 1 1, 0, 0, 0, 0 1 L 1 1 Z"></path>
                </g>
            </svg>

    .. container:: eight columns

        The highlighted section is the full square minus a quarter circle with
        radius of unit length. The highlighted area can be found by simple
        subtraction.

        .. math::

            A = 1 - \frac{\pi}{4}

Step 2
~~~~~~

.. container:: row

    .. container:: four columns

        .. raw:: html

            <svg version="1.1" xmlns="http://www.w3.org/2000/svg"
                 class="u-max-full-width"
                 viewBox="0 0 1 1">
                <g stroke="black" stroke-width="0.005">
                    <rect x="0" y="0" width="1" height="1" fill="white"></rect>

                    <path fill="chartreuse" d="M 0 1 L 0.5 0.1339745962155614 L 1 1 Z"></path>

                    <path fill="none" d="M 0 0 A 1 1, 0, 0, 0, 1 1 L 1 0 Z"></path>
                    <path fill="none" d="M 0 1 A 1 1, 0, 0, 0, 1 0 L 0 0 Z"></path>
                    <path fill="none" d="M 1 1 A 1 1, 0, 0, 0, 0 0 L 0 1 Z"></path>
                    <path fill="none" d="M 1 0 A 1 1, 0, 0, 0, 0 1 L 1 1 Z"></path>
                </g>
            </svg>

    .. container:: eight columns

        Since the edges of the highlighted triangle are all on circular arcs
        of unit length, the highlighted triangle is an equilateral triangle.
        That the triangle is equilateral means that the intersection points
        between the arcs trisect each arc. That the triangle is equilateral
        and has unit length sides further allows us to calculate the height of
        the triangle.

        .. math::

            h = \frac{\sqrt{3}}{2}

Step 3
~~~~~~

.. container:: row

    .. container:: four columns

        .. raw:: html

            <svg version="1.1" xmlns="http://www.w3.org/2000/svg"
                 class="u-max-full-width"
                 viewBox="0 0 1 1">
                <g stroke="black" stroke-width="0.005">
                    <rect x="0" y="0" width="1" height="1" fill="white"></rect>

                    <path fill="red" d="M 1 0 A 1 1, 0, 0, 0, 0.5 0.1339745962155614 L 1 1 Z"></path>

                    <path fill="none" d="M 0 0 A 1 1, 0, 0, 0, 1 1 L 1 0 Z"></path>
                    <path fill="none" d="M 0 1 A 1 1, 0, 0, 0, 1 0 L 0 0 Z"></path>
                    <path fill="none" d="M 1 1 A 1 1, 0, 0, 0, 0 0 L 0 1 Z"></path>
                    <path fill="none" d="M 1 0 A 1 1, 0, 0, 0, 0 1 L 1 1 Z"></path>
                </g>
            </svg>

    .. container:: eight columns

        Having noted in Step 2 that the arc intersections trisect the arcs,
        the highlighted wedge becomes one twelfth of a circle with radius of
        unit length. The area can be found simply.

        .. math::

            A = \frac{\pi}{12}

Step 4
~~~~~~

.. container:: row

    .. container:: four columns

        .. raw:: html

            <svg version="1.1" xmlns="http://www.w3.org/2000/svg"
                 class="u-max-full-width"
                 viewBox="0 0 1 1">
                <g stroke="black" stroke-width="0.005">
                    <rect x="0" y="0" width="1" height="1" fill="white"></rect>

                    <path fill="red" d="M 1 0 L 0.5 0 L 0.5 0.1339745962155614 L 1 1 Z"></path>

                    <path fill="none" d="M 0 0 A 1 1, 0, 0, 0, 1 1 L 1 0 Z"></path>
                    <path fill="none" d="M 0 1 A 1 1, 0, 0, 0, 1 0 L 0 0 Z"></path>
                    <path fill="none" d="M 1 1 A 1 1, 0, 0, 0, 0 0 L 0 1 Z"></path>
                    <path fill="none" d="M 1 0 A 1 1, 0, 0, 0, 0 1 L 1 1 Z"></path>
                </g>
            </svg>

    .. container:: eight columns

        Since we know the height of the triangle from Step 2, we can subtract
        that from the height of the total square to get the left side of the
        highlighted trapezoid. The right side of the highlighted trapezoid is,
        of course, unit length. The width of the trapezoid, by symmetry, is one
        half unit length. Knowing both sides and the width, we can calculate
        the area of the highlighted trapezoid.

        .. math::

            A = \frac{1}{2} \cdot (1 + (1 - \frac{\sqrt{3}}{2})) \cdot \frac{1}{2} = \frac{4 - \sqrt{3}}{8}

Step 5
~~~~~~

.. container:: row

    .. container:: four columns

        .. raw:: html

            <svg version="1.1" xmlns="http://www.w3.org/2000/svg"
                 class="u-max-full-width"
                 viewBox="0 0 1 1">
                <g stroke="black" stroke-width="0.005">
                    <rect x="0" y="0" width="1" height="1" fill="white"></rect>

                    <path fill="red" d="M 1 0 A 1 1, 0, 0, 0, 0.5 0.1339745962155614 L 0.5 0 Z"></path>

                    <path fill="none" d="M 0 0 A 1 1, 0, 0, 0, 1 1 L 1 0 Z"></path>
                    <path fill="none" d="M 0 1 A 1 1, 0, 0, 0, 1 0 L 0 0 Z"></path>
                    <path fill="none" d="M 1 1 A 1 1, 0, 0, 0, 0 0 L 0 1 Z"></path>
                    <path fill="none" d="M 1 0 A 1 1, 0, 0, 0, 0 1 L 1 1 Z"></path>
                </g>
            </svg>

    .. container:: eight columns

        By subtracting the area found in Step 3 from the area found in Step 4,
        we can find the highlighted area.

        .. math::

            A = \frac{4 - \sqrt{3}}{8} - \frac{\pi}{12} = \frac{12 - 3 \sqrt{3} - 2 \pi}{24}

Step 6
~~~~~~

.. container:: row

    .. container:: four columns

        .. raw:: html

            <svg version="1.1" xmlns="http://www.w3.org/2000/svg"
                 class="u-max-full-width"
                 viewBox="0 0 1 1">
                <g stroke="black" stroke-width="0.005">
                    <rect x="0" y="0" width="1" height="1" fill="white"></rect>

                    <path fill="red" d="M 1 0 A 1 1, 0, 0, 0, 0.5 0.1339745962155614 A 1 1, 0, 0, 0, 0 0 Z"></path>

                    <path fill="none" d="M 0 0 A 1 1, 0, 0, 0, 1 1 L 1 0 Z"></path>
                    <path fill="none" d="M 0 1 A 1 1, 0, 0, 0, 1 0 L 0 0 Z"></path>
                    <path fill="none" d="M 1 1 A 1 1, 0, 0, 0, 0 0 L 0 1 Z"></path>
                    <path fill="none" d="M 1 0 A 1 1, 0, 0, 0, 0 1 L 1 1 Z"></path>
                </g>
            </svg>

    .. container:: eight columns

        By symmetry, we know that the highlighted area is twice the area found
        in Step 5.

        .. math::

            A = \frac{12 - 3 \sqrt{3} - 2 \pi}{12}

Step 7
~~~~~~

.. container:: row

    .. container:: four columns

        .. raw:: html

            <svg version="1.1" xmlns="http://www.w3.org/2000/svg"
                 class="u-max-full-width"
                 viewBox="0 0 1 1">
                <g stroke="black" stroke-width="0.005">
                    <rect x="0" y="0" width="1" height="1" fill="white"></rect>

                    <path fill="red" d="
                        M 0 1
                        A 1 1, 0, 0, 1, 0.5 0.1339745962155614
                        A 1 1, 0, 0, 0, 0 0
                        Z"></path>

                    <path fill="none" d="M 0 0 A 1 1, 0, 0, 0, 1 1 L 1 0 Z"></path>
                    <path fill="none" d="M 0 1 A 1 1, 0, 0, 0, 1 0 L 0 0 Z"></path>
                    <path fill="none" d="M 1 1 A 1 1, 0, 0, 0, 0 0 L 0 1 Z"></path>
                    <path fill="none" d="M 1 0 A 1 1, 0, 0, 0, 0 1 L 1 1 Z"></path>
                </g>
            </svg>

    .. container:: eight columns

        By subtracting the area found in Step 6 from the area found in Step 1,
        we can find the highlighted area.

        .. math::

            A = (1 - \frac{\pi}{4}) - \frac{12 - 3 \sqrt{3} - 2 \pi}{12} = \frac{3 \sqrt{3} - \pi}{12}

Step 8
~~~~~~

.. container:: row

    .. container:: four columns

        .. raw:: html

            <svg version="1.1" xmlns="http://www.w3.org/2000/svg"
                 class="u-max-full-width"
                 viewBox="0 0 1 1">
                <g stroke="black" stroke-width="0.005">
                    <rect x="0" y="0" width="1" height="1" fill="red"></rect>

                    <path fill="white" d="
                        M 0.5 0.1339745962155614
                        A 1 1, 0, 0, 1, 0.8660254037844386 0.5
                        A 1 1, 0, 0, 1, 0.5 0.8660254037844386
                        A 1 1, 0, 0, 1, 0.1339745962155614 0.5
                        A 1 1, 0, 0, 1, 0.5 0.1339745962155614
                        Z"></path>

                    <path fill="none" d="M 0 0 A 1 1, 0, 0, 0, 1 1 L 1 0 Z"></path>
                    <path fill="none" d="M 0 1 A 1 1, 0, 0, 0, 1 0 L 0 0 Z"></path>
                    <path fill="none" d="M 1 1 A 1 1, 0, 0, 0, 0 0 L 0 1 Z"></path>
                    <path fill="none" d="M 1 0 A 1 1, 0, 0, 0, 0 1 L 1 1 Z"></path>
                </g>
            </svg>

    .. container:: eight columns

        By symmetry, we know that the highlighted area is four times the area
        found in Step 7.

        .. math::

            A = \frac{3 \sqrt{3} - \pi}{3} = \sqrt{3} - \frac{\pi}{3}

Solution
~~~~~~~~

.. container:: row

    .. container:: four columns

        .. raw:: html

            <svg version="1.1" xmlns="http://www.w3.org/2000/svg"
                 class="u-max-full-width"
                 viewBox="0 0 1 1">
                <g stroke="black" stroke-width="0.005">
                    <rect x="0" y="0" width="1" height="1" fill="white"></rect>

                    <path fill="red" d="
                        M 0.5 0.1339745962155614
                        A 1 1, 0, 0, 1, 0.8660254037844386 0.5
                        A 1 1, 0, 0, 1, 0.5 0.8660254037844386
                        A 1 1, 0, 0, 1, 0.1339745962155614 0.5
                        A 1 1, 0, 0, 1, 0.5 0.1339745962155614
                        Z"></path>

                    <path fill="none" d="M 0 0 A 1 1, 0, 0, 0, 1 1 L 1 0 Z"></path>
                    <path fill="none" d="M 0 1 A 1 1, 0, 0, 0, 1 0 L 0 0 Z"></path>
                    <path fill="none" d="M 1 1 A 1 1, 0, 0, 0, 0 0 L 0 1 Z"></path>
                    <path fill="none" d="M 1 0 A 1 1, 0, 0, 0, 0 1 L 1 1 Z"></path>
                </g>
            </svg>

    .. container:: eight columns

        By subtracting the area found in Step 8 from the area of a unit length
        sided square, we can obtain the area of the highlighted region.

        .. math::

            A = 1 - (\sqrt{3} - \frac{\pi}{3}) = 1 + \frac{\pi}{3} - \sqrt{3} \approx 0.3151467

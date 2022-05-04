On airplane bandwidth and latency
=================================

:slug: on-airplane-bandwidth-and-latency
:date: 2009-07-03 00:21:27+00:00
:tags: computers, intzorweb
:has_math: yes

Having recently used Virgin America to transport myself across the
country, I was very pleased to have Internet access while I was in the
air. This, however, is not the sort of airplane bandwidth and latency
that I am going to talk about. Instead, I would like to discuss a
comparison between the bandwidth and latency of typical Internet
connections with those associated with taking a hard drive on an
airplane.

Let's say we compare a high speed (:math:`15\mathrm{Mbit}`) DSL connection to taking a
moderately large hard drive (:math:`500\mathrm{GB}`) on a plane for data rates between
San Francisco and Boston (:math:`\approx 7\mathrm{hr}`):

Bandwidth:

    -   DSL: :math:`15\frac{\mathrm{Mbit}}{\mathrm{s}}`
    -   Airplane: :math:`\frac{500\mathrm{GB}}{7\mathrm{hr}} \times \frac{1\mathrm{hr}}{60\mathrm{min}} \times \frac{1\mathrm{min}}{60\mathrm{s}} \times \frac{8000\mathrm{Mbit}}{1\mathrm{GB}} \approx 150\frac{\mathrm{Mbit}}{\mathrm{s}}`

Latency:

    -   DSL: :math:`\approx 100\mathrm{ms}`
    -   Airplane: :math:`>7\mathrm{hr}`

For fun, let's try something a little bigger on both sides: OC-768 vs
Boeing 747-400F plane filled with :math:`2\mathrm{TB}` hard drives.

Bandwidth:

    -   OC-768: :math:`38\frac{\mathrm{Gbit}}{\mathrm{s}}`
    -   747-400F: :math:`\frac{250000\mathrm{lb}}{7\mathrm{hr}} \times \frac{2\mathrm{TB}}{1.7\mathrm{lb}} \times \frac{1\mathrm{hr}}{60\mathrm{min}} \times \frac{1\mathrm{min}}{60\mathrm{s}} \times \frac{8\mathrm{Tbit}}{1\mathrm{TB}} \approx 93\frac{\mathrm{Tbit}}{\mathrm{s}}`

Latency:

    -   OC-768: :math:`<100\mathrm{ms}`
    -   747-400F: :math:`>7\mathrm{hr}`

Clearly, hard drives on an airplane will win in a purely bandwidth
driven application but airplanes suffer from incredibly high latency.
You will have to decide which is best choice based on your particular
use scenario.

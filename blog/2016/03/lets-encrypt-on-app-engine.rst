Let's Encrypt on App Engine
===========================

:slug: lets-encrypt-on-app-engine
:date: 2016-03-13 07:25:01+00:00
:updated: 2018-09-09T07:03:28+00:00
:tags: meta, code snippets
:category: meta

**UPDATE**: `As of September, 2017 <https://cloudplatform.googleblog.com/2017/09/introducing-managed-SSL-for-Google-App-Engine.html>`__,
Google App Engine will `manage SSL certificates for you <https://cloud.google.com/appengine/docs/standard/python/securing-custom-domains-with-ssl>`__.

--------

`Let's Encrypt <https://letsencrypt.org/>`_ is a fantastically convenient way
to get SSL certificates for your website without paying a bunch of money or
resorting to a `self-signed certificate <https://en.wikipedia.org/wiki/Self-signed_certificate>`__. It's also pretty easy to set up.

Easy as it is to set up, the instructions don't really explain much about
setup for `App Engine <https://cloud.google.com/appengine/>`_. It turns out to
be pretty straightforward.

.. TEASER_END


Prepare Your App
----------------

We need to modify our app.yaml file and set up a static route for the
let's encrypt challenge/response data. Add the following to the beginning of
the handlers section of your app.yaml file:

.. code-block:: yaml

    - url: /\.well-known/acme-challenge/(.+)
      static_files: letsencrypt/\1
      upload: letsencrypt/(.+)
      mime_type: text/plain

Also create a "letsencrypt" folder in your app directory.


Fire up Let's Encrypt
---------------------

Starting from the instructions on the `Let's Encrypt GitHub repo <https://github.com/letsencrypt/letsencrypt>`__,
let's retrieve and fire up letsencrypt. Outside your app folder, in a separate
terminal:

.. code-block:: sh

    git clone https://github.com/letsencrypt/letsencrypt
    cd letsencrypt
    ./letsencrypt-auto -a manual certonly

We want to run in manual mode and generate certs because there isn't currently
a plugin for handling app engine.

Let's Encrypt will ask you for a list of domains. After you enter the target
domains, it will show you a series of challenge response requests:

::

    Make sure your web server displays the following content at
    http://www.example.com/.well-known/acme-challenge/{ABC} before continuing:

    {ABC}.{DEF}

    If you don't have HTTP server configured, you can run the following
    command on the target server (as root):

    mkdir -p /tmp/letsencrypt/public_html/.well-known/acme-challenge
    cd /tmp/letsencrypt/public_html
    printf "%s" {ABC}.{DEF} > .well-known/acme-challenge/{ABC}
    # run only once per server:
    $(command -v python2 || command -v python2.7 || command -v python2.6) -c \
    "import BaseHTTPServer, SimpleHTTPServer; \
    s = BaseHTTPServer.HTTPServer(('', 80), SimpleHTTPServer.SimpleHTTPRequestHandler); \
    s.serve_forever()"
    Press ENTER to continue

In this case, {ABC} is the challenge and {ABC}.{DEF} is the response.

Don't press enter yet.


Prepare the challenge/response
------------------------------

Switch to the terminal in your app directory and run a modified version of
the printf command letsencrypt suggests:

.. code-block:: sh

    printf "%s" {ABC}.{DEF} > letsencrypt/{ABC}

Now, re-upload your app to app engine:

.. code-block:: sh

    appcfg.py update .


Finish building the certificate
-------------------------------

Now go back and press enter in letsencrypt-auto.

Repeat preparing the challenge/response and pressing enter until you've finished
running through all of your requested domains.

Hopefully you should see a message to the effect of:

::

     - Congratulations! Your certificate and chain have been saved at
       /etc/letsencrypt/live/www.example.com/fullchain.pem. Your cert will expire
       on YYYY-MM-DD. To obtain a new version of the certificate in the
       future, simply run Let's Encrypt again.
     - If you like Let's Encrypt, please consider supporting our work by:

       Donating to ISRG / Let's Encrypt:   https://letsencrypt.org/donate
       Donating to EFF:                    https://eff.org/donate-le


Upload your certificates
------------------------

Fire up the `cloud console <https://console.cloud.google.com/>`__. Go to
App Engine > Settings > SSL Certificates and click Upload a new
certificate. Give your certificate a name; I like letsencrypt-YYYYMMDD where
YYYYMMDD is the issuing date (today).

Now, in your terminal, retrieve the public key:

.. code-block:: sh

    cat /etc/letsencrypt/live/www.example.com/fullchain.pem

And paste the output into the public key box in the cloud console.

If you run into a permission error, try calling the command with sudo.

Now, in your terminal, retrieve the private key and convert to RSA PEM format:

.. code-block:: sh

    openssl rsa -inform pem -in /etc/letsencrypt/live/www.example.com/privkey.pem -outform pem

And paste the output into the box in the cloud console.

Ditto on possibly needing sudo.

You should now be able to enable this certificate for all of your app's
domains.

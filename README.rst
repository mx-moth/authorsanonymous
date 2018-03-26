=================
Authors Anonymous
=================

A website for an author who wishes to remain anonymous.

Running
=======

Runs using ``docker-compose``:

.. code-block:: console

    $ docker-compose up

Publishing
==========

Build the image, tag it, then push:

.. code-block:: console

    $ docker-compose build --no-cache --pull backend
    $ docker tag authorsanonymous_backend timheap/authorsanonymous:latest
    $ docker push timheap/authorsanonymous:latest

Then pull the image down and restart which ever docker host it is deployed on.

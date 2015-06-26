# -*- coding: utf-8 -*-
import subprocess
import os

from bottle import post, request, run


def _search(query):
    """
    Search method
    """
    q = 'howdoi {}'.format(query)
    p = subprocess.Popen(q, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                         shell=True)
    output, error = p.communicate()
    if error:
        return error

    output = "```\n{}```".format(output)
    return output


@post('/howdoi')
def howdoi():
    """
    Example:
        /howdoi open file python
    """
    text = request.query.text
    if not text:
        return 'Please type a ?text= param'

    output = _search(text)
    # formatting
    return output


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('DEBUG', False)
    run(host='0.0.0.0', port=port, debug=debug)

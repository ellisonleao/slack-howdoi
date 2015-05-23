# -*- coding: utf-8 -*-
import subprocess
import os

from flask import Flask, request, Response


app = Flask(__name__)
app.debug = os.environ.get('DEBUG', False)


def _search(query):
    """
    Search method
    """
    q = 'howdoi {}'.format(query)
    p = subprocess.Popen(q, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                         shell=True)
    output, error = p.communicate()
    return output or error


@app.route('/howdoi', methods=['post'])
def howdoi():
    """
    Example:
        /howdoi open file python
    """
    text = request.values.get('text')
    output = _search(text)

    # cleaning
    filter(None, output.replace('\r', '').split('\n'))

    # formatting
    output = """
    ```
    {}
    ```
    """.format(output)
    return Response(output, content_type='text/plain; charset=utf-8')


@app.route('/')
def home():
    return Response(':)', content_type='text/plain; charset=utf-8')


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

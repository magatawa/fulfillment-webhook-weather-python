from __future__ import print_function
from future.standard_library import install_aliases
install_aliases()

from urllib.parse import urlparse, urlencode
from urllib.request import urlopen, Request
from urllib.error import HTTPError

import json
import os

from flask import Flask
from flask import request
from flask import make_response, jsonify
import gspread
from oauth2client.service_account import SignedJwtAssertionCredentials


# Flask app should start in global layout
app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)
    result = req.get("result")
    parameters = result.get("parameters")
    weapon_name = parameters.get("weapon_name")

    json_key = json.load(open('TEST-543f03087558.json'))
    scope = ['https://spreadsheets.google.com/feeds']

    #ダウンロードしたjsonファイルを同じフォルダに格納して指定する
    credentials = SignedJwtAssertionCredentials(json_key['test-f6d93@appspot.gserviceaccount.com'], json_key['-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQDQWTBw/lFZTgKc\nAW7iSr3vIxPzqxqzGzj9rZMYzeR/1YWJuPJebWLGYwlyRXIcBkbrBHPhBMUqpXik\nEHXEMglLk86pkGdwNDksrDIN85tab6+tULO2u/KYxHUQCWLY5Y8+McV2f1/r9JQt\n7Ao9KEW9b0rFXnI1c0N7q91IfSkbX96AfLWwxghnxWc2AZ6hqyGw/5LILEt8DHSI\nYW/8x5HtGeiSOx3UqSJCpjOWDmTBMphmAROgl8ZSPZ62U21+f7sQQ/4fXx6wNJJU\nlxFCqIyRp4oFM4/oOIuAipdDFUwUp9Zcnh1iI2e9vURKG7K2D1Us4qFWTAFTP3d8\nFF34rJuFAgMBAAECggEAC7rtM+muxPWdNGyf8jamoVdR41JfoPRMxMQfEzvKoNXf\nfFcJ+2u75W5/lLnLNhskFJaQX+leoLj491oD4/MiF44md5ekF89XwQMNKq5ZaG9t\nd241PuedUA78qtWv4M5yLDfkbtPbMgrBDmrUCZq47CuDsYiZz6i44CQgnzSIwynD\nESz2Zh4ugkxjkF7CcHOmSKAMjz7fW2/REfgddXqV4dMvPaG3bezTRTItwqfktlYC\nxhqHLqmysVo68BNdvnOUPMC/I1Kzwk12w/U42RTW2QTmuOVBIJ+fsnw6MJR1bf2H\ngWCcvpBSB2Uky63b4AMiMe8hfn/O7tvTJX2kWM0/iwKBgQD1ZARZhvxAhXM3aaoT\nAE5vtCP/xfUoz0RYqEK5D1s5Qon8E4ituB6aG1fBfiHq5YPuDqbtSrqRnIhET9IO\n5YTe8D3ueYelB+gePjbez8Oy9W7Z2MJYUveTHzMnrBnRrW5L1QASQCyN0NsXb823\nzIB9khnM73T3QqO2nmkGfKm7IwKBgQDZWzAy6nAh0Vb6hAKMJVuS5Bw9OAFIrxvW\nCKpE2qNGmo90EphMB1UmT3TlQdGrZRmgw4Fy7u+pSSXVdelb5Pvh7NJikBeOuBZN\nUulMA62zxdt8+EjQ7Yc9lbvzk0AQtc5l1DDOFI3uaEzBa0jkSc2lqSIztj69C68v\nQOX+nJLtNwKBgEgU6B4wQ5rkWHLXjAjm1yOC4+w3BwvEzovIaUkZFK/eNtAgIM7+\nvaaBD6cb2PS6FKXyEeC0SdeKBpEibU7I5t3h7h9F/a1hhDKWDeInX5IK/FPrkzME\ntAq4aHtn13G7IyINYGb8CNpjlmftBJ3P6ZJ5PzDuygnzvklfgPRR3D3HAoGAS3zh\nE33abdRPmffJDrVWxYBV0mkmAQFX8JDX2cv5UucRFWXz4MvXJdQIrCqc0CLvsKbV\nyX30XF3cNvOZlWHEnSVrt/GFTPrgPACkp9LLPBlmblOorm8gPiJHwYONh4As666z\nOI9o77jnl3FUQnzjYDqKd10/EtcBA69NcY0ddicCgYB2E3/yGxftQrLDromDC1ji\n+Pr5CzVcimXQYH3bX0LenNzcGOPIRvBXsfaw/fcRlPhw0KEyNMzSqSJ6e2HctHm3\ni5sK5kq4mLya1ynNJIMDHzhajjd4/BzZYt3NvEM0+IOkJn3NDpL+auwbBKLxFnDr\nwOgmHSEv85WWRo9bjla7ng==\n-----END PRIVATE KEY-----\n'].encode(), scope)

    gc = gspread.authorize(credentials)
    # # 共有設定したスプレッドシートの名前を指定する
    wks = gc.open("Google Assistant Commands").sheet1

    cell = worksheet.find(weapon_name)

    text = str(cell.value) + str(worksheet.cell(cell.row,cell.col+1).value) + "パーセント"
    r = make_response(jsonify({'speech':text,'displayText':text}))
    r.headers['Content-Type'] = 'application/json'
    return r

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print("Starting app on port %d" % port)

    app.run(debug=False, port=port, host='0.0.0.0')

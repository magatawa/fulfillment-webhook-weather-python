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
from oauth2client.service_account import ServiceAccountCredentials


# Flask app should start in global layout
app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)
    result = req.get("result")
    parameters = result.get("parameters")
    weapon_name = parameters.get("weapon_name")

    scope = ['https://spreadsheets.google.com/feeds']

    #ダウンロードしたjsonファイルを同じフォルダに格納して指定する
    credentials = ServiceAccountCredentials.from_json_keyfile_name('TEST-1db5de85b421.json', scope)
    gc = gspread.authorize(credentials)

    # # 共有設定したスプレッドシートの名前を指定する
    worksheet = gc.open("Google Assistant Commands").get_worksheet(1)
#以下、動作テスト
# A1セルの値を取得
print worksheet.cell(1,1)
# A1セルを更新
worksheet.update_cell(1,1, u'Hello, gspread.')
if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print("Starting app on port %d" % port)

    app.run(debug=False, port=port, host='0.0.0.0')

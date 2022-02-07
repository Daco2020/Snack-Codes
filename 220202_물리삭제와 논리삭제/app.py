'''
1. 두 가지 종류의 삭제요청이 'DELETE' 혹은 'PUT' 메서드로 들어온다.
    'DELETE'는 '물리삭제' 실행
    'PUT'는 '논리삭제' 실행
2. 물리삭제의 경우 데이터베이스에서 삭제한다.
3. 논리삭제의 경우 데이터베이스에서 삭제플레그를 1로 수정한다.
4. 삭제요청에 대한 결과 값으로 현재 저장된 모든 데이터를 반환한다.
'''

from flask import Flask, request, jsonify
from connections import SnackDelete


app = Flask(__name__)


@app.route("/snack/<int:id>", methods=["DELETE", "PUT"])
def delete(id):
    if request.method == "DELETE":
        SnackDelete.delete_physics(id)

    elif request.method == "PUT":
        SnackDelete.delete_logical(id)

    result_value = SnackDelete.select_all()

    return jsonify({"remaining_users": result_value}), 200


if __name__ == "__main__":
    app.debug = True
    app.run()

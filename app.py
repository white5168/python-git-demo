# �ޤJ flask �M��U�����O�M�禡�A�`�N���O requests
from flask import Flask, request

# �ϥ� __name__ �N��ثe�B�@���{�����ҲզW�ٷ�@���ѦW�٨ϥΡA�U�����ͤ@�Ӻ������A������Ҫ���
app = Flask(__name__)

# ���� decorator ������}�� / �ɥѳo�Ө禡�t�d�B�z�A�Y�אּ @app.route('/hello') �h����} /hello �~���L�B�z
@app.route('/')
def hello():
    # request �� flask ���ت������ШD����A�i�H���X�����ШD��a����ơA�Ҧp�G���}�ѼơAex. name�Cget ��k���Y���}���S�� name �ѼơA�h�w�]�� World �r��C�Ҧp�Glocalhost:8080/?name=Jack
    name = request.args.get("name", "World")
    # ���A���^�� Hello, name �ܼƭ�
    return f'Hello, {name}!'

# �B�� Flask server�A�]�w��ť port 8080�]���� IP ��m�f�t Port �i�H���ѥX�n������ШD�e�쨺�� xxx.xxx.xxx.xxx:port�A0.0.0.0 �N����� IP�^
app.run(host='0.0.0.0', port=8080)
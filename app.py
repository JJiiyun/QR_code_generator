from flask import Flask, request, jsonify, render_template, send_from_directory
import qrcode
from io import BytesIO
import base64
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate-qr', methods=['GET'])
def generate_qr():
    try:
        # 파라미터 검증
        url = request.args.get('url')
        if not url:
            return jsonify({'error': 'URL parameter is required'}), 400

        # 크기 계산 로직 추가
        try:
            size = int(request.args.get('size', 300))
            box_size = max(5, min(size // 30, 20))  # 100~600px 범위 제한
        except ValueError:
            return jsonify({'error': 'Invalid size parameter'}), 400

        # QR 코드 최적화 생성
        qr = qrcode.QRCode(
            version=None,  # 자동 버전 선택
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=box_size,  # 동적 크기 조절
            border=4,
        )
        
        qr.add_data(url)
        qr.make(fit=True)

        # 이미지 품질 개선
        img = qr.make_image(fill_color="black", back_color="white")
        buffer = BytesIO()
        img.save(buffer, format="PNG", optimize=True)
        img_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')

        return jsonify({
            'qr_code': img_base64,
            'meta': {
                'requested_size': size,
                'actual_size': img.size[0],  # 실제 생성 크기
                'box_size': box_size
            }
        })

    except Exception as e:
        app.logger.error(f'Error: {str(e)}')
        return jsonify({'error': 'Internal server error'}), 500

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(
        os.path.join(app.root_path, 'static'),
        'favicon.ico',
        mimetype='image/vnd.microsoft.icon'
    )

if __name__ == '__main__':
    app.run(port=5001, debug=False) 
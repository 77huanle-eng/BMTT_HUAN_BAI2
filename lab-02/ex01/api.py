import sys
import os

# Thêm đường dẫn để tìm thấy các module trong thư mục 'cipher'
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from flask import Flask, request, jsonify
from cipher.caesar.caesar_cipher import CaesarCipher
from cipher.vigenere.vigenere_cipher import VigenereCipher
from cipher.railfence.railfence_cipher import RailFenceCipher
from cipher.playfair.playfair_cipher import PlayFairCipher
from cipher.transposition.transposition_cipher import TranspositionCipher
app = Flask(__name__)

# Khởi tạo đối tượng
rf_cipher = RailFenceCipher()
pf_cipher = PlayFairCipher()
trans_cipher = TranspositionCipher()
# --- Caesar Cipher ---
@app.route("/api/caesar/encrypt", methods=["POST"])
def caesar_encrypt():
    data = request.get_json()
    return jsonify({"cipher_text": CaesarCipher.encrypt_text(data['plain_text'], int(data['key']))})

@app.route("/api/caesar/decrypt", methods=["POST"])
def caesar_decrypt():
    data = request.get_json()
    return jsonify({"plain_text": CaesarCipher.decrypt_text(data['cipher_text'], int(data['key']))})

# --- Vigenere Cipher ---
@app.route("/api/vigenere/encrypt", methods=["POST"])
def vigenere_encrypt():
    data = request.get_json()
    return jsonify({"cipher_text": VigenereCipher.encrypt_text(data['plain_text'], data['key'])})

@app.route("/api/vigenere/decrypt", methods=["POST"])
def vigenere_decrypt():
    data = request.get_json()
    return jsonify({"plain_text": VigenereCipher.decrypt_text(data['cipher_text'], data['key'])})

# --- Rail Fence Cipher ---
@app.route("/api/railfence/encrypt", methods=["POST"])
def railfence_encrypt():
    data = request.get_json()
    encrypted = rf_cipher.rail_fence_encrypt(data['plain_text'], int(data['key']))
    return jsonify({"encrypted_text": encrypted})

@app.route("/api/railfence/decrypt", methods=["POST"])
def railfence_decrypt():
    data = request.get_json()
    decrypted = rf_cipher.rail_fence_decrypt(data['cipher_text'], int(data['key']))
    return jsonify({"decrypted_text": decrypted})

# --- Playfair Cipher ---
@app.route("/api/playfair/creamatrix", methods=["POST"])
def get_matrix():
    data = request.get_json()
    matrix = pf_cipher.create_playfair_matrix(data['key'])
    return jsonify({"matrix": matrix})
@app.route("/api/playfair/encrypt", methods=["POST"])
def playfair_encrypt():
    data = request.get_json()
    # Chuyển key thành string bằng str() trước khi truyền vào
    key = str(data.get("key")) 
    matrix = pf_cipher.create_playfair_matrix(key)
    cipher_text = pf_cipher.playfair_encrypt(data.get("plain_text"), matrix)
    return jsonify({"cipher_text": cipher_text})

@app.route("/api/playfair/decrypt", methods=["POST"])
def playfair_decrypt():
    data = request.get_json()
    # Chuyển key thành string bằng str() trước khi truyền vào
    key = str(data.get("key"))
    matrix = pf_cipher.create_playfair_matrix(key)
    plain_text = pf_cipher.playfair_decrypt(data.get("cipher_text"), matrix)
    return jsonify({"plain_text": plain_text})
# --- Route cho Transposition Cipher ---
@app.route("/api/transposition/encrypt", methods=["POST"])
def transposition_encrypt():
    data = request.get_json()
    return jsonify({
        "cipher_text": trans_cipher.encrypt(data['plain_text'], int(data['key']))
    })

@app.route("/api/transposition/decrypt", methods=["POST"])
def transposition_decrypt():
    data = request.get_json()
    result = trans_cipher.decrypt(data['cipher_text'], int(data['key']))
    return jsonify({"decrypted_text": result}) 

if __name__ == "__main__":
    app.run(debug=True)
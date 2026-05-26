import sys
import os

# Thêm thư mục lab-02 vào sys.path để Python tìm thấy folder 'cipher'
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from flask import Flask, request, jsonify
from cipher.caesar.caesar_cipher import CaesarCipher
from cipher.vigenere.vigenere_cipher import VigenereCipher

app = Flask(__name__)
# ... (Phần code còn lại)
@app.route("/api/caesar/encrypt", methods=["POST"])
def caesar_encrypt():

    data = request.get_json()

    plain_text = data.get("plain_text")
    key = int(data.get("key"))

    cipher_text = CaesarCipher.encrypt_text(
        plain_text,
        key
    )

    return jsonify({
        "cipher_text": cipher_text
    })


@app.route("/api/caesar/decrypt", methods=["POST"])
def caesar_decrypt():

    data = request.get_json()

    cipher_text = data.get("cipher_text")
    key = int(data.get("key"))

    plain_text = CaesarCipher.decrypt_text(
        cipher_text,
        key
    )

    return jsonify({
        "plain_text": plain_text
    })


@app.route("/api/vigenere/encrypt", methods=["POST"])
def vigenere_encrypt():

    data = request.get_json()

    plain_text = data.get("plain_text")
    key = data.get("key")

    cipher_text = VigenereCipher.encrypt_text(
        plain_text,
        key
    )

    return jsonify({
        "cipher_text": cipher_text
    })


@app.route("/api/vigenere/decrypt", methods=["POST"])
def vigenere_decrypt():

    data = request.get_json()

    cipher_text = data.get("cipher_text")
    key = data.get("key")

    plain_text = VigenereCipher.decrypt_text(
        cipher_text,
        key
    )

    return jsonify({
        "plain_text": plain_text
    })


if __name__ == "__main__":
    app.run(debug=True)
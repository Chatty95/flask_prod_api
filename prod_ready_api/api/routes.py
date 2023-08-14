from . import api_bp
from flask import request, jsonify
import numpy as np
import hashlib


@api_bp.route("/generate_random_array", methods=["POST"])
def generate_random_array():
    """
    Post endpoint
    """
    data = request.get_json()

    if "sentence" not in data:
        return jsonify({"error": "Please provide a valid input"}), 400
    sentence = data["sentence"]

    sentence_hash = hashlib.sha256(sentence.encode()).digest()
    # rng = np.random.Generator(np.random.SeedSequence(sentence_hash))
    seed = int.from_bytes(sentence_hash, byteorder="big")
    rng = np.random.default_rng(seed)
    random_array = rng.random(size=500).tolist()

    response = {"sentence": sentence, "random_array": random_array}
    return jsonify(response)


@api_bp.route("/generate-array", methods=["GET"])
def generate_array():
    """
    Demo get endpoint
    """
    return jsonify({"message": "Hello World"}), 200

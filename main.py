import jwt
def decode_jwt(token):
    try:
        decoded_token = jwt.decode(token, options={"verify_signature": False})
        return decoded_token
    except jwt.DecodeError:
        return "Invalid token"

if __name__ == "__main__":
    jwt_token = input("Digite o JWT: ")
    decoded = decode_jwt(jwt_token)
    print("Token decodificado:", decoded)
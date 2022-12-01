import jwt
import datetime
import configs.main_config

app_config = configs.main_config.APP_CONFIG
jwt_alg = "HS256"
def decode_auth_token(auth_jwt_token):
    try:
        payload = jwt.decode(auth_jwt_token, app_config.get("jwt_secret_key"), algorithms=jwt_alg)
        return payload
    except jwt.ExpiredSignatureError:
        raise Exception("Signature expired. Please log in again.")
    except jwt.InvalidTokenError:
        raise Exception("Invalid Token. Pleas log in again.")
    except Exception as ex:
        raise ex


def encode_auth_token(user_id, email, role):
    """Generate the Auth Token

    Args:
        id (number):
        userName (string):
    """
    
    try:
        payload = {
            "exp": datetime.datetime.utcnow() + datetime.timedelta(days=1),
            "iat": datetime.datetime.utcnow(),
            "sub": {"id": user_id, "email": email, "role": role}
        }
        return jwt.encode(
            payload,
            app_config.get("jwt_secret_key"),
            algorithm=jwt_alg
        )
    except Exception as ex:
        raise ex
    


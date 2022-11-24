import jwt
import datetime
import configs.main_config

app_config = configs.main_config.APP_CONFIG

def decode_auth_token(auth_token):
    pass



def encode_auth_token(password):
    """Generate the Auth Token

    Args:
        userName (string): 
    """
    
    try:
        payload = {
            "exp": datetime.datetime.utcnow() + datetime.timedelta(days=1),
            "iat": datetime.datetime.utcnow(),
            "sub": password
        }
        return jwt.encode(
            payload,
            app_config.get("jwt_secret_key"),
            algorithm="HS256"
        ).decode('utf-8')
    except Exception as ex:
        return ex
        
    pass    
    


import os
from requests import request
import json
from otc_api_sign_core import signer

def handler (event, context):

    # get ecs endpoint from environment variable or use default    
    endpoint= os.environ.get("ECS_ENDPOINT", "ecs.eu-de.otc.t-systems.com")
    
    # get project_id and instance_id from environment variables
    project_id = os.environ.get("RUNTIME_PROJECT_ID")
    
    # get instance_id from user data
    instance_id=context.getUserData("INSTANCE_ID")
    
    print(f"ECS-Endpoint: {endpoint}")
    print(f"Project ID: {project_id}")
    print(f"Instance ID: {instance_id}")  

    sig = signer.Signer()
    sig.Key = context.getSecurityAccessKey()
    sig.Secret = context.getSecuritySecretKey()
    sig.SecurityToken = context.getSecurityToken()
    
    
    method = "POST"

    url = f"https://{endpoint}/v1/{project_id}/cloudservers/action"

    headers = {
      "host": endpoint,
      "Content-Type": "application/json;charset=utf8",
      # To access resources in a subproject by calling APIs,
      # add the X-Project-Id parameter to the request header 
      # and set the parameter value to the project ID.
      "X-Project-Id": project_id,
      }

    body = {
        "os-start": {
            "servers": [
               {"id": instance_id},
            ]
        }
    }

    body_json = json.dumps(body)

    # sign
    r = signer.HttpRequest(method, url, headers, body_json)
    sig.Sign(r)
    print(f"X-SDK-Date: {r.headers['X-Sdk-Date']}")
    print(f"Authorization: {r.headers['Authorization']}")
    print(f"X-Security-Token: {r.headers['X-Security-Token']}")
    
    # send request
    resp = request(method, url, headers=r.headers, data=body_json.encode())
    print(resp.status_code, resp.reason)
    print(resp.content)

    # verify
    v = sig.Verify(r, r.headers["Authorization"])
    print(f"Verify: {v}")


    return {
        "statusCode": resp.status_code,
        "isBase64Encoded": False,
        "body": resp.text,
        "headers": {
            "Content-Type": "application/json"
        }
    }
    

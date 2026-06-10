# coding=utf-8
import json
import os
import requests
from otc_api_sign_core import signer

# Example to start an ECS instance using AK/SK authentication
if __name__ == "__main__":
  
    ecs_endpoint = "ecs.eu-de.otc.t-systems.com"
  
    ak=os.environ.get("OTC_SDK_AK")
    sk=os.environ.get("OTC_SDK_SK")   
    
    project_id = os.environ.get("OTC_SDK_PROJECTID")
    instance_id = os.environ.get("ECS_INSTANCE_ID")
    
    if ak is None or sk is None:
        print("Please set environment variables OTC_SDK_AK and OTC_SDK_SK")
        exit(1) 
        
    if project_id is None:
        print("Please set environment variable OTC_SDK_PROJECTID")
        exit(1) 
        
    if instance_id is None:
        print("Please set environment variable ECS_INSTANCE_ID")
        exit(1)

    print(f"Using AK: {ak}")
    print(f"Using Project ID: {project_id}")
    print(f"Using Endpoint: {ecs_endpoint}")
    print(f"Using Instance ID: {instance_id}")

    sig = signer.Signer()

    sig.Key = ak
    sig.Secret = sk

    method = "POST"

    url = f"https://{ecs_endpoint}/v1/{project_id}/cloudservers/action"

    headers = {
      "host": ecs_endpoint,
      "X-Project-Id": project_id,
      "Content-Type": "application/json;charset=utf8",
      "x-sdk-content-sha256": "UNSIGNED-PAYLOAD"
      }

    body = {
        "os-start": {
            "servers": [
                {"id": instance_id},
            ]
        }
    }

    body_json = json.dumps(body)

    # sign request
    r = signer.HttpRequest(method, url, headers, body_json)
    sig.Sign(r)
    print(f"X-Sdk-Date: {r.headers['X-Sdk-Date']}")
    print(f"Authorization: {r.headers['Authorization']}")

    # send request
    resp = requests.request(method, url, headers=r.headers, data=body_json.encode())
    print(f"Response status: {resp.status_code} {resp.reason}")
    print(f"Response text: {resp.text}")

    # verify
    v = sig.Verify(r, r.headers["Authorization"])
    print(f"Verification result: {v}")

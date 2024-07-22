from loguru import logger
import os
import requests
from http import HTTPStatus
from requests.models import Response, ConnectionError
from dataclasses import dataclass
from rich.pretty import pprint


@dataclass
class Client:
    #+-------------------------------------
    # API Connection Details
    #+-------------------------------------
    API_HOST = os.environ.get("API_HOST", "localhost")
    API_PORT = os.environ.get("API_PORT", 8800)
    API_HEADERS = {"Content-Type": "application/json", "accept": "application/json"}
    API_URL:str = "UNKNOWN"
    API_REQUEST_TIMEOUT = 10
    #+-------------------------------------

    def __post_init__(self):
        self.API_URL = f"http://{self.API_HOST}:{self.API_PORT}"

    def api_check_health(self, endpoint:str="/health") -> dict:
        return self.api_get_request(url=self.API_URL, headers=self.API_HEADERS, endpoint=endpoint)

    def api_get_request(self, url:str, headers:dict, endpoint:str, showresponse:bool=False) -> dict:
        data = {'status':True}
        response = Response()
        try:
            response = requests.get(url=f"{url}{endpoint}", headers=headers, timeout=self.API_REQUEST_TIMEOUT)
        except ConnectionError as e:
            logger.error(f"Unable to connect to API\n{e}")
        except Exception as e:
            data['status'] = False
            logger.error(f"Unable to make API call\n{e}")
        finally:
            if response.status_code != HTTPStatus.OK:
                data['status'] = False
            if data['status']:
                data['data'] = response.json()
                logger.debug(f"RequestType=GET; Endpoint={endpoint}; Response={data['data']}")
                if showresponse:
                    pprint(data['data'])
            else:
                data['data'] = str(response.content)
                logger.error(f"RequestType=GET; Endpoint={endpoint}; Response={data['data']}")
        return data

    def api_post_request(self, url:str, headers:dict, endpoint:str, data:dict, showresponse:bool=False) -> bool:
        status = True
        response = Response()
        try:
            response = requests.post(url=f"{url}{endpoint}", headers=headers, json=data, timeout=self.API_REQUEST_TIMEOUT)
        except ConnectionError as e:
            logger.error(f"Unable to connect to API\n{e}")
        except Exception as e:
            status = False
            logger.error(f"Unable to make API call\n{e}")
        finally:
            if response.status_code != HTTPStatus.OK:
                status = False
            if status:
                logger.debug(f"RequestType=POST; Endpoint={endpoint}; Data={data}; Response={response.json()}")
                if showresponse:
                    pprint(response.json())
            else:
                logger.error(f"RequestType=POST; Endpoint={endpoint}; Data={data}; Response={str(response.content)}")
        return status


if __name__ == "__main__":
    client = Client()
    responsedata = client.api_check_health()
    pprint(responsedata)

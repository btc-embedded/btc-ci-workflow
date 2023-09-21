import os
import platform
import subprocess
import time

import requests
from btc_config import get_global_config


class EPRestApi:
    #Starter for the EP executable
    def __init__(self, host='http://localhost', port=1337, version=None, install_location=None, lic='', config=None, use_docker=False):
        """
        Wrapper for the BTC EmbeddedPlatform REST API
        - when created without arguments, it uses the default install location & version defined in the global config (btc_config.yml)

        On Mac and Linux operating systems, the tool start is not handled by the wrapper.
        Instead, it tries to connect to a running instance at the specified port.
        You can call something like
           'docker run -p 1337:8080 -v "/my/workdir:/my/workdir" btces/ep'
        to run the BTC EmbeddedPlatform docker image.
        """
        if not (port and version and install_location) and not config:
            config = get_global_config()
        if config and config['installationRoot'] and config['epVersion']:
            version = config['epVersion']
            install_location = f"{config['installationRoot']}/ep{config['epVersion']}"
        self._PORT_ = str(port)
        self._HOST_ = host
        self.definitively_closed = False
        self.actively_started = False
        if not self.is_rest_service_available():
            if platform.system() == 'Windows':
                appdata_location = os.environ['APPDATA'].replace('\\', '/') + f"/BTC/ep/{version}/"
                print('Waiting for BTC EmbeddedPlatform to be available:')
                ml_port = 29300 + (port % 100)
                if ml_port == port:
                    ml_port -= 100
                args = f"{install_location}/rcp/ep.exe" + \
                    ' -clearPersistedState' + \
                    ' -application' + " ep.application.headless" + \
                    ' -nosplash' + \
                    ' -vmargs' + \
                    ' -Dep.runtime.batch=ep' + \
                    ' -Dep.runtime.api.port=' + str(ml_port) + \
                    ' -Dosgi.configuration.area.default="' + appdata_location + self._PORT_ + '/configuration"' + \
                    ' -Dosgi.instance.area.default="' + appdata_location + self._PORT_ + '/workspace"' + \
                    ' -Dep.configuration.logpath=AppData/Roaming/BTC/ep/' + version + '/' + self._PORT_ + '/logs' + \
                    ' -Dep.runtime.workdir=BTC/ep/' + version + '/' + self._PORT_ + \
                    ' -Dep.licensing.package=' + lic + \
                    ' -Dep.rest.port=' + self._PORT_
                subprocess.Popen(args, stdout=open(os.devnull, 'wb'), stderr=subprocess.STDOUT)
                self.actively_started = True
        else:
            print(f'Connected to BTC EmbeddedPlatform REST API at {host}:{port}')
            return
        print(f'Connecting to BTC EmbeddedPlatform REST API at {host}:{port}')
        while not self.is_rest_service_available():
            time.sleep(2)
            print('.', end='')
        print('\nBTC EmbeddedPlatform has started.')

    # closes the application
    def close_application(self):
        print('Exiting EP... please wait while we save your data.')
        request = requests.delete(self._url('/application'))
        print(request.text)
        self.definitively_closed = True

    def __del__(self):
        # might already be closed. not our problem.
        if self.actively_started and not self.definitively_closed:
            try: 
                pass
                #self.close_application()
            except:
                pass

    # wrapper directly returns the relevant object if possible
    def get(self, urlappendix, message=None):
        """Returns the result object, or the response, if no result object is available."""
        response = self.get_req(urlappendix, message)
        return self.extract_result(response)
    
    # wrapper directly returns the relevant object if possible
    def post(self, urlappendix, requestBody=None, message=None):
        """Returns the result object, or the response, if no result object is available."""
        response = self.post_req(urlappendix, requestBody, message)
        return self.extract_result(response)
    
    # wrapper directly returns the relevant object if possible
    def put(self, urlappendix, requestBody=None, message=None):
        """Returns the result object, or the response, if no result object is available."""
        response = self.put_req(urlappendix, requestBody, message)
        return self.extract_result(response)

    # wrapper directly returns the relevant object if possible
    def delete(self, urlappendix, message=None):
        """Performs a delete request and returns the response object"""
        return self.delete_req(urlappendix, message)

    # extracts the response object which can be nested in different ways
    def extract_result(self, response):
        """If the response object contains data, it is accessed via .json().
        If this data has a result field (common for post requests), its content is returned, otherwise the data object itself.
        If the response object has no data, the response iteslf is returned."""
        try:
            result = response.json()
            if 'result' in result:
                return result['result']
            else:
                return result
        except Exception:
            return response

    # Performs a get request on the given url extension
    def get_req(self, urlappendix, message=None):
        """Returns an http response object. If the POST method is expected to return an object,
        it's usually accessed by calling response.json()"""
        if not 'progress' in urlappendix:
            # print this unless it's a progress query (to avoid flooding the console)
            if message: print(message)
        response = requests.get(self._url(urlappendix.replace('\\', '/').replace(' ', '%20')))
        if not response.ok:
            raise Exception(f"Error during request GET {urlappendix}: {response.status_code}: {response.content}")
        return self.check_long_running(response)
    
    # Performs a delete request on the given url extension
    def delete_req(self, urlappendix, message=None):
        if message: print(message)
        response = requests.delete(self._url(urlappendix.replace('\\', '/').replace(' ', '%20')))
        if not response.ok:
            raise Exception(f"Error during request DELETE {urlappendix}: {response.status_code}: {response.content}")
        return self.check_long_running(response)

    # Performs a post request on the given url extension. The optional requestBody contains the information necessary for the request
    def post_req(self, urlappendix, requestBody=None, message=None):
        """Returns an http response object. If the POST method is expected to return an object,
        it's usually accessed by calling response.json()['result']"""
        url = urlappendix.replace('\\', '/').replace(' ', '%20')
        if message: print(message)
        if requestBody == None:
            response = requests.post(self._url(url))
        else:
            response = requests.post(self._url(url),json=requestBody)
        if not response.ok:
            raise Exception(f"Error during request POST {url}: {response.status_code}: {response.content}")
        return self.check_long_running(response)

    # Performs a post request on the given url extension. The optional requestBody contains the information necessary for the request
    def put_req(self, urlappendix, requestBody=None, message=None):
        url = urlappendix.replace('\\', '/').replace(' ', '%20')
        if message: print(message)
        if requestBody == None:
            response = requests.put(self._url(url))
        else:
            response = requests.put(self._url(url),json=requestBody)
        if not response.ok:
            raise Exception(f"Error during request PUT {url}: {response}")
        return self.check_long_running(response)

    # Checks if the REST Server is available
    def is_rest_service_available(self):
        try:
            response = requests.get(self._url('/test'))
        except requests.exceptions.ConnectionError:
            return False
        return response.ok

    # it's not important if the path starts with /, ep/ or directly with a resource
    def _url(self, path):
        return f"{self._HOST_}:{self._PORT_}/ep/{path.lstrip('/')}"

    # This method is used to poll a request until the progress is done.
    def check_long_running(self, response):
        if response.status_code == 202:
            jsonResponse = response.json()
            for key, value in jsonResponse.items():
                if key == 'jobID':
                    while response.status_code == 202:
                        time.sleep(2)
                        print('.', end='')
                        response = self.poll_long_running(value)
                    print('')
        return response

    def poll_long_running(self, jobID):
        return self.get_req('/progress?progress-id=' + jobID)


# if called directly, starts EP based on the global config
if __name__ == '__main__':
    EPRestApi(config=get_global_config())
    

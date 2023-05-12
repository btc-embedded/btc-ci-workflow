import os
import subprocess
import time

try:
    import requests
except Exception:
    print("Please run 'pip install requests' in terminal to install necessary dependencies.")
    exit(1)


class EPRestApi:
    #Starter for the EP executable
    def __init__(self, host='http://localhost', port=29267, version=None, install_location=None, lic='', config=None):
        if config and config['installationRoot'] and config['epVersion']:
            version = config['epVersion']
            install_location = f"{config['installationRoot']}/ep{config['epVersion']}"
        self._PORT_ = str(port)
        self._HOST_ = host
        self.definitively_closed = False
        if not self.is_rest_service_available():
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
        else:
            return
        while not self.is_rest_service_available():
            time.sleep(2)
            print('.', end='')
        print('\nBTC EmbeddedPlatform has started.')

    # closes the application
    def close_application(self):
        print('Exiting EP... please wait while we save your data.')
        request = requests.delete(self._url('/application'))
        print(request.text)
        print("Data saved!")
        self.definitively_closed = True

    def __del__(self):
        # might already be closed. not our problem.
        if not self.definitively_closed:
            try: 
                self.close_application()
                pass
            except:
                pass

    # Performs a get request on the given url extension
    def get_req(self, urlappendix):
        if not 'progress' in urlappendix:
            # print this unless it's a progress query (to avoid flooding the console)
            print('Fetching from: '+ self._url(urlappendix))
        response = requests.get(self._url(urlappendix.replace('\\', '/').replace(' ', '%20')))
        if not response.ok:
            raise Exception(f"Error during request POST {urlappendix}: {response.status_code}: {response.content}")
        return self.check_long_running(response)

    # Performs a post request on the given url extension. The optional requestBody contains the information necessary for the request
    def post_req(self, urlappendix, requestBody=None):
        url = urlappendix.replace('\\', '/').replace(' ', '%20')
        print('Posting to: ' +  self._url(url))
        if requestBody == None:
            response = requests.post(self._url(url))
        else:
            response = requests.post(self._url(url),json=requestBody)
        if not response.ok:
            raise Exception(f"Error during request POST {url}: {response.status_code}: {response.content}")
        return self.check_long_running(response)

    # Performs a post request on the given url extension. The optional requestBody contains the information necessary for the request
    def put_req(self, urlappendix, requestBody=None):
        url = urlappendix.replace('\\', '/').replace(' ', '%20')
        print('Posting to: ' +  self._url(url))
        if requestBody == None:
            response = requests.put(self._url(url))
        else:
            response = requests.put(self._url(url),json=requestBody)
        if not response.ok:
            raise Exception(f"Error during request POST {url}: {response}")
        return self.check_long_running(response)

    # Checks if the REST Server is available
    def is_rest_service_available(self):
        try:
            response = requests.get(self._url('/test'))
        except requests.exceptions.ConnectionError:
            return False
        return response.ok

    # URL appender
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

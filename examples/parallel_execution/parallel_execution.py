##############################################################################################
#
#    Example, demonstrating how to run tests for multiple test projects (*.epp)
#    in parallel using Python and BTC EmbeddedPlatform REST API with Docker.
#
##############################################################################################
import os
from concurrent.futures import ProcessPoolExecutor
from glob import glob
from multiprocessing import Manager

import docker
from create_test_report_summary import create_test_report_summary

from test_workflow import run_btc_test

CLIENT          = docker.from_env()          # client to interact with docker
IMAGE_NAME      = 'btces/ep'                 # official btc embeddedplatform image on dockerhub
LICENSE_SERVER  = '27000@my.license.server'  # replace with valid license server address
NO_WORKERS      = 3                          # Number of tests to run in parallel

def test_all_the_things(entrypoint=None):
    """
    Main Function
    """
    # find all epp files below the entrypoint directory
    if not entrypoint: entrypoint = os.getcwd()
    epp_files = glob(os.path.abspath(os.path.join(entrypoint, "**/*.epp")), recursive=True)

    # make a port queue so the parallel processes know which host-ports are available
    port_queue = Manager().Queue()
    for port in range(1337, 1337 + NO_WORKERS): port_queue.put(port)  # [ 1337, 1338, 1339 ]

    # iterate over *.epp's and schedule test executions in parallel
    futures = []
    print(f"Scheduling {len(epp_files)} test projects for execution using {NO_WORKERS} parallel workers.")
    with ProcessPoolExecutor(max_workers=NO_WORKERS) as worker_pool:
        for epp_file_abspath in epp_files:
            # Schedule this job's execution once a runner is available
            future = worker_pool.submit(run_workflow, epp_file_abspath, port_queue)
            futures.append(future)

    # access future-object to collect the results of the run_workflow calls
    results = [future.result() for future in futures]
    # create summary report
    create_test_report_summary(results)


def run_workflow(epp_file_abspath, port_queue):
    """
    Wrapper for process-safe execution of test workflows with BTC EmbeddedPlatform inside a docker container.
    - Starts up the container at an available port (from the port_queue)
    - Mounts the current epp_file's parent directory as a workspace
    - Executes the test workflow
    - Stops (well, actually kills) the container

    Returns the result object, that can be used for a summary report.
    """
    work_dir = os.path.dirname(epp_file_abspath)
    # Claim port from shared queue
    port = port_queue.get_nowait()
    # spin up docker container
    print(f'Starting container at port {port}')
    container = run_container(IMAGE_NAME, work_dir, port, { 'LICENSE': LICENSE_SERVER })
    
    # run test workflow
    result = run_btc_test(epp_file_abspath, port)
    
    # discard container
    print(f'Killing container at port {port}')
    container.kill()
    # Returning port
    port_queue.put(port)

    return result
    

def run_container(image_name, work_dir=None, port=None, env=None):
    """
    Runs the specified container image, mounting the work_dir,
    binding the port and setting the environment (if specified).

    Returns the container object
    """
    # Define configuration
    if work_dir: volumes = { f"{work_dir}": { 'bind': f"{work_dir}", 'mode': 'rw' } }
    if port: ports = { 8080 : port } # { container_port : host_port }
    # Create and start the container
    container = CLIENT.containers.run(
        image_name,
        volumes=volumes,
        environment=env,
        ports=ports,
        remove=True,
        detach=True
    )
    return container


if __name__ == '__main__':
    import sys
    entrypoint = sys.argv[1] if len(sys.argv) > 1 else None
    test_all_the_things(entrypoint)

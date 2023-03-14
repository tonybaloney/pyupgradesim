import subprocess
import pathlib

def test_version(version, time=60, users=4):
    root_path = pathlib.Path.cwd().parent
    # start the server
    subprocess.run(['docker', 'run', '--rm', '-d', '--network', 'host', "--name", f"benchmark-server-{version}", f"benchapp-{version}"], check=True)
    # run the tests
    subprocess.run(['python', '-m', 'profiler', f'results_{version}', str(time), str(users)], cwd=root_path, check=True)
    # stop the server
    subprocess.run(['docker', 'stop', f'benchmark-server-{version}'], check=True)

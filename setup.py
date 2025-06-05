from setuptools import setup
from setuptools.command.install import install
import subprocess
import os

class InstallFastAgentDepsCommand(install):
    def run(self):
        submodule_path = os.path.join(os.path.dirname(__file__), 'ext', 'fast-agent')
        
        # Check for the source file (e.g. pyproject.toml)
        source_file = os.path.join(submodule_path, 'pyproject.toml')
        if not os.path.exists(source_file):
            raise FileNotFoundError(f"Missing required source file for uv.lock: {source_file}")
        
        # Run uv pip sync in the correct directory
        subprocess.check_call(['uv', 'pip', 'sync', 'pyproject.toml'], cwd=submodule_path)
        
        install.run(self)

setup(
    name='veratemple',
    # arguments=[],
    version='0.1.0',
    # packages=['veratemple'],
    install_requires=[
        # Root-level deps here
    ],
    cmdclass={
        'install': InstallFastAgentDepsCommand,
    },
)
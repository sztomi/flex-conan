from conans import ConanFile, CMake, tools
from glob import glob
import os


class FlexConan(ConanFile):
    name = 'flex'
    version = '2.6.3'
    license = 'MIT'
    url = 'https://github.com/sztomi/flex-conan.git'
    description = 'This is a tooling package for GNU flex'
    settings = 'os', 'compiler', 'build_type', 'arch'
    generators = 'cmake', 'virtualenv'
    requires = (
        'autoconf/2.69@sztomi/testing',
        'automake/1.15@sztomi/testing',
        'm4/latest@sztomi/testing',
        'bison/3.0.4@sztomi/testing',
    )

    def source(self):
        self.tarball_url = 'https://github.com/westes/flex/releases/download/v{}/flex-{}.tar.gz'.format(self.version, self.version)
        tgz = self.tarball_url.split('/')[-1]
        tools.download(self.tarball_url, tgz)
        tools.untargz(tgz)
        os.unlink(tgz)

    def build(self):
        self.dirname = glob('flex-*')[0]
        os.chdir(self.dirname)
        def run_in_env(cmd):
            activate = '. ../activate.sh && '
            self.run(activate + cmd)
        run_in_env('./configure --prefix={}'.format(self.package_folder))
        run_in_env('make')
        self.run('make install')

    def package(self):
        pass

    def package_info(self):
        self.env_info.path.append(os.path.join(self.package_folder, 'bin'))
        

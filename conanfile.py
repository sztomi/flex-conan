from conans import ConanFile, CMake, tools
from glob import glob
import os


class M4Conan(ConanFile):
    name = "m4"
    version = "latest"
    license = "GNU m4"
    url = "https://github.com/sztomi/m4-conan.git"
    description = "This is a tooling package for GNU m4"
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake", "virtualenv"

    tarball_url = "https://gnu.cu.be/m4/m4-latest.tar.gz"

    def source(self):
        tgz = self.tarball_url.split('/')[-1]
        tools.download(self.tarball_url, tgz)
        tools.untargz(tgz)
        os.unlink(tgz)
        self.dirname = glob('m4-*')[0]

    def build(self):
        os.chdir(self.dirname)
        self.run('./configure --prefix={}'.format(self.package_folder))
        self.run('make')
        self.run('make install')

    def package(self):
        pass

    def package_info(self):
        self.env_info.path.append(os.path.join(self.package_folder, "bin"))
        

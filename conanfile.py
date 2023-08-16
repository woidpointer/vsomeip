from conan import ConanFile
from conan.tools.cmake import CMakeToolchain, CMake, cmake_layout


class VSomeIpRecipe(ConanFile):
    name = "vsomeip"
    version = "3.3.8"

    settings = "os", "compiler", "build_type", "arch"

    def config_options(self):
        pass

    def layout(self):
        cmake_layout(self)

    def generate(self):
        tc = CMakeToolchain(self)
        tc.generate()

    def requirements(self):
        self.requires("boost/1.82.0")

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()

    def export_sources(self):
        pass

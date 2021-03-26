from conans import ConanFile, CMake, tools
import os

class H5cpp11Conan(ConanFile):
    name = "h5cpp11"
    version = "0.1"
    license = "<Put the package license here>"
    author = "<Put your name here> <And your email here>"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "<Description of H5cpp11 here>"
    topics = ("<Put some tag here>", "<here>", "<and here>")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": False, "fPIC": True}
    generators = "cmake"
    requires = ["eigen/3.3.5@conan/stable",
                "hdf5/1.10.5",
                "gtest/1.10.0",
                "zlib/1.2.11@conan/stable"]

    exports_sources = "patch_file/cmake.patch"

    def source(self):
        self.run("git clone https://github.com/skulumani/fdcl-hdf5.git")

        patch_path = "../export_source/patch_file/cmake.patch"
        # file_path = "fdcl-hdf5/CMakeLists.txt"
        # self.run(f"patch {file_path} -i {patch_path} -o {file_path} -f")
        tools.patch(patch_file=patch_path)
 
    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder="fdcl-hdf5")
        cmake.build()

        # Explicit way:
        # self.run('cmake %s/hello %s'
        #          % (self.source_folder, cmake.command_line))
        # self.run("cmake --build . %s" % cmake.build_config)

    def package(self):
        self.copy("*.h*", dst="include", src="fdcl-hdf5/include")
        self.copy("*.h*", dst="include", src="build/include")
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.so.*", dst="lib", keep_path=False)

    def package_info(self):
        libs_list = self.collect_libs()
        undesired_libs = ["gtest"]
        libs_list = [x for x in libs_list if x not in undesired_libs]
        print(libs_list)

        self.cpp_info.libs = libs_list
        self.cpp_info.includedirs = ['include']
        self.cpp_info.libdirs = ['lib']

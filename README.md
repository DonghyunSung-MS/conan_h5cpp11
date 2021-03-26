# conan h5cpp11

## How to Download
```script
# git clone this repo
$ conan create .
```
* !warning before build set conan profile to ABI 11 compiler.libcxx=libstdc++11

## How to Use
1. General Cmake
```script
# In build dir
$ conan install <path to conanfile>
```
``` CMakeLists.txt
# In CMakeLists.txt
...
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()
set(CMAKE_CXX_STANDARD 11)

add_executable(example example.cpp)
target_link_libraries(example ${CONAN_LIBS})
...

or

...
include(${CMAKE_BINARY_DIR}/conan_paths.cmake)

find_package(h5cpp11 REQUIRED)
include_directories(${h5cpp11_INCLUDE_DIRS})

set(CMAKE_CXX_STANDARD 11)

add_executable(example example.cpp)
target_link_libraries(example ${h5cpp11_LIBRARIES})
...
```
1. In Ros Catkin Env
* conan_basic_setup() will destory catkin build environment, just use path generator to make compatiable.
```script
# In <catkin workspace dir>/build 
$ conan install <path to conanfile> #ex. conan install ../src/<pkg_name>/<conan_file>
```
``` CMakeLists.txt
...
include(${CMAKE_BINARY_DIR}/conan_paths.cmake)

find_package(h5cpp11 REQUIRED)
include_directories(${h5cpp11_INCLUDE_DIRS})

set(CMAKE_CXX_STANDARD 11)

add_executable(example example.cpp)
target_link_libraries(example ${h5cpp11_LIBRARIES})
...
```
## Credit
https://github.com/skulumani/fdcl-hdf5.git

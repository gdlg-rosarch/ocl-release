# Script generated with Bloom
pkgdesc="ROS - Orocos component library This package contains standard components for the Orocos Toolchain"
url='http://www.orocos.org/ocl'

pkgname='ros-kinetic-ocl'
pkgver='2.9.0_2'
pkgrel=1
arch=('any')
license=('LGPL v2'
)

makedepends=('cmake'
'lua'
'ncurses'
'netcdf'
'readline'
'ros-kinetic-catkin'
'ros-kinetic-log4cpp'
'ros-kinetic-rtt'
)

depends=('lua'
'ncurses'
'netcdf'
'readline'
'ros-kinetic-catkin'
'ros-kinetic-log4cpp'
'ros-kinetic-rtt'
)

conflicts=()
replaces=()

_dir=ocl
source=()
md5sums=()

prepare() {
    cp -R $startdir/ocl $srcdir/ocl
}

build() {
  # Use ROS environment variables
  source /usr/share/ros-build-tools/clear-ros-env.sh
  [ -f /opt/ros/kinetic/setup.bash ] && source /opt/ros/kinetic/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/kinetic \
        -DPYTHON_EXECUTABLE=/usr/bin/python2 \
        -DPYTHON_INCLUDE_DIR=/usr/include/python2.7 \
        -DPYTHON_LIBRARY=/usr/lib/libpython2.7.so \
        -DPYTHON_BASENAME=-python2.7 \
        -DSETUPTOOLS_DEB_LAYOUT=OFF
  make
}

package() {
  cd "${srcdir}/build"
  make DESTDIR="${pkgdir}/" install
}


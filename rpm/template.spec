Name:           ros-jade-ocl
Version:        2.8.2
Release:        0%{?dist}
Summary:        ROS ocl package

Group:          Development/Libraries
License:        LGPL v2
URL:            http://www.orocos.org/ocl
Source0:        %{name}-%{version}.tar.gz

Requires:       compat-lua-devel
Requires:       ncurses-devel
Requires:       netcdf
Requires:       readline-devel
Requires:       ros-jade-catkin
Requires:       ros-jade-log4cpp
Requires:       ros-jade-rtt
BuildRequires:  cmake
BuildRequires:  compat-lua-devel
BuildRequires:  ncurses-devel
BuildRequires:  netcdf
BuildRequires:  readline-devel
BuildRequires:  ros-jade-catkin
BuildRequires:  ros-jade-log4cpp
BuildRequires:  ros-jade-rtt

%description
Orocos component library This package contains standard components for the
Orocos Toolchain

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/jade" \
        -DCMAKE_PREFIX_PATH="/opt/ros/jade" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/jade

%changelog
* Fri Jun 24 2016 Orocos Developers <orocos-dev@lists.mech.kuleuven.be> - 2.8.2-0
- Autogenerated by Bloom

* Wed Jul 22 2015 Orocos Developers <orocos-dev@lists.mech.kuleuven.be> - 2.8.1-0
- Autogenerated by Bloom


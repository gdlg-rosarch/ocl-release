Name:           ros-indigo-ocl
Version:        2.8.1
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
Requires:       ros-indigo-catkin
Requires:       ros-indigo-log4cpp
Requires:       ros-indigo-rtt
BuildRequires:  cmake
BuildRequires:  compat-lua-devel
BuildRequires:  ncurses-devel
BuildRequires:  netcdf
BuildRequires:  readline-devel
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-log4cpp
BuildRequires:  ros-indigo-rtt

%description
Orocos component library This package contains standard components for the
Orocos Toolchain

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Tue Jul 21 2015 Orocos Developers <orocos-dev@lists.mech.kuleuven.be> - 2.8.1-0
- Autogenerated by Bloom

* Tue May 05 2015 Orocos Developers <orocos-dev@lists.mech.kuleuven.be> - 2.8.0-1
- Autogenerated by Bloom

* Fri Jan 23 2015 OCL Development Team <orocos-dev@lists.mech.kuleuven.be> - 2.8.0-0
- Autogenerated by Bloom


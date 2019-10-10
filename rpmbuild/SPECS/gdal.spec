# Tests can be of a different version
%global testversion 2.2.3
%global run_tests 0
#%global _prefix	/usr/local

%global bashcompletiondir %(pkg-config --variable=compatdir bash-completion)

Name:		gdal
Version:	2.2.3
Release:	14%{?dist}%{?bootstrap:.%{bootstrap}.bootstrap}
Summary:	GIS file format library
License:	MIT
URL:		http://www.gdal.org
Source:	%{name}-%{version}.tar.gz


%description
Geospatial Data Abstraction Library (GDAL/OGR) is a cross platform
C++ translator library for raster and vector geospatial data formats.
As a library, it presents a single abstract data model to the calling
application for all supported formats. It also comes with a variety of
useful commandline utilities for data translation and processing.

It provides the primary data access engine for many applications.
GDAL/OGR is the most widely used geospatial data access library.

%prep
%setup -T -D

%build
#CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=%{_prefix}  --mandir=%{_mandir} --sysconfdir=/etc

%install
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT LIBDIR=%_libdir install
#make prefix="${RPM_BUILD_ROOT}/usr/local" install
#make prefix="${RPM_BUILD_ROOT}/usr/local" libdir="${RPM_BUILD_ROOT}/usr/local/lib" install
# to silence the check-rpath error
export QA_RPATHS=$[ 0x0002 ]

#%clean
#[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf "$RPM_BUILD_ROOT"

%files
%defattr(-,root,root)
%dir /usr/local/bin
%{_bindir}/*
%{_prefix}/share/*
%{_libdir}/*
%{_prefix}/include/*

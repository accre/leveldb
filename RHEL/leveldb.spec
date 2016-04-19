Name:		leveldb
Version:	2.0.17
Release:	1%{?dist}
Summary:	Basho's fork of Googles LevelDB, a fast and lightweight key/value database library

Group:		Applications/Databases
License:	BSD
URL:		https://github.com/basho/leveldb
Source0:	https://github.com/basho/leveldb/archive/%{version}.tar.gz

Patch1:		leveldb-0001-initial-build-changes.patch

# snappy and tcmalloc from gperftools are both potentially optional 
#BuildRequires:	snappy-devel,gperftools-devel
#Requires:	

%description
Basho's fork of Googles LevelDB, a fast and lightweight key/value database library



%package devel
Summary:        The development files for %{name}
Group:          Development/Libraries

%description devel
Additional header files for development with %{name}.



%package doc
Summary:        The documentation files for %{name}
Group:          Documentation

%description doc
Additional documentation for %{name}.


%prep
%setup -q
%patch1 -p1

%build
make %{?_smp_mflags} PREFIX=/usr LIBDIR=$(basename %{_libdir})


%install
make install DESTDIR=%{buildroot} PREFIX=/usr LIBDIR=$(basename %{_libdir})


%files
%doc AUTHORS LICENSE README README.GOOGLE
%{_libdir}/lib%{name}.so.*

%files devel
%{_includedir}/%{name}/
%{_libdir}/lib%{name}.so
%{_libdir}/lib%{name}.a
%{_libdir}/libmemenv.a
# TODO add pkgconfig

%files doc
%doc doc/

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%changelog
* Mon Apr 18 2016 Matthew Heller <matthew.f.heller@accre.vanderbilt.edu> - 2.0.17-1
- Initial RPM packaging support

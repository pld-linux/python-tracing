%define 	module	tracing
Summary:	Python debug logging helper
Name:		python-%{module}
Version:	0.8
Release:	1
License:	GPL v3+
Group:		Libraries/Python
Source0:	http://code.liw.fi/debian/pool/main/p/python-%{module}/%{name}_%{version}.orig.tar.gz
# Source0-md5:	9f449746b2ae19ca62bca5363ae0b432
URL:		http://liw.fi/tracing
BuildRequires:	python-Sphinx
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Python library tracing helps with logging debug messages. It
provides a couple of functions for logging debug messages, and allows
the user to enable or disable logging for particular code modules.

It is sometimes practical to add a lot of debugging log messages to a
program, but having them enabled all the time results in very large
log files. Also, logging that much takes quite a bit of time.

This module provides a way to turn such debugging or tracing messages
on and off, based on the filename they occur in. The logging can that
be left in the code, and only enabled when it is needed.

%package doc
Summary:	Documentation for %{module}
Requires:	%{name} = %{version}-%{release}

%description doc
This package contains the documentation for %{module}, a Python debug
logging helper.

%prep
%setup -q

%build
%{__python} setup.py build

# Build documentation
%{__make} -C doc html

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	--skip-build \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS README
%{py_sitescriptdir}/tracing.py[co]
%{py_sitescriptdir}/tracing-%{version}-py*.egg-info

%files doc
%defattr(644,root,root,755)
%doc doc/_build/html/* example.py

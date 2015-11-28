
%define 	module	pyrad

Summary:	pyrad - Python implementation of a RADIUS client
Summary(pl.UTF-8):	pyrad - implementacja klienta RADIUS w Pythonie
Name:		python-%{module}
Version:	1.1
Release:	3
License:	BSD-like
Group:		Libraries/Python
Source0:	http://pypi.python.org/packages/source/p/pyrad/%{module}-%{version}.tar.gz
# Source0-md5:	ab1502f8ccd7409ced757d78b0dee7df
URL:		http://www.wiggy.net/code/pyrad/
BuildRequires:	python-devel >= 1:2.3
BuildRequires:	python-modules
BuildRequires:	python-setuptools
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-libs
BuildRequires:	rpmbuild(macros) >= 1.219
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pyrad is an implementation of a RADIUS client as described in RFC2865.
It takes care of all the details like building RADIUS packets, sending
them and decoding responses.

%description -l pl.UTF-8
pyrad jest implementacją klienta protokołu RADIUS, opisanego w
dokumencie RFC2865. Moduł ten odpowiada za wszystkie aspekty
przetwarzania protokołu RADIUS, takie jak budowanie pakietów
protokołu, wysyłanie ich oraz odkodowywanie odpowiedzi.

%package examples
Summary:	Example programs for Python pyrad module
Summary(pl.UTF-8):	Programy przykładowe do modułu Pythona pyrad
Group:		Development/Languages/Python
Requires:	%{name} = %{version}-%{release}

%description examples
This package contains example programs for Python pyrad module.

%description examples -l pl.UTF-8
Pakiet zawierający programy przykładowe dla modułu Pythona pyrad.

%prep
%setup -q -n %{module}-%{version}

%build
python setup.py build_ext

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{py_sitescriptdir},%{_examplesdir}/%{name}-%{version}}

%py_install \
	--install-lib=%{py_sitescriptdir} \
	--optimize=2
%py_postclean

cp -a example/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.txt
%{py_sitescriptdir}/pyrad
%{py_sitescriptdir}/%{module}-*.egg-info

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}

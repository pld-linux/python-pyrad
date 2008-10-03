
%define 	module	pyrad

Summary:	pyrad - Python implementation of a RADIUS client
Summary(pl.UTF-8):	pyrad - implementacja klienta RADIUS w Pythonie
Name:		python-%{module}
Version:	0.9
Release:	2
License:	BSD-like
Group:		Libraries/Python
Source0:	http://www.wiggy.net/files/%{module}-%{version}.tar.gz
# Source0-md5:	c28a055eefc4244b6b7b09a6c1083d3a
URL:		http://www.wiggy.net/code/pyrad/
BuildRequires:	python-devel >= 1:2.3
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

python setup.py install \
	--root=$RPM_BUILD_ROOT \
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

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}

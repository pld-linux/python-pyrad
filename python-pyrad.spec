
%define 	module	pyrad

Summary:	pyrad - Python implementation of a RADIUS client
Summary(pl):	pyrad - implementacja klienta RADIUS w Pythonie
Name:		python-%{module}
Version:	0.7
Release:	1
License:	BSD-like
Group:		Libraries/Python
Source0:	http://www.wiggy.net/files/%{module}-%{version}.tar.gz
# Source0-md5:	6492e9e04f401c23a9021928553dea66
URL:		http://www.wiggy.net/code/pyrad/
BuildRequires:	python-devel >= 2.3
Requires:	python >= 2.3
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pyrad is an implementation of a RADIUS client as described in RFC2865.
It takes care of all the details like building RADIUS packets, sending
them and decoding responses.

%description -l pl
pyrad jest implementacj± klienta protoko³u RADIUS, opisanego w
dokumencie RFC2865. Modu³ ten odpowiada za wszystkie aspekty
przetwarzania protoko³u RADIUS, takie jak budowanie pakietów
protoko³u, wysy³anie ich oraz odkodowywanie odpowiedzi.

%package examples
Summary:	Example programs for Python pyrad module
Summary(pl):	Programy przyk³adowe do modu³u Pythona pyrad
Group:		Development/Languages/Python
Requires:	%{name} = %{version}-%{release}

%description examples
This package contains example programs for Python pyrad module.

%description examples -l pl
Pakiet zawieraj±cy programy przyk³adowe dla modu³u Pythona pyrad.

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

find $RPM_BUILD_ROOT%{py_sitescriptdir} -name \*.py -exec rm {} \;

cp -ar example/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.txt
%{py_sitescriptdir}/pyrad

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}

%define oname pyflakes

Summary:	Simple program which checks Python source files for errors
Name:		python-%{oname}
Version:	3.0.1
Release:	1
License:	BSD
Group:		Development/Python
Url:		https://github.com/PyCQA/pyflakes
Source0:	https://files.pythonhosted.org/packages/source/p/%{oname}/%{oname}-%{version}.tar.gz
BuildRequires:  pkgconfig(python)
BuildRequires:  python3egg(setuptools)
Provides:       pyflakes = %{EVRD}
Obsoletes:      pyflakes < %{EVRD}
BuildArch:	noarch

%description
Pyflakes is a simple program which checks Python source files for errors. It is
similar to PyChecker in scope, but differs in that it does not execute the
modules to check them. This is both safer and faster, although it does not
perform as many checks.

Unlike PyLint, Pyflakes checks only for logical errors in programs; it does
not perform any checks on style.

%files
%license LICENSE
%doc AUTHORS NEWS.rst README.rst
%{_bindir}/pyflakes-%{python3_version}
%{_bindir}/pyflakes-3
%{_bindir}/pyflakes
%{python3_sitelib}/pyflakes*
%exclude %{python3_sitelib}/pyflakes/test/
#----------------------------------------------------------------------------

%prep
%setup -qn %{oname}-%{version}

%build
%py3_build

%install
%py3_install

mv %{buildroot}%{_bindir}/pyflakes %{buildroot}%{_bindir}/pyflakes-%{python3_version}
ln -s pyflakes-%{python3_version} %{buildroot}%{_bindir}/pyflakes-3
ln -s pyflakes-3 %{buildroot}%{_bindir}/pyflakes

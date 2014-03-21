%define _enable_debug_packages %{nil}
%define debug_package %{nil}

%define modname benchmark

Summary:	OCaml module for benchmarking code
Name:		ocaml-%{modname}
Version:	0.9
Release:	2
License:	LGPLv2+ with exceptions
Group:		Development/Other
Url:		https://forge.ocamlcore.org/projects/ocaml-benchmark/
Source0:	https://forge.ocamlcore.org/frs/download.php/533/%{modname}-%{version}.tar.gz
BuildRequires:	ocaml
BuildRequires:	ocaml-findlib-devel

%description
OCaml Benchmark is a small module to benchmark running times of code.

%files
%doc LICENSE
%{_libdir}/ocaml/%{modname}
%exclude %{_libdir}/ocaml/%{modname}/*.a
%exclude %{_libdir}/ocaml/%{modname}/*.cmxa
%exclude %{_libdir}/ocaml/%{modname}/*.mli

#----------------------------------------------------------------------------

%package devel
Summary:	Development files for %{name}
Requires:	%{name} = %{EVRD}

%description devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%files devel
%doc LICENSE README
%{_libdir}/ocaml/%{modname}/*.a
%{_libdir}/ocaml/%{modname}/*.cmxa
%{_libdir}/ocaml/%{modname}/*.mli

#----------------------------------------------------------------------------

%prep
%setup -q -n %{modname}-%{version}

%build
make all opt

%install
mkdir -p %{buildroot}%{_libdir}/ocaml
make install DESTDIR=%{buildroot}%{_libdir}/ocaml


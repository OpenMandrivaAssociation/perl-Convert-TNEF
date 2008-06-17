%define	module	Convert-TNEF
%define	name	perl-%{module}
%define version	0.17
%define release	%mkrel 8

Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
License: 	GPL
Group: 		Development/Perl
Source: 	%{module}-%{version}.tar.bz2
URL: 		http://www.cpan.org/modules/by-module/Convert/
BuildRequires:	perl-devel perl-MIME-tools
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires: 	perl
Summary:	%{module} module for perl
BuildArch:	noarch

%description
%{module} module for perl

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make
make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
 
%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{perl_vendorlib}/Convert/*
%{_mandir}/*/*
%doc MANIFEST README Changes



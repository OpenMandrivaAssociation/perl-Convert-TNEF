%define	modname	Convert-TNEF
%define modver	0.17

Summary:	%{modname} module for perl
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	13
License:	GPLv2
Group:		Development/Perl
Url:		http://www.cpan.org/modules/by-module/Convert/
Source0:	%{modname}-%{modver}.tar.bz2
BuildArch:	noarch
BuildRequires:	perl-MIME-tools
BuildRequires:	perl-devel

%description
%{modname} module for perl

%prep
%setup -qn %{modname}-%{modver}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std
 
%files
%doc MANIFEST README Changes
%{perl_vendorlib}/Convert/*
%{_mandir}/man3/*


%define	modname	Convert-TNEF
%define modver	0.18

Summary:	%{modname} module for perl
Name:		perl-%{modname}
Version:	%{modver}
Release:	1
License:	GPLv2
Group:		Development/Perl
Url:		https://metacpan.org/dist/Convert-TNEF
Source0:	https://cpan.metacpan.org/authors/id/D/DO/DOUGW/Convert-TNEF-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	make
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


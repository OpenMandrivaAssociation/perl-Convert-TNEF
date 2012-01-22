%define	upstream_name	 Convert-TNEF
%define upstream_version 0.17

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 4

Summary:	%{upstream_name} module for perl
License: 	GPL
Group: 		Development/Perl
Url: 		http://www.cpan.org/modules/by-module/Convert/
Source0:	%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-MIME-tools
BuildArch:	noarch
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}

%description
%{upstream_name} module for perl

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make
make test

%install
rm -rf %{buildroot}
%makeinstall_std
 
%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{perl_vendorlib}/Convert/*
%{_mandir}/*/*
%doc MANIFEST README Changes

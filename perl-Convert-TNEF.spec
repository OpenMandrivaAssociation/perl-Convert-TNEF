%define	upstream_name	 Convert-TNEF
%define upstream_version 0.17

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	%{upstream_name} module for perl
License:	GPL
Group:		Development/Perl
Url:		http://www.cpan.org/modules/by-module/Convert/
Source0:	%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-MIME-tools
BuildRequires:	perl-devel
BuildArch:	noarch

%description
%{upstream_name} module for perl

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
make
make test

%install
%makeinstall_std
 
%files
%{perl_vendorlib}/Convert/*
%{_mandir}/*/*
%doc MANIFEST README Changes


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 0.170.0-4mdv2012.0
+ Revision: 765113
- rebuilt for perl-5.14.2
- rebuilt for perl-5.14.x

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.170.0-2
+ Revision: 667055
- mass rebuild

* Tue Aug 04 2009 Jérôme Quelin <jquelin@mandriva.org> 0.170.0-1mdv2010.1
+ Revision: 408942
- rebuild using %%perl_convert_version

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 0.17-8mdv2009.0
+ Revision: 223579
- rebuild

* Thu Mar 06 2008 Oden Eriksson <oeriksson@mandriva.com> 0.17-7mdv2008.1
+ Revision: 180369
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Sun Mar 18 2007 Buchan Milne <bgmilne@mandriva.org> 0.17-6mdv2007.1
+ Revision: 146144
- Rebuild

  + Guillaume Rousse <guillomovitch@mandriva.org>
    - Import perl-Convert-TNEF

